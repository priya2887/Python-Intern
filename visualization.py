from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main() -> None:
    plots_dir = Path(__file__).parent / "plots"
    plots_dir.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(42)
    days = np.arange(1, 8)
    temperatures = rng.normal(loc=30, scale=2, size=7)
    rain_mm = rng.uniform(0, 20, size=7)

    df = pd.DataFrame({"day": days, "temperature": temperatures, "rain_mm": rain_mm})

    plt.figure()
    plt.plot(df["day"], df["temperature"], marker="o")
    plt.title("Daily Temperature")
    plt.xlabel("Day")
    plt.ylabel("Temperature (C)")
    plt.tight_layout()
    plt.savefig(plots_dir / "temperature_line.png")
    plt.close()

    plt.figure()
    plt.bar(df["day"], df["rain_mm"], color="skyblue")
    plt.title("Daily Rainfall")
    plt.xlabel("Day")
    plt.ylabel("Rain (mm)")
    plt.tight_layout()
    plt.savefig(plots_dir / "rainfall_bar.png")
    plt.close()

    plt.figure()
    plt.hist(df["temperature"], bins=5, color="salmon", edgecolor="black")
    plt.title("Temperature Distribution")
    plt.xlabel("Temperature (C)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(plots_dir / "temperature_hist.png")
    plt.close()

    print(f"Saved plots to {plots_dir}")


if __name__ == "__main__":
    main()
