object = {'a':{'b':{'c':'d'}}}
key = "a/b/c"
another_key = "a/b/c/d"

def get_nested_value(object, key):
    """Return the nested value from a given key.

        >>> get_nested_value(object,key)
        'd'
        >>> get_nested_value(object,another_key)
        Traceback (most recent call last):
        ValueError: Path not found in object
    """
    if isinstance(key, str):
        list_to_trav = key.split("/")
    else:
        list_to_trav = key
    for item in list_to_trav:
        del list_to_trav[0]
        if isinstance(object, dict):
            object = object[item]
            return get_nested_value(object, list_to_trav)
        else:
            raise ValueError("Path not found in object")
    return object



