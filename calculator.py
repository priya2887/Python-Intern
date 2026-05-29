import argparse


def calculate(op: str, a: float, b: float) -> float:
    if op == "add":
        return a + b
    if op == "sub":
        return a - b
    if op == "mul":
        return a * b
    if op == "div":
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
    raise ValueError(f"Unsupported operation: {op}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Basic calculator")
    parser.add_argument("--op", choices=["add", "sub", "mul", "div"])
    parser.add_argument("--a", type=float)
    parser.add_argument("--b", type=float)
    args = parser.parse_args()

    if args.op and args.a is not None and args.b is not None:
        result = calculate(args.op, args.a, args.b)
        print(f"{args.a} {args.op} {args.b} = {result}")
        return

    demo = [("add", 10, 5), ("sub", 10, 5), ("mul", 10, 5), ("div", 10, 5)]
    for op, a, b in demo:
        print(f"{a} {op} {b} = {calculate(op, a, b)}")


if __name__ == "__main__":
    main()
