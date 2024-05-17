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
st.image('planck_logo.png', width=100)
st.title('$PLN Earning Calculator')

# Conversion rates
ram_rate = 10  # 1GiB RAM = 10PLN
vram_rate = 3.75  # 24GiB vRAM = 90PLN (90/24)
vcpu_rate = 5  # 1 vCPU = 5PLN
cpu_rate = 3  # 1 CPU = 3PLN
gpu_rate = 20  # 1 GPU = 20PLN

# Input fields
ram = st.number_input('Enter amount of RAM (GiB)', min_value=0.0, step=1.0)
vram = st.number_input('Enter amount of vRAM (GiB)', min_value=0.0, step=1.0)
vcpus = st.number_input('Enter number of vCPUs', min_value=0, step=1)
cpus = st.number_input('Enter number of CPUs', min_value=0, step=1)
gpus = st.number_input('Enter number of GPUs', min_value=0, step=1)

# Calculate total PLN
total_pln = ram * ram_rate + vram * vram_rate + vcpus * vcpu_rate + cpus * cpu_rate + gpus * gpu_rate

# Display result
st.write(f'Total PLN: {total_pln}')

if __name__ == '__main__':
    st.run(port=port, address=address)
