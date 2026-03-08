import streamlit as st
import pandas as pd
import plotly.express as px
import os
from datetime import datetime

# =======================================
# 1. KONFIGURASI & FUNGSI DATA (TARUH DI SINI)
# =======================================
DATA_FILE = 'data_keuangan.csv'

def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        # Jika file belum ada, buat DataFrame kosong dengan kolom yang sesuai
        return pd.DataFrame(columns=['Tanggal', 'Kategori', 'Deskripsi', 'Jumlah'])

      # Fungsi untuk menyimpan data ke file CSV
def save_data(data):
    data.to_csv(DATA_FILE, index=False)

    # Initialisasi data saat aplikasi dibuka
    if 'transactions' not in st.session_state:
        st.session_state.transactions = load_data()

     # Kode input form

    if submit:
     # Buat baris data  baru
     new_row = {'Tanggal': tanggal, 'Kategori': kategori, 'Deskripsi': deskripsi, 'Jumlah': jumlah}

     # Masukan ke session state
     st.session_state.transactions = st.session_state.transactions.append(new_row, ignore_index=True)

     # SIMPAN KE FILE FISIK
     save_data(st.session_state.transactions)

     st.success("Data berhasil disimpan secara permanen!")
