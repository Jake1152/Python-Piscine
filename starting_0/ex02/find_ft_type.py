def all_thing_is_obj(object: any) -> int:
    type_str = ''
    if isinstance(object, list):
        type_str = 'List'
    elif isinstance(object, tuple):
        type_str = 'Tuple'
    elif isinstance(object, set):
        type_str = 'Set'
    elif isinstance(object, dict):
        type_str = 'Dict'
    elif isinstance(object, str):
        type_str = f'{object} is in the kitchen'
    else:
        print("Type not found")
        return 42
    print(f"{type_str} : {type(object)}")
    return 42
