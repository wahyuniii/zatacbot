import streamlit as st

# Menghilangkan tombol Menu
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Mengganti Background dengan gambar
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://64.media.tumblr.com/19e325c4db0127cb929c480ab8a6a6be/1a9c54c2177c376d-da/s500x750/748f7658e9c6ef4c0118eaf3494e318b7fe2333f.pnj");
background-size: cover;
}

[data-testid="stHeader"] {
background-color: rgba{0, 0, 0, 0};
}

[data-testid="stToolbar"] {
right: 2rem;
}

[data-testid="stSidebar"] {
background-image: url("https://64.media.tumblr.com/4c02b74ff816cbfb7cd0984e11beb3dc/5d89598f9be0fd33-1c/s2048x3072/b8061c275a1b5d1d564f43ab6433b97927929cdc.pnj");
background-size: cover;
}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Mulai Title
st.title("Pengembang Zatacbot")
st.write("---")
st.image("https://64.media.tumblr.com/71cc949c33c2a11f8ebfeec4da8ed25f/8668cd133f446a1c-7e/s1280x1920/26ebef31acf2b00120788f09d4f749628dd4d867.pnj", width=200)

st.write("---")
st.write("Nama: Wahyuni")
st.write("Alamat: Cilacap, Indonesia")
st.write("Instansi: Universitas Negeri Semarang")
st.write("Fakultas: Ilmu Pendidikan")
st.write("Jurusan: Pendidikan Guru Sekolah Dasar")
st.write("---")
st.write("Untuk saran dan masukan hub: 085758447988")


#Ganti Page Berdampingan
st.markdown(
    """
    <style>
    .stButton button {
        font-size: 18px;
        background-color: #ff8c00; /* Ubah dengan kode warna coklat pastel yang diinginkan */
        color: white;
        width:100%
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("---")

from streamlit_extras.switch_page_button import switch_page

want_to_menu = st.button("\u25C0   Menu")
if want_to_menu:
   switch_page("Menu")



