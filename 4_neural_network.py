import numpy as np


def neural_network(inputs, weights):
    """
    Takes an input vector and runs it through a 1-layer neural network
    with a given weight matrix and returns the output.

    Arg:
      inputs - 2 x 1 NumPy array
      weights - 2 x 1 NumPy array
    Returns (in this order):
      out - a 1 x 1 NumPy array, representing the output of the neural network
    """
    z = np.dot(weights.T, inputs)
    out = np.tanh(z)

    return out


def main():
    # Input for the neural network
    inputs = np.array([float(input("Enter input 1: ")), float(
        input("Enter input 2: "))]).reshape(2, 1)
    weights = np.array([float(input("Enter weight 1: ")),
                       float(input("Enter weight 2: "))]).reshape(2, 1)

    # Get the output from the neural network
    output = neural_network(inputs, weights)

    # Print the result
    print(f"Output of the neural network: {output}")


if __name__ == "__main__":
    main()
