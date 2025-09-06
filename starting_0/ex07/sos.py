"""
# flake8사용.

pip install flake8
export PATH="/home/jim/.local/bin:$PATH"
"""

"""
$> python sos.py "sos" | cat -e
... --- ...$
$> python sos.py 'h$llo'
AssertionError: the arguments are bad
$>
"""


def parse_argument(args):
    """validation과 parse를 같이 진행한다."""
    corpus = ""
    if len(args) != 2:
        raise ValueError("the arguments are bad")
    try:
        for ch in args[1]:
            if not ch.isalnum():
                raise ValueError("the arguments are bad")
            if ch.isalpha():
                ch = ch.upper()
            corpus += ch
    except ValueError as err:
        raise ValueError(err)
    return corpus


def handle_error(err):
    """에러핸들링."""
    print(f"AssertionError : {err}")
    return 1


def main():
    """알파벳을 받아서 모스부호로 변환한다. 모스부호가 아니라면 에러를 발생시킨다."""
    from sys import argv, stdout

    NESTED_MORSE = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----."
    }

    try:
        corpus = parse_argument(argv)
        for idx in range(len(corpus) - 1):
            ch = corpus[idx]
            stdout.write(NESTED_MORSE[ch] + ' ')
        print(NESTED_MORSE[corpus[len(corpus) - 1]])

    except IndexError as err:
        handle_error(err)
    except ValueError as err:
        handle_error(err)
    except Exception as err:
        handle_error(f"ExceptionError : {err}")


if __name__ == "__main__":
    main()
