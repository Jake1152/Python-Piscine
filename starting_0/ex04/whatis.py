'''
ref:
- https://sseongju1.tistory.com/34#google_vignette
- https://docs.python.org/ko/3.13/tutorial/errors.html
- https://docs.python.org/ko/3.13/tutorial/errors.html

'''

'''
$> python whatis.py 14
I'm Even.
$>
$> python whatis.py -5
I'm Odd.
$>
$> python whatis.py
$>
$> python whatis.py 0
I'm Even.
$>
$> python whatis.py Hi!
AssertionError: argument is not an integer
$>
$> python whatis.py 13 5
AssertionError: more than one argument is provided
$>
'''


def main():
    from sys import argv
    try:
        if len(argv) > 2:
            raise ValueError("more than one argument is provided")
        if len(argv) < 2:
            return
        num = ''
        try:
            num = abs(int(argv[1]))
        except ValueError:
            raise ValueError("argument is not an integer")
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except ValueError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
