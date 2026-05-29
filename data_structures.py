def sum_of_squares(numbers: list[int]) -> int:
    return sum(n * n for n in numbers)


def filter_greater_than(numbers: list[int], threshold: int) -> list[int]:
    return [n for n in numbers if n > threshold]


def unique_names(names: list[str]) -> list[str]:
    seen: set[str] = set()
    unique: list[str] = []
    for name in names:
        if name not in seen:
            seen.add(name)
            unique.append(name)
    return unique


def main() -> None:
    numbers = [1, 2, 2, 3, 4, 5]
    names = ["Ava", "Liam", "Ava", "Noah", "Mia", "Noah"]

    print("Sum of squares:", sum_of_squares(numbers))
    print("Greater than 3:", filter_greater_than(numbers, 3))
    print("Unique names:", unique_names(names))

    student_scores = {"Ava": 85, "Liam": 92, "Noah": 78}
    print("Student scores:", student_scores)
    print("Top scorer:", max(student_scores, key=student_scores.get))


if __name__ == "__main__":
    main()
