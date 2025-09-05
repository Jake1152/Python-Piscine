'''
# flake8사용
pip install flake8
export PATH="/home/jim/.local/bin:$PATH"
'''
'''

'''
def handle_error(err):
    """
    에러핸들링
    """
    print(f"AssertionError : {err}")
    return 1

'''
filter(조건거르는 함수, 반복가능한 자료구조)
e.g) for _ in fitler(isdigit, [1,'a','b', 42])
'''
# iterable data는 dict, set, tuple 등도 되는가?
# list만 되는가?
# 어떻게 iterable한지 알아낼 것인가?
# 직접 dict, set, tuple, list인지 비교해서?
# 이미 있는 메서드는 없는가?  is_iterable
'''
아래 유형별로 별도처리
- set, dict는 합쳐도 되는지 고려
- list, tuple도 분리안해도 되는지도 조사
- list, tuple
- dict
- set
'''
def ft_filter(ft_fn, iterable_data):
    pass

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