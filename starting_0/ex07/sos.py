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
        raise AssertionError("the arguments are bad")
    for ch in args[1]:
        if not ch.isalnum() and ch != " ":
            raise AssertionError("the arguments are bad")
        corpus += ch.upper()
    return corpus


def handle_error(err):
    """에러핸들링."""
    print(f"AssertionError: {err}")
    return 1


def main():
    """알파벳을 받아서 모스부호로 변환한다. 모스부호가 아니라면 에러를 발생시킨다."""
    from sys import argv

    NESTED_MORSE = {
        " ": "/",
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
        encoded = [NESTED_MORSE[ch] for ch in corpus]
        print(" ".join(encoded))

    except AssertionError as err:
        handle_error(err)


if __name__ == "__main__":
    main()
