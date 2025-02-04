import numpy as np


def norm(A, B):
    """
    Takes two Numpy column arrays, A and B, and returns the L2 norm of their
    sum.

    Arg:
      A - a Numpy array
      B - a Numpy array
    Returns:
      s - the L2 norm of A+B.
    """
    sum_array = A + B
    s = np.linalg.norm(sum_array)

    return s


def main():
    # Input for the column arrays
    A = np.array(list(map(float, input(
        "Enter the elements of array A (separated by spaces): ").split()))).reshape(-1, 1)
    B = np.array(list(map(float, input(
        "Enter the elements of array B (separated by spaces): ").split()))).reshape(-1, 1)

    # Calculate the L2 norm of the sum
    result = norm(A, B)

    # Print the result
    print(f"L2 norm of the sum of A and B: {result}")


if __name__ == "__main__":
    main()
