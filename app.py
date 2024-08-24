import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Viz Demo")

with open('df.pkl', 'rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

st.header('Enter your inputs')

# brand_names
brand_names = st.selectbox('Brand Names', sorted(df['brand_names'].unique().tolist()))

# rating
rating = float(st.slider('Rating', 0.0, 100.0, 50.0))

# has_5g
has_5g = int(st.selectbox('Has 5G', [0, 1]))

# has_nfc
has_nfc = int(st.selectbox('Has NFC', [0, 1]))

# processor_brand
processor_brand = st.selectbox('Processor Brand', sorted(df['processor_brand'].unique().tolist()))

# num_cores
num_cores = float(st.slider('Number of Cores', 1, 16, 8))

# processor_speed
processor_speed = float(st.slider('Processor Speed (GHz)', 0.5, 5.0, 2.5))

# ram_capacity
ram_capacity = float(st.slider('RAM Capacity (GB)', 1.0, 16.0, 8.0))

# internal_memory
internal_memory = float(st.slider('Internal Memory (GB)', 16.0, 1024.0, 128.0))

# battery_capacity
battery_capacity = float(st.slider('Battery Capacity (mAh)', 1000.0, 6000.0, 5000.0))

# fast_charging
fast_charging = float(st.slider('Fast Charging (W)', 0.0, 120.0, 68.0))

# screen_size
screen_size = float(st.slider('Screen Size (inches)', 3.0, 7.0, 6.55))

# resolution
resolution = st.text_input('Resolution', '1080 x 2400 ')

# refresh_rate
refresh_rate = float(st.slider('Refresh Rate (Hz)', 60.0, 144.0, 144.0))

# os
os = st.selectbox('Operating System', sorted(df['os'].unique().tolist()))

# primary_camera_rear
primary_camera_rear = float(st.slider('Primary Rear Camera (MP)', 1.0, 108.0, 50.0))

# primary_camera_front
primary_camera_front = float(st.slider('Primary Front Camera (MP)', 1.0, 50.0, 32.0))

# extended_memory_available
extended_memory_available = float(st.slider('Extended Memory Available (GB)', 0.0, 1.0, 0.0))

if st.button('Predict'):
    # form a dataframe
    data = [[brand_names, rating, has_5g, has_nfc, processor_brand, num_cores,
             processor_speed, ram_capacity, internal_memory, battery_capacity,
             fast_charging, screen_size, resolution, refresh_rate, os,
             primary_camera_rear, primary_camera_front, extended_memory_available]]

    columns = ['brand_names', 'rating', 'has_5g', 'has_nfc', 'processor_brand',
               'num_cores', 'processor_speed', 'ram_capacity', 'internal_memory',
               'battery_capacity', 'fast_charging', 'screen_size', 'resolution',
               'refresh_rate', 'os', 'primary_camera_rear', 'primary_camera_front',
               'extended_memory_available']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    # Predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 2800
    high = base_price + 2800

    # Display
    st.text(f"The price of the mobile phone is between {low} and {high}")
