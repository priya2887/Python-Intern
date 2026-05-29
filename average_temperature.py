def average(values: list[float]) -> float:
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def main() -> None:
    temperatures = [28.5, 29.0, 30.2, 31.5, 29.8, 27.9, 28.3]
    avg = average(temperatures)
    print(f"Average temperature for the week: {avg:.2f} C")


if __name__ == "__main__":
    main()
