import jinja2
import yaml

from rdy2cpl.namcouple.types import Grid, Link, LinkEndPoint, Namcouple, Transformation


def from_dict(thedict):
    opt_args = {
        arg: thedict[arg]
        for arg in ("description", "runtime", "nlogprt", "nnorest")
        if arg in thedict
    }
    return Namcouple(
        **opt_args,
        links=[
            Link(
                description=link.get("description"),
                dt=link["dt"],
                lag=link.get("lag", 0),
                mode=link.get("mode", "EXPORTED"),
                restart_file=link.get("restart_file", "none"),
                source=LinkEndPoint(
                    fields=link["source"]["fields"], grid=Grid(**link["source"]["grid"])
                ),
                target=LinkEndPoint(
                    fields=link["target"]["fields"], grid=Grid(**link["target"]["grid"])
                ),
                transformations=[
                    Transformation(name=t["name"], opts=t["opts"])
                    for t in link.get("transformations", [])
                ],
            )
            for link in thedict["links"]
        ],
    )


def _replace_none(thing):
    """Used to replace None by empty string after Jinja rendering"""
    return thing if thing is not None else ""


def _render_once(item, context):
    """Render item once with Jinja, and then parse with YAML to create proper types (i.e. lists, dicts)
    If item is not a string, return unmodified"""
    if isinstance(item, str):
        env = jinja2.Environment(finalize=_replace_none)
        return yaml.safe_load(env.from_string(item).render(**(context or {})))
    return item


def _render_recursive(item, context):
    """Renders item recursively with Jinja until no Jinja expressions are left"""
    rendered_0 = _render_once(item, context)
    rendered_1 = _render_once(rendered_0, context)
    while rendered_0 != rendered_1:
        rendered_1 = rendered_0
        rendered_0 = _render_once(rendered_1)
    return rendered_0


def _parse(item, context=None):
    if isinstance(item, list):
        return [_parse(i, context) for i in item]
    if isinstance(item, dict):
        return {k: _parse(v, context) for k, v in item.items()}
    return _render_recursive(item, context)


def _load_yaml_docs(stream):
    docs = yaml.load_all(stream, Loader=yaml.SafeLoader)
    first = next(docs)
    try:
        return first, next(docs)
    except StopIteration:
        return {}, first


def from_yaml(stream, context=None):
    config, namcouple_spec = _load_yaml_docs(stream)
    full_context = {**_parse(config, context), **(context or {})}
    namcouple_spec = _parse(namcouple_spec, full_context)
    return from_dict(namcouple_spec)
