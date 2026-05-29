import numpy as np
import pandas as pd


def make_dataset(seed: int = 7) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    categories = np.array(["A", "B", "C"])
    data = {
        "category": rng.choice(categories, size=120),
        "value": rng.normal(loc=50, scale=10, size=120),
    }
    df = pd.DataFrame(data)
    df.loc[rng.choice(df.index, size=10, replace=False), "value"] = np.nan
    df.loc[rng.choice(df.index, size=5, replace=False), "value"] = -5
    return df


def clean_and_aggregate(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    cleaned = cleaned.dropna(subset=["value"])
    cleaned = cleaned[cleaned["value"] >= 0]
    aggregated = cleaned.groupby("category", as_index=False)["value"].mean()
    return aggregated


def main() -> None:
    df = make_dataset()
    print("Raw dataset sample:\n", df.head())
    aggregated = clean_and_aggregate(df)
    print("\nAverage value by category:\n", aggregated)


if __name__ == "__main__":
    main()
