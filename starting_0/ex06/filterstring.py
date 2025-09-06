"""
# flake8사용.

pip install flake8
export PATH="/home/jim/.local/bin:$PATH"
"""

"""
$>python building.py "Python 3.0, released in 2008, was a major revision
that is not completely backward
compatible with earlier versions.
Python 2 was discontinued with version 2.7.18 in 2020."
The text contains 171 characters:
2 upper letters
121 lower letters
7 punctuation marks
26 spaces
15 digits
$>
"""


def parse_argument(args):
    """validation과 parse를 같이 진행한다."""
    corpus = ""
    if len(args) != 3:
        raise ValueError("the arguments are bad")
    try:
        num = int(args[2])
        if num < 0:
            raise ValueError("err")
    except ValueError:
        raise ValueError("the arguments are bad")

    if (not isinstance(args[1], str)) or (not isinstance(num, int)):
        raise ValueError("the arguments are bad")
    else:
        corpus = args[1]
    return [corpus, num]


def handle_error(err):
    """에러핸들링."""
    print(f"AssertionError : {err}")
    return 1


# TODO: 테스트
def main():
    """프로그램 실행 흐름만 담당함.
    인자받아서 처리함수로 넘기고 결과 받기까지 등등
    """
    from sys import argv
    from ft_filter import ft_filter

    try:
        args = argv
        corpus, num = parse_argument(args)
        words = corpus.split()
        filtered_iterable = ft_filter(lambda x: len(x) > num, words)
        if filtered_iterable != 1:
            print(filtered_iterable)

    except ValueError as err:
        return handle_error(err)


if __name__ == "__main__":
    main()
