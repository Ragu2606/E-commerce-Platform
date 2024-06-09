Project: E-commerce Logistics Data Integration with AWS Services


Introduction


This project outlines the development of a real-time data integration solution for an e-commerce company's online platform and delivery truck fleet. The goal is to seamlessly integrate clickstream data from the website and telemetry data from IoT sensors installed in trucks to optimize customer experience, logistics efficiency, and operational insights.


Data Streams and Processing


Clickstream Data (Real-time)

Item ID

Item Name

Click Count

This data will be used to understand customer preferences, personalize marketing strategies, and enhance user experience for key product categories (mobile phones, laptops, cameras).


Truck Telemetry Data (Near Real-time - every 1 minute)

Truck ID
GPS Location (Latitude, Longitude, Altitude, Speed)
Vehicle Speed
Engine Diagnostics (Engine RPM, Fuel Level, Temperature, Oil Pressure, Battery Voltage)
Odometer Reading
Fuel Consumption
Vehicle Health and Maintenance (Brake Status, Tire Pressure, Transmission Status)
Environmental Conditions (Temperature, Humidity, Atmospheric Pressure)
This data will be used to optimize delivery routes, reduce fuel consumption, proactively address maintenance issues, ensure vehicle safety, and gain insights into fleet operations.
AWS Services

Kinesis Firehose (Data Ingestion)
Continuously capture and ingest real-time clickstream and truck telemetry data streams in a format compatible with downstream processing.
Lambda Functions (Data Processing)
Process ingested data streams to extract valuable insights.
Clickstream data: Analyze customer behavior, generate recommendations, personalize marketing.
Truck telemetry data: Implement route optimization algorithms, predict maintenance needs, monitor fuel efficiency, track environmental impact.
Snowflake/DynamoDB (Data Storage)
Store processed clickstream and truck telemetry data for historical analysis, reporting, and integration with other business systems.
Snowflake (preferred): Provides a scalable, cloud-based data warehouse solution for historical data storage and complex analytics.
DynamoDB (alternative): Offers a NoSQL database suitable for storing frequently accessed truck telemetry data with high throughput and low latency.
SCD (Slowly Changing Dimension) Type 2 for Truck Data

This approach maintains historical data for each truck's attributes by adding the following columns to the database schema:

Effective From (Timestamp): Denotes the start time when a specific data point becomes valid.
Effective To (Timestamp): Denotes the end time when a specific data point becomes invalid (null for the current record).
