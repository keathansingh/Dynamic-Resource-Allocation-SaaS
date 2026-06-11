import docker
import time
import os
import csv
from datetime import datetime

client = docker.from_env()

TENANTS = ["tenant_a", "tenant_b"]
CPU_THRESHOLD = 50.0
CHECK_INTERVAL = 3

LOG_FILE = "cpu_log.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "container_name", "cpu_usage"])


def get_cpu_usage(container_name):
    try:
        output = os.popen(
            f"docker stats {container_name} --no-stream --format '{{{{.CPUPerc}}}}'"
        ).read().strip()

        if output.endswith("%"):
            return float(output.replace("%", ""))

        return 0.0

    except Exception as e:
        print(f"⚠️ Error getting CPU for {container_name}: {e}")
        return 0.0


while True:

    usage = {}

    print("\n🧠 Checking container CPU usage...")

    for tenant in TENANTS:

        cpu = get_cpu_usage(tenant)
        usage[tenant] = cpu

        print(f"{tenant}: {cpu}% CPU")

        with open(LOG_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    tenant,
                    cpu
                ]
            )

    for tenant, cpu in usage.items():

        if cpu > CPU_THRESHOLD:

            print(
                f"⚙️ {tenant} is busy → increasing CPU allocation to 1 CPU"
            )

            os.system(
                f"docker update --cpus=1 {tenant}"
            )

        else:

            print(
                f"💤 {tenant} is idle → reducing CPU allocation to 0.5 CPU"
            )

            os.system(
                f"docker update --cpus=0.5 {tenant}"
            )

    print("-" * 60)

    time.sleep(CHECK_INTERVAL)
