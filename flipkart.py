import streamlit as st
import pandas as pd
import boto3
import json
from datetime import datetime

# Function to load AWS credentials from an Excel file
@st.cache_data
def load_aws_credentials():
    credentials_df = pd.read_excel('aws_credentials.xlsx')
    return {
        'AWS_REGION': credentials_df.loc[0, 'AWS_REGION'],
        'AWS_ACCESS_KEY': credentials_df.loc[0, 'AWS_ACCESS_KEY'],
        'AWS_SECRET_KEY': credentials_df.loc[0, 'AWS_SECRET_KEY']
    }

# Load AWS credentials
aws_credentials = load_aws_credentials()

# AWS settings
AWS_REGION = aws_credentials['AWS_REGION']
AWS_ACCESS_KEY = aws_credentials['AWS_ACCESS_KEY']
AWS_SECRET_KEY = aws_credentials['AWS_SECRET_KEY']

# Create a boto3 client for Kinesis
kinesis_client = boto3.client(
    'kinesis',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

stream_name = 'flipkart'

# Function to send data to Kinesis
def send_data_to_kinesis(payload):
    response = kinesis_client.put_record(
        StreamName=stream_name,
        Data=json.dumps(payload),
        PartitionKey=str(payload['item_id'])  # Ensure PartitionKey is a string
    )
    return response

# Function to query DynamoDB for clickstream data
def get_clickstream_data():
    dynamodb = boto3.resource(
        'dynamodb',
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )
    table = dynamodb.Table('ClickstreamData')
    response = table.scan()
    data = response['Items']
    
    # Convert DynamoDB response to a DataFrame and handle missing or invalid values
    df = pd.DataFrame(data)
    df['click_count'] = pd.to_numeric(df['click_count'], errors='coerce').fillna(0).astype(int)
    return df

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv('products.csv')
    return data

# Load data
data = load_data()

# Debug: Print column names to verify
st.write("Column names in the dataset:", data.columns.tolist())

# Ensure 'ItemID' exists in the dataset
if 'ItemID' not in data.columns:
    st.error("The 'ItemID' column is missing from the dataset.")
else:
    # Sidebar for filters
    st.sidebar.header('Filter Products')
    categories = data['Category'].unique()
    selected_category = st.sidebar.selectbox('Category', categories)

    # Search bar
    search_query = st.sidebar.text_input('Search Products')

    # Filter data based on selection
    filtered_data = data[(data['Category'] == selected_category) & 
                         (data['ProductName'].str.contains(search_query, case=False))]

    # Display products
    st.title('Flipkart')
    st.subheader(f'Category: {selected_category}')

    for index, row in filtered_data.iterrows():
        st.image(row['ImageURL'], width=100)
        st.write(f"**{row['ProductName']}**")
        st.write(f"Price: ₹{row['Price']}")
        view_button = st.button('View', key=index)

        if view_button:
            # Create clickstream data payload
            clickstream_data = {
                "timestamp": datetime.now().isoformat(),
                "product_category": row['Category'],
                "action": "view",
                "product_name": row['ProductName'],
                "item_id": str(row['ItemID']),  # Ensure item_id is a string
                "click_count": 1
            }
            
            # Log the clickstream data
            st.write(f"Sending data to Kinesis: {clickstream_data}")
            
            # Send data to Kinesis
            response = send_data_to_kinesis(clickstream_data)
            st.write(f"Kinesis response: {response}")

        st.write("---")

    if filtered_data.empty:
        st.write("No products found")
