"""
File Handling & I/O: Binary File Operations

This module demonstrates binary file operations (`'rb'`, `'wb'`, `'ab'`):
- Reading and writing raw byte buffers (`bytes`, `bytearray`).
- Chunked file copying to prevent memory exhaustion on large binary assets.
- Header magic number inspection (e.g. PNG, GIF, JPEG signatures).
"""
import os
from typing import Tuple


def write_binary_data(filepath: str, data: bytes) -> int:
    """
    Writes raw bytes to a file in binary write ('wb') mode.

    Args:
        filepath (str): Target binary file path.
        data (bytes): Byte buffer to write.

    Returns:
        int: Number of bytes written.
    """
    with open(filepath, "wb") as f:
        return f.write(data)


def read_binary_data(filepath: str) -> bytes:
    """
    Reads the complete contents of a binary file into bytes ('rb' mode).

    Args:
        filepath (str): Binary file path to read.

    Returns:
        bytes: Raw byte buffer.
    """
    with open(filepath, "rb") as f:
        return f.read()


def copy_binary_file_chunked(src_path: str, dest_path: str, chunk_size: int = 4096) -> int:
    """
    Copies a binary file using fixed-size chunks to minimize memory footprint.

    Args:
        src_path (str): Source file path.
        dest_path (str): Destination file path.
        chunk_size (int): Size of buffer chunk in bytes (default: 4KB).

    Returns:
        int: Total number of bytes copied.
    """
    total_bytes = 0
    with open(src_path, "rb") as src, open(dest_path, "wb") as dest:
        while True:
            chunk = src.read(chunk_size)
            if not chunk:
                break
            dest.write(chunk)
            total_bytes += len(chunk)
    return total_bytes


def inspect_binary_header(filepath: str, num_bytes: int = 8) -> Tuple[bytes, str]:
    """
    Reads the header byte signature of a file for magic number identification.

    Args:
        filepath (str): File path to inspect.
        num_bytes (int): Number of header bytes to read.

    Returns:
        Tuple[bytes, str]: (Raw bytes header, Hexadecimal representation).
    """
    with open(filepath, "rb") as f:
        header = f.read(num_bytes)
        hex_rep = " ".join(f"{b:02X}" for b in header)
        return header, hex_rep


def main() -> None:
    """Demonstrates binary file operations."""
    print("=" * 60)
    print("2. Binary File Operations (`rb`, `wb`, chunked copying)")
    print("=" * 60)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    sample_bin = os.path.join(base_dir, "sample.bin")
    copy_bin = os.path.join(base_dir, "sample_copy.bin")

    # Sample binary data (Header + bytes)
    sample_bytes = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01"

    # 1. Write binary data
    bytes_written = write_binary_data(sample_bin, sample_bytes)
    print(f"\n1. Wrote {bytes_written} raw bytes to {sample_bin}")

    # 2. Inspect magic number header
    raw_header, hex_header = inspect_binary_header(sample_bin, 8)
    print(f"2. Header Inspection: Raw={raw_header!r}, Hex=[{hex_header}]")

    # 3. Chunked file copy
    copied_bytes = copy_binary_file_chunked(sample_bin, copy_bin, chunk_size=8)
    print(f"3. Copied {copied_bytes} bytes to {copy_bin} using 8-byte chunks.")


if __name__ == "__main__":
    main()
