import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==================================
# CONFIG
# ==================================
st.set_page_config(
    page_title="AquaCek",
    page_icon="💧",
    layout="wide"
)

# ==================================
# SESSION STATE
# ==================================
if "history" not in st.session_state:
    st.session_state.history = []

# ==================================
# CSS PREMIUM
# ==================================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #E3F2FD, #F5FBFF, #D6F5FF);
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

.block-container {
    animation: fadeIn 0.8s ease;
}

.glass {
    background: rgba(255,255,255,0.75);
    backdrop-filter: blur(12px);
    padding: 25px;
    border-radius: 25px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    transition: 0.3s;
}

.glass:hover {
    transform: scale(1.01);
    box-shadow: 0px 10px 30px rgba(0,180,219,0.25);
}

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

.stButton button {
    background: linear-gradient(90deg, #00B4DB, #0083B0) !important;
    color: white !important;
    font-size: 16px !important;
    font-weight: bold !important;
    height: 50px !important;
    border-radius: 12px !important;
    width: 100%;
}

</style>
""", unsafe_allow_html=True)

# ==================================
# SIDEBAR MENU
# ==================================
menu = st.sidebar.radio(
    "💧 AQUACEK MENU",
    [
        "🏠 Home",
        "📊 Evaluasi Kualitas Air",
        "💧 Baku Mutu Air Kelas 1",
        "🧪 Interpretasi Parameter",
        "⚖️ Landasan Hukum",
        "📜 Riwayat Sampel",
        "👨‍💻 Pengembang"
    ]
)

# ==================================
# HOME
# ==================================
def home():
    st.markdown("""
    <div class="glass" style="text-align:center;">
        <div class="hero">💧</div>
        <h1>AquaCek</h1>
        <h3>Evaluasi Kualitas Air Kelas I</h3>
        <p>Berdasarkan PP No. 22 Tahun 2021</p>
    </div>
    """, unsafe_allow_html=True)

# ==================================
# EVALUASI
# ==================================
def evaluasi():

    st.markdown("""
    <div class="glass" style="text-align:center;">
        <h2>📊 Evaluasi Kualitas Air</h2>
    </div>
    """, unsafe_allow_html=True)

    nama = st.text_input("Nama Sampel")

    col1, col2 = st.columns(2)

    with col1:
        ph = st.number_input("pH", 0.0, 14.0, 7.0)
        bod = st.number_input("BOD", 0.0, 100.0, 1.0)
        cod = st.number_input("COD", 0.0, 500.0, 5.0)

    with col2:
        do = st.number_input("DO", 0.0, 20.0, 7.0)
        tss = st.number_input("TSS", 0.0, 1000.0, 20.0)
        tds = st.number_input("TDS", 0.0, 5000.0, 500.0)

    if st.button("🔍 Evaluasi"):

        data = [
            ["pH", ph, "6-9", "✅" if 6 <= ph <= 9 else "❌"],
            ["BOD", bod, "≤2", "✅" if bod <= 2 else "❌"],
            ["COD", cod, "≤10", "✅" if cod <= 10 else "❌"],
            ["DO", do, "≥6", "✅" if do >= 6 else "❌"],
            ["TSS", tss, "≤40", "✅" if tss <= 40 else "❌"],
            ["TDS", tds, "≤1000", "✅" if tds <= 1000 else "❌"],
        ]

        df = pd.DataFrame(data, columns=["Parameter", "Nilai", "Baku Mutu", "Status"])

        st.dataframe(df, use_container_width=True)

        lolos = (df["Status"] == "✅").sum()
        gagal = (df["Status"] == "❌").sum()
        persen = (lolos / len(df)) * 100

        st.metric("Memenuhi", lolos)
        st.metric("Tidak Memenuhi", gagal)
        st.metric("Kepatuhan", f"{persen:.1f}%")

        st.progress(int(persen))

        # grafik
        fig, ax = plt.subplots()
        ax.bar(["OK", "Tidak"], [lolos, gagal])
        st.pyplot(fig)

        # kesimpulan
        if gagal == 0:
            st.success(f"{nama} MEMENUHI baku mutu")
        else:
            st.error(f"{nama} TIDAK MEMENUHI baku mutu")

        # history
        st.session_state.history.append([nama, lolos, gagal, persen])

        # download
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download CSV", csv, "hasil_aqua.csv")

# ==================================
# BAKU MUTU
# ==================================
def baku_mutu():
    st.markdown("<div class='glass'><h2>💧 Baku Mutu Air Kelas I</h2></div>", unsafe_allow_html=True)

    df = pd.DataFrame({
        "Parameter": ["pH","BOD","COD","DO","TSS","TDS"],
        "Baku Mutu": ["6-9","≤2","≤10","≥6","≤40","≤1000"]
    })

    st.dataframe(df, use_container_width=True)

# ==================================
# INTERPRETASI
# ==================================
def interpretasi():

    st.markdown("<div class='glass'><h2>🧪 Interpretasi Parameter</h2></div>", unsafe_allow_html=True)

    data = [
        ["pH","Keasaman air"],
        ["BOD","Oksigen biologis (semakin tinggi → tercemar)"],
        ["COD","Oksigen kimia"],
        ["DO","Oksigen terlarut (semakin tinggi semakin baik)"],
        ["TSS","Padatan tersuspensi"],
        ["TDS","Zat terlarut"]
    ]

    st.dataframe(pd.DataFrame(data, columns=["Parameter","Makna"]))

# ==================================
# HUKUM
# ==================================
def hukum():

    st.markdown("<div class='glass'><h2>⚖️ Landasan Hukum</h2></div>", unsafe_allow_html=True)

    st.write("""
    - PP No. 22 Tahun 2021
    - Baku Mutu Air Permukaan
    - Air Kelas I = air baku minum
    """)

# ==================================
# RIWAYAT
# ==================================
def riwayat():

    st.markdown("<div class='glass'><h2>📜 Riwayat Sampel</h2></div>", unsafe_allow_html=True)

    if len(st.session_state.history) == 0:
        st.info("Belum ada data")
    else:
        st.dataframe(pd.DataFrame(st.session_state.history,
                                  columns=["Nama","Lolos","Gagal","%"]))

# ==================================
# PENGEMBANG
# ==================================
def pengembang():

    st.markdown("<div class='glass'><h2>👨‍💻 Pengembang AquaCek</h2></div>", unsafe_allow_html=True)

    data = {
        "Nama":[
            "Dela Rahayu Putri",
            "Mutiara Shifwah A",
            "Putri Bilqis Aliyyu N",
            "Rae Putri Kavi",
            "Salsabila Putri"
        ],
        "NIM":[
            "2530606",
            "2530640",
            "2530647",
            "2530648",
            "2530650"
        ]
    }

    st.dataframe(pd.DataFrame(data), use_container_width=True)

    st.success("AquaCek Team - AKA Bogor 2026")

# ==================================
# ROUTING
# ==================================
if menu == "🏠 Home":
    home()
elif menu == "📊 Evaluasi Kualitas Air":
    evaluasi()
elif menu == "💧 Baku Mutu Air Kelas 1":
    baku_mutu()
elif menu == "🧪 Interpretasi Parameter":
    interpretasi()
elif menu == "⚖️ Landasan Hukum":
    hukum()
elif menu == "📜 Riwayat Sampel":
    riwayat()
elif menu == "👨‍💻 Pengembang":
    pengembang()
    import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================
# CONFIG
# ==================================
st.set_page_config(
    page_title="AquaCek",
    page_icon="💧",
    layout="wide"
)

# ==================================
# SESSION STATE
# ==================================
if "history" not in st.session_state:
    st.session_state.history = []

# ==================================
# CSS
# ==================================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #E3F2FD, #F5FBFF, #D6F5FF);
}

.glass {
    background: rgba(255,255,255,0.75);
    backdrop-filter: blur(12px);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

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

</style>
""", unsafe_allow_html=True)

# ==================================
# MENU
# ==================================
menu = st.sidebar.radio(
    "💧 AQUACEK MENU",
    [
        "🏠 Home",
        "📊 Evaluasi",
        "💧 Baku Mutu",
        "🧪 Interpretasi",
        "⚖️ Hukum",
        "📜 Riwayat",
        "👨‍💻 Pengembang"
    ]
)

# ==================================
# HOME
# ==================================
def home():

    st.markdown("""
    <div class="glass" style="text-align:center;">
        <div class="hero">💧</div>
        <h1>AquaCek</h1>
        <h3>Evaluasi Kualitas Air Kelas I</h3>
        <p>PP No. 22 Tahun 2021</p>
    </div>
    """, unsafe_allow_html=True)

    total = len(st.session_state.history)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sampel", total)

    if total > 0:
        avg = sum([x[3] for x in st.session_state.history]) / total
        best = max([x[3] for x in st.session_state.history])
    else:
        avg = 0
        best = 0

    col2.metric("Rata-rata Kepatuhan", f"{avg:.1f}%")
    col3.metric("Tertinggi", f"{best:.1f}%")

# ==================================
# EVALUASI
# ==================================
def evaluasi():

    st.markdown("""
    <div class="glass" style="text-align:center;">
        <h2>📊 Evaluasi Kualitas Air</h2>
    </div>
    """, unsafe_allow_html=True)

    nama = st.text_input("Nama Sampel")

    col1, col2 = st.columns(2)

    with col1:
        ph = st.number_input("pH", 0.0, 14.0, 7.0)
        bod = st.number_input("BOD", 0.0, 100.0, 1.0)
        cod = st.number_input("COD", 0.0, 500.0, 5.0)

    with col2:
        do = st.number_input("DO", 0.0, 20.0, 7.0)
        tss = st.number_input("TSS", 0.0, 1000.0, 20.0)
        tds = st.number_input("TDS", 0.0, 5000.0, 500.0)

    if st.button("🔍 Evaluasi"):

        df = pd.DataFrame([
            ["pH", ph, "6-9", "OK" if 6 <= ph <= 9 else "NO"],
            ["BOD", bod, "≤2", "OK" if bod <= 2 else "NO"],
            ["COD", cod, "≤10", "OK" if cod <= 10 else "NO"],
            ["DO", do, "≥6", "OK" if do >= 6 else "NO"],
            ["TSS", tss, "≤40", "OK" if tss <= 40 else "NO"],
            ["TDS", tds, "≤1000", "OK" if tds <= 1000 else "NO"],
        ], columns=["Parameter", "Nilai", "Standar", "Status"])

        st.dataframe(df, use_container_width=True)

        ok = (df["Status"] == "OK").sum()
        no = (df["Status"] == "NO").sum()
        persen = (ok / len(df)) * 100

        col1, col2, col3 = st.columns(3)
        col1.metric("Memenuhi", ok)
        col2.metric("Tidak", no)
        col3.metric("Kepatuhan", f"{persen:.1f}%")

        fig = px.bar(
            x=["OK", "NO"],
            y=[ok, no],
            title="Kepatuhan Air"
        )
        st.plotly_chart(fig, use_container_width=True)

        if no == 0:
            st.success(f"{nama} MEMENUHI baku mutu")
        else:
            st.error(f"{nama} TIDAK MEMENUHI baku mutu")

        st.session_state.history.append([nama, ok, no, persen])

        st.download_button(
            "📥 Download CSV",
            df.to_csv(index=False).encode("utf-8"),
            "aqua_cek.csv"
        )

# ==================================
# BAKU MUTU
# ==================================
def baku_mutu():

    st.markdown("<div class='glass'><h2>💧 Baku Mutu Air Kelas I</h2></div>", unsafe_allow_html=True)

    df = pd.DataFrame({
        "Parameter": ["pH","BOD","COD","DO","TSS","TDS"],
        "Standar": ["6-9","≤2","≤10","≥6","≤40","≤1000"]
    })

    st.dataframe(df, use_container_width=True)

# ==================================
# INTERPRETASI
# ==================================
def interpretasi():

    st.markdown("<div class='glass'><h2>🧪 Interpretasi</h2></div>", unsafe_allow_html=True)

    df = pd.DataFrame([
        ["pH","Keasaman air"],
        ["BOD","Pencemaran organik"],
        ["COD","Pencemaran kimia"],
        ["DO","Oksigen air"],
        ["TSS","Kekeruhan"],
        ["TDS","Zat terlarut"]
    ], columns=["Parameter","Arti"])

    st.dataframe(df, use_container_width=True)

# ==================================
# HUKUM
# ==================================
def hukum():

    st.markdown("<div class='glass'><h2>⚖️ Landasan Hukum</h2></div>", unsafe_allow_html=True)

    st.write("""
    - PP No. 22 Tahun 2021
    - Baku Mutu Air Permukaan
    - Air Kelas I untuk air baku minum
    """)

# ==================================
# RIWAYAT
# ==================================
def riwayat():

    st.markdown("<div class='glass'><h2>📜 Riwayat</h2></div>", unsafe_allow_html=True)

    if len(st.session_state.history) == 0:
        st.info("Belum ada data")
    else:
        st.dataframe(pd.DataFrame(
            st.session_state.history,
            columns=["Nama","OK","NO","%"]
        ))

# ==================================
# PENGEMBANG
# ==================================
def pengembang():

    st.markdown("<div class='glass'><h2>👨‍💻 Pengembang</h2></div>", unsafe_allow_html=True)

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

    st.success("AquaCek Team — AKA Bogor 2026 💧")

# ==================================
# ROUTING
# ==================================
if menu == "🏠 Home":
    home()
elif menu == "📊 Evaluasi":
    evaluasi()
elif menu == "💧 Baku Mutu":
    baku_mutu()
elif menu == "🧪 Interpretasi":
    interpretasi()
elif menu == "⚖️ Hukum":
    hukum()
elif menu == "📜 Riwayat":
    riwayat()
elif menu == "👨‍💻 Pengembang":
    pengembang()
    import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================
# CONFIG
# ==================================
st.set_page_config(
    page_title="AquaCek PRO",
    page_icon="💧",
    layout="wide"
)

# ==================================
# SESSION STATE
# ==================================
if "history" not in st.session_state:
    st.session_state.history = []

# ==================================
# CSS PREMIUM
# ==================================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #E3F2FD, #F5FBFF, #D6F5FF);
}

.glass {
    background: rgba(255,255,255,0.75);
    backdrop-filter: blur(12px);
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    margin-bottom: 15px;
    transition: 0.3s;
}

.glass:hover {
    transform: scale(1.01);
}

.hero {
    font-size: 75px;
    text-align: center;
    animation: float 3s infinite;
}

@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-12px);}
    100% {transform: translateY(0px);}
}

.stButton button {
    background: linear-gradient(90deg, #00B4DB, #0083B0) !important;
    color: white !important;
    font-weight: bold !important;
    height: 50px !important;
    border-radius: 12px !important;
    width: 100%;
}

</style>
""", unsafe_allow_html=True)

# ==================================
# MENU
# ==================================
menu = st.sidebar.radio(
    "💧 AQUACEK PRO",
    [
        "🏠 Home",
        "📊 Evaluasi",
        "💧 Baku Mutu",
        "🧪 Interpretasi",
        "⚖️ Hukum",
        "📜 Riwayat",
        "👨‍💻 Pengembang"
    ]
)

# ==================================
# HOME
# ==================================
def home():

    st.markdown("""
    <div class="glass" style="text-align:center;">
        <div class="hero">💧</div>
        <h1>AquaCek PRO</h1>
        <h3>Water Quality Intelligence System</h3>
        <p>PP No. 22 Tahun 2021</p>
    </div>
    """, unsafe_allow_html=True)

    total = len(st.session_state.history)

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Sampel", total)

    if total > 0:
        avg = sum([x[3] for x in st.session_state.history]) / total
        best = max([x[3] for x in st.session_state.history])
    else:
        avg = 0
        best = 0

    col2.metric("Rata-rata", f"{avg:.1f}%")
    col3.metric("Tertinggi", f"{best:.1f}%")

# ==================================
# EVALUASI
# ==================================
def evaluasi():

    st.markdown("""
    <div class="glass" style="text-align:center;">
        <h2>📊 Evaluasi Kualitas Air</h2>
    </div>
    """, unsafe_allow_html=True)

    nama = st.text_input("Nama Sampel")

    col1, col2 = st.columns(2)

    with col1:
        ph = st.number_input("pH", 0.0, 14.0, 7.0)
        bod = st.number_input("BOD", 0.0, 100.0, 1.0)
        cod = st.number_input("COD", 0.0, 500.0, 5.0)

    with col2:
        do = st.number_input("DO", 0.0, 20.0, 7.0)
        tss = st.number_input("TSS", 0.0, 1000.0, 20.0)
        tds = st.number_input("TDS", 0.0, 5000.0, 500.0)

    if st.button("🔍 Analisis AquaCek PRO"):

        df = pd.DataFrame([
            ["pH", ph, "6-9", 1 if 6 <= ph <= 9 else 0],
            ["BOD", bod, "≤2", 1 if bod <= 2 else 0],
            ["COD", cod, "≤10", 1 if cod <= 10 else 0],
            ["DO", do, "≥6", 1 if do >= 6 else 0],
            ["TSS", tss, "≤40", 1 if tss <= 40 else 0],
            ["TDS", tds, "≤1000", 1 if tds <= 1000 else 0],
        ], columns=["Parameter","Nilai","Standar","Status"])

        df["Label"] = df["Status"].apply(lambda x: "OK" if x == 1 else "NO")

        st.dataframe(df)

        ok = df["Status"].sum()
        no = 6 - ok
        persen = (ok / 6) * 100

        col1, col2, col3 = st.columns(3)

        col1.metric("Memenuhi", ok)
        col2.metric("Tidak", no)
        col3.metric("Kepatuhan", f"{persen:.1f}%")

        # chart PRO
        fig = px.pie(
            names=["Memenuhi","Tidak"],
            values=[ok,no],
            title="Kepatuhan Kualitas Air"
        )

        st.plotly_chart(fig, use_container_width=True)

        if no == 0:
            st.success(f"💧 {nama} LAYAK (MEMENUHI STANDAR)")
        else:
            st.error(f"⚠️ {nama} TIDAK LAYAK")

        st.session_state.history.append([nama, ok, no, persen])

        st.download_button(
            "📥 Export Data",
            df.to_csv(index=False).encode("utf-8"),
            "aquacek_pro.csv"
        )

# ==================================
# BAKU MUTU
# ==================================
def baku_mutu():

    st.markdown("<div class='glass'><h2>💧 Baku Mutu Air Kelas I</h2></div>", unsafe_allow_html=True)

    df = pd.DataFrame({
        "Parameter": ["pH","BOD","COD","DO","TSS","TDS"],
        "Standar": ["6-9","≤2","≤10","≥6","≤40","≤1000"]
    })

    st.dataframe(df, use_container_width=True)

# ==================================
# INTERPRETASI
# ==================================
def interpretasi():

    st.markdown("<div class='glass'><h2>🧪 Interpretasi Parameter</h2></div>", unsafe_allow_html=True)

    df = pd.DataFrame([
        ["pH","Asam / basa air"],
        ["BOD","Pencemar organik"],
        ["COD","Pencemar kimia"],
        ["DO","Oksigen terlarut"],
        ["TSS","Kekeruhan air"],
        ["TDS","Mineral terlarut"]
    ], columns=["Parameter","Arti"])

    st.dataframe(df, use_container_width=True)

# ==================================
# HUKUM
# ==================================
def hukum():

    st.markdown("<div class='glass'><h2>⚖️ Landasan Hukum</h2></div>", unsafe_allow_html=True)

    st.write("""
    ✔ PP No. 22 Tahun 2021  
    ✔ Baku Mutu Air Permukaan  
    ✔ Air Kelas I (air baku minum)
    """)

# ==================================
# RIWAYAT
# ==================================
def riwayat():

    st.markdown("<div class='glass'><h2>📜 Riwayat Analisis</h2></div>", unsafe_allow_html=True)

    if len(st.session_state.history) == 0:
        st.info("Belum ada data")
    else:
        st.dataframe(pd.DataFrame(
            st.session_state.history,
            columns=["Nama","OK","NO","%"]
        ))

# ==================================
# PENGEMBANG
# ==================================
def pengembang():

    st.markdown("<div class='glass'><h2>👨‍💻 Tim Pengembang</h2></div>", unsafe_allow_html=True)

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

    st.success("AquaCek PRO — AKA Bogor 2026 💧")

# ==================================
# ROUTING
# ==================================
if menu == "🏠 Home":
    home()
elif menu == "📊 Evaluasi":
    evaluasi()
elif menu == "💧 Baku Mutu":
    baku_mutu()
elif menu == "🧪 Interpretasi":
    interpretasi()
elif menu == "⚖️ Hukum":
    hukum()
elif menu == "📜 Riwayat":
    riwayat()
elif menu == "👨‍💻 Pengembang":
    pengembang()
