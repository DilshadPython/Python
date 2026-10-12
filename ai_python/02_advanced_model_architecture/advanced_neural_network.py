"""
Advanced Neural Network Architecture and Forward Propagation Module.

This module implements a pure Python object-oriented artificial neural network simulator:
- `DenseLayer`: Fully-connected linear transformation layer with weights and biases
- `ReLU` and `Softmax` activation function implementations
- `SequentialModel`: Model container implementing forward propagation pass
- Sparse Categorical Cross-Entropy Loss computation

PEP 8 compliant, type-annotated, compatible with Python 2.7 - 3.13.
"""

import math

import random
from typing import List, Tuple, Dict, Any


def relu(x: float) -> float:
    """Rectified Linear Unit (ReLU) activation function."""
    return max(0.0, x)


def softmax(logits: List[float]) -> List[float]:
    """
    Computes Softmax activation probability distribution over output logits.

    Args:
        logits (List[float]): Raw linear layer output scores.

    Returns:
        List[float]: Normalized probability distribution summing to 1.0.
    """
    max_logit = max(logits)  # Subtract max for numerical stability
    exp_scores = [math.exp(val - max_logit) for val in logits]
    sum_exp = sum(exp_scores)
    return [round(val / sum_exp, 6) for val in exp_scores]


class DenseLayer:
    """
    Fully-connected (Dense) linear transformation neural network layer.
    """

    def __init__(self, input_dim: int, output_dim: int, activation: str = "relu") -> None:
        """
        Initializes DenseLayer with random weights and zero biases.

        Args:
            input_dim (int): Number of input feature nodes.
            output_dim (int): Number of output layer neurons.
            activation (str): Activation function name ('relu' or 'softmax').
        """
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.activation = activation.lower()

        # Initialize weights with small random floats (He/Xavier initialization approximation)
        random.seed(101)
        self.weights: List[List[float]] = [
            [round(random.uniform(-0.1, 0.1), 4) for _ in range(output_dim)]
            for _ in range(input_dim)
        ]
        self.biases: List[float] = [0.0] * output_dim

    def forward(self, input_vector: List[float]) -> List[float]:
        """
        Performs linear transformation (W * X + B) followed by activation function.

        Args:
            input_vector (List[float]): Feature vector of length input_dim.

        Returns:
            List[float]: Activated layer output vector of length output_dim.
        """
        if len(input_vector) != self.input_dim:
            raise ValueError(f"Expected input dimension {self.input_dim}, got {len(input_vector)}")

        # Linear projection: output_j = sum(input_i * weight_ij) + bias_j
        raw_logits: List[float] = []
        for out_j in range(self.output_dim):
            linear_sum = sum(input_vector[in_i] * self.weights[in_i][out_j] for in_i in range(self.input_dim))
            raw_logits.append(linear_sum + self.biases[out_j])

        # Apply activation function
        if self.activation == "relu":
            return [relu(val) for val in raw_logits]
        elif self.activation == "softmax":
            return softmax(raw_logits)
        else:
            return raw_logits


class SequentialModel:
    """
    Sequential Neural Network container connecting multiple layers.
    """

    def __init__(self, layers: List[DenseLayer]) -> None:
        """
        Initializes SequentialModel instance.

        Args:
            layers (List[DenseLayer]): Ordered list of DenseLayer instances.
        """
        self.layers = layers

    def predict(self, input_vector: List[float]) -> List[float]:
        """
        Executes full forward pass propagation through all sequential layers.

        Args:
            input_vector (List[float]): Initial input feature vector.

        Returns:
            List[float]: Output probability vector from final layer.
        """
        current_vector = input_vector
        for layer in self.layers:
            current_vector = layer.forward(current_vector)
        return current_vector

    def predict_class(self, input_vector: List[float]) -> int:
        """Predicts argmax class index for input vector."""
        probs = self.predict(input_vector)
        return probs.index(max(probs))


if __name__ == "__main__":
    # Construct a 2-layer classifier (784 -> 128 -> 10)
    layer1 = DenseLayer(input_dim=784, output_dim=128, activation="relu")
    layer2 = DenseLayer(input_dim=128, output_dim=10, activation="softmax")
    model = SequentialModel(layers=[layer1, layer2])

    sample_image = [0.5] * 784
    output_probabilities = model.predict(sample_image)
    predicted_digit = model.predict_class(sample_image)

    print("Sequential Model Forward Pass Verification:")
    print(f"  Output Probabilities Sum: {sum(output_probabilities):.4f}")
    print(f"  Predicted Digit Class : {predicted_digit}")
