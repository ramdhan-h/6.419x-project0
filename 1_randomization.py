import numpy as np


def randomization(n):
    """
    Arg:
      n - an integer
    Returns:
      A - a randomly-generated nx1 Numpy array.
    """
    A = np.random.rand(n).reshape(-1, 1)
    return A


def main():
    n = int(input("Enter a positive integer: "))
    result = randomization(n)
    print(f"Random {n}x1 Numpy array:\n{result}")


if __name__ == "__main__":
    main()
