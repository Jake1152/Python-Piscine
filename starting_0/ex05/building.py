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


def building(corpus):
    """문자열을 넘겨받아서 각 조건에 맞게 카운팅 한 글자씩 읽어서 처리."""
    from string import punctuation
    from collections import defaultdict

    count_dict = defaultdict(int)
    for ch in corpus:
        if ch.islower():
            count_dict["lower"] += 1
        elif ch.isupper():
            count_dict["upper"] += 1
        elif ch in punctuation:
            count_dict["punctuation"] += 1
        elif ch.isspace():
            count_dict["space"] += 1
        elif ch.isdigit():
            count_dict["digit"] += 1

    total_ch_count = count_dict["upper"] + count_dict["lower"]\
        + count_dict["punctuation"]\
        + count_dict["space"] + count_dict["digit"]
    print(f"The text contains {total_ch_count} characters:")
    print(f"{count_dict['upper']} upper letters")
    print(f"{count_dict['lower']} lower letters")
    print(f"{count_dict['punctuation']} punctuation marks")
    print(f"{count_dict['space']} spaces")
    print(f"{count_dict['digit']} digits")
    return 0


def get_corpus(args):
    """말뭉치 전달 및 인자 검증."""
    from sys import stdin

    corpus = ""
    if len(args) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(args) < 2:
        try:
            print("What is the text to count?")
            corpus = stdin.readline()
        except Exception as err:
            raise err
    else:
        corpus = args[1]
    return corpus


def handle_error(err):
    """에러핸들링."""
    print(f"AssertionError : {err}")
    return 1

# TODO: assert를 활용한 처리
def main():
    """
    프로그램 실행 흐름만 담당함.

    인자받아서 처리함수로 넘기고 결과 받기까지 등등
    """
    from sys import argv

    try:
        args = argv
        corpus = get_corpus(args)
        building(corpus)

    except AssertionError as err:
        return handle_error(err)
    except KeyboardInterrupt as err:
        pass
    ## TODO: CTRL+Z, CTRL+\ 처리

if __name__ == "__main__":
    main()
