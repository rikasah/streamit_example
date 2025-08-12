import streamlit as st
import math

st.title("Kalkulator Luas Bangun Datar 🧮")

# Pilihan bangun datar
bangun = st.selectbox(
    "Pilih bangun datar:",
    ["Persegi", "Persegi Panjang", "Segitiga", "Lingkaran"]
)

# Input sisi sesuai pilihan
if bangun == "Persegi":
    sisi = st.number_input("Masukkan panjang sisi (cm)", min_value=0.0)
    if sisi:
        luas = sisi ** 2
        st.success(f"Luas Persegi = {luas} cm²")

elif bangun == "Persegi Panjang":
    panjang = st.number_input("Masukkan panjang (cm)", min_value=0.0)
    lebar = st.number_input("Masukkan lebar (cm)", min_value=0.0)
    if panjang and lebar:
        luas = panjang * lebar
        st.success(f"Luas Persegi Panjang = {luas} cm²")

elif bangun == "Segitiga":
    alas = st.number_input("Masukkan alas (cm)", min_value=0.0)
    tinggi = st.number_input("Masukkan tinggi (cm)", min_value=0.0)
    if alas and tinggi:
        luas = 0.5 * alas * tinggi
        st.success(f"Luas Segitiga = {luas} cm²")

elif bangun == "Lingkaran":
    jari = st.number_input("Masukkan jari-jari (cm)", min_value=0.0)
    if jari:
        luas = math.pi * (jari ** 2)
        st.success(f"Luas Lingkaran = {luas:.2f} cm²")
