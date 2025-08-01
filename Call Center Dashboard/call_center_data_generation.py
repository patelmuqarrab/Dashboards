import pandas as pd
import numpy as np
from numpy.random import default_rng

rng = default_rng(2024)        # reproducible seed
N = 10_000

# --- fixed call-center mapping ---
call_centers = {
    "Bengaluru": "Karnataka",
    "Gurugram": "Haryana",
    "Hyderabad": "Telangana",
    "Pune": "Maharashtra"
}
cc_cities = list(call_centers.keys())
cc_states = [call_centers[c] for c in cc_cities]

# --- Indian client geography ---
states_cities = {
    "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Thane"],
    "Karnataka": ["Bengaluru", "Mysuru", "Hubballi"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"],
    "Delhi": ["New Delhi"],
    "Uttar Pradesh": ["Lucknow", "Noida", "Varanasi"],
    "Telangana": ["Hyderabad", "Warangal"],
    "West Bengal": ["Kolkata", "Howrah"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara"],
    "Rajasthan": ["Jaipur", "Udaipur"],
    "Kerala": ["Kochi", "Thiruvananthapuram"]
}
states = list(states_cities.keys())
reasons = ["billing_question", "service_outage", "payments"]
sentiments = ["Very Negative", "Negative", "Neutral", "Positive", "Very Positive"]
channels = ["call_center", "chat_bot", "email", "web"]

# --- generate data step by step ---
# First, generate the basic columns
call_center_cities = rng.choice(cc_cities, N)
client_states = rng.choice(states, N)
call_sentiments = rng.choice(sentiments, N, p=[0.05, 0.15, 0.30, 0.35, 0.15])

# Generate dependent columns
call_center_states = [call_centers[city] for city in call_center_cities]
client_cities = [rng.choice(states_cities[state]) for state in client_states]
csat_scores = [{"Very Negative": 1, "Negative": 2, "Neutral": 3, "Positive": 4, "Very Positive": 5}[sentiment] 
               for sentiment in call_sentiments]

# Create the DataFrame
df = pd.DataFrame({
    "id": np.arange(1, N + 1),
    "call_center_city": call_center_cities,
    "call_center_state": call_center_states,
    "date_of_call": pd.Timestamp("2024-08-01") + pd.to_timedelta(
        rng.integers(0, 365, N), unit="D"
    ),
    "reason_of_call": rng.choice(reasons, N),
    "client_city": client_cities,
    "client_state": client_states,
    "call_sentiment": call_sentiments,
    "call_duration_min": rng.gamma(3, 4, N).round(1).clip(0.5, 30),
    "csat_score": csat_scores,
    "channel": rng.choice(channels, N, p=[0.40, 0.25, 0.20, 0.15])
})

# reorder columns
df = df[
    ["id", "call_center_city", "call_center_state", "date_of_call",
     "reason_of_call", "client_city", "client_state", "call_sentiment",
     "call_duration_min", "csat_score", "channel"]
]

# export
df.to_csv("call_center_india_10k.csv", index=False)

print("Data generated successfully!")
print(f"Shape: {df.shape}")
print("\nFirst few rows:")
print(df.head())