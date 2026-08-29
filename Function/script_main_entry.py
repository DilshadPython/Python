"""
Demonstrates standard script entry point pattern ( function).
"""


def hello(to: str = 'python') -> str:
    """Return greeting string."""
    return f"Hello, {to}"


def main(name: str = 'python') -> str:
    """Main execution function."""
    return hello(name)


if __name__ == '__main__':
    print(main("World"))
