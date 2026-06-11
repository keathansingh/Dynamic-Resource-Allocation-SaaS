import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("cpu_log.csv")

# Create a sample number for x-axis
df["sample"] = range(len(df))

# Plot data for each tenant
for container in df["container_name"].unique():
    data = df[df["container_name"] == container]

    plt.plot(
        data["sample"],
        data["cpu_usage"],
        marker="o",
        label=container
    )

plt.xlabel("Sample Number")
plt.ylabel("CPU Usage (%)")
plt.title("Dynamic Resource Allocation for Tenants")
plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig("cpu_usage_plot.png")

print("✅ Graph saved as cpu_usage_plot.png")

