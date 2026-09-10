"""
Remote Web Resource TCP Socket Client.

This module demonstrates retrieving web pages over port 80 using raw TCP socket calls.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import socket`: Low-level socket interface for network socket operations.
# - `import sys`: System utilities for execution status.
# =========================================================================
import socket
import sys


def fetch_remote_page(
    domain: str = "data.pr4e.org",
    port: int = 80,
    resource: str = "/page1.htm",
) -> str:
    """Connect to a remote web server via socket and return page content.

    Args:
        domain (str): Remote host domain name. Defaults to "data.pr4e.org".
        port (int): Remote HTTP port. Defaults to 80.
        resource (str): Resource path. Defaults to "/page1.htm".

    Returns:
        str: Decoded HTTP response string.
    """
    cmd = f"GET http://{domain}{resource} HTTP/1.0\r\n\r\n".encode("utf-8")
    chunks: list[str] = []

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((domain, port))
        client_socket.sendall(cmd)

        while True:
            data = client_socket.recv(512)
            if not data:
                break
            chunks.append(data.decode("utf-8", errors="replace"))

    return "".join(chunks)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for remote socket client."""
    print("=== Remote Web Server TCP Socket Client ===")
    try:
        content = fetch_remote_page()
        print(content)
    except socket.gaierror as err:
        print(f"Network error resolving host: {err}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
