import logging
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

            self.log_debug(f"Running r2c using {tmp_namcouple_file}")
            subprocess.run(
                [
                    "srun",
                    "--nodes",
                    str(nweights),
                    "--ntasks",
                    str(nweights),
                    "--ntasks-per-node",
                    "1",
                    "r2c",
                    tmp_namcouple_file,
                ]
            )

            tmp_namcouple_file.unlink()

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
