import streamlit as st

st.header(':blue[Ini adalah aplikasi kalkulator penjumlahan]')
st.write('Silakan input angka numerik yang ingin dihitung ! :sunglasses:')

number1 = st.number_input('Masukkan bilangan pertama')
st.write(f'Bilangan pertama adalah {number1}')

number2 = st.number_input('Masukkan bilangan kedua')
st.write(f'Bilangan kedua adalah {number2}')

if st.button('Hitung'):
    hasil = number1 + number2
    st.success(f'hasil penjumlahan dari {number1} + {number2} = {hasil}', icon="✔")
    st.balloons()
else:
   st.write('Silakan klik tombol "Hitung" jika kamu ingin melakukan kalkulasi')