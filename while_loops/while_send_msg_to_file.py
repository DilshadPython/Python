"""
Demonstrates appending user message inputs to a target file until sentinel 'q' is received.
"""
import os
from typing import List


def send_messages_to_file(filepath: str, inputs: List[str]) -> int:
    """Write input strings to file until encountering exit sentinel 'q'."""
    written_count = 0
    with open(filepath, 'w', encoding='utf-8') as f:
        for msg in inputs:
            if msg.strip() == 'q':
                break
            f.write(f"You entered > {msg}\n")
            written_count += 1
    return written_count


if __name__ == '__main__':
    news_path = os.path.join(os.path.dirname(__file__), 'news.txt')
    lines_written = send_messages_to_file(news_path, ['hello', '23', 'q'])
    print(f"Wrote {lines_written} entry lines to {news_path}")
