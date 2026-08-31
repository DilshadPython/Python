"""
Demonstrates standard script entry point pattern (`main()` function).
"""


def hello_entry(to: str = 'python') -> str:
    """Return greeting string."""
    return f"Hello, {to}"


def main(name: str = 'python') -> str:
    """Main execution function."""
    return hello_entry(name)


if __name__ == '__main__':
    print(main("World"))
