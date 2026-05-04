# Starting 0 Subject Summary

이 문서는 `starting_0/en.subject.pdf`의 핵심 요구사항을 빠르게 확인하기 위한 요약본입니다.

## 공통 규칙

- Python 3.10을 사용한다.
- 라이브러리 import는 명시적으로 작성한다.
- `from module import *` 형식은 금지된다.
- 전역 변수는 사용할 수 없다.
- 허용된 함수나 라이브러리 제한을 각 exercise마다 확인한다.
- 예기치 않은 예외가 밖으로 터지면 해당 exercise가 무효 처리될 수 있다.
- ex05부터는 반드시 `main()`과 `if __name__ == "__main__":` 구조를 사용한다.
- ex05부터 모든 함수는 docstring을 가져야 한다.
- 코드는 `flake8` 기준을 따라야 한다.

## Exercise Overview

| Exercise | 제출 파일 | 핵심 목표 |
| --- | --- | --- |
| ex00 | `Hello.py` | list, tuple, set, dict 값을 수정해서 지정된 인사말 출력 |
| ex01 | `format_ft_time.py` | 현재 시간을 Unix timestamp와 날짜 문자열로 포맷 |
| ex02 | `find_ft_type.py` | 객체 타입을 출력하고 `42` 반환 |
| ex03 | `NULL_not_found.py` | `None`, `NaN`, `0`, 빈 문자열, `False` 구분 |
| ex04 | `whatis.py` | CLI 인자 하나를 정수로 받아 홀짝 판별 |
| ex05 | `building.py` | 문자열의 대문자, 소문자, 구두점, 공백, 숫자 개수 출력 |
| ex06 | `ft_filter.py`, `filterstring.py` | 내장 `filter` 재구현 및 길이 기준 단어 필터링 |
| ex07 | `sos.py` | 문자열을 Morse Code로 인코딩 |
| ex08 | `Loading.py` | `yield`를 사용해 `tqdm`과 유사한 진행률 함수 구현 |
| ex09 | package files | `ft_package` 패키지를 만들고 설치 가능하게 구성 |

## Exercise별 핵심

### ex00

각 자료형의 특징을 이용해 출력값을 맞춘다.

- list는 인덱스로 수정 가능하다.
- tuple은 불변이므로 새 tuple을 만든다.
- set은 순서가 없으므로 새 set을 만든다.
- dict는 key에 대응하는 value를 바꾼다.

### ex01

현재 시간을 가져와 아래 두 형식으로 출력한다.

- 초 단위 Unix timestamp, 천 단위 쉼표 포함
- scientific notation
- 월, 일, 연도 형식의 날짜

### ex02

`all_thing_is_obj(object)` 함수가 타입별 메시지를 출력하고 항상 `42`를 반환해야 한다.
모듈 파일을 직접 실행했을 때는 아무 출력도 없어야 한다.

### ex03

입력값이 어떤 Null 계열 값인지 판별한다.
정상 판별 시 `0`, 판별 실패 시 `Type not Found` 출력 후 `1`을 반환한다.

### ex04

CLI 인자를 검사한다.

- 인자가 없으면 아무것도 출력하지 않는다.
- 인자가 하나이고 정수면 홀짝을 출력한다.
- 인자가 둘 이상이면 `AssertionError: more than one argument is provided`를 출력한다.
- 정수가 아니면 `AssertionError: argument is not an integer`를 출력한다.

### ex05

문자열 하나를 분석해 문자 종류별 개수를 출력한다.
인자가 없으면 표준 입력으로 문자열을 받는다.
인자가 둘 이상이면 `AssertionError`를 출력한다.

### ex06

`ft_filter`는 내장 `filter`를 list comprehension으로 재구현한다.
`filterstring.py`는 문자열과 정수 기준을 받아 길이가 기준보다 긴 단어 목록을 출력한다.

### ex07

알파벳, 숫자, 공백을 Morse Code로 변환한다.
공백은 `/`로 표현하고, 잘못된 문자가 있으면 AssertionError 메시지를 출력한다.

### ex08

`ft_tqdm`은 반복 가능한 값을 하나씩 `yield`하면서 진행률 바를 출력해야 한다.
출력은 실제 `tqdm`과 최대한 비슷해야 한다.

### ex09

`ft_package`라는 설치 가능한 Python 패키지를 만든다.
패키지에는 `count_in_list` 함수가 있어야 하며, wheel과 source distribution 둘 다 설치 가능해야 한다.
