
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

/* =========================
BACKGROUND
========================= */

.stApp{
background:linear-gradient(
135deg,
#dff6ff,
#b8e8fc,
#e3f8ff,
#caf0f8
);
background-size:400% 400%;
animation:bgmove 15s ease infinite;
}

@keyframes bgmove{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}
.glass:hover{
transform:translateY(-8px);
transition:0.3s;
box-shadow:0 15px 30px rgba(0,180,219,0.25);
}
/* =========================
CARD
========================= */

.glass{
background:rgba(255,255,255,0.75);
backdrop-filter:blur(12px);
padding:25px;
border-radius:25px;
box-shadow:0 8px 30px rgba(0,0,0,0.08);

animation:fadeUp 0.8s ease;
}

@keyframes fadeUp{
from{
opacity:0;
transform:translateY(30px);
}
to{
opacity:1;
transform:translateY(0);
}
}

/* =========================
HERO ICON
========================= */

.hero{
font-size:90px;
text-align:center;
animation:floatWater 3s ease-in-out infinite;
}

@keyframes floatWater{
0%{transform:translateY(0px);}
50%{transform:translateY(-18px);}
100%{transform:translateY(0px);}
}

/* =========================
SIDEBAR
========================= */

section[data-testid="stSidebar"]{
background:linear-gradient(
180deg,
#0ea5e9,
#38bdf8
);
}

/* Menu jadi kotak */

div[role="radiogroup"] > label{
background:white !important;
padding:12px !important;
margin-bottom:10px !important;
border-radius:15px !important;

box-shadow:0 5px 15px rgba(0,0,0,0.08);

transition:0.3s;
}

div[role="radiogroup"] > label:hover{
transform:translateY(-4px);
box-shadow:0 10px 20px rgba(14,165,233,0.3);
}

/* =========================
BUTTON
========================= */

.stButton button{

background:linear-gradient(
90deg,
#00b4db,
#0083b0
)!important;

color:white!important;

border-radius:15px!important;

height:50px!important;

font-weight:bold!important;

transition:0.3s;
}

.stButton button:hover{

transform:scale(1.05);

box-shadow:0 8px 20px rgba(0,180,219,0.4);

}

/* =========================
TABLE
========================= */

[data-testid="stDataFrame"]{

border-radius:15px;

overflow:hidden;

box-shadow:0 5px 15px rgba(0,0,0,0.08);

}

/* =========================
METRIC CARD
========================= */

[data-testid="stMetric"]{

background:white;

padding:15px;

border-radius:15px;

box-shadow:0 5px 15px rgba(0,0,0,0.08);

}
/* =========================
KARTU PARAMETER
========================= */

.param-card{
padding:20px;
border-radius:20px;
margin-bottom:15px;
color:white;
transition:0.3s;
box-shadow:0 8px 20px rgba(0,0,0,0.15);
}

.param-card:hover{
transform:translateY(-8px) scale(1.02);
}

.ph{
background:linear-gradient(135deg,#2196F3,#64B5F6);
}

.bod{
background:linear-gradient(135deg,#FF9800,#FFB74D);
}

.cod{
background:linear-gradient(135deg,#9C27B0,#BA68C8);
}

.do{
background:linear-gradient(135deg,#4CAF50,#81C784);
}

.tss{
background:linear-gradient(135deg,#795548,#A1887F);
}

.tds{
background:linear-gradient(135deg,#607D8B,#90A4AE);
}
.glass{
transition: all 0.3s ease;
}

.glass:hover{
transform: translateY(-8px);
box-shadow: 0 15px 30px rgba(0,180,219,0.25);
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

    st.markdown("""
    <div class="glass">
    <h1 style="text-align:center;">
    🧪 Interpretasi Parameter Kualitas Air
    </h1>
    <p style="text-align:center;">
    Belajar parameter air dengan cara yang lebih menyenangkan 💧
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="param-card ph">
    <h2>⚖️ pH</h2>
    <h3>💙 Derajat Keasaman</h3>
    <p>
    Menunjukkan tingkat keasaman atau kebasaan air.
    Air yang baik memiliki pH 6–9.
    </p>
    <h2>😖 ← 🧪 → 😊</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="param-card bod">
    <h2>🍂 BOD</h2>
    <h3>🦠 Bahan Organik</h3>
    <p>
    Menunjukkan kebutuhan oksigen mikroorganisme
    untuk menguraikan bahan organik.
    </p>
    <h2>🍌 🍃 🌱</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="param-card cod">
    <h2>⚗️ COD</h2>
    <h3>🧪 Pencemar Kimia</h3>
    <p>
    Menunjukkan jumlah oksigen yang diperlukan
    untuk mengoksidasi bahan pencemar kimia.
    </p>
    <h2>🏭 🧴 ⚗️</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="param-card do">
    <h2>🐟 DO</h2>
    <h3>💨 Oksigen Terlarut</h3>
    <p>
    Semakin tinggi DO,
    semakin baik kualitas air.
    </p>
    <h2>🐠 🐟 🦐 🌊</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="param-card tss">
    <h2>🌫️ TSS</h2>
    <h3>🟤 Padatan Tersuspensi</h3>
    <p>
    Lumpur, pasir dan partikel
    yang melayang dalam air.
    </p>
    <h2>🌊 + 🟤🟤🟤</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="param-card tds">
    <h2>🧂 TDS</h2>
    <h3>💎 Padatan Terlarut</h3>
    <p>
    Menunjukkan jumlah zat
    yang larut dalam air.
    </p>
    <h2>🧂 💎 ⚗️</h2>
    </div>
    """, unsafe_allow_html=True)

    st.success("""
🎯 Ringkasan Cepat

💙 pH = Keasaman

🍂 BOD = Organik

⚗️ COD = Kimia

🐟 DO = Oksigen Terlarut

🌫️ TSS = Padatan Tersuspensi

🧂 TDS = Padatan Terlarut
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

    st.markdown("""
    <div class="glass">
        <div style="text-align:center;">
            <h1>🏫 AKA BOGOR</h1>
            <h2>💧 AquaCek Development Team</h2>
            <h3>🎓 Tugas Akhir Mata Kuliah Logika Pemrograman</h3>
            <h4>🧪 Program Studi Pengelolaan Limbah Industri</h4>
            <h4>📚 Semester II • Tahun Akademik 2026</h4>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.balloons()

    st.markdown("## 👥 Tim Pengembang")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="glass">
        <h3>🧪 Dela Rahayu Putri</h3>
        <h4>🎓 NIM : 2530606</h4>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="glass">
        <h3>🔬 Putri Bilqis Aliyyu N</h3>
        <h4>🎓 NIM : 2530647</h4>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="glass">
        <h3>🧫 Salsabila Putri</h3>
        <h4>🎓 NIM : 2530650</h4>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="glass">
        <h3>⚙️ Mutiara Shifwah A</h3>
        <h4>🎓 NIM : 2530640</h4>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="glass">
        <h3>💻 Rae Putri Kavi</h3>
        <h4>🎓 NIM : 2530648</h4>
        </div>
        """, unsafe_allow_html=True)
st.markdown("""
<div class="glass">
<div style="text-align:center;">

<h2>💙 Tentang AquaCek</h2>

<p style="font-size:18px;">

💧 <b>AquaCek</b> merupakan aplikasi evaluasi kualitas air yang
dirancang untuk membantu pengguna dalam membandingkan hasil
pengujian kualitas air dengan baku mutu Air Kelas I berdasarkan
Peraturan Pemerintah Nomor 22 Tahun 2021.

</p>

<p style="font-size:18px;">

🧪 Aplikasi ini mampu melakukan evaluasi terhadap beberapa
parameter penting kualitas air seperti pH, BOD, COD, DO,
TSS, dan TDS serta memberikan interpretasi parameter secara
interaktif dan mudah dipahami.

</p>

<p style="font-size:18px;">

📊 AquaCek dikembangkan sebagai proyek Tugas Akhir Mata Kuliah
Logika Pemrograman oleh mahasiswa Program Studi Pengelolaan
Limbah Industri Semester II Angkatan XI Tahun 2026
Akademi Kimia Analis Bogor.

</p>

<p style="font-size:18px;">

🌊 Melalui tampilan yang interaktif, informatif, dan edukatif,
AquaCek diharapkan dapat membantu proses pembelajaran,
praktikum, serta pemahaman mengenai evaluasi kualitas air
sesuai peraturan yang berlaku di Indonesia.

</p>

<h3>
🏫 AKA Bogor • 🧪 Pengelolaan Limbah Industri • 💧 AquaCek 2026
</h3>

</div>
</div>
""", unsafe_allow_html=True)
    
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
