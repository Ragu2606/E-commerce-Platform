import requests
import json
import random
from decimal import Decimal
from datetime import datetime

# Define the API endpoint
API_URL = "https://qnzhotwtl5.execute-api.ap-south-1.amazonaws.com/production/truck_data"

# Function to generate random telemetry data for a truck
def generate_truck_data(truck_id):
    return {
        "truck_id": truck_id,
        "timestamp": datetime.utcnow().isoformat(),
        "gps_location": {
            "latitude": Decimal(str(round(random.uniform(-90, 90), 6))),
            "longitude": Decimal(str(round(random.uniform(-180, 180), 6))),
            "altitude": Decimal(str(round(random.uniform(0, 1000), 1))),
            "speed": Decimal(str(round(random.uniform(0, 100), 1)))
        },
        "vehicle_speed": Decimal(str(round(random.uniform(0, 100), 1))),
        "engine_diagnostics": {
            "engine_rpm": Decimal(str(random.randint(1500, 5000))),
            "fuel_level": Decimal(str(round(random.uniform(0, 100), 1))),
            "temperature": Decimal(str(round(random.uniform(70, 120), 1))),
            "oil_pressure": Decimal(str(round(random.uniform(25, 65), 1))),
            "battery_voltage": Decimal(str(round(random.uniform(11, 30), 1)))
        },
        "odometer_reading": Decimal(str(round(random.uniform(10000, 20000), 1))),
        "fuel_consumption": Decimal(str(round(random.uniform(5, 20), 1))),
        "vehicle_health_and_maintenance": {
            "brake_status": random.choice(["Good", "Fair", "Poor"]),
            "tire_pressure": {
                "front_left": Decimal(str(round(random.uniform(30, 35), 1))),
                "front_right": Decimal(str(round(random.uniform(30, 35), 1))),
                "rear_left": Decimal(str(round(random.uniform(30, 35), 1))),
                "rear_right": Decimal(str(round(random.uniform(30, 35), 1)))
            },
            "transmission_status": random.choice(["Operational", "Needs Service"])
        },
        "environmental_conditions": {
            "temperature": Decimal(str(round(random.uniform(-20, 50), 1))),
            "humidity": Decimal(str(round(random.uniform(0, 100), 1))),
            "atmospheric_pressure": Decimal(str(round(random.uniform(900, 1100), 1)))
        }
    }

# Custom JSON encoder to handle Decimal types
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super(DecimalEncoder, self).default(obj)

# Generate telemetry data for three trucks
trucks_data = []

for truck_id in ["TRK001", "TRK002", "TRK003"]:
    truck_data = generate_truck_data(truck_id)
    trucks_data.append(truck_data)

# Prepare data with trucks list
data = {"trucks": trucks_data}

# Convert data to JSON with custom encoder
data_json = json.dumps(data, cls=DecimalEncoder)

# Send data to the API
response = requests.post(API_URL, data=data_json, headers={"Content-Type": "application/json"})

# Print the response
print("Response:", response.status_code)
print("Response content:", response.content)
