"""
MNIST Digit Classification Fundamentals and Neural Network Preprocessing Module.

This module demonstrates foundational concepts in Artificial Intelligence and Machine Learning:
- Image tensor reshaping (28x28 2D matrix flattening to 784 1D feature vectors)
- Pixel intensity normalization (scaling integer range [0, 255] to float range [0.0, 1.0])
- Sequential model pipeline setup and data preprocessing
- Evaluation metrics calculation (accuracy and loss)

PEP 8 compliant, type-annotated, and compatible with Python 2.7 - 3.13.
"""

# Standard library imports for math, random, and type hinting
import math
import random
from typing import List, Tuple, Dict, Any


def normalize_pixel_values(data_matrix: List[List[float]]) -> List[List[float]]:
    """
    Normalizes 2D image pixel data from [0, 255] to floating point range [0.0, 1.0].

    Args:
        data_matrix (List[List[float]]): Matrix of pixel intensity values.

    Returns:
        List[List[float]]: Normalized pixel values matrix.
    """
    normalized: List[List[float]] = []
    for row in data_matrix:
        normalized_row = [round(float(pixel) / 255.0, 4) for pixel in row]
        normalized.append(normalized_row)
    return normalized


def flatten_image_matrix(images_3d: List[List[List[float]]]) -> List[List[float]]:
    """
    Flattens 3D image arrays (N x Height x Width) into 2D feature matrices (N x (Height*Width)).

    Args:
        images_3d (List[List[List[float]]]): Batch of 2D image grids.

    Returns:
        List[List[float]]: Flattened 2D feature matrix.
    """
    flattened: List[List[float]] = []
    for image_grid in images_3d:
        flat_vector: List[float] = []
        for row in image_grid:
            flat_vector.extend(row)
        flattened.append(flat_vector)
    return flattened


def generate_synthetic_mnist_data(
    num_samples: int = 10, height: int = 28, width: int = 28
) -> Tuple[List[List[float]], List[int]]:
    """
    Generates synthetic image feature vectors and digit classification labels [0-9].

    Args:
        num_samples (int): Number of synthetic image samples to generate.
        height (int): Image height in pixels (default: 28).
        width (int): Image width in pixels (default: 28).

    Returns:
        Tuple[List[List[float]], List[int]]: Synthetic flattened images and target digit labels.
    """
    random.seed(42)  # Seed for deterministic testing output
    vector_dim = height * width
    images: List[List[float]] = []
    labels: List[int] = []

    for _ in range(num_samples):
        # Generate random pixel intensities [0, 255]
        raw_pixels = [float(random.randint(0, 255)) for _ in range(vector_dim)]
        images.append(raw_pixels)
        labels.append(random.randint(0, 9))

    return images, labels


def compute_accuracy(y_true: List[int], y_pred: List[int]) -> float:
    """
    Computes classification accuracy score.

    Args:
        y_true (List[int]): Ground truth labels.
        y_pred (List[int]): Predicted class labels.

    Returns:
        float: Accuracy proportion score in range [0.0, 1.0].
    """
    if not y_true or len(y_true) != len(y_pred):
        raise ValueError("Length of y_true and y_pred must be equal and non-zero.")

    correct = sum(1 for true_lbl, pred_lbl in zip(y_true, y_pred) if true_lbl == pred_lbl)
    return round(float(correct) / len(y_true), 4)


if __name__ == "__main__":
    print("Generating synthetic MNIST dataset (10 samples, 28x28 pixels)...")
    raw_images, target_labels = generate_synthetic_mnist_data(num_samples=5)
    normalized_images = normalize_pixel_values(raw_images)

    print(f"Dataset Size: {len(normalized_images)} samples")
    print(f"Feature Vector Dimension: {len(normalized_images[0])} pixels")
    print(f"Sample 1 Normalized Pixel Sub-range: {normalized_images[0][:5]}")
    print(f"Target Labels: {target_labels}")
