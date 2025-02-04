import pdb


def get_sum_metrics(predictions, metrics=None):
    """
    Computes and sums up all the metric functions applied to the prediction.

    Args:
    predictions - A single numeric prediction value.
    metrics - A list of functions that take a number and return a number.

    Returns:
    sum_metrics - The sum of all metric function outputs.
    """
    # pdb.set_trace()
    if metrics is None:  # Fix mutable default argument issue
        metrics = []

    for i in range(3):
        # pdb.set_trace()
        metrics.append(lambda x, i=i: x + i)  # Capture i correctly

    sum_metrics = sum(metric(predictions) for metric in metrics)

    return sum_metrics


def main():
    print(get_sum_metrics(0))  # Should be (0 + 0) + (0 + 1) + (0 + 2) = 3
    print(get_sum_metrics(1))  # Should be (1 + 0) + (1 + 1) + (1 + 2) = 6
    print(get_sum_metrics(2))  # Should be (2 + 0) + (2 + 1) + (2 + 2) = 9
    # Should be (3) + (3 + 0) + (3 + 1) + (3 + 2) = 15
    print(get_sum_metrics(3, [lambda x: x]))
    print(get_sum_metrics(0))  # Should be (0 + 0) + (0 + 1) + (0 + 2) = 3
    print(get_sum_metrics(1))  # Should be (1 + 0) + (1 + 1) + (1 + 2) = 6
    print(get_sum_metrics(2))  # Should be (2 + 0) + (2 + 1) + (2 + 2) = 9


if __name__ == "__main__":
    main()
