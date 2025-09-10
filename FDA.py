import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file 
file_path = r'C:\nilay code\Projects\fda\PersonalFitnessDataAnalyzer.csv'
data = pd.read_csv(file_path)

# Calculate averages 
print("\nAverage values:")
print(data.mean(numeric_only=True))

data.columns = data.columns.str.strip()  
print("Columns:", data.columns.tolist())



# Find Best and Worst Days based on Steps
best_day = data.loc[data['steps'].idxmax()]
worst_day = data.loc[data['steps'].idxmin()]

print("\nBest Day (Steps):")
print(best_day)

print("\nWorst Day (Steps):")
print(worst_day)

#Simple Report with Recommendations
avg_steps = data['steps'].mean()
avg_sleep = data['sleep_hours'].mean()
avg_water = data['water_intake_liters'].mean()
print("\n Personal Fitness Report")
print("--------------------------")
print(f"Average daily steps: {avg_steps:.0f}")
print(f"Average sleep hours: {avg_sleep:.1f}")
print(f"Average water intake: {avg_water:.1f} L")

print("\nRecommendations:")
print("- Aim for 8 hours of sleep.")
print(f"- Try to stay above {avg_steps:.0f} steps daily.")
print("- Drink at least 2.5 L of water daily.")

# --- Trend Over Time (7-day rolling average for steps) 
data['date'] = pd.to_datetime(data['date'])   
data = data.sort_values('date')

data['steps_trend'] = data['steps'].rolling(window=7).mean()

plt.figure(figsize=(10,5))
plt.plot(data['date'], data['steps'], label='Daily Steps', alpha=0.5)
plt.plot(data['date'], data['steps_trend'], label='7-Day Rolling Average', linewidth=2, color='red')
plt.title("Steps Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Steps")
plt.legend()
plt.grid(True)
plt.show()
