from dataclasses import dataclass, field
from typing import List


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
    description: str = field(default=None, compare=False)
    transformations: List[Transformation] = field(default_factory=list)
    lag: int = field(default=0, compare=False)
    mode: str = field(default="EXPORTED", compare=False)
    restart_file: str = field(default="none", compare=False)

    def __str__(self):
        header = f"# {self.description}\n" if self.description else ""
        first = (
            f" {':'.join(self.source.fields)} {':'.join(self.target.fields)} 1 "
            f"{self.dt} "
            f"{len(self.transformations)} "
            f"{self.restart_file} "
            f"{self.mode}\n"
        )
        second = f" {self.source.grid.name} {self.target.grid.name}" + (
            f" LAG={self.lag}\n" if self.lag != 0 else "\n"
        )
        third = (
            f" {self.source.grid.type} {self.source.grid.overlap}"
            f" {self.target.grid.type} {self.target.grid.overlap}\n"
        )
        tlines = f" {' '.join(t.name for t in self.transformations)}\n"
        for t in self.transformations:
            for opt in t.opts:
                tlines += f"  {opt}\n"
        return header + first + second + third + tlines


@dataclass
class Namcouple:
    links: List[Link]
    description: str = field(default=None)
    runtime: int = field(default=1)
    nlogprt: str = field(default="1 0")
    nnorest: bool = field(default=False)

    @property
    def num_links(self):
        return len(self.links)

    def reduced(self):
        """Returns the reduced namcouple version, with unique links"""
        rn = Namcouple(
            description=f"Reduced version of: {self.description}"
            if self.description
            else None,
            links=[],
        )
        unique_links = []
        for idx, lnk in enumerate(self.links):
            if lnk not in unique_links:
                unique_links.append(lnk)
                rn.links.append(
                    Link(
                        dt=1,
                        source=LinkEndPoint([f"VAR_{idx:02}_S"], lnk.source.grid),
                        target=LinkEndPoint([f"VAR_{idx:02}_T"], lnk.target.grid),
                        transformations=lnk.transformations,
                    )
                )
        return rn

    def __str__(self):
        """Returns file representation in OASIS namcouple syntax"""

        def global_parameter(name, value):
            return f"${name}\n    {value}\n\n"

        title = f"# {self.description.strip()}\n\n" if self.description else ""
        header = (
            f"{global_parameter('NFIELDS', self.num_links)}"
            f"{global_parameter('RUNTIME', self.runtime)}"
            f"{global_parameter('NLOGPRT', self.nlogprt)}"
            f"{global_parameter('NNOREST', 'True' if self.nnorest else 'False')}"
            "$STRINGS\n\n"
        )
        links = "\n".join([str(link) for link in self.links])
        footer = "\n$END\n"
        return title + header + links + footer
