import numpy as np
import pandas as pd


def main() -> None:
    array = np.array([[1, 2, 3], [4, 5, 6]])
    print("Array:\n", array)
    print("Array + 10:\n", array + 10)

    temperatures = pd.DataFrame(
        {
            "city": ["Delhi", "Delhi", "Mumbai", "Mumbai", "Chennai", "Chennai"],
            "day": [1, 2, 1, 2, 1, 2],
            "temperature": [30.2, 31.1, 28.0, 29.5, 32.4, 33.0],
        }
    )
    print("\nDataFrame:\n", temperatures)

    grouped = temperatures.groupby("city", as_index=False)["temperature"].mean()
    print("\nAverage temperature by city:\n", grouped)


if __name__ == "__main__":
    main()
