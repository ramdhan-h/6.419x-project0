import numpy as np


def operations(h, w):
    """
    Takes two inputs, h and w, and makes two Numpy arrays A and B of size
    h x w, and returns A, B, and s, the sum of A and B.

    Arg:
      h - an integer describing the height of A and B
      w - an integer describing the width of A and B
    Returns (in this order):
      A - a randomly-generated h x w Numpy array.
      B - a randomly-generated h x w Numpy array.
      s - the sum of A and B.
    """
    A = np.random.rand(h, w)
    B = np.random.rand(h, w)
    s = A + B

    return A, B, s


def main():
    # Input for matrix dimensions
    h = int(input("Enter the number of rows (h): "))
    w = int(input("Enter the number of columns (w): "))

    # Get matrices A, B, and their sum
    A, B, s = operations(h, w)

    # Print the results
    print("\nMatrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    print("\nSum of A and B:")
    print(s)


if __name__ == "__main__":
    main()
