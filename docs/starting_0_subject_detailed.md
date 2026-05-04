# Starting 0 Subject Detailed Explanation

이 문서는 `starting_0/en.subject.pdf`를 exercise별로 자세히 풀어쓴 해설입니다.
각 항목은 요구사항, 구현 방향, 주의사항을 중심으로 정리했습니다.

## General Rules

프로젝트는 Python 기초 문법을 단계적으로 익히는 구성입니다. 제출물은 지정된 디렉터리와 파일 이름을 정확히 맞춰야 하며, 평가자는 Git 저장소 안의 파일만 확인합니다.

기본 규칙은 다음과 같습니다.

- Python 3.10을 사용한다.
- exercise별 allowed functions 제한을 따른다.
- import는 명시적으로 작성한다.
- wildcard import는 금지된다.
- 전역 변수는 사용하지 않는다.
- 예기치 않은 예외가 발생하면 평가가 실패할 수 있다.
- ex05 이후 exercise는 단순 스크립트가 아니라 `main()` 진입점을 가진 프로그램이어야 한다.
- ex05 이후 모든 함수는 docstring을 가져야 한다.
- `flake8` 기준을 통과하는 스타일로 작성한다.

권장 기본 구조는 다음과 같다.

```python
def main():
    """Program entry point."""
    ...


if __name__ == "__main__":
    main()
```

## Exercise 00: First Python Script

제출 경로는 `starting_0/ex00/Hello.py`입니다.

주어진 자료형의 값을 바꿔서 아래와 같은 결과를 출력해야 합니다.

```text
['Hello', 'World!']
('Hello', 'France!')
{'Hello', 'Paris!'}
{'Hello': '42Paris!'}
```

이 문제의 목적은 Python 기본 컨테이너 타입의 차이를 확인하는 것입니다.

list는 mutable이므로 특정 인덱스 값을 직접 바꿀 수 있습니다. tuple은 immutable이므로 기존 tuple을 직접 수정할 수 없고 새 tuple을 만들어야 합니다. set은 순서가 없고 인덱스로 접근할 수 없기 때문에 새 set을 구성하는 편이 단순합니다. dict는 key를 기준으로 value를 수정하면 됩니다.

캠퍼스 국가, 도시, 캠퍼스 이름은 subject 예시 기준으로 각각 `France!`, `Paris!`, `42Paris!`를 사용합니다. 다른 캠퍼스라면 본인 캠퍼스에 맞는 값으로 바꾸면 됩니다.

## Exercise 01: First Use of Package

제출 경로는 `starting_0/ex01/format_ft_time.py`입니다.

현재 시각을 가져와 다음 두 줄 형식으로 출력해야 합니다.

```text
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation
Oct 21 2022
```

실행 시점에 따라 숫자와 날짜는 달라집니다. 중요한 것은 값이 아니라 포맷입니다.

구현 방향은 다음과 같습니다.

- `time.time()`으로 Unix timestamp를 얻는다.
- 일반 표기는 천 단위 쉼표를 포함한다.
- scientific notation은 소수 둘째 자리 정도로 맞춘다.
- 날짜는 `strftime`을 사용해 `Oct 21 2022` 형태로 출력한다.

출력 문자열의 쉼표, 공백, 대소문자가 subject와 맞아야 합니다.

## Exercise 02: First Function Python

제출 경로는 `starting_0/ex02/find_ft_type.py`입니다.

`all_thing_is_obj(object: any) -> int` 함수를 작성합니다. 함수는 입력 객체의 타입을 출력하고 `42`를 반환해야 합니다.

타입별 출력은 다음과 같습니다.

- list: `List : <class 'list'>`
- tuple: `Tuple : <class 'tuple'>`
- set: `Set : <class 'set'>`
- dict: `Dict : <class 'dict'>`
- str: `{문자열} is in the kitchen : <class 'str'>`
- 그 외: `Type not found`

중요한 점은 파일을 직접 실행했을 때 아무것도 출력하지 않아야 한다는 것입니다. 따라서 테스트 코드를 전역에 두면 안 됩니다. 함수 정의만 두거나, 필요한 경우 `if __name__ == "__main__":` 아래에 아무 동작도 하지 않도록 둡니다.

타입 판별은 `type(object)` 또는 `isinstance()`를 사용할 수 있습니다. subject의 예상 출력은 `<class 'list'>` 형식을 요구하므로 출력에는 실제 type 객체를 그대로 넣는 방식이 적합합니다.

## Exercise 03: NULL Not Found

제출 경로는 `starting_0/ex03/NULL_not_found.py`입니다.

`NULL_not_found(object: any) -> int` 함수를 작성합니다. 이 함수는 여러 종류의 Null처럼 보이는 값을 구분해 출력합니다.

테스트 대상은 다음과 같습니다.

- `None`
- `float("NaN")`
- `0`
- `""`
- `False`

예상 출력은 다음과 같습니다.

```text
Nothing: None <class 'NoneType'>
Cheese: nan <class 'float'>
Zero: 0 <class 'int'>
Empty: <class 'str'>
Fake: False <class 'bool'>
Type not Found
1
```

정상적으로 판별한 경우 `0`을 반환하고, 판별하지 못한 경우 `Type not Found`를 출력한 뒤 `1`을 반환합니다.

주의할 점은 bool이 int의 하위 타입처럼 동작한다는 것입니다. Python에서 `False == 0`은 참이므로, `False`를 먼저 검사하지 않으면 `0`으로 잘못 분류될 수 있습니다. 따라서 bool과 int를 구분할 때는 검사 순서가 중요합니다.

또 다른 주의점은 NaN입니다. NaN은 자기 자신과 비교해도 같지 않습니다. 즉 `nan != nan`이 참입니다. allowed functions가 `None`이므로 외부 라이브러리 없이 이 성질을 이용하면 됩니다.

## Exercise 04: The Even and the Odd

제출 경로는 `starting_0/ex04/whatis.py`입니다.

프로그램은 CLI 인자를 하나 받아 정수인지 검사하고, 짝수인지 홀수인지 출력합니다.

요구사항은 다음과 같습니다.

- 인자가 없으면 아무 출력도 하지 않는다.
- 인자가 하나이고 정수면 결과를 출력한다.
- 인자가 둘 이상이면 `AssertionError: more than one argument is provided`를 출력한다.
- 인자가 정수로 변환될 수 없으면 `AssertionError: argument is not an integer`를 출력한다.

예시는 다음과 같습니다.

```text
python whatis.py 14
I'm Even.

python whatis.py -5
I'm Odd.

python whatis.py Hi!
AssertionError: argument is not an integer
```

구현은 `sys.argv`를 사용하면 됩니다. 인자 개수를 먼저 검사하고, 그 다음 정수 변환 가능 여부를 검사하는 순서가 자연스럽습니다.

정수 판별에서 `str.isdigit()`만 사용하면 음수를 처리하지 못합니다. `int()` 변환을 `try` 블록 안에서 수행하는 방식이 더 단순합니다. 단, 예외는 밖으로 새면 안 되므로 반드시 잡아서 subject가 요구하는 메시지를 출력해야 합니다.

## Additional Rules from Exercise 05

ex05부터는 추가 규칙이 적용됩니다.

- 전역 스코프에서 실행되는 코드를 두지 않는다.
- `main()` 함수를 작성한다.
- `if __name__ == "__main__": main()` 구조를 사용한다.
- 잡히지 않은 예외가 없어야 한다.
- 모든 함수는 docstring을 가져야 한다.
- `flake8` 기준을 따른다.

이후 exercise에서 CLI 프로그램을 작성할 때도 인자 검사와 에러 출력을 `main()` 안에서 처리해야 합니다.

## Exercise 05: First Standalone Program Python

제출 경로는 `starting_0/ex05/building.py`입니다.

문자열 하나를 받아 다음 개수를 출력합니다.

- 전체 문자 수
- 대문자 수
- 소문자 수
- punctuation 수
- 공백 수
- 숫자 수

인자가 없으면 사용자에게 입력을 요청해야 합니다.

```text
What is the text to count?
```

인자가 두 개 이상이면 AssertionError 메시지를 출력해야 합니다.

문자 판별은 Python 문자열 메서드를 활용하면 됩니다.

- `isupper()`
- `islower()`
- `isdigit()`
- `isspace()`

punctuation은 `string.punctuation`을 사용하면 직접 구두점 목록을 만들 필요가 없습니다. subject가 "Don't reinvent the wheel"이라고 말하는 부분이 이 지점입니다.

주의할 점은 표준 입력으로 받을 때 줄바꿈 문자를 어떻게 처리할지입니다. subject는 carriage return도 space로 센다고 설명합니다. 입력 방식에 따라 개수가 달라질 수 있으므로 테스트 예시와 맞춰 확인해야 합니다.

## Exercise 06: Recode Filter and Filter String

제출 경로는 다음 두 파일입니다.

- `starting_0/ex06/ft_filter.py`
- `starting_0/ex06/filterstring.py`

### Part 1: `ft_filter`

내장 `filter` 함수를 직접 재구현합니다. 원래 `filter()` 사용은 금지입니다.

요구사항은 다음과 같습니다.

- list comprehension을 사용한다.
- 내장 `filter`와 같은 방식으로 동작해야 한다.
- `print(filter.__doc__)`와 같은 docstring을 제공해야 한다.

Python의 `filter(function, iterable)`은 function이 `None`이면 iterable의 truthy 값만 남깁니다. function이 있으면 function 결과가 truthy인 값만 남깁니다.

간단한 구현 방향은 generator expression 또는 list comprehension 기반 iterable을 반환하는 것입니다. subject는 list comprehension 사용을 요구하므로 내부 필터링 표현식에 list comprehension을 포함해야 합니다.

### Part 2: `filterstring.py`

프로그램은 문자열 `S`와 정수 `N`을 인자로 받아, `S` 안의 단어 중 길이가 `N`보다 큰 단어만 리스트로 출력합니다.

예시는 다음과 같습니다.

```text
python filterstring.py 'Hello the World' 4
['Hello', 'World']
```

요구사항은 다음과 같습니다.

- 인자는 정확히 2개여야 한다.
- 첫 번째 인자는 문자열이어야 한다.
- 두 번째 인자는 정수여야 한다.
- list comprehension을 최소 1번 사용한다.
- lambda를 최소 1번 사용한다.
- 인자가 잘못되면 `AssertionError: the arguments are bad`를 출력한다.

CLI에서는 모든 인자가 문자열로 들어옵니다. 따라서 "첫 번째 인자가 문자열인지"는 실제 타입 검사보다는 두 번째 인자가 정수로 변환 가능한지, 인자 수가 맞는지, subject가 금지한 상황인지 확인하는 방식으로 처리합니다.

`S.split()`을 사용하면 공백 기준으로 단어를 분리할 수 있습니다. subject는 문자열 안에 punctuation이나 invisible character가 없다고 가정합니다.

## Exercise 07: Dictionaries SoS

제출 경로는 `starting_0/ex07/sos.py`입니다.

문자열을 Morse Code로 변환하는 프로그램입니다.

요구사항은 다음과 같습니다.

- 인자는 정확히 1개여야 한다.
- 알파벳, 숫자, 공백만 지원한다.
- 알파벳은 대소문자를 구분하지 않고 처리하는 편이 좋다.
- 각 Morse 문자는 공백 하나로 구분한다.
- 입력 문자열의 공백은 `/`로 표현한다.
- Morse Code 매핑은 dictionary에 저장한다.
- 잘못된 문자가 있으면 `AssertionError: the arguments are bad`를 출력한다.

예시는 다음과 같습니다.

```text
python sos.py "sos"
... --- ...

python sos.py 'h$llo'
AssertionError: the arguments are bad
```

구현 방향은 Morse dictionary를 만들고, 입력 문자열을 대문자로 바꾼 뒤 각 문자를 dictionary에서 찾는 방식입니다. 최종 출력에서 마지막에 불필요한 공백이 붙지 않도록 `join()`을 사용하는 편이 좋습니다.

## Exercise 08: Loading ...

제출 경로는 `starting_0/ex08/Loading.py`입니다.

`ft_tqdm(lst: range) -> None` 함수를 작성합니다. 이 함수는 `tqdm`처럼 진행률을 표시하면서 iterable의 값을 하나씩 넘겨야 합니다.

핵심은 `yield`입니다. 함수가 단순히 출력만 하고 끝나는 것이 아니라, 다음과 같은 사용을 지원해야 합니다.

```python
for elem in ft_tqdm(range(333)):
    sleep(0.005)
```

구현 방향은 다음과 같습니다.

- iterable의 전체 길이를 구한다.
- 반복할 때마다 현재 진행 개수를 계산한다.
- 퍼센트와 bar를 `\r`로 같은 줄에 갱신한다.
- 각 요소를 `yield`한다.
- 마지막에는 100% 상태가 보이도록 한다.

allowed function은 `os`입니다. subject는 `get_terminal_size`를 사용해 터미널 크기에 맞출 수 있다고 힌트를 줍니다.

정확히 원본 `tqdm`과 같을 필요는 없지만, subject 예시처럼 진행률, bar, 현재 개수와 전체 개수가 보여야 합니다.

## Exercise 09: My First Package Creation

제출 경로는 `starting_0/ex09/`입니다.

`ft_package`라는 Python 패키지를 만들고, wheel과 source distribution으로 설치 가능하게 구성해야 합니다.

설치 명령은 둘 다 동작해야 합니다.

```sh
pip install ./dist/ft_package-0.0.1.tar.gz
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

`pip show -v ft_package`에서 다음과 같은 패키지 정보가 보여야 합니다.

- Name: `ft_package`
- Version: `0.0.1`
- Summary: `A sample test package`
- Author 정보
- License 정보

패키지는 다음 코드에서 사용할 수 있어야 합니다.

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
print(count_in_list(["toto", "tata", "toto"], "tutu"))
```

출력은 각각 `2`, `0`입니다.

구현할 함수는 리스트에서 특정 값이 몇 번 등장하는지 세는 단순한 함수입니다. Python의 `list.count()`를 사용하면 됩니다.

패키징은 `pyproject.toml` 기반으로 구성하는 것이 현재 Python 생태계에서 가장 단순합니다. 필요한 파일은 보통 다음과 같습니다.

- `pyproject.toml`
- `README.md`
- `LICENSE`
- `ft_package/__init__.py`
- 실제 함수가 들어 있는 `.py` 파일

빌드 후 `dist/` 아래에 `.tar.gz`와 `.whl` 파일이 생성되어야 합니다.

## 제출 전 체크리스트

- 디렉터리 이름이 subject와 정확히 같은가?
- 제출 파일 이름이 subject와 정확히 같은가?
- 실행했을 때 예상 출력과 공백, 대소문자가 맞는가?
- 예외가 밖으로 터지지 않는가?
- ex05 이후 `main()` 구조를 지켰는가?
- 함수에 docstring이 있는가?
- 금지된 built-in 또는 library를 사용하지 않았는가?
- `flake8` 기준을 통과하는가?
- 직접 실행하면 출력이 없어야 하는 모듈에서 불필요한 출력이 없는가?
