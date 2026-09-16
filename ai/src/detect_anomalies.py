from pathlib import Path

import numpy as np
import pandas as pd


FEATURE_COLUMNS = [
    "temperature",
    "humidity",
    "hive_weight",
    "bee_activity",
    "honey_production_kg",
]


def detect_anomalies(df: pd.DataFrame, threshold: float = 3.0) -> pd.DataFrame:
    """Flag rows whose numeric features are unusually far from the mean."""
    df = df.copy()

    for col in FEATURE_COLUMNS:
        if col not in df.columns:
            raise KeyError(f"Missing required column: {col}")

    z_scores = (df[FEATURE_COLUMNS] - df[FEATURE_COLUMNS].mean()) / df[FEATURE_COLUMNS].std(ddof=0)
    df["anomaly_score"] = np.abs(z_scores).max(axis=1)
    df["predicted_anomaly"] = (df["anomaly_score"] > threshold).astype(int)
    return df


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    input_path = root / "data" / "hive_sensor_data_with_anomalies.csv"
    output_path = root / "data" / "detected_anomalies.csv"

    if not input_path.exists():
        raise FileNotFoundError(
            f"Input dataset not found: {input_path}. Run add_anomalies.py first."
        )

    data = pd.read_csv(input_path)
    detected = detect_anomalies(data)
    detected.to_csv(output_path, index=False)

    detected_count = int(detected["predicted_anomaly"].sum())
    print("Anomaly detection complete.")
    print(f"Input file: {input_path}")
    print(f"Output file: {output_path}")
    print(f"Detected anomalies: {detected_count}")
    print(detected[["temperature", "humidity", "hive_weight", "bee_activity", "honey_production_kg", "predicted_anomaly"]].head(10))


if __name__ == "__main__":
    main()
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix

# Load the dataset
data = pd.read_csv("data/hive_sensor_data_with_anomalies.csv")

# Features used by the AI model
features = [
    "temperature",
    "humidity",
    "hive_weight",
    "bee_activity"
]

X = data[features]

# Create the Isolation Forest model
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

# Train the model and predict anomalies
predictions = model.fit_predict(X)

# Isolation Forest gives:
#  1  = Normal
# -1  = Anomaly
data["ai_prediction"] = predictions

# Convert prediction into our format:
# 0 = Normal
# 1 = Anomaly
data["ai_anomaly"] = data["ai_prediction"].apply(
    lambda x: 1 if x == -1 else 0
)

# Compare AI prediction with our known labels
print("AI Anomaly Detection Results")
print("--------------------------------")

print("\nActual anomalies:", data["is_anomaly"].sum())
print("AI detected anomalies:", data["ai_anomaly"].sum())

print("\nConfusion Matrix:")
print(confusion_matrix(
    data["is_anomaly"],
    data["ai_anomaly"]
))

print("\nClassification Report:")
print(classification_report(
    data["is_anomaly"],
    data["ai_anomaly"]
))

# Save the results
data.to_csv(
    "data/anomaly_detection_results.csv",
    index=False
)

print("\nResults saved successfully!")