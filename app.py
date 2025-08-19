import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Import model and dataframe
pipe = pickle.load(open('pkl files/pipe.pkl', 'rb'))
df = pickle.load(open('pkl files/df.pkl', 'rb'))

# Load CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")

# Header Bar
st.markdown(
    """<div class="header">💻 Laptop Price Predictor</div>""", unsafe_allow_html=True
)

st.write("")
st.markdown("----")

# User Inputs
col1, col2 = st.columns(2)

with col1:
    company = st.selectbox('Brand / Company', df['Company'].unique())
    type_name = st.selectbox('Type', df['TypeName'].unique())
    ram = st.selectbox('Select RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
    os = st.selectbox('Choose OS', df['OpSys'].unique())
    weight = st.number_input('Enter Weight in Kg')

with col2:
    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
    ips = st.selectbox('IPS Display', ['No', 'Yes'])
    screen_size = st.number_input('Enter Screen Size in Inches')
    selected_resolution = st.selectbox("Select Screen Resolution:", [
        "1366x768 (HD)",
        "1600x900 (HD+)",
        "1920x1080 (Full HD)",
        "1920x1200 (WUXGA)",
        "2560x1440 (2K / QHD)",
        "2560x1600 (QHD+)",
        "2880x1800 (Retina)",
        "3200x1800 (QHD+)",
        "3840x2160 (4K UHD)",
    ])
    st.write("You selected:", selected_resolution)

# Additional inputs
cpu_brand = st.selectbox('Select CPU Brand', df['CpuBrand'].unique())
cpu_speed = st.number_input('Enter CPU Speed (GHz)')
hdd = st.selectbox('Select HDD (GB)', np.sort(df['HDD'].unique()))
ssd = st.selectbox('Select SSD (GB)', np.sort(df['SSD'].unique()))
gpu_brand = st.selectbox('Select GPU Brand', df['GpuBrand'].unique())

st.markdown("---")

# Predict Button
if st.button('Predict Price'):

    # Extract numeric resolution
    numeric_part = selected_resolution.split()[0]
    x_res, y_res = map(int, numeric_part.split('x'))
    ppi = ((x_res ** 2 + y_res ** 2) ** 0.5) / screen_size if screen_size > 0 else None

    # Transform Yes/No to 0/1
    touchscreen_val = 1 if touchscreen == 'Yes' else 0
    ips_val = 1 if ips == 'Yes' else 0

    # Prepare query as DataFrame to match training
    query_df = pd.DataFrame([[
        company, type_name, ram, os, weight, touchscreen_val, ips_val,
        ppi, cpu_brand, cpu_speed, hdd, ssd, gpu_brand
    ]], columns=[
        'Company', 'TypeName', 'Ram', 'OpSys', 'Weight', 'TouchScreen', 'IPS',
        'PPI', 'CpuBrand', 'CpuSpeed', 'HDD', 'SSD', 'GpuBrand'
    ])

    # Prediction
    predicted_price = int(np.exp(pipe.predict(query_df)[0]))

    st.markdown(
        f'<div class="result-box">💰 Predicted Price:  {predicted_price} PKR</div>',
        unsafe_allow_html=True
    )
