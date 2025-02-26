"""
we have to run mypy exam.py output should be
Success: no issues found in 1 source file
"""
# we defile n: int
def number(n: int) -> str:
    return f"Hello {n}\n" * n

# Solution
num: int = int(input('Enter a number: '))
# this is like default return None as default if -> None in line 6
number: str = number(num)
print(number, end='')