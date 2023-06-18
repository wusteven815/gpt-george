def create_arg(desc, _type="string", enum=None):

    result = {
        "type": _type,
        "description": desc
    }
    if enum is not None:
        result["enum"] = enum

    return result


def create_config(name, desc, required=None, **kwargs):

    if required is None:
        required = []

    result = {
        "name": name,
        "description": desc,
        "parameters": {
            "type": "object",
            "properties": kwargs
        },
        "required": required
    }

    return result