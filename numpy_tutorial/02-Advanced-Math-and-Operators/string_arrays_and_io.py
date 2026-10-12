"""
NumPy String Arrays and I/O Operations Module.

This module demonstrates:
- Manipulating string arrays using np.char functions (uppercase, lower, strip, replace).
- Binary array persistence with np.save, np.load, and np.savez compressed archives.
- Text matrix input/output using np.savetxt and np.loadtxt.
"""

# Import pathlib for safe temporary file path handling
from pathlib import Path

# Import numpy for string array routines and persistence methods
import numpy as np


def demonstrate_string_array_operations() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Perform string operations on NumPy character arrays.

    Returns:
        tuple[np.ndarray, np.ndarray, np.ndarray]: Uppercased, replaced, and boolean compared arrays.
    """
    car_brands = np.array(["Toyota", "Honda", "Ford", "Chevrolet", "BMW", "Audi"])

    # Convert elements to uppercase using np.char.upper
    upper_cars: np.ndarray = np.char.upper(car_brands)

    # Replace substring within character elements
    replaced_cars: np.ndarray = np.char.replace(car_brands, "o", "0")

    # Vectorized equality check
    is_ford: np.ndarray = np.char.equal(car_brands, "Ford")

    return upper_cars, replaced_cars, is_ford


def save_and_load_binary_array(data: np.ndarray, file_path: Path) -> np.ndarray:
    """Save array to binary format (.npy) and reload it.

    Args:
        data (np.ndarray): Target array to save.
        file_path (Path): Path destination for saving.

    Returns:
        np.ndarray: Reloaded NumPy array.
    """
    np.save(file_path, data)
    loaded_array: np.ndarray = np.load(file_path)
    return loaded_array


def save_and_load_text_matrix(matrix: np.ndarray, file_path: Path) -> np.ndarray:
    """Save 2D matrix to text file and reload it.

    Args:
        matrix (np.ndarray): Numeric matrix.
        file_path (Path): Target text file path.

    Returns:
        np.ndarray: Reloaded floating-point matrix.
    """
    np.savetxt(file_path, matrix, fmt="%.4f", delimiter=",")
    loaded_matrix: np.ndarray = np.loadtxt(file_path, delimiter=",")
    return loaded_matrix


if __name__ == "__main__":
    up, rep, contains = demonstrate_string_array_operations()
    print("--- String Array Operations ---")
    print("Uppercase Cars: ", up)
    print("Replaced Cars:  ", rep)
    print("Ford Equality:  ", contains)

    temp_dir = Path("./temp_io_data")
    temp_dir.mkdir(exist_ok=True)
    bin_file = temp_dir / "sample_array.npy"
    txt_file = temp_dir / "sample_matrix.csv"

    sample_arr = np.array([10, 20, 30, 40, 50])
    loaded_bin = save_and_load_binary_array(sample_arr, bin_file)
    print("\n--- Binary I/O Check ---", np.array_equal(sample_arr, loaded_bin))

    sample_mat = np.eye(4)
    loaded_txt = save_and_load_text_matrix(sample_mat, txt_file)
    print("--- Text I/O Check ---", np.allclose(sample_mat, loaded_txt))

    # Clean up temp directory files
    bin_file.unlink(missing_ok=True)
    txt_file.unlink(missing_ok=True)
    temp_dir.rmdir()
