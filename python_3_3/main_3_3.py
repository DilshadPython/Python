"""
Python 3.3 Feature Demonstration
--------------------------------
Highlights:
1. `yield from` generator delegation (PEP 380)
2. `ipaddress` module for network address manipulation (PEP 3144)
3. `types.MappingProxyType` for read-only dictionary views
4. `shutil.which` for finding executable paths
"""

import ipaddress
import shutil
from types import MappingProxyType
from typing import Generator, Iterable, Any


# 1. Generator Delegation using `yield from` (PEP 380)
def sub_generator() -> Generator[str, None, str]:
    yield "Python"
    yield "3.3"
    return "Completed"


def main_generator() -> Generator[str, None, None]:
    yield "Starting..."
    # Delegate iteration directly to sub_generator
    result = yield from sub_generator()
    yield f"Sub-generator status: {result}"
    yield "Finished!"


def demo_yield_from() -> None:
    print("--- 1. Demo: yield from (PEP 380) ---")
    gen = main_generator()
    for item in gen:
        print(f"  Got: {item}")
    print()


# 2. IP Address & Network Handling (PEP 3144)
def demo_ipaddress() -> None:
    print("--- 2. Demo: ipaddress Module (PEP 3144) ---")
    net = ipaddress.ip_network("192.168.1.0/28")
    print(f"  Network: {net}")
    print(f"  Total Hosts: {net.num_addresses}")
    print(f"  Netmask: {net.netmask}")
    print(f"  Is private? {net.is_private}")
    
    # Iterate through hosts
    hosts = [str(host) for host in net.hosts()]
    print(f"  First 3 usable hosts: {hosts[:3]}")
    print()


# 3. Read-Only Dictionary View (`types.MappingProxyType`)
def demo_mapping_proxy() -> None:
    print("--- 3. Demo: MappingProxyType ---")
    writable_config = {"theme": "dark", "version": "3.3"}
    read_only_config = MappingProxyType(writable_config)
    
    print(f"  Read-Only View: {read_only_config['theme']}")
    
    # Updates to source dict reflect in proxy
    writable_config["theme"] = "light"
    print(f"  Updated source dict -> Proxy view: {read_only_config['theme']}")
    
    try:
        # Modifying proxy directly raises TypeError
        read_only_config["theme"] = "blue"  # type: ignore
    except TypeError as err:
        print(f"  Caught expected error modifying MappingProxyType: {err}")
    print()


# 4. Utility: shutil.which
def demo_shutil_which() -> None:
    print("--- 4. Demo: shutil.which ---")
    python_path = shutil.which("python3")
    print(f"  Executable location for 'python3': {python_path}")
    print()


if __name__ == "__main__":
    print("========================================")
    print("        PYTHON 3.3 FEATURE DEMO        ")
    print("========================================\n")
    demo_yield_from()
    demo_ipaddress()
    demo_mapping_proxy()
    demo_shutil_which()
