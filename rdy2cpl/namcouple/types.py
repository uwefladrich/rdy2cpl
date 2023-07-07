from dataclasses import dataclass, field
from typing import List


@dataclass
class Grid:
    name: str
    type: str
    overlap: int

    def as_dict(self):
        return {"name": self.name, "type": self.type, "overlap": self.overlap}


@dataclass
class Transformation:
    name: str
    opts: List[str]

    def as_dict(self):
        return {"name": self.name, "opts": self.opts}


@dataclass
class LinkEndPoint:
    fields: List[str] = field(compare=False)
    grid: Grid

    def as_dict(self):
        return {"fields": self.fields, "grid": self.grid.as_dict()}


@dataclass
class Link:
    source: LinkEndPoint
    target: LinkEndPoint
    dt: int
    description: str = field(default=None)
    active: bool = field(default=True)
    transformations: List[Transformation] = field(default_factory=list)
    lag: int = field(default=0)
    mode: str = field(default="EXPORTED")
    restart_file: str = field(default="none")

    def __eq__(self, other):
        """Two Links are considered equal if they would result in the same OASIS
        remapping weight file (rmp_*.nc). This is the case if, and only if, they
        have the same source and target and use the same SCRIP remapping method
        with the same parameters."""
        return (
            (self.source == other.source)
            and (self.target == other.target)
            and (
                [t for t in self.transformations if t.name == "SCRIPR"]
                == [t for t in other.transformations if t.name == "SCRIPR"]
            )
        )

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

    def as_dict(self):
        return {
            "description": self.description,
            "active": self.active,
            "dt": self.dt,
            "lag": self.lag,
            "source": self.source.as_dict(),
            "target": self.target.as_dict(),
            "transformations": [t.as_dict() for t in self.transformations],
            "mode": self.mode,
            "restart_file": self.restart_file,
        }


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
        for lnk in self.links:
            if lnk.active and lnk not in unique_links:
                unique_links.append(lnk)
                rn.links.append(
                    Link(
                        dt=1,
                        source=LinkEndPoint(
                            [f"VAR_{len(unique_links)-1:02}_S"], lnk.source.grid
                        ),
                        target=LinkEndPoint(
                            [f"VAR_{len(unique_links)-1:02}_T"], lnk.target.grid
                        ),
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
        links = "\n".join([str(link) for link in self.links if link.active])
        footer = "\n$END\n"
        return title + header + links + footer

    def save(self, name="namcouple"):
        with open(name, "w") as f:
            f.write(str(self))

    def as_dict(self):
        return {
            "description": self.description,
            "runtime": self.runtime,
            "nlogprt": self.nlogprt,
            "nnorest": self.nnorest,
            "links": [l.as_dict() for l in self.links],
        }
