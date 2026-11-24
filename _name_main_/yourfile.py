"""Consumer module demonstrating the behavior of imported modules.

This script imports `myfile` and runs its own `main()` function to compare:
- `myfile.__name__` (equals 'myfile')
- Current module `__name__` (equals '__main__' when executed directly)
"""

try:
    # Handle both direct execution in folder and package-level imports
    from _name_main_ import myfile
except ImportError:
    import myfile


def main() -> dict[str, str]:
    """Execute main comparison between current file and imported module.

    Returns:
        dict[str, str]: Dictionary comparing current __name__ with imported module's __name__.
    """
    print(f"\nRunning 'yourfile' as main script.")
    print(f"Current script __name__:         '{__name__}'")
    print(f"Imported myfile.__name__:        '{myfile.__name__}'")

    # Call the helper function from the imported module
    imported_result = myfile.hello_py()

    return {
        "current_name": __name__,
        "imported_name": myfile.__name__,
        "imported_result": imported_result,
    }


if __name__ == "__main__":
    main()
