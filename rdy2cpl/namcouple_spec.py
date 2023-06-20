import jinja2
import yaml

from rdy2cpl.namcouple import from_dict


def _replace_none(thing):
    return thing if thing is not None else ""


def _render_once(item, context=None):
    if isinstance(item, str):
        e = jinja2.Environment(finalize=_replace_none)
        return yaml.safe_load(e.from_string(item).render(**(context or {})))
    return item


def _render_recursive(item, context=None):
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


def _load_yaml_file(name):
    with open(name) as f:
        docs = yaml.load_all(f, Loader=yaml.SafeLoader)
        first = next(docs)
        try:
            return first, next(docs)
        except StopIteration:
            return {}, first


def read(filename, context=None):
    config, namcouple_spec = _load_yaml_file(filename)
    full_context = {**_parse(config, context), **(context or {})}
    namcouple_spec = _parse(namcouple_spec, full_context)
    return from_dict(namcouple_spec)
