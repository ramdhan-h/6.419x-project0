def scalar_function(x, y):
    """
    Returns the f(x, y) defined in the problem statement.
    """
    if x <= y:
        return x * y
    else:
        return x / y


def main():
    # Input for x and y
    x = float(input("Enter the value of x: "))
    y = float(input("Enter the value of y: "))

    # Get the result from the scalar_function
    result = scalar_function(x, y)

    # Print the result
    print(f"The result of the scalar function f({x}, {y}) is: {result}")


if __name__ == "__main__":
    main()
