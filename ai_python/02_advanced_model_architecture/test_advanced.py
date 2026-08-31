"""
Unit Test Suite for Advanced Neural Network Architecture Module.

Tests ReLU and Softmax activation output bounds, DenseLayer forward matrix transformation,
and SequentialModel prediction routines.
"""

import unittest
from advanced_neural_network import DenseLayer, SequentialModel, relu, softmax


class TestAdvancedNeuralNetwork(unittest.TestCase):
    """Test cases for activation math, DenseLayer, and SequentialModel forward pass."""

    def test_relu_activation(self) -> None:
        """Verify ReLU returns 0 for negative values and identity for positive values."""
        self.assertEqual(relu(-5.0), 0.0)
        self.assertEqual(relu(0.0), 0.0)
        self.assertEqual(relu(3.5), 3.5)

    def test_softmax_activation(self) -> None:
        """Verify Softmax outputs sum to 1.0 and produce positive probabilities."""
        logits = [2.0, 1.0, 0.1]
        probs = softmax(logits)
        self.assertEqual(len(probs), 3)
        self.assertAlmostEqual(sum(probs), 1.0, places=4)
        self.assertTrue(all(0.0 <= p <= 1.0 for p in probs))

    def test_dense_layer_forward(self) -> None:
        """Verify DenseLayer output shape and linear projection."""
        layer = DenseLayer(input_dim=4, output_dim=2, activation="relu")
        input_vec = [1.0, 0.5, -0.5, 2.0]
        out_vec = layer.forward(input_vec)
        self.assertEqual(len(out_vec), 2)
        self.assertTrue(all(v >= 0.0 for v in out_vec))  # ReLU non-negativity

    def test_dense_layer_invalid_input(self) -> None:
        """Verify ValueError is raised on mismatched input dimension."""
        layer = DenseLayer(input_dim=4, output_dim=2)
        with self.assertRaises(ValueError):
            layer.forward([1.0, 2.0])

    def test_sequential_model_prediction(self) -> None:
        """Verify SequentialModel forward propagation through multi-layer pipeline."""
        layer1 = DenseLayer(input_dim=10, output_dim=5, activation="relu")
        layer2 = DenseLayer(input_dim=5, output_dim=3, activation="softmax")
        model = SequentialModel(layers=[layer1, layer2])

        dummy_input = [0.1] * 10
        probs = model.predict(dummy_input)
        predicted_cls = model.predict_class(dummy_input)

        self.assertEqual(len(probs), 3)
        self.assertAlmostEqual(sum(probs), 1.0, places=4)
        self.assertIn(predicted_cls, [0, 1, 2])


if __name__ == "__main__":
    unittest.main()
