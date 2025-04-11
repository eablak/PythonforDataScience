def all_thing_is_obj(object: any) -> int:

    object_type = type(object)

    if object_type == str:
        print(f"{object} is in the kitchen: {object_type}")
    elif object_type in [list, tuple, set, dict]:
        print(f"{object_type.__name__.capitalize()} : {object_type}")
    else:
        print("Type not found")
    return (42)
