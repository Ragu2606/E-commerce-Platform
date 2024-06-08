# E-commerce-Platform
From Clicks to Deliveries: Maximizing E-commerce Performance with Real-Time Data Integration

# E-commerce Platform and Fleet Management Integration

## Overview

This project aims to integrate real-time data streams from an e-commerce platform and a fleet of delivery trucks to optimize operations and customer satisfaction. The data will be processed using AWS Kinesis and AWS Lambda, and stored in DynamoDB for historical analysis.

## Components

1. **Clickstream Data API**: Captures and retrieves clickstream data.
2. **Truck Telemetry Data API**: Captures and retrieves telemetry data from delivery trucks.
3. **AWS Kinesis**: Streams real-time data for processing.
4. **AWS Lambda**: Processes data and stores it in DynamoDB.
5. **DynamoDB**: Stores processed data for historical analysis.

## Setup Instructions

### API Setup

1. Install dependencies:
    ```bash
    pip install flask boto3
    ```

2. Create the `clickstream` API:
    - Save the code in `clickstream_api.py` and run:
        ```bash
        python clickstream_api.py
        ```

3. Create the `truck` API:
    - Save the code in `truck_api.py` and run:
        ```bash
        python truck_api.py
        ```

### AWS Setup

1. **Kinesis Streams**
    - Create two Kinesis streams: `clickstream` and `truckstream`.

2. **DynamoDB Tables**
    - Create `ClickstreamData` table with `item_id` and `timestamp` as keys.
    - Create `TruckTelemetryData` table with `truck_id` and `timestamp` as keys.

3. **Lambda Functions**
    - Create `process_clickstream` and `process_truckstream` Lambda functions.
    - Add the provided code to the respective Lambda functions.
    - Set up the triggers from the Kinesis streams to the Lambda functions.

### Data Processing

1. **Sending Clickstream Data**
    - Use the `clickstream` API to send clickstream data.
    - Example payload:
        ```json
        {
            "item_id": "123",
            "item_name": "Mobile Phone",
            "click_count": 10
        }
        ```

2. **Sending Truck Telemetry Data**
    - Use the `truck` API to send telemetry data.
    - Example payload:
        ```json
        {
            "truck_id": "TRK001",
            "gps_location": {
                "latitude": 34.052235,
                "longitude": -118.243683,
                "altitude": 89.0,
                "speed": 65.0
            },
            "vehicle_speed": 65.0,
            "engine_diagnostics": {
                "engine_rpm": 2500,
                "fuel_level": 75.0,
                "temperature": 90.0,
                "oil_pressure": 40.0,
                "battery_voltage": 13.8
            },
            "odometer_reading": 102345.6,
            "fuel_consumption": 15.5,
            "vehicle_health_and_maintenance": {
                "brake_status": "Good",
                "tire_pressure": {
                    "front_left": 32.0,
                    "front_right": 32.0,
                    "rear_left": 35.0,
                    "rear_right": 35.0
                },
                "transmission_status": "Operational"
            },
            "environmental_conditions": {
           
