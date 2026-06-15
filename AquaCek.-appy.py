
import streamlit as st
import pandas as pd

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="AquaCek",
    page_icon="💧",
    layout="wide"
)

# =========================
# CSS ANIMASI AMAN
# =========================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(-45deg, #e3f2fd, #bbdefb, #e1f5fe, #b3e5fc);
    background-size: 400% 400%;
    animation: bg 10s ease infinite;
}

@keyframes bg {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.glass {
    background: rgba(255,255,255,0.85);
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    margin-bottom: 15px;
}

.hero {
    font-size: 80px;
    text-align: center;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0% {transform: translateY(0);}
    50% {transform: translateY(-12px);}
    100% {transform: translateY(0);}
}

h1, h2, h3 {
    color: #0d47a1;
}

.stButton button {
    background: linear-gradient(90deg,#00B4DB,#0083B0) !important;
    color: white !important;
    font-weight: bold !important;
    border-radius: 12px !important;
    width: 100%;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SESSION STORAGE
# =========================
if "data" not in st.session_state:
    st.session_state.data = []

# =========================
# MENU
# =========================
menu = st.sidebar.radio(
    "💧 AQUACEK MENU",
    [
        "Home",
        "Evaluasi Kualitas Air",
        "Baku Mutu Air Kelas I",
        "Interpretasi Parameter",
        "Landasan Hukum",
        "Pengembang",
        "Riwayat"
    ]
)

# =========================
# HOME
# =========================
def home():
    st.markdown("""
    <div class="glass" style="text-align:center;">
        <div class="hero">💧</div>
        <h1>AquaCek</h1>
        <h3>Evaluasi Kualitas Air Kelas I</h3>
        <b>PP No. 22 Tahun 2021</b>
    </div>
    """, unsafe_allow_html=True)

    st.info("Aplikasi evaluasi kualitas air berbasis parameter lingkungan")

# =========================
# EVALUASI
# =========================
def evaluasi():

    st.markdown("<div class='glass'><h2>Evaluasi Kualitas Air</h2></div>", unsafe_allow_html=True)

    nama = st.text_input("Nama Sampel")

    ph = st.number_input("pH",0.0,14.0,7.0)
    bod = st.number_input("BOD",0.0,100.0,1.0)
    cod = st.number_input("COD",0.0,500.0,5.0)
    do = st.number_input("DO",0.0,20.0,7.0)
    tss = st.number_input("TSS",0.0,1000.0,20.0)
    tds = st.number_input("TDS",0.0,5000.0,500.0)

    if st.button("Analisis"):

        hasil = [
            ["pH", ph, "6-9", "✔" if 6<=ph<=9 else "✖"],
            ["BOD", bod, "≤2", "✔" if bod<=2 else "✖"],
            ["COD", cod, "≤10", "✔" if cod<=10 else "✖"],
            ["DO", do, "≥6", "✔" if do>=6 else "✖"],
            ["TSS", tss, "≤40", "✔" if tss<=40 else "✖"],
            ["TDS", tds, "≤1000", "✔" if tds<=1000 else "✖"],
        ]

        df = pd.DataFrame(hasil, columns=["Parameter","Nilai","Standar","Status"])

        st.dataframe(df, use_container_width=True)

        ok = df["Status"].value_counts().get("✔",0)
        no = df["Status"].value_counts().get("✖",0)

        persen = (ok/6)*100

        st.success(f"Memenuhi: {ok}")
        st.error(f"Tidak: {no}")
        st.progress(int(persen))

        st.session_state.data.append([nama,ok,no,persen])

# =========================
# BAKU MUTU
# =========================
def baku_mutu():

    st.markdown("<div class='glass'><h2>Baku Mutu Air Kelas I</h2></div>", unsafe_allow_html=True)

    df = pd.DataFrame({
        "Parameter":["pH","BOD","COD","DO","TSS","TDS"],
        "Standar":["6-9","≤2","≤10","≥6","≤40","≤1000"]
    })

    st.table(df)

# =========================
# INTERPRETASI
# =========================
def interpretasi():

    st.markdown("<div class='glass'><h2>Interpretasi Parameter</h2></div>", unsafe_allow_html=True)

    st.write("""
    pH = tingkat keasaman air  
    BOD = bahan organik  
    COD = bahan kimia  
    DO = oksigen terlarut  
    TSS = kekeruhan  
    TDS = zat terlarut
    """)

# =========================
# LANDASAN HUKUM
# =========================
def hukum():

    st.markdown("<div class='glass'><h2>Landasan Hukum</h2></div>", unsafe_allow_html=True)

    st.info("PP No. 22 Tahun 2021 tentang Perlindungan dan Pengelolaan Lingkungan Hidup")

# =========================
# PENGEMBANG
# =========================
def pengembang():

    st.markdown("<div class='glass'><h2>Pengembang</h2></div>", unsafe_allow_html=True)

    df = pd.DataFrame({
        "Nama":[
            "Dela Rahayu Putri",
            "Mutiara Shifwah A",
            "Putri Bilqis Aliyyu N",
            "Rae Putri Kavi",
            "Salsabila Putri"
        ],
        "NIM":[
            "2530606","2530640","2530647","2530648","2530650"
        ]
    })

    st.table(df)

# =========================
# RIWAYAT
# =========================
def riwayat():

    st.markdown("<div class='glass'><h2>Riwayat Evaluasi</h2></div>", unsafe_allow_html=True)

    if len(st.session_state.data) == 0:
        st.info("Belum ada data")
    else:
        df = pd.DataFrame(st.session_state.data,
                          columns=["Nama","OK","NO","Kepatuhan"])

        st.dataframe(df, use_container_width=True)

        st.bar_chart(df.set_index("Nama")["Kepatuhan"])

# =========================
# ROUTING
# =========================
if menu == "Home":
    home()
elif menu == "Evaluasi Kualitas Air":
    evaluasi()
elif menu == "Baku Mutu Air Kelas I":
    baku_mutu()
elif menu == "Interpretasi Parameter":
    interpretasi()
elif menu == "Landasan Hukum":
    hukum()
elif menu == "Pengembang":
    pengembang()
elif menu == "Riwayat":
    riwayat()
