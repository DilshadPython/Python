# Socket Programming & Networking Master Module

Welcome to the **Socket Programming & Networking Module**, a production-grade educational reference detailing low-level TCP socket communication (`socket.AF_INET`, `socket.SOCK_STREAM`), HTTP protocol parsing, high-level URL retrieval via `urllib.request`, unit testing, and Python version evolutions from **Python 2.7 to Python 3.13**.

---

## 📌 Table of Contents

1. [Overview & Technical Architecture](#-overview--technical-architecture)
2. [Directory Structure & Module Overview](#-directory-structure--module-overview)
3. [How to Run the Code](#-how-to-run-the-code)
4. [Running Unit Tests](#-running-unit-tests)
5. [Python 3.3 to 3.13 Version Evolution Matrix (with Python 2.7 Context)](#-python-33-to-313-version-evolution-matrix-with-python-27-context)
6. [Python `range()` Sequence Mechanics & Introspection (`dir(range)`)](#-python-range-sequence-mechanics--introspection-dirrange)

---

## 🌐 Overview & Technical Architecture

### 1. Low-Level TCP Sockets (`socket`) vs High-Level (`urllib.request`)

Socket programming provides direct access to network communication primitives:
- **Low-Level Socket API (`socket`)**: Operates directly at the TCP transport layer. Manages host binding (`bind`), listening backlog (`listen`), accepting client sockets (`accept`), transmitting raw byte streams (`sendall`), and buffer chunk reception (`recv`).
- **High-Level URL API (`urllib.request`)**: Abstracts away raw socket creation, connection handshakes, HTTP request line crafting, and byte buffer decoding into high-level file-like objects (`urlopen()`).

```python
# Low-Level BSD Socket HTTP GET Request:
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(('127.0.0.1', 8001))
    client_socket.sendall(b"GET /readme.txt HTTP/1.0\r\n\r\n")
    response_data = client_socket.recv(4096)

# High-Level urllib URL Retrieval:
import urllib.request
with urllib.request.urlopen("http://127.0.0.1:8001/readme.txt") as response:
    content = response.read().decode("utf-8")
```

---

## 📁 Directory Structure & Module Overview

```text
socket_programming/
├── README.md                   # Master documentation and evolution guide
├── server.py                   # Modular TCP socket HTTP web server
├── client_socket.py            # Local TCP socket HTTP client fetcher
├── sockets.py                  # Remote HTTP client fetcher (data.pr4e.org)
├── urllib_request.py           # High-level HTTP fetcher using urllib.request
├── readme.txt                  # HTML sample resource fixture
└── test_socket_programming.py  # Unit test suite verifying socket I/O & urllib
```

| File Name | Purpose & Functionality | Key Functions |
| :--- | :--- | :--- |
| `server.py` | TCP socket HTTP web server with `SO_REUSEADDR` | `build_http_response()`, `run_http_server()` |
| `client_socket.py` | Low-level TCP HTTP GET client | `fetch_http_page()` |
| `sockets.py` | Remote TCP HTTP client | `fetch_remote_page()` |
| `urllib_request.py` | High-level `urllib.request` URL fetcher | `fetch_url_content()` |
| `test_socket_programming.py` | Unit test suite (unittest framework) | `TestSocketProgramming` |

---

## 🚀 How to Run the Code

### 1. Start the HTTP Web Server
In your first terminal tab:
```bash
python3 server.py
# Output: Server active and listening on http://127.0.0.1:8001
```

### 2. Run the Clients
In a second terminal tab:
```bash
# Run low-level TCP socket client
python3 client_socket.py

# Run high-level urllib fetcher
python3 urllib_request.py

# Run remote socket client
python3 sockets.py
```

---

## 🧪 Running Unit Tests

Execute unit tests via `unittest` or `pytest`:

```bash
# Run unittest suite directly
python3 -m unittest test_socket_programming.py

# Run with pytest from repository root
pytest socket_programming/
```

---

## ⚡ Python 3.3 to 3.13 Version Evolution Matrix (with Python 2.7 Context)

| Python Version | Language Features & Syntax Additions | Standard Library & Networking Evolution | Python 2.7 Context Comparison |
| :--- | :--- | :--- | :--- |
| **Python 2.7** | Legacy baseline syntax | `urllib`, `urllib2`, `httplib` separate modules | `urllib2.urlopen()`, `import socket`, `socket.error`. |
| **Python 3.3** | `yield from` (PEP 380), `u'str'` syntax | Reorganized `urllib.request`, `socket.create_connection()` | Unified `urllib` package hierarchy; explicit bytes required for `send()`. |
| **Python 3.4** | `pathlib.Path`, `enum.Enum` | `asyncio` introduced (PEP 3156) for async socket I/O | Event loop network sockets (`asyncio.start_server`). |
| **Python 3.5** | Type Hints (`typing`), `async`/`await` | Native `async def` socket coroutines, `socket.socketpair()` | Type signatures for socket parameters (`host: str, port: int`). |
| **Python 3.6** | F-strings `f"{var}"`, PEP 506 `secrets` | Socket `sendfile()` high-performance zero-copy transfer | Fast string formatting for HTTP request headers (`f"GET {path} HTTP/1.0"`). |
| **Python 3.7** | `@dataclass`, `breakpoint()` built-in | `asyncio.run()` high-level runner for socket servers | Standardized async socket lifecycle management. |
| **Python 3.8** | Walrus operator `:=`, Positional-only `/` | Socket `timeout` parameter improvements | Concise socket read loops: `while (data := sock.recv(512)):`. |
| **Python 3.9** | Dict Union `|`, Built-in generics `list[str]` | IPv6 scope ID support in `socket.getaddrinfo()` | Native generic collection type annotations (`list[bytes]`). |
| **Python 3.10**| Pattern Matching `match/case` (PEP 634) | Union operator `X \| Y` for socket exception handling | Match statements for HTTP response status codes. |
| **Python 3.11**| Faster CPython (10-60% runtime speedup) | Adaptive bytecode interpreter for socket loop execution | Reduced latency for socket buffer decoding operations. |
| **Python 3.12**| Syntactic `type` statements, `@override` | Improved `asyncio` task group socket server management | Enhanced socket tracebacks and formal type statements. |
| **Python 3.13**| Free-threaded GIL-free CPython, Tier 2 JIT | `TypeIs`, `ReadOnly`, GIL-free parallel socket threads | High-concurrency multi-threaded TCP servers without GIL lock contention. |

---

## 🔢 Python `range()` Sequence Mechanics & Introspection (`dir(range)`)

Socket buffer iteration and connection retry loops often utilize `range()` sequence objects:

```python
# Retrying socket connections using range()
for attempt in range(1, 4):
    try:
        fetch_http_page(port=8001)
        break
    except ConnectionRefusedError:
        print(f"Connection attempt {attempt} failed, retrying...")
```

### Range Performance & Memory Notes
1. **Python 2.7 vs Python 3.x**:
   - In Python 2.7, `range(1_000_000)` constructed an eager list of 1,000,000 integer objects in RAM (~8 MB).
   - In Python 3.0+, `xrange()` was removed, and `range()` became an immutable sequence object operating with constant $O(1)$ memory (48 bytes).
2. **$O(1)$ Containment Testing**:
   - Evaluating `500 in range(1_000_000)` computes using constant-time arithmetic evaluation.

### Attributes and Methods Inspection (`dir(range)`)

Inspecting `dir(range)` shows standard sequence methods:

```python
r = range(8000, 8010, 2)
print(r.start)  # Output: 8000
print(r.stop)   # Output: 8010
print(r.step)   # Output: 2

print(r.index(8004))  # Output: 2
print(r.count(8002))  # Output: 1
```

Public methods returned by `dir(range)`:
- **`start`**, **`stop`**, **`step`**: Range sequence boundaries.
- **`index(x)`**: Returns index of element $x$ in range ($O(1)$ calculation).
- **`count(x)`**: Returns count of occurrences of $x$ (0 or 1).
- **`__contains__(x)`**: Evaluates membership `x in range` in $O(1)$ time.
