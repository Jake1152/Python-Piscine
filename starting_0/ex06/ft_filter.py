"""
# flake8사용.

pip install flake8
export PATH="/home/jim/.local/bin:$PATH"
alias norminette="flake8"
"""


"""
filter(조건거르는 함수, 반복가능한 자료구조).

e.g) for _ in fitler(isdigit, [1,'a','b', 42])
iterable data는 dict, set, tuple 등도 되는가?
list만 되는가?
=> list comprehension을 쓰라고 했으므로 list로만 구현한다.
어떻게 iterable한지 알아낼 것인가?
직접 dict, set, tuple, list인지 비교해서?
이미 있는 메서드는 없는가?  is_iterable
아래 유형별로 별도처리
- set, dict는 합쳐도 되는지 고려
- list, tuple도 분리안해도 되는지도 조사
- list, tuple
- dict
- set
"""


def handle_error(err):
    """에러핸들링."""
    print(f"AssertionError : {err}")
    return 1


def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object\n\nReturn
    an iterator yielding those items of iterable for which function(item)\nis true.
    If function is None, return the items that are true.
    """
    filtered_iterable = None
    if function is None:
        filtered_iterable = (val for val in iterable if val)
    else:
        filtered_iterable = (val for val in iterable if function(val))
    return filtered_iterable
