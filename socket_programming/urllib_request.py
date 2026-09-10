"""
High-Level HTTP URL Fetching Module (`urllib.request`).

This module demonstrates retrieving web content using CPython's standard high-level
`urllib.request` library, abstracting away raw TCP socket management.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System utilities for process exit code management.
# - `import urllib.error`: Standard library HTTP/URL error exception classes.
# - `import urllib.request`: High-level URL opening and request handling library.
# =========================================================================
import sys
import urllib.error
import urllib.request


def fetch_url_content(url: str = "http://127.0.0.1:8001/readme.txt") -> str:
    """Fetch URL text content using urllib.request.urlopen.

    Args:
        url (str): Target URL string. Defaults to local server URL.

    Returns:
        str: Decoded string content of the response.

    Raises:
        urllib.error.URLError: If connection fails or URL is invalid.
    """
    lines: list[str] = []
    with urllib.request.urlopen(url, timeout=5) as response:
        for line in response:
            lines.append(line.decode("utf-8", errors="replace").strip())

    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for urllib HTTP fetcher."""
    print("=== High-Level urllib.request HTTP Fetcher ===")
    target_url = argv[0] if argv else "http://127.0.0.1:8001/readme.txt"

    try:
        content = fetch_url_content(target_url)
        print(f"Content retrieved from '{target_url}':")
        print(content)
    except urllib.error.URLError as err:
        print(f"Failed to fetch '{target_url}': {err}")
        print("Note: Ensure local HTTP server is running via 'python3 server.py'")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())