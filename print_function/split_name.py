"""
Splitting names and string unpacking in Python.
Signature: print(*objects, sep=' ', end='\\n', file=sys.stdout, flush=False)
"""

# Notices:
# 1. str.split(sep=None): When sep is omitted or None, split() splits by any whitespace
#    and automatically discards extra consecutive spaces.
# 2. In Python 3, extended unpacking (e.g. first, *middle, last = name.split()) can safely
#    handle names with multiple words.


def demonstrate_split_name(full_name: str = "john doe") -> None:
    # Clean the input with method chaining
    name = full_name.strip().title()

    # Split into first name and last name
    parts = name.split()
    if len(parts) >= 2:
        fname = parts[0]
        lname = parts[-1]
    else:
        fname = parts[0] if parts else "Unknown"
        lname = ""

    # -------------------------------------------------------------
    # [Old Version / Legacy String Formatting]
    # -------------------------------------------------------------
    # print('Hey, ' + name + '\n')
    # print('Hi, %s\n' % fname)
    # print('Hi, %s\n' % lname)
    # print('Hello, {} {}'.format(fname, lname))

    # -------------------------------------------------------------
    # [New Version / Python 3.6+ f-strings]
    # -------------------------------------------------------------
    print(f"Hey, {name}\n")
    print(f"Hi, {fname}\n")
    print(f"Hi, {lname}\n")
    print(f"Hello, {fname} {lname}")


if __name__ == "__main__":
    user_input = input("Please enter your full name: ")
    if user_input.strip():
        demonstrate_split_name(user_input)
    else:
        demonstrate_split_name()
