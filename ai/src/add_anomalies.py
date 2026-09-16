import numpy as np
import pandas as pd
from pathlib import Path


np.random.seed(42)


def add_anomalies(
    df: pd.DataFrame,
    anomaly_rate: float = 0.05,
    anomaly_magnitude: float = 2.0,
) -> pd.DataFrame:
    """Inject realistic anomalies into synthetic hive sensor data."""
    df = df.copy()
    num_anomalies = max(1, int(len(df) * anomaly_rate))
    anomaly_indices = np.random.choice(df.index, size=num_anomalies, replace=False)

    for idx in anomaly_indices:
        row = df.loc[idx]

        # Temperature spikes or sudden drops
        if np.random.random() < 0.5:
            df.at[idx, "temperature"] = row["temperature"] + np.random.normal(8, 3)
        else:
            df.at[idx, "temperature"] = row["temperature"] - np.random.normal(8, 3)

        # Humidity may become abnormally high or low
        df.at[idx, "humidity"] = row["humidity"] + np.random.normal(25, 8)

        # Hive weight can drop sharply, indicating stress or damage
        df.at[idx, "hive_weight"] = row["hive_weight"] - np.random.normal(12, 4)

        # Bee activity may fluctuate dramatically
        df.at[idx, "bee_activity"] = row["bee_activity"] + np.random.normal(30, 12)

        # Honey production may fall or rise sharply
        df.at[idx, "honey_production_kg"] = row["honey_production_kg"] + np.random.normal(
            0, anomaly_magnitude * 2
        )

    df["is_anomaly"] = 0
    df.loc[anomaly_indices, "is_anomaly"] = 1
    return df


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    input_path = root / "data" / "hive_sensor_data.csv"
    output_path = root / "data" / "hive_sensor_data_with_anomalies.csv"

    if not input_path.exists():
        raise FileNotFoundError(
            f"Input dataset not found: {input_path}. Run generate_data.py first."
        )

    data = pd.read_csv(input_path)
    anomaly_data = add_anomalies(data)
    anomaly_data.to_csv(output_path, index=False)

    print("Anomalies injected successfully!")
    print(f"Input file: {input_path}")
    print(f"Output file: {output_path}")
    print(f"Anomaly count: {anomaly_data['is_anomaly'].sum()}")
    print(anomaly_data.head())


if __name__ == "__main__":
    main()
