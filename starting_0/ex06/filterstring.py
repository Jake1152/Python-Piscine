'''
# flake8사용
pip install flake8
export PATH="/home/jim/.local/bin:$PATH"
'''
'''
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
'''
from sys import argv, stdin

def building(corpus):
    """
    문자열을 넘겨받아서 각 조건에 맞게 카운팅
    한 글자씩 읽어서 처리
    """
    def ispunctuation(ch):
        """
        문장부호 검사용
        """
        import string 
        if ch in string.punctuation:
            return True
        return False

    count_dict = {"lower": 0, "upper":0, "punctuation": 0, "space": 0, "digit": 0 } # default dict사용하면 간단
    for ch in corpus:
        if ch.islower():
            count_dict["lower"] += 1
        elif ch.isupper():
            count_dict["upper"] += 1
        elif ispunctuation(ch):
            count_dict["punctuation"] += 1
        elif ch.isspace():
            count_dict["space"] += 1
        elif ch.isdigit():
            count_dict["digit"] += 1
        # else: # 엄격하게 처리하는 버젼
        #     raise ValueError(f"유효하지 않은 데이터가 있습니다. 문제의 문자: {ch}")

    total_ch_count =  count_dict["upper"] + count_dict["lower"] + count_dict["punctuation"] + count_dict["space"] + count_dict["digit"]
    print(f"The text contains {total_ch_count} characters:")
    print(f"{count_dict["upper"]} upper letters")
    print(f"{count_dict["lower"]} lower letters")
    print(f"{count_dict["punctuation"]} punctuation marks")
    print(f"{count_dict["space"]} spaces")
    print(f"{count_dict["digit"]} digits")
    return 0


def get_corpus(args):
    """
    말뭉치 전달 및 인자 검증
    """
    corpus = ""
    if len(args) > 2:
        raise ValueError("more than one argument is provided")
    elif len(args) < 2:
        try:
            print("What is the text to count?")
            # while 
            corpus = stdin.readline()
        except Exception as err:
            raise(err)
    else:
        corpus = args[1]
    return corpus

def handle_error(err):
    """
    에러핸들링
    """
    print(f"AssertionError : {err}")
    return 1

def main():
    """
    프로그램 실행 흐름만 담당함
    인자받아서 처리함수로 넘기고 결과 받기까지 등등.
    """
    try:
        args = argv
        corpus = get_corpus(args)
        building(corpus)

    except ValueError as err:
        return handle_error(err)

if __name__ == "__main__":
    main()