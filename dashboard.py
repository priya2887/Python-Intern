from pathlib import Path

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main() -> None:
    plots_dir = Path(__file__).parent / "plots"
    plots_dir.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(10)
    df = pd.DataFrame(
        {
            "temperature": rng.normal(30, 3, size=200),
            "humidity": rng.uniform(30, 90, size=200),
            "wind_speed": rng.uniform(0, 20, size=200),
            "rain_mm": rng.gamma(shape=2, scale=2, size=200),
        }
    )

    sns.set_theme(style="whitegrid")

    plt.figure()
    sns.scatterplot(data=df, x="temperature", y="humidity", hue="rain_mm", palette="viridis")
    plt.title("Temperature vs Humidity")
    plt.tight_layout()
    plt.savefig(plots_dir / "scatter_temp_humidity.png")
    plt.close()

    plt.figure()
    sns.histplot(data=df, x="rain_mm", bins=20, kde=True, color="teal")
    plt.title("Rainfall Distribution")
    plt.tight_layout()
    plt.savefig(plots_dir / "rain_hist.png")
    plt.close()

    plt.figure()
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(plots_dir / "correlation_heatmap.png")
    plt.close()

    pairplot = sns.pairplot(df.sample(80, random_state=1))
    pairplot.fig.suptitle("Feature Pairplot", y=1.02)
    pairplot.savefig(plots_dir / "pairplot.png")
    plt.close("all")

    print(f"Saved dashboard plots to {plots_dir}")


if __name__ == "__main__":
    main()
