import ast
import os
import re
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def run_python(*args, cwd=ROOT, input_text=None):
    """Run a Python exercise and return the completed process."""
    env = os.environ.copy()
    env["COLUMNS"] = "80"
    return subprocess.run(
        [PYTHON, *args],
        cwd=cwd,
        input=input_text,
        text=True,
        capture_output=True,
        env=env,
        timeout=5,
    )


class StartingZeroTests(unittest.TestCase):
    """Subject-level smoke tests for starting_0 exercises 00 through 08."""

    def test_ex00_hello(self):
        result = run_python("starting_0/ex00/Hello.py")
        self.assertEqual(result.returncode, 0, result.stderr)
        lines = result.stdout.splitlines()
        self.assertEqual(lines[0], "['Hello', 'World!']")
        self.assertEqual(lines[1], "('Hello', 'Korea!')")
        self.assertEqual(ast.literal_eval(lines[2]), {"Hello", "Seoul!"})
        self.assertEqual(lines[3], "{'Hello': '42Seoul!'}")

    def test_ex01_format_time_shape(self):
        result = run_python("starting_0/ex01/format_ft_time.py")
        self.assertEqual(result.returncode, 0, result.stderr)
        lines = result.stdout.splitlines()
        self.assertEqual(len(lines), 2)
        self.assertRegex(
            lines[0],
            r"^Seconds since January 1, 1970: "
            r"\d{1,3}(,\d{3})*\.\d{4} or \d\.\d{2}e\+\d{2} "
            r"in scientific notation$",
        )
        self.assertRegex(lines[1], r"^[A-Z][a-z]{2} \d{2} \d{4}$")

    def test_ex02_find_ft_type(self):
        script = (
            "from find_ft_type import all_thing_is_obj\n"
            "ft_list = ['Hello', 'tata!']\n"
            "ft_tuple = ('Hello', 'toto!')\n"
            "ft_set = {'Hello', 'tutu!'}\n"
            "ft_dict = {'Hello': 'titi!'}\n"
            "all_thing_is_obj(ft_list)\n"
            "all_thing_is_obj(ft_tuple)\n"
            "all_thing_is_obj(ft_set)\n"
            "all_thing_is_obj(ft_dict)\n"
            "all_thing_is_obj('Brian')\n"
            "all_thing_is_obj('Toto')\n"
            "print(all_thing_is_obj(10))\n"
        )
        result = run_python("-c", script, cwd=ROOT / "starting_0/ex02")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            result.stdout,
            "List : <class 'list'>\n"
            "Tuple : <class 'tuple'>\n"
            "Set : <class 'set'>\n"
            "Dict : <class 'dict'>\n"
            "Brian is in the kitchen : <class 'str'>\n"
            "Toto is in the kitchen : <class 'str'>\n"
            "Type not found\n"
            "42\n",
        )

    def test_ex03_null_not_found(self):
        script = (
            "from NULL_not_found import NULL_not_found\n"
            "Nothing = None\n"
            "Garlic = float('NaN')\n"
            "Zero = 0\n"
            "Empty = ''\n"
            "Fake = False\n"
            "NULL_not_found(Nothing)\n"
            "NULL_not_found(Garlic)\n"
            "NULL_not_found(Zero)\n"
            "NULL_not_found(Empty)\n"
            "NULL_not_found(Fake)\n"
            "print(NULL_not_found('Brian'))\n"
        )
        result = run_python("-c", script, cwd=ROOT / "starting_0/ex03")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            result.stdout,
            "Nothing: None <class 'NoneType'>\n"
            "Cheese: nan <class 'float'>\n"
            "Zero: 0 <class 'int'>\n"
            "Empty: <class 'str'>\n"
            "Fake: False <class 'bool'>\n"
            "Type not Found\n"
            "1\n",
        )

    def test_ex04_whatis(self):
        cases = [
            (["starting_0/ex04/whatis.py", "14"], "I'm Even.\n"),
            (["starting_0/ex04/whatis.py", "-5"], "I'm Odd.\n"),
            (["starting_0/ex04/whatis.py"], ""),
            (["starting_0/ex04/whatis.py", "0"], "I'm Even.\n"),
            (
                ["starting_0/ex04/whatis.py", "Hi!"],
                "AssertionError: argument is not an integer\n",
            ),
            (
                ["starting_0/ex04/whatis.py", "13", "5"],
                "AssertionError: more than one argument is provided\n",
            ),
        ]
        for argv, expected in cases:
            with self.subTest(argv=argv):
                result = run_python(*argv)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, expected)

    def test_ex05_building_argument(self):
        result = run_python("starting_0/ex05/building.py", "Hello, 42!")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            result.stdout,
            "The text contains 10 characters:\n"
            "1 upper letters\n"
            "4 lower letters\n"
            "2 punctuation marks\n"
            "1 spaces\n"
            "2 digits\n",
        )

    def test_ex05_building_stdin(self):
        result = run_python("starting_0/ex05/building.py", input_text="Hello World!\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            result.stdout,
            "What is the text to count?\n"
            "The text contains 13 characters:\n"
            "2 upper letters\n"
            "8 lower letters\n"
            "1 punctuation marks\n"
            "2 spaces\n"
            "0 digits\n",
        )

    def test_ex06_ft_filter(self):
        script = (
            "from ft_filter import ft_filter\n"
            "print(ft_filter.__doc__ == filter.__doc__)\n"
            "print(list(ft_filter(lambda x: x > 2, [1, 2, 3, 4])))\n"
            "print(list(ft_filter(None, [0, 1, '', 'hello'])))\n"
        )
        result = run_python("-c", script, cwd=ROOT / "starting_0/ex06")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "True\n[3, 4]\n[1, 'hello']\n")

    def test_ex06_filterstring(self):
        cases = [
            (
                ["filterstring.py", "Hello the World", "4"],
                "['Hello', 'World']\n",
            ),
            (["filterstring.py", "Hello the World", "99"], "[]\n"),
            (
                ["filterstring.py", "3", "Hello the World"],
                "AssertionError: the arguments are bad\n",
            ),
            (["filterstring.py"], "AssertionError: the arguments are bad\n"),
        ]
        for argv, expected in cases:
            with self.subTest(argv=argv):
                result = run_python(*argv, cwd=ROOT / "starting_0/ex06")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, expected)

    def test_ex07_sos(self):
        cases = [
            (["starting_0/ex07/sos.py", "sos"], "... --- ...\n"),
            (
                ["starting_0/ex07/sos.py", "h$llo"],
                "AssertionError: the arguments are bad\n",
            ),
        ]
        for argv, expected in cases:
            with self.subTest(argv=argv):
                result = run_python(*argv)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, expected)

    def test_ex08_loading(self):
        script = (
            "from Loading import ft_tqdm\n"
            "values = []\n"
            "for elem in ft_tqdm(range(5)):\n"
            "    values.append(elem)\n"
            "print()\n"
            "print(values)\n"
        )
        result = run_python("-c", script, cwd=ROOT / "starting_0/ex08")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("100%|[", result.stdout)
        self.assertIn("]| 5/5", result.stdout)
        self.assertTrue(result.stdout.endswith("\n[0, 1, 2, 3, 4]\n"))


if __name__ == "__main__":
    unittest.main()
