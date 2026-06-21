import streamlit as st
from collections import deque

# Judul aplikasi
st.title("Simulasi Queue (Antrian) - FIFO")

# Membuat queue di session state
if "queue" not in st.session_state:
    st.session_state.queue = deque()

# Input data
data = st.text_input("Masukkan data ke antrian:")

# Tombol Enqueue
if st.button("Enqueue"):
    if data:
        st.session_state.queue.append(data)
        st.success(f"{data} berhasil ditambahkan ke antrian.")
    else:
        st.warning("Masukkan data terlebih dahulu!")

# Tombol Dequeue
if st.button("Dequeue"):
    if st.session_state.queue:
        keluar = st.session_state.queue.popleft()
        st.success(f"{keluar} keluar dari antrian.")
    else:
        st.warning("Antrian masih kosong!")

# Menampilkan isi queue
st.subheader("Isi Antrian")
if st.session_state.queue:
    for i, item in enumerate(st.session_state.queue, start=1):
        st.write(f"{i}. {item}")
else:
    st.info("Antrian kosong.")

# Menampilkan informasi queue
st.subheader("Informasi Queue")
if st.session_state.queue:
    st.write(f"Front : {st.session_state.queue[0]}")
    st.write(f"Rear  : {st.session_state.queue[-1]}")
    st.write(f"Jumlah Data : {len(st.session_state.queue)}")
else:
    st.write("Front : -")
    st.write("Rear : -")
    st.write("Jumlah Data : 0")
