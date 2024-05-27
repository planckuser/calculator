import streamlit as st
import os

# Set server address and port
port = int(os.environ.get('PORT', 8501))
address = '0.0.0.0'

# Set page configuration
st.set_page_config(
    page_title='$PLN Earning Calculator',
    page_icon='💰',
    layout='centered',
    initial_sidebar_state='auto'
)

# Add logo and title
st.image('planck.jpeg', width=200)
st.title('$PLN Earning Calculator')

# Conversion rates
ram_rate = 10  # 1GiB RAM = 10PLN
vram_rate = 3.75  # 24GiB vRAM = 90PLN (90/24)
vcpu_rate = 5  # 1 vCPU = 5PLN
cpu_rate = 3  # 1 CPU = 3PLN
gpu_rate = 20  # 1 GPU = 20PLN

# Input fields for resources
ram = st.number_input('Enter amount of RAM (GiB)', min_value=0.0, step=1.0)
vram = st.number_input('Enter amount of vRAM (GiB)', min_value=0.0, step=1.0)
vcpus = st.number_input('Enter number of vCPUs', min_value=0, step=1)
cpus = st.number_input('Enter number of CPUs', min_value=0, step=1)
gpus = st.number_input('Enter number of GPUs', min_value=0, step=1)

# Input fields for mining parameters
hash_rate = st.number_input('Enter your hash rate (H/s)', min_value=0.0, step=1.0)
total_network_hash_rate = st.number_input('Enter total network hash rate (H/s)', min_value=0.0, step=1.0)
block_reward = st.number_input('Enter block reward', min_value=0.0, step=0.1)
electricity_cost_per_kwh = st.number_input('Enter electricity cost per kWh', min_value=0.0, step=0.01)
power_consumption_per_gpu = st.number_input('Enter power consumption of GPU (kW)', min_value=0.0, step=0.01)

# Calculate total PLN for resources
total_pln_resources = ram * ram_rate + vram * vram_rate + vcpus * vcpu_rate + cpus * cpu_rate + gpus * gpu_rate

# Calculate earnings based on the formula
if total_network_hash_rate > 0:  # To avoid division by zero
    mining_earnings = (hash_rate / total_network_hash_rate) * block_reward
else:
    mining_earnings = 0

# Calculate electricity cost
electricity_cost = electricity_cost_per_kwh * power_consumption_per_gpu * gpus

# Calculate total earnings
total_earnings = mining_earnings - electricity_cost

# Display results
st.write(f'Total $PLN for resources: {total_pln_resources}')
st.write(f'Mining Earnings: {mining_earnings}')
st.write(f'Electricity Cost: {electricity_cost}')
st.write(f'Total Earnings: {total_earnings}')
