"""
Unit Test Suite for `socket_programming` Modules.

This test suite verifies:
1. `build_http_response()` formatting and status codes.
2. Low-level TCP socket client/server communication using a background server thread.
3. `urllib_request.fetch_url_content()` functionality against a test socket server.
"""

import threading
import time
import unittest

# Support both package and local directory import paths
try:
    from socket_programming.server import build_http_response, run_http_server
    from socket_programming.client_socket import fetch_http_page
    from socket_programming.urllib_request import fetch_url_content
except ImportError:
    from server import build_http_response, run_http_server
    from client_socket import fetch_http_page
    from urllib_request import fetch_url_content


class TestSocketProgramming(unittest.TestCase):
    """Test suite for TCP socket server, socket client, and urllib fetcher."""

    TEST_HOST = "127.0.0.1"
    TEST_PORT = 8099

    def test_build_http_response(self) -> None:
        """Verify build_http_response encodes headers and HTML body properly."""
        body = "<h2>Test Page</h2>"
        response = build_http_response(body_html=body, status_code=200)

        self.assertIsInstance(response, bytes)
        decoded = response.decode("utf-8")
        self.assertIn("HTTP/1.1 200 OK", decoded)
        self.assertIn("Content-Type: text/html", decoded)
        self.assertIn("<h2>Test Page</h2>", decoded)

    def test_socket_client_server_integration(self) -> None:
        """Verify client-server TCP communication over localhost thread server."""
        # Start server in background daemon thread (handles 1 request and exits)
        server_thread = threading.Thread(
            target=run_http_server,
            kwargs={
                "host": self.TEST_HOST,
                "port": self.TEST_PORT,
                "single_request_only": True,
            },
            daemon=True,
        )
        server_thread.start()

        # Give server time to bind and listen
        time.sleep(0.1)

        # Execute client fetch request
        response_text = fetch_http_page(
            host=self.TEST_HOST,
            port=self.TEST_PORT,
            resource_path="/readme.txt",
        )

        self.assertIn("HTTP/1.1 200 OK", response_text)
        self.assertIn("Welcome to Python Server", response_text)
        server_thread.join(timeout=1.0)

    def test_urllib_request_integration(self) -> None:
        """Verify urllib.request fetches response content from background socket server."""
        port = self.TEST_PORT + 1

        server_thread = threading.Thread(
            target=run_http_server,
            kwargs={
                "host": self.TEST_HOST,
                "port": port,
                "single_request_only": True,
            },
            daemon=True,
        )
        server_thread.start()
        time.sleep(0.1)

        url = f"http://{self.TEST_HOST}:{port}/readme.txt"
        content = fetch_url_content(url)

        self.assertIn("Welcome to Python Server", content)
        server_thread.join(timeout=1.0)


if __name__ == "__main__":
    unittest.main()
