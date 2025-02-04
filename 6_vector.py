import numpy as np


def scalar_function(x, y):
    """
    Returns the f(x, y) defined in the problem statement.
    """
    if x <= y:
        return x * y
    else:
        return x / y


def vector_function(x, y):
    """
    Make sure vector_function can deal with vector input x, y.
    Applies the scalar function element-wise to input vectors.
    """
    vectorized_function = np.vectorize(scalar_function)

    return vectorized_function(x, y)


def main():
    # Input for x and y vectors
    x = np.array(
        list(map(float, input("Enter the elements of vector x (separated by spaces): ").split())))
    y = np.array(
        list(map(float, input("Enter the elements of vector y (separated by spaces): ").split())))

    # Get the result from the vector_function
    result = vector_function(x, y)

    # Print the result
    print(f"The result of the vector function f(x, y) is: {result}")


if __name__ == "__main__":
    main()
