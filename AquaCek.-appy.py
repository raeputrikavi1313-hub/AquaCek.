
import streamlit as st
import pandas as pd

# ==================================
# KONFIGURASI HALAMAN
# ==================================
st.set_page_config(
    page_title="AquaCheck",
    page_icon="💧",
    layout="wide"
)

# ==================================
# CSS PREMIUM
# ==================================
st.markdown("""
<style>

/* Background */
.stApp{
background: linear-gradient(
135deg,
#E3F2FD,
#F5FBFF,
#D6F5FF
);
}

/* Animasi */
@keyframes fadeIn{
from{
opacity:0;
transform:translateY(20px);
}
to{
opacity:1;
transform:translateY(0px);
}
}

.block-container{
animation: fadeIn 0.8s ease;
}

/* Glass Card */
.glass{
background: rgba(255,255,255,0.75);
backdrop-filter: blur(10px);
padding:25px;
border-radius:25px;
box-shadow:0px 8px 25px rgba(0,0,0,0.08);
}

/* Icon Mengambang */
@keyframes float{
0%{transform:translateY(0px);}
50%{transform:translateY(-8px);}
100%{transform:translateY(0px);}
}

.hero-icon{
font-size:70px;
animation: float 3s infinite;
text-align:center;
}

/* Tombol */
.stButton button{
background: linear-gradient(
90deg,
#00B4DB,
#0083B0
)!important;

color:white!important;
font-size:18px!important;
font-weight:bold!important;
height:55px!important;
border-radius:15px!important;
border:none!important;
transition:0.3s!important;
width:100%;
}

.stButton button:hover{
transform:scale(1.05);
box-shadow:0px 10px 25px rgba(0,180,219,0.4);
}

/* Metric */
[data-testid="stMetric"]{
background:white;
padding:15px;
border-radius:15px;
box-shadow:0px 2px 8px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# ==================================
# SIDEBAR
# ==================================
menu = st.sidebar.selectbox(
    "📂 Menu",
    [
        "🏠 Evaluasi Kualitas Air",
        "👨‍💻 Tentang Pengembang"
    ]
)

# ==================================
# HALAMAN PENGEMBANG
# ==================================
if menu == "👨‍💻 Tentang Pengembang":

    st.markdown("""
    <div class="glass">
    <h1 style="text-align:center;">
    👨‍💻 Tentang Pengembang
    </h1>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### 💧 AquaCheck

    AquaCheck merupakan aplikasi evaluasi kualitas air
    berdasarkan Peraturan Pemerintah Nomor 22 Tahun 2021
    untuk Air Kelas I.
    """)

    st.info("""
    Mata Kuliah : Logika Pemrograman

    Program Studi : Pengelolaan Limbah Industri

    Semester : II

    Tahun Akademik : 2026

    Institusi : Akademi Kimia Analis Bogor
    """)

    st.subheader("👥 Tim Pengembang")

    data_tim = {
        "Nama": [
            "Dela Rahayu Putri",
            "Mutiara Shifwah A.",
            "Putri Bilqis Aliyyu N.",
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
    }

    st.table(pd.DataFrame(data_tim))

    st.success("""
    © 2026 AquaCheck Team

    Hak cipta dimiliki oleh Tim AquaCheck
    Program Studi Pengelolaan Limbah Industri.

    Aplikasi ini dibuat untuk tujuan pendidikan
    dan pengembangan akademik.
    """)

    st.stop()

# ==================================
# HEADER
# ==================================
st.markdown("""
<div class="glass" style="text-align:center;">
<div class="hero-icon">💧</div>

<h1 style="color:#1B4F72;">
AquaCheck
</h1>

<h3 style="color:#2874A6;">
Water Quality Assessment
</h3>

<p>
Evaluasi Kualitas Air Kelas I
Berdasarkan PP No. 22 Tahun 2021
</p>

</div>
""", unsafe_allow_html=True)

st.subheader(
    "Acuan : Peraturan Pemerintah Nomor 22 Tahun 2021"
)

st.write("""
Aplikasi ini digunakan untuk mengevaluasi
kualitas air terhadap baku mutu
Air Kelas I.
""")

st.divider()

# ==================================
# INPUT DATA
# ==================================
st.markdown('<div class="glass">', unsafe_allow_html=True)

st.header("📋 Input Data Sampel")

nama_sampel = st.text_input(
    "Nama Sampel",
    placeholder="Contoh: Sungai Ciliwung Titik 1"
)

col1, col2 = st.columns(2)

with col1:

    ph = st.number_input(
        "pH",
        min_value=0.0,
        max_value=14.0,
        value=7.0,
        step=0.1
    )

    bod = st.number_input(
        "BOD (mg/L)",
        min_value=0.0,
        value=1.0,
        step=0.1
    )

    cod = st.number_input(
        "COD (mg/L)",
        min_value=0.0,
        value=5.0,
        step=0.1
    )

with col2:

    do = st.number_input(
        "DO (mg/L)",
        min_value=0.0,
        value=7.0,
        step=0.1
    )

    tss = st.number_input(
        "TSS (mg/L)",
        min_value=0.0,
        value=20.0,
        step=0.1
    )

    tds = st.number_input(
        "TDS (mg/L)",
        min_value=0.0,
        value=500.0,
        step=1.0
    )

st.markdown("</div>", unsafe_allow_html=True)

# ==================================
# EVALUASI
# ==================================
if st.button("🔍 Evaluasi Kualitas Air"):

    hasil = []

    hasil.append([
        "pH",
        ph,
        "6 - 9",
        "✅ Memenuhi" if 6 <= ph <= 9 else "❌ Tidak Memenuhi"
    ])

    hasil.append([
        "BOD",
        bod,
        "≤ 2",
        "✅ Memenuhi" if bod <= 2 else "❌ Tidak Memenuhi"
    ])

    hasil.append([
        "COD",
        cod,
        "≤ 10",
        "✅ Memenuhi" if cod <= 10 else "❌ Tidak Memenuhi"
    ])

    hasil.append([
        "DO",
        do,
        "≥ 6",
        "✅ Memenuhi" if do >= 6 else "❌ Tidak Memenuhi"
    ])

    hasil.append([
        "TSS",
        tss,
        "≤ 40",
        "✅ Memenuhi" if tss <= 40 else "❌ Tidak Memenuhi"
    ])

    hasil.append([
        "TDS",
        tds,
        "≤ 1000",
        "✅ Memenuhi" if tds <= 1000 else "❌ Tidak Memenuhi"
    ])

    df = pd.DataFrame(
        hasil,
        columns=[
            "Parameter",
            "Hasil",
            "Baku Mutu",
            "Status"
        ]
    )

    st.divider()

    st.header("📊 Hasil Evaluasi")

    st.dataframe(
        df,
        use_container_width=True
    )

    jumlah_memenuhi = (
        df["Status"] == "✅ Memenuhi"
    ).sum()

    jumlah_tidak = (
        df["Status"] == "❌ Tidak Memenuhi"
    ).sum()

    persentase = (
        jumlah_memenuhi / len(df)
    ) * 100

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "✅ Memenuhi",
            jumlah_memenuhi
        )

    with col2:
        st.metric(
            "❌ Tidak Memenuhi",
            jumlah_tidak
        )

    with col3:
        st.metric(
            "📈 Kepatuhan",
            f"{persentase:.1f}%"
        )

    st.subheader("📈 Tingkat Kepatuhan")

    st.progress(int(persentase))

    st.subheader("📋 Ringkasan Parameter")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("pH", ph)
        st.metric("BOD", f"{bod} mg/L")

    with c2:
        st.metric("COD", f"{cod} mg/L")
        st.metric("DO", f"{do} mg/L")

    with c3:
        st.metric("TSS", f"{tss} mg/L")
        st.metric("TDS", f"{tds} mg/L")

    st.divider()

    st.header("📝 Kesimpulan")

    if jumlah_tidak == 0:

        st.balloons()

        st.success(
            f"Sampel '{nama_sampel}' MEMENUHI "
            "Baku Mutu Air Kelas I."
        )

    else:

        st.error(
            f"Sampel '{nama_sampel}' TIDAK MEMENUHI "
            "Baku Mutu Air Kelas I."
        )

        gagal = df[
            df["Status"].str.contains("Tidak")
        ]["Parameter"].tolist()

        st.warning(
            "Parameter yang tidak memenuhi: "
            + ", ".join(gagal)
        )

    st.divider()

    st.caption(
        "© 2026 AquaCheck Team | Akademi Kimia Analis Bogor"
    )
