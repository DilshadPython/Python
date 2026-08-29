"""
Demonstrates passing parameters explicitly into handler functions.
"""


def hello(name: str = 'python') -> str:
    """Return greeting string for given name."""
    return f"Hello, {name}"


def main(name: str = 'python') -> str:
    """Execute script main workflow with parameter passing."""
    return hello(name)


if __name__ == '__main__':
    print(main("Dilshad"))
