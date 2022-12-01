from dataclasses import dataclass, field
from typing import List

import yaml


@dataclass
class Grid:
    name: str
    type: str
    overlap: int


@dataclass
class Transformation:
    name: str
    opts: List[str]


@dataclass
class LinkEndPoint:
    fields: List[str] = field(compare=False)
    grid: Grid


@dataclass
class Link:
    source: LinkEndPoint
    target: LinkEndPoint
    dt: int = field(compare=False)
    transformations: List[Transformation] = field(default_factory=list)
    description: str = field(default=None, compare=False)
    lag: int = field(default=0, compare=False)
    mode: str = field(default="EXPORTED", compare=False)
    restart_file: str = field(default="none", compare=False)

    @property
    def out(self):
        """Returns Link representation in OASIS namcouple syntax"""
        title = f"# {self.description.strip()}\n" if self.description else ""
        first = (
            f" {':'.join(self.source.fields)} {':'.join(self.target.fields)} 1 "
            f"{self.dt} "
            f"{len(self.transformations)} "
            f"{self.restart_file} "
            f"{self.mode}\n"
        )
        second = f" {self.source.grid.name} {self.target.grid.name}"
        second += f" LAG={self.lag}\n" if self.lag != 0 else "\n"
        third = (
            f" {self.source.grid.type} {self.source.grid.overlap}"
            f" {self.target.grid.type} {self.target.grid.overlap}\n"
        )
        trans = " " + " ".join(t.name for t in self.transformations) + "\n"
        for t in self.transformations:
            for opt in t.opts:
                trans += "  " + opt + "\n"
        return title + first + second + third + trans


@dataclass
class Namcouple:
    links: List[Link]
    description: str = field(default=None)
    runtime: int = field(default=1)
    nlogprt: str = field(default="1 0")
    nnorest: str = field(default=False)

    @property
    def num_links(self):
        return len(self.links)

    @property
    def out(self):
        """Returns file representation in OASIS namcouple syntax"""

        def global_parameter(name, value):
            return f"${name}\n    {value}\n\n"

        title = (
            f"# {self.description.strip()}\n\n"
            if self.description
            else "# Auto-generated OASIS namcouple file\n\n"
        )
        header = (
            f"{global_parameter('NFIELDS', self.num_links)}"
            f"{global_parameter('RUNTIME', self.runtime)}"
            f"{global_parameter('NLOGPRT', self.nlogprt)}"
            f"{global_parameter('NNOREST', 'True' if self.nnorest else 'False')}"
            "$STRINGS\n\n"
        )
        links = "\n".join([link.out for link in self.links])
        footer = "\n$END\n"
        return title + header + links + footer


def reduce(nmcpl):
    """Returns a reduced version, with unique links, of the Namcouple argument"""
    reduced_namcouple = Namcouple(
        description=(
            f"Reduced version of '{nmcpl.description}'" if nmcpl.description else None
        ),
        nlogprt="0 0",
        links=[],
    )
    unique_links = []
    for index, link in enumerate(nmcpl.links):
        if link in unique_links:
            continue
        reduced_namcouple.links.append(
            Link(
                dt=1,
                source=LinkEndPoint([f"VAR_{index:02}_S"], link.source.grid),
                target=LinkEndPoint([f"VAR_{index:02}_T"], link.target.grid),
                transformations=link.transformations,
            )
        )
    return reduced_namcouple


def from_dict(thedict):
    nondefault_args = {}
    for arg in ("description", "runtime", "nlogprt", "nnorest"):
        if arg in thedict:
            nondefault_args[arg] = thedict[arg]
    return Namcouple(
        **nondefault_args,
        links=[
            Link(
                description=link.get("description", ""),
                dt=link["dt"],
                lag=link.get("lag", 0),
                mode=link.get("mode", "EXPORTED"),
                restart_file=link.get("restart_file", "none"),
                source=LinkEndPoint(
                    fields=link["source"]["fields"],
                    grid=Grid(**link["source"]["grid"]),
                ),
                target=LinkEndPoint(
                    fields=link["target"]["fields"],
                    grid=Grid(**link["target"]["grid"]),
                ),
                transformations=[
                    Transformation(
                        name=transformation["name"],
                        opts=transformation["opts"],
                    )
                    for transformation in link.get("transformations", [])
                ],
            )
            for link in thedict["links"]
        ],
    )


def read_namcouple_spec(namcouple_spec_file):
    with open(namcouple_spec_file) as f:
        namcouple = from_dict(yaml.load(f, yaml.SafeLoader))
    return namcouple


def write_namcouple(namcouple, filename="namcouple"):
    with open(filename, "w") as f:
        f.write(namcouple.out)


def number_of_links(namcouple):
    "Returns the number of *distinct* links"
    return len(reduce(namcouple).links)
