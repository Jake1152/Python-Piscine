'''
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
===============================================================================
$>python tester.py | cat -e
Nothing: None <class 'NoneType'>$
Cheese: nan <class 'float'>$
Zero: 0 <class 'int'>$
Empty: <class 'str'>$
Fake: False <class 'bool'>$
Type not Found$
1$
$>
'''
def NULL_not_found(object: any) -> int:
    type_str = ''
    # print("object: #{object}")
    if isinstance(object, type(None)):
        type_str = 'Nothing: None'
    elif isinstance(object, float):
        type_str = 'Cheese: nan'
    elif isinstance(object, bool):
        type_str = 'Fake: '
        if object:
            type_str += "True"
        else:
            type_str += "False"
    elif isinstance(object, int):
        type_str = 'Zero: 0'
    elif isinstance(object, str):
        if not object:
            type_str = f'Empty:'
        else:
            print("Type not Found")
            return 1
    else:
        print("Type not Found")
        return 1
    print(f"{type_str} {type(object)}")
    return 0

    #your code here