import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="AquaCek",
    page_icon="💧",
    layout="wide"
)

# =========================
# UI ANIMASI
# =========================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(-45deg, #e3f2fd, #bbdefb, #e1f5fe, #b3e5fc);
    background-size: 400% 400%;
    animation: moveBG 10s ease infinite;
}

@keyframes moveBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.glass {
    background: rgba(255,255,255,0.75);
    backdrop-filter: blur(12px);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 0 25px rgba(0,180,219,0.15);
    margin-bottom: 15px;
}

.hero {
    font-size: 80px;
    text-align: center;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0% {transform: translateY(0);}
    50% {transform: translateY(-15px);}
    100% {transform: translateY(0);}
}

.stButton button {
    background: linear-gradient(90deg, #00B4DB, #0083B0) !important;
    color: white !important;
    font-weight: bold !important;
    border-radius: 12px !important;
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
        "📊 Evaluasi",
        "💧 Baku Mutu",
        "🧪 Interpretasi",
        "⚖️ Hukum",
        "👨‍💻 Pengembang",
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
        <h1>AQUACEK</h1>
        <h3>Evaluasi Kualitas Air Kelas I</h3>
        <p><b>PP No. 22 Tahun 2021</b></p>
    </div>
    """, unsafe_allow_html=True)

    total = len(st.session_state.history)

    if total > 0:
        avg = sum([x[3] for x in st.session_state.history]) / total
    else:
        avg = 0

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sampel", total)
    col2.metric("Rata-rata Kepatuhan", f"{avg:.1f}%")
    col3.metric("Status Sistem", "Aktif 💧")

    if total > 0:
        df = pd.DataFrame(st.session_state.history,
                          columns=["Nama","OK","NO","Kepatuhan"])

        fig = px.bar(df, x="Nama", y="Kepatuhan",
                     color="Kepatuhan",
                     title="📊 Dashboard Kepatuhan")
        st.plotly_chart(fig, use_container_width=True)

        fig2 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=avg,
            title={"text": "Indeks Kualitas Air"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#00B4DB"},
                "steps": [
                    {"range": [0, 50], "color": "#ff6b6b"},
                    {"range": [50, 80], "color": "#feca57"},
                    {"range": [80, 100], "color": "#1dd1a1"}
                ]
            }
        ))

        st.plotly_chart(fig2, use_container_width=True)

# =========================
# EVALUASI
# =========================
def evaluasi():

    st.markdown("<div class='glass'><h2>📊 Evaluasi Air</h2></div>", unsafe_allow_html=True)

    nama = st.text_input("Nama Sampel")

    ph = st.number_input("pH", 0.0, 14.0, 7.0)
    bod = st.number_input("BOD", 0.0, 100.0, 1.0)
    cod = st.number_input("COD", 0.0, 500.0, 5.0)
    do = st.number_input("DO", 0.0, 20.0, 7.0)
    tss = st.number_input("TSS", 0.0, 1000.0, 20.0)
    tds = st.number_input("TDS", 0.0, 5000.0, 500.0)

    if st.button("🔍 Analisis"):

        df = pd.DataFrame({
            "Parameter": ["pH","BOD","COD","DO","TSS","TDS"],
            "Nilai": [ph,bod,cod,do,tss,tds],
            "Status": [
                "✔" if 6<=ph<=9 else "✖",
                "✔" if bod<=2 else "✖",
                "✔" if cod<=10 else "✖",
                "✔" if do>=6 else "✖",
                "✔" if tss<=40 else "✖",
                "✔" if tds<=1000 else "✖"
            ]
        })

        ok = df["Status"].value_counts().get("✔",0)
        no = df["Status"].value_counts().get("✖",0)
        persen = (ok/6)*100

        st.dataframe(df, use_container_width=True)

        col1,col2,col3 = st.columns(3)
        col1.metric("Memenuhi", ok)
        col2.metric("Tidak", no)
        col3.metric("Kepatuhan", f"{persen:.1f}%")

        st.progress(int(persen))

        fig = px.pie(df, names="Status", title="Distribusi Kualitas")
        st.plotly_chart(fig, use_container_width=True)

        st.session_state.history.append([nama,ok,no,persen])

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

    fig = px.bar(df, x="Parameter", y=[1,1,1,1,1,1],
                 title="Visual Parameter Air")
    st.plotly_chart(fig, use_container_width=True)

# =========================
# INTERPRETASI
# =========================
def interpretasi():

    st.markdown("<div class='glass'><h2>🧪 Interpretasi</h2></div>", unsafe_allow_html=True)

    df = pd.DataFrame([
        ["pH","Asam/basa"],
        ["BOD","Organik"],
        ["COD","Kimia"],
        ["DO","Oksigen"],
        ["TSS","Kekeruhan"],
        ["TDS","Zat terlarut"]
    ], columns=["Parameter","Arti"])

    st.dataframe(df, use_container_width=True)

# =========================
# HUKUM
# =========================
def hukum():

    st.markdown("<div class='glass'><h2>⚖️ Landasan Hukum</h2></div>", unsafe_allow_html=True)

    st.info("PP No. 22 Tahun 2021 tentang Perlindungan dan Pengelolaan Lingkungan Hidup")

# =========================
# PENGEMBANG
# =========================
def pengembang():

    st.markdown("<div class='glass'><h2>👨‍💻 Pengembang</h2></div>", unsafe_allow_html=True)

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

    st.dataframe(df, use_container_width=True)

# =========================
# RIWAYAT
# =========================
def riwayat():

    st.markdown("<div class='glass'><h2>📜 Riwayat</h2></div>", unsafe_allow_html=True)

    if len(st.session_state.history)==0:
        st.info("Belum ada data")
    else:
        df = pd.DataFrame(st.session_state.history,
                          columns=["Nama","OK","NO","Kepatuhan"])

        st.dataframe(df, use_container_width=True)

        fig = px.line(df, x="Nama", y="Kepatuhan", markers=True,
                      title="Tren Kualitas Air")
        st.plotly_chart(fig, use_container_width=True)

# =========================
# ROUTING
# =========================
if menu=="🏠 Home":
    home()
elif menu=="📊 Evaluasi":
    evaluasi()
elif menu=="💧 Baku Mutu":
    baku_mutu()
elif menu=="🧪 Interpretasi":
    interpretasi()
elif menu=="⚖️ Hukum":
    hukum()
elif menu=="👨‍💻 Pengembang":
    pengembang()
elif menu=="📜 Riwayat":
    riwayat()
