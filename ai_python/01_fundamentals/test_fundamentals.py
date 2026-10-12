"""
Unit Test Suite for AI Fundamentals and MNIST Preprocessing Module.

Tests pixel normalization scaling, image matrix flattening, synthetic dataset generation,
and classification accuracy calculations.
"""

import unittest
from mnist_classifier_basics import (
    compute_accuracy,
    flatten_image_matrix,
    generate_synthetic_mnist_data,
    normalize_pixel_values,
)


class TestAiFundamentals(unittest.TestCase):
    """Test cases for pixel normalization, flattening, and classification metrics."""

    def test_normalize_pixel_values(self) -> None:
        """Verify pixel intensity scaling from [0, 255] to [0.0, 1.0]."""
        raw_matrix = [[0.0, 127.5, 255.0]]
        normalized = normalize_pixel_values(raw_matrix)
        self.assertEqual(normalized[0][0], 0.0)
        self.assertAlmostEqual(normalized[0][1], 0.5, places=3)
        self.assertEqual(normalized[0][2], 1.0)

    def test_flatten_image_matrix(self) -> None:
        """Verify 3D grid flattening into 2D feature vectors."""
        image_3d = [
            [[1.0, 2.0], [3.0, 4.0]],  # 2x2 grid
        ]
        flattened = flatten_image_matrix(image_3d)
        self.assertEqual(len(flattened), 1)
        self.assertEqual(flattened[0], [1.0, 2.0, 3.0, 4.0])

    def test_generate_synthetic_mnist_data(self) -> None:
        """Verify synthetic MNIST dataset generation shape and label bounds."""
        images, labels = generate_synthetic_mnist_data(num_samples=5, height=28, width=28)
        self.assertEqual(len(images), 5)
        self.assertEqual(len(images[0]), 784)  # 28 * 28
        self.assertEqual(len(labels), 5)
        self.assertTrue(all(0 <= lbl <= 9 for lbl in labels))

    def test_compute_accuracy(self) -> None:
        """Verify classification accuracy computation."""
        y_true = [0, 1, 2, 3, 4]
        y_pred = [0, 1, 2, 9, 4]  # 4 out of 5 correct
        score = compute_accuracy(y_true, y_pred)
        self.assertEqual(score, 0.8)

    def test_compute_accuracy_invalid_lengths(self) -> None:
        """Verify ValueError is raised when label vector lengths mismatch."""
        with self.assertRaises(ValueError):
            compute_accuracy([1, 2], [1])


if __name__ == "__main__":
    unittest.main()
