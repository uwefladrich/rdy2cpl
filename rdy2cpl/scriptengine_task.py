import logging
import shutil
import subprocess
from pathlib import Path

import yaml

from rdy2cpl.namcouple.factory import from_yaml

try:
    from scriptengine.exceptions import ScriptEngineTaskRunError
    from scriptengine.tasks.core import Task, timed_runner
except (ModuleNotFoundError, ImportError) as e:
    logging.warning(
        "The ScriptEngine module could not be loaded, which means "
        "that the rdy2cpl ScriptEngine tasks will not be available. "
        f"(the error was: {e})"
    )
else:

    class MakeAll(Task):
        _required_arguments = ("namcouple",)

        def __init__(self, arguments):
            MakeAll.check_arguments(arguments)
            super().__init__(arguments)

        @timed_runner
        def run(self, context):
            namcouple_file = Path(self.getarg("namcouple", context))
            self.log_info(f"Open namcouple spec file: {namcouple_file}")
            try:
                with open(namcouple_file) as f:
                    namcouple_spec = f.read()
            except OSError as e:
                self.log_error(f"Could not open/read namcouple spec file: {e}")
                raise ScriptEngineTaskRunError
            namcouple = from_yaml(namcouple_spec, context)

            tmp_namcouple_file = namcouple_file.with_stem(namcouple_file.stem + ".tmp")
            self.log_debug(
                f"Writing temporary namcouple spec file: {tmp_namcouple_file}"
            )
            try:
                with open(tmp_namcouple_file, "w") as f:
                    f.write(yaml.safe_dump(namcouple.as_dict()))
            except OSError as e:
                self.log_error(
                    f"Could not open/write the temporary namcouple spec file: {e}"
                )
                raise ScriptEngineTaskRunError

            nweights = namcouple.reduced().num_links

            if not shutil.which("srun"):
                self.log_error(
                    "SLURM 'srun' command not found (rdy2cp needs a working SLURM environment)"
                )
                raise ScriptEngineTaskRunError

            srun_opts = self.getarg(
                "srun_opts",
                context,
                default=[
                    "--nodes", nweights,
                    "--ntasks", nweights,
                    "--ntasks-per-node", 1,
                ],
            )

            self.log_debug(f"Running r2c using {tmp_namcouple_file}")

            cmd = ["srun", *srun_opts, "r2c"]
            couple_grid_spec = self.getarg("couple_grid_spec", context, default=None)
            if couple_grid_spec is not None:
                self.log_info(f"Reading couple grid spec from {couple_grid_spec}")
                cmd.extend(["--couple-grid-spec", couple_grid_spec])
            cmd.append(tmp_namcouple_file)

            try:
                subprocess.run(map(str, cmd), capture_output=True, check=True)
            except subprocess.CalledProcessError as e:
                self.log_error(
                    f"Failed running r2c: return code is '{e.returncode}'."
                    " Full error message follows if loglevel is 'debug'"
                )
                self.log_debug(f"Full r2c error message:\n{e.stderr.decode()}")
                raise ScriptEngineTaskRunError
            else:
                self.log_info(
                    "Grid files, weights and namcouple file created; cleaning temporary OASIS files"
                )
                for p in (
                    tmp_namcouple_file,
                    *Path(".").glob("debug.*.??"),
                    *Path(".").glob("nout.??????"),
                ):
                    p.unlink()

    class MakeNamcouple(Task):
        _required_arguments = ("namcouple",)

        def __init__(self, arguments):
            MakeAll.check_arguments(arguments)
            super().__init__(arguments)

        @timed_runner
        def run(self, context):
            namcouple_file = Path(self.getarg("namcouple", context))
            self.log_info(f"Open namcouple spec file: {namcouple_file}")
            try:
                with open(namcouple_file) as f:
                    namcouple_spec = f.read()
            except OSError as e:
                self.log_error(f"Could not open/read namcouple spec file: {e}")
                raise ScriptEngineTaskRunError
            namcouple = from_yaml(namcouple_spec, context)

            self.log_debug("Writing new namcouple file")
            try:
                namcouple.save()
            except OSError as e:
                self.log_error(f"Could not open/write the namcouple file: {e}")
                raise ScriptEngineTaskRunError
