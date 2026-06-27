def calculate_average(numbers):
    """Return the arithmetic mean of numbers. Returns 0.0 for an empty list."""
    if not numbers:
        return 0.0
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def divide_numbers(a, b):
    """Return a / b, or None if b is zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return None


def hello():
    print("Hello World")


def demo_average():
    data = [10, 20, 30, 40, 50]
    print("Average is:", calculate_average(data))

    empty_data = []
    print("Average of empty list is:", calculate_average(empty_data))


def demo_divide():
    numbers = [10, 0, 5]
    for n in numbers:
        result = divide_numbers(100, n)
        if result is None:
            print("Cannot divide by", n, "- division by zero")
        else:
            print("100 divided by", n, "=", result)


if __name__ == "__main__":
    # Simple dispatcher to show functionality when running this file directly
    hello()
    demo_average()
    demo_divide()

