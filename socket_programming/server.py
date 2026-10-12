"""
Modular TCP Socket HTTP Server Demonstration.

This module provides a simple, single-threaded HTTP web server implementation using
CPython's standard low-level `socket` interface (`AF_INET`, `SOCK_STREAM`).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import socket`: Low-level networking interface providing BSD socket API.
# - `import sys`: System interaction and process exit code propagation.
# - `from typing import Tuple`: PEP 484 type hint annotations.
# =========================================================================
import socket
import sys
from typing import Tuple


def build_http_response(
    body_html: str = "<h1>Welcome to Python Server</h1><p>This is a paragraph.</p>",
    status_code: int = 200,
) -> bytes:
    """Construct a standard HTTP/1.1 response byte string with header metadata.

    Args:
        body_html (str): HTML body content.
        status_code (int): HTTP status code. Defaults to 200.

    Returns:
        bytes: Encoded HTTP response ready for socket transmission.
    """
    full_body_html = f"<!DOCTYPE html><html><head><title>Python Server</title></head><body>{body_html}</body></html>\r\n\r\n"
    encoded_body = full_body_html.encode("utf-8")

    response_lines = [
        f"HTTP/1.1 {status_code} OK",
        "Content-Type: text/html; charset=utf-8",
        f"Content-Length: {len(encoded_body)}",
        "Connection: close",
        "",
        full_body_html,
    ]
    return "\r\n".join(response_lines).encode("utf-8")


def run_http_server(
    host: str = "127.0.0.1",
    port: int = 8001,
    max_connections: int = 5,
    single_request_only: bool = False,
) -> None:
    """Bind and run TCP socket HTTP server on specified host and port.

    Args:
        host (str): Binding host IP address. Defaults to "127.0.0.1".
        port (int): Port number. Defaults to 8001.
        max_connections (int): Maximum queued connection backlog. Defaults to 5.
        single_request_only (bool): If True, handles 1 request and exits (useful for tests).
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable address reuse to avoid 'Address already in use' socket error on restart
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((host, port))
        server_socket.listen(max_connections)
        print(f"Server active and listening on http://{host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

            with client_socket:
                request_bytes = client_socket.recv(4096)
                if request_bytes:
                    request_text = request_bytes.decode("utf-8", errors="replace")
                    first_line = request_text.splitlines()[0] if request_text.splitlines() else "EMPTY"
                    print(f"Received Request: {first_line}")

                    response_bytes = build_http_response()
                    client_socket.sendall(response_bytes)
                    client_socket.shutdown(socket.SHUT_WR)

            if single_request_only:
                break

    except KeyboardInterrupt:
        print("\nServer shutting down gracefully via KeyboardInterrupt...")
    except Exception as exc:
        print(f"Server runtime error: {exc}")
    finally:
        server_socket.close()
        print("Server socket closed.")


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for HTTP server."""
    print("=== Low-Level Python Socket HTTP Server ===")
    run_http_server()
    return 0


if __name__ == "__main__":
    sys.exit(main())