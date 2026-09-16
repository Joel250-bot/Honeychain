import numpy as np
import pandas as pd

# Make the results reproducible
np.random.seed(42)

# Number of sensor readings
num_samples = 1000

# Generate simulated hive data
temperature = np.random.normal(34, 2, num_samples)
humidity = np.random.normal(65, 8, num_samples)
hive_weight = np.random.normal(42, 5, num_samples)
bee_activity = np.random.normal(80, 10, num_samples)
day = np.arange(1, num_samples + 1)

# Simulated honey production
honey_production = (
    0.05 * hive_weight
    + 0.02 * bee_activity
    - 0.01 * abs(temperature - 34)
    + np.random.normal(0, 0.2, num_samples)
)

# Create a DataFrame
data = pd.DataFrame({
    "temperature": temperature,
    "humidity": humidity,
    "hive_weight": hive_weight,
    "bee_activity": bee_activity,
    "day": day,
    "honey_production_kg": honey_production
})

# Save the dataset
data.to_csv("data/hive_sensor_data.csv", index=False)

print("HoneyAI dataset generated successfully!")
print(f"Number of records: {len(data)}")
print("\nFirst 5 records:")
print(data.head())