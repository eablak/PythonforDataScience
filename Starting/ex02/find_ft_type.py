def all_thing_is_obj(object: any) -> int:
    
    object_type = type(object)

    if object_type == str:
        print(f"{object} is in the kitchen: {object_type}")
    elif object_type in [list, tuple, set, dict]:
        print(f"{object_type.__name__.capitalize()} : {object_type}")
    else:
        print("Type not found")
    return(42)


"""x: int
x = 5
print(type(x), " ", x)
y: int = "5"
print(type(y), " ", y)

from typing import Any

def myprint(obj: Any) -> None:
    print(obj)

def my_function(my_string: str) -> int:
    return len(my_string)

myprint("42")"""