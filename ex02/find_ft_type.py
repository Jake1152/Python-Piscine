from time import time
from datetime import datetime

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

def main():
    ''' 출력문 예시
    $>python tester.py | cat -e
    List : <class 'list'>$
    Tuple : <class 'tuple'>$
    Set : <class 'set'>$
    Dict : <class 'dict'>$
    Brian is in the kitchen : <class 'str'>$
    Toto is in the kitchen : <class 'str'>$
    Type not found$
    42$
    $>
    '''
    from find_ft_type import all_thing_is_obj

    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello" : "titi!"}

    all_thing_is_obj(ft_list)
    all_thing_is_obj(ft_tuple)
    all_thing_is_obj(ft_set)
    all_thing_is_obj(ft_dict)
    all_thing_is_obj("Brian")
    all_thing_is_obj("Toto")

    print(all_thing_is_obj(10))


if __name__ == "__main__":
    main()