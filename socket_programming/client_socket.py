"""
Low-Level TCP Socket HTTP Client Demonstration.

This module demonstrates low-level TCP socket communication by crafting an HTTP GET
request payload, transmitting it over a socket stream, and decoding the server response.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import socket`: Low-level BSD socket interface for TCP/IP networking.
# - `import sys`: System utilities for CLI argument processing.
# - `from typing import Tuple`: PEP 484 type annotations.
# =========================================================================
import socket
import sys
from typing import Tuple


def fetch_http_page(
    host: str = "127.0.0.1",
    port: int = 8001,
    resource_path: str = "/readme.txt",
    buffer_size: int = 512,
) -> str:
    """Send an HTTP 1.0 GET request over a TCP socket and return decoded response text.

    Args:
        host (str): Destination hostname or IP address. Defaults to "127.0.0.1".
        port (int): Port number. Defaults to 8001.
        resource_path (str): Target resource path. Defaults to "/readme.txt".
        buffer_size (int): Socket chunk receive size in bytes. Defaults to 512.

    Returns:
        str: Accumulated response string.
    """
    request_command = f"GET http://{host}:{port}{resource_path} HTTP/1.0\r\n\r\n".encode("utf-8")

    response_chunks: list[str] = []
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(request_command)

        while True:
            data = client_socket.recv(buffer_size)
            if not data:
                break
            response_chunks.append(data.decode("utf-8", errors="replace"))

    return "".join(response_chunks)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for low-level TCP socket client."""
    print("=== Low-Level TCP Socket Client ===")
    try:
        response = fetch_http_page()
        print("Received Server Response:")
        print(response)
    except ConnectionRefusedError:
        print("Error: Could not connect to server at 127.0.0.1:8001.")
        print("Please start the server first by running: python3 server.py")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
