import argparse


def c_to_f(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def main() -> None:
    parser = argparse.ArgumentParser(description="Temperature converter")
    parser.add_argument("--c", type=float, help="Convert Celsius to Fahrenheit")
    parser.add_argument("--f", type=float, help="Convert Fahrenheit to Celsius")
    args = parser.parse_args()

    if args.c is not None:
        print(f"{args.c:.2f} C = {c_to_f(args.c):.2f} F")
        return
    if args.f is not None:
        print(f"{args.f:.2f} F = {f_to_c(args.f):.2f} C")
        return

    demo_values = [0, 10, 25, 37, 100]
    print("Demo (C to F):")
    for value in demo_values:
        print(f"  {value:>5.1f} C -> {c_to_f(value):>6.1f} F")


if __name__ == "__main__":
    main()
