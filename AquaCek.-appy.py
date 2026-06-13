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
# CSS / UI
# =========================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #E3F2FD, #F5FBFF, #D6F5FF);
}

/* animasi */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

.block-container {
    animation: fadeIn 0.8s ease;
}

/* glass card */
.glass {
    background: rgba(255,255,255,0.75);
    backdrop-filter: blur(10px);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

/* hero icon */
.hero {
    font-size: 70px;
    text-align: center;
    animation: float 3s infinite;
}

@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-10px);}
    100% {transform: translateY(0px);}
}

/* button */
.stButton button {
    background: linear-gradient(90deg, #00B4DB, #0083B0) !important;
    color: white !important;
    font-weight: bold !important;
    border-radius: 12px !important;
    height: 45px !important;
    width: 100%;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SESSION
# =========================
if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# MENU
# =========================
menu = st.sidebar.radio(
    "💧 AQUACEK MENU",
    [
        "🏠 Home",
        "📊 Evaluasi Kualitas Air",
        "💧 Baku Mutu Air Kelas I",
        "🧪 Interpretasi Parameter",
        "⚖️ Landasan Hukum",
        "👨‍💻 Tentang Pengembang",
        "📜 Riwayat"
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
        <p>Berdasarkan PP No. 22 Tahun 2021</p>
    </div>
    """, unsafe_allow_html=True)

    total = len(st.session_state.history)

    if total > 0:
        avg = sum([x[3] for x in st.session_state.history]) / total
    else:
        avg = 0

    col1, col2 = st.columns(2)
    col1.metric("Total Sampel", total)
    col2.metric("Rata-rata Kepatuhan", f"{avg:.1f}%")

# =========================
# EVALUASI
# =========================
def evaluasi():

    st.markdown("""
    <div class="glass">
        <h2>📊 Evaluasi Kualitas Air</h2>
    </div>
    """, unsafe_allow_html=True)

    nama = st.text_input("Nama Sampel")

    ph = st.number_input("pH", 0.0, 14.0, 7.0)
    bod = st.number_input("BOD (mg/L)", 0.0, 100.0, 1.0)
    cod = st.number_input("COD (mg/L)", 0.0, 500.0, 5.0)
    do = st.number_input("DO (mg/L)", 0.0, 20.0, 7.0)
    tss = st.number_input("TSS (mg/L)", 0.0, 1000.0, 20.0)
    tds = st.number_input("TDS (mg/L)", 0.0, 5000.0, 500.0)

    if st.button("🔍 Evaluasi"):

        data = [
            ["pH", ph, "6-9", "✔" if 6 <= ph <= 9 else "✖"],
            ["BOD", bod, "≤2", "✔" if bod <= 2 else "✖"],
            ["COD", cod, "≤10", "✔" if cod <= 10 else "✖"],
            ["DO", do, "≥6", "✔" if do >= 6 else "✖"],
            ["TSS", tss, "≤40", "✔" if tss <= 40 else "✖"],
            ["TDS", tds, "≤1000", "✔" if tds <= 1000 else "✖"],
        ]

        df = pd.DataFrame(data, columns=["Parameter","Nilai","Standar","Status"])

        st.dataframe(df, use_container_width=True)

        ok = df["Status"].value_counts().get("✔", 0)
        no = df["Status"].value_counts().get("✖", 0)

        persen = (ok / 6) * 100

        col1, col2, col3 = st.columns(3)
        col1.metric("Memenuhi", ok)
        col2.metric("Tidak", no)
        col3.metric("Kepatuhan", f"{persen:.1f}%")

        if no == 0:
            st.success(f"💧 {nama} MEMENUHI BAKU MUTU AIR KELAS I")
        else:
            st.error(f"⚠️ {nama} TIDAK MEMENUHI BAKU MUTU")

        st.session_state.history.append([nama, ok, no, persen])

# =========================
# BAKU MUTU
# =========================
def baku_mutu():

    st.markdown("<div class='glass'><h2>💧 Baku Mutu Air Kelas I</h2></div>", unsafe_allow_html=True)

    df = pd.DataFrame({
        "Parameter": ["pH","BOD","COD","DO","TSS","TDS"],
        "Baku Mutu": ["6-9","≤2","≤10","≥6","≤40","≤1000"]
    })

    st.dataframe(df, use_container_width=True)

# =========================
# INTERPRETASI
# =========================
def interpretasi():

    st.markdown("<div class='glass'><h2>🧪 Interpretasi Parameter</h2></div>", unsafe_allow_html=True)

    df = pd.DataFrame([
        ["pH","Tingkat keasaman air"],
        ["BOD","Kandungan bahan organik"],
        ["COD","Kandungan bahan kimia"],
        ["DO","Oksigen terlarut"],
        ["TSS","Kekeruhan air"],
        ["TDS","Zat terlarut"]
    ], columns=["Parameter","Keterangan"])

    st.dataframe(df, use_container_width=True)

# =========================
# LANDASAN HUKUM
# =========================
def hukum():

    st.markdown("<div class='glass'><h2>⚖️ Landasan Hukum</h2></div>", unsafe_allow_html=True)

    st.write("""
    ✔ PP No. 22 Tahun 2021  
    ✔ Baku Mutu Air Permukaan  
    ✔ Standar Air Kelas I
    """)

# =========================
# PENGEMBANG
# =========================
def pengembang():

    st.markdown("<div class='glass'><h2>👨‍💻 Tentang Pengembang</h2></div>", unsafe_allow_html=True)

    df = pd.DataFrame({
        "Nama": [
            "Dela Rahayu Putri",
            "Mutiara Shifwah A",
            "Putri Bilqis Aliyyu N",
            "Rae Putri Kavi",
            "Salsabila Putri"
        ],
        "NIM": [
            "2530606",
            "2530640",
            "2530647",
            "2530648",
            "2530650"
        ]
    })

    st.dataframe(df, use_container_width=True)

# =========================
# RIWAYAT
# =========================
def riwayat():

    st.markdown("<div class='glass'><h2>📜 Riwayat Evaluasi</h2></div>", unsafe_allow_html=True)

    if len(st.session_state.history) == 0:
        st.info("Belum ada data")
    else:
        df = pd.DataFrame(
            st.session_state.history,
            columns=["Nama","OK","NO","Kepatuhan"]
        )

        st.dataframe(df, use_container_width=True)

# =========================
# ROUTING
# =========================
if menu == "🏠 Home":
    home()
elif menu == "📊 Evaluasi Kualitas Air":
    evaluasi()
elif menu == "💧 Baku Mutu Air Kelas I":
    baku_mutu()
elif menu == "🧪 Interpretasi Parameter":
    interpretasi()
elif menu == "⚖️ Landasan Hukum":
    hukum()
elif menu == "👨‍💻 Tentang Pengembang":
    pengembang()
elif menu == "📜 Riwayat":
    riwayat()
