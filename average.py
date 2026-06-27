def calculate_average(numbers):
    """Return the arithmetic mean of numbers. Returns 0.0 for an empty list."""
    if not numbers:
        return 0.0
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def main():
    data = [10, 20, 30, 40, 50]
    print("Average is:", calculate_average(data))

    empty_data = []
    print("Average of empty list is:", calculate_average(empty_data))


if __name__ == "__main__":
    main()

