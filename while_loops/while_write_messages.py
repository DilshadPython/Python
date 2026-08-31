"""
Demonstrates writing message sequences to a destination text file.
"""
import os
from typing import List


def write_messages_to_file(filepath: str, messages: List[str]) -> int:
    """Write list of message strings to specified file, returning line count written."""
    with open(filepath, 'w', encoding='utf-8') as f:
        for msg in messages:
            f.write(msg.rstrip('\n') + '\n')
    return len(messages)


if __name__ == '__main__':
    dest = os.path.join(os.path.dirname(__file__), 'msg.txt')
    msgs = [
        'Welcome to Python',
        'Welcome to C++',
        'Welcome to Google',
        'Welcome to Apple',
        'Welcome to Java',
        'Welcome to the end.'
    ]
    written = write_messages_to_file(dest, msgs)
    print(f"Successfully wrote {written} lines to {dest}")
