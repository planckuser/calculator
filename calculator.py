import streamlit as st

ram_rate = 10  # 1GiB RAM = 10PLN
vram_rate = 3.75  # 24GiB vRAM = 90PLN (90/24)
vcpu_rate = 5  # 1 vCPU = 5PLN
cpu_rate = 3  # 1 CPU = 3PLN
gpu_rate = 20  # 1 GPU = 20PLN

st.title('Crypto Token Calculator')

ram = st.number_input('Enter amount of RAM (GiB)', min_value=0.0, step=1.0)
vram = st.number_input('Enter amount of vRAM (GiB)', min_value=0.0, step=1.0)
vcpus = st.number_input('Enter number of vCPUs', min_value=0, step=1)
cpus = st.number_input('Enter number of CPUs', min_value=0, step=1)
gpus = st.number_input('Enter number of GPUs', min_value=0, step=1)

total_pln = ram * ram_rate + vram * vram_rate + vcpus * vcpu_rate + cpus * cpu_rate + gpus * gpu_rate

st.write(f'Total PLN: {total_pln}')
