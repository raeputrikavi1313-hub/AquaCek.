from datetime import datetime
from io import BytesIO

import streamlit as st
import pandas as pd

# ==================================
# CONFIG
# ==================================
st.set_page_config(
    page_title="AquaCek",
    page_icon="💧",
    layout="wide"
)

# ==================================
# CSS (WARNA + ANIMASI)
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
    backdrop-filter: blur(10px);
    padding: 20px;
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

# ==================================
# SESSION
# ==================================
if "history" not in st.session_state:
    st.session_state.history = []

# ==================================
# MENU
# ==================================
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

# ==================================
# HOME
# ==================================
def home():
    
    st.markdown("""
    <div class="glass" style="text-align:center;">
        <div style="font-size:70px;">💧</div>
        <h1>AquaCek</h1>
        <h3>Evaluasi Kualitas Air Kelas I</h3>
        <p>PP No. 22 Tahun 2021</p>
    </div>
    """, unsafe_allow_html=True)

    total = len(st.session_state.history)

    if total > 0:
        avg = sum([x[3] for x in st.session_state.history]) / total
        best = max([x[3] for x in st.session_state.history])
    else:
        avg = 0
        best = 0

    st.markdown("### 📊 Dashboard Ringkasan")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Sampel", total)
    col2.metric("Rata-rata Kepatuhan", f"{avg:.1f}%")
    col3.metric("Tertinggi", f"{best:.1f}%")

    st.success("Sistem AquaCek aktif dan siap digunakan 💧")
    def export_pdf(nama, df):

    buffer = BytesIO()

    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet

    doc = SimpleDocTemplate(buffer)
    elements = []

    styles = getSampleStyleSheet()
    title = Paragraph("Laporan AquaCek - Evaluasi Kualitas Air", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    sub = Paragraph(f"Nama Sampel: {nama}", styles["Normal"])
    elements.append(sub)
    elements.append(Spacer(1, 12))

    table_data = [df.columns.to_list()] + df.values.tolist()

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black)
    ]))

    elements.append(table)

    doc.build(elements)

    return buffer.getvalue()
# ==================================
# EVALUASI (MASIH SIMPLE DI TAHAP 1)
# ==================================
def evaluasi():

    st.markdown("""
    <div class="glass">
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

    if st.button("🔍 Analisis AquaCek"):

        df = pd.DataFrame([
            ["pH", ph, "6-9", 1 if 6 <= ph <= 9 else 0],
            ["BOD", bod, "≤2", 1 if bod <= 2 else 0],
            ["COD", cod, "≤10", 1 if cod <= 10 else 0],
            ["DO", do, "≥6", 1 if do >= 6 else 0],
            ["TSS", tss, "≤40", 1 if tss <= 40 else 0],
            ["TDS", tds, "≤1000", 1 if tds <= 1000 else 0],
        ], columns=["Parameter","Nilai","Standar","Status"])

        df["Label"] = df["Status"].map({1:"Memenuhi", 0:"Tidak"})

        st.dataframe(df, use_container_width=True)

        ok = df["Status"].sum()
        no = 6 - ok
        persen = (ok / 6) * 100

        # ==================================
        # STATISTIK
        # ==================================
        col1, col2, col3 = st.columns(3)

        col1.metric("Memenuhi", ok)
        col2.metric("Tidak Memenuhi", no)
        col3.metric("Kepatuhan", f"{persen:.1f}%")

        st.progress(int(persen))

        # ==================================
        # GRAFIK PIE (MODERN)
        # ==================================
        fig = px.pie(
            names=["Memenuhi", "Tidak Memenuhi"],
            values=[ok, no],
            title="📊 Kepatuhan Kualitas Air"
        )

        st.plotly_chart(fig, use_container_width=True)
        def export_pdf(nama, df):

    buffer = BytesIO()

    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet

    doc = SimpleDocTemplate(buffer)
    elements = []

    styles = getSampleStyleSheet()
    title = Paragraph("Laporan AquaCek - Evaluasi Kualitas Air", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    sub = Paragraph(f"Nama Sampel: {nama}", styles["Normal"])
    elements.append(sub)
    elements.append(Spacer(1, 12))

    table_data = [df.columns.to_list()] + df.values.tolist()

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black)
    ]))

    elements.append(table)

    doc.build(elements)

    return buffer.getvalue()

        # ==================================
        # KESIMPULAN
        # ==================================
        if no == 0:
            st.success(f"💧 {nama} MEMENUHI baku mutu Air Kelas I")
        else:
            st.error(f"⚠️ {nama} TIDAK MEMENUHI baku mutu")

        # simpan riwayat
        st.session_state.history.append([nama, ok, no, persen])

pdf = export_pdf(nama, df)

st.download_button(
    "📄 Download PDF Laporan",
    data=pdf,
    file_name="laporan_aquacek.pdf",
    mime="application/pdf"
    def export_pdf(nama, df):

    buffer = BytesIO()

    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet

    doc = SimpleDocTemplate(buffer)
    elements = []

    styles = getSampleStyleSheet()
    title = Paragraph("Laporan AquaCek - Evaluasi Kualitas Air", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    sub = Paragraph(f"Nama Sampel: {nama}", styles["Normal"])
    elements.append(sub)
    elements.append(Spacer(1, 12))

    table_data = [df.columns.to_list()] + df.values.tolist()

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black)
    ]))

    elements.append(table)

    doc.build(elements)

    return buffer.getvalue()
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
def export_pdf(nama, df):

    buffer = BytesIO()

    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet

    doc = SimpleDocTemplate(buffer)
    elements = []

    styles = getSampleStyleSheet()
    title = Paragraph("Laporan AquaCek - Evaluasi Kualitas Air", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    sub = Paragraph(f"Nama Sampel: {nama}", styles["Normal"])
    elements.append(sub)
    elements.append(Spacer(1, 12))

    table_data = [df.columns.to_list()] + df.values.tolist()

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black)
    ]))

    elements.append(table)

    doc.build(elements)

    return buffer.getvalue()def export_pdf(nama, df):

    buffer = BytesIO()

    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet

    doc = SimpleDocTemplate(buffer)
    elements = []

    styles = getSampleStyleSheet()
    title = Paragraph("Laporan AquaCek - Evaluasi Kualitas Air", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    sub = Paragraph(f"Nama Sampel: {nama}", styles["Normal"])
    elements.append(sub)
    elements.append(Spacer(1, 12))

    table_data = [df.columns.to_list()] + df.values.tolist()

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black)
    ]))

    elements.append(table)

    doc.build(elements)

    return buffer.getvalue()
# ==================================
# INTERPRETASI
# ==================================
def interpretasi():

    st.markdown("<div class='glass'><h2>🧪 Interpretasi Parameter</h2></div>", unsafe_allow_html=True)

    df = pd.DataFrame([
        ["pH","Asam / basa air"],
        ["BOD","Pencemaran organik"],
        ["COD","Pencemaran kimia"],
        ["DO","Oksigen terlarut"],
        ["TSS","Kekeruhan air"],
        ["TDS","Zat terlarut"]
    ], columns=["Parameter","Arti"])

    st.dataframe(df, use_container_width=True)
    def export_pdf(nama, df):

    buffer = BytesIO()

    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet

    doc = SimpleDocTemplate(buffer)
    elements = []

    styles = getSampleStyleSheet()
    title = Paragraph("Laporan AquaCek - Evaluasi Kualitas Air", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    sub = Paragraph(f"Nama Sampel: {nama}", styles["Normal"])
    elements.append(sub)
    elements.append(Spacer(1, 12))

    table_data = [df.columns.to_list()] + df.values.tolist()

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black)
    ]))

    elements.append(table)

    doc.build(elements)

    return buffer.getvalue()
    def export_pdf(nama, df):

    buffer = BytesIO()

    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet

    doc = SimpleDocTemplate(buffer)
    elements = []

    styles = getSampleStyleSheet()
    title = Paragraph("Laporan AquaCek - Evaluasi Kualitas Air", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    sub = Paragraph(f"Nama Sampel: {nama}", styles["Normal"])
    elements.append(sub)
    elements.append(Spacer(1, 12))

    table_data = [df.columns.to_list()] + df.values.tolist()

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black)
    ]))

    elements.append(table)

    doc.build(elements)

    return buffer.getvalue()

# ==================================
# HUKUM
# ==================================
def hukum():

    st.markdown("<div class='glass'><h2>⚖️ Landasan Hukum</h2></div>", unsafe_allow_html=True)

    st.write("""
    - PP No. 22 Tahun 2021
    - Baku Mutu Air Permukaan
    - Air Kelas I (air baku minum)
    """)
def export_pdf(nama, df):

    buffer = BytesIO()

    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet

    doc = SimpleDocTemplate(buffer)
    elements = []

    styles = getSampleStyleSheet()
    title = Paragraph("Laporan AquaCek - Evaluasi Kualitas Air", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    sub = Paragraph(f"Nama Sampel: {nama}", styles["Normal"])
    elements.append(sub)
    elements.append(Spacer(1, 12))

    table_data = [df.columns.to_list()] + df.values.tolist()

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black)
    ]))

    elements.append(table)

    doc.build(elements)

    return buffer.getvalue()
# ==================================
# PENGEMBANG
# ==================================
def pengembang():

   def pengembang():

    st.markdown("""
    <div class="glass" style="text-align:center;">
        <h1>👨‍💻 Tentang Pengembang</h1>
        <p>Aplikasi AquaCek - Prodi Pengelolaan Limbah Industri</p>
    </div>
    """, unsafe_allow_html=True)

    st.info("""
    🎓 Akademi Kimia Analis Bogor  
    📚 Prodi: Pengelolaan Limbah Industri  
    📅 Semester: 2  
    🧪 Tahun: 2026  
    """)

    data = {
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
    }

    st.dataframe(pd.DataFrame(data), use_container_width=True)

    st.success("© AquaCek Team 2026 - All Rights Reserved 💧")
       def export_pdf(nama, df):

    buffer = BytesIO()

    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet

    doc = SimpleDocTemplate(buffer)
    elements = []

    styles = getSampleStyleSheet()
    title = Paragraph("Laporan AquaCek - Evaluasi Kualitas Air", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    sub = Paragraph(f"Nama Sampel: {nama}", styles["Normal"])
    elements.append(sub)
    elements.append(Spacer(1, 12))

    table_data = [df.columns.to_list()] + df.values.tolist()

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black)
    ]))

    elements.append(table)

    doc.build(elements)

    return buffer.getvalue()
# ==================================
# RIWAYAT
# ==================================
def riwayat():

    def riwayat():

    st.markdown("<div class='glass'><h2>📜 Riwayat Analisis AquaCek</h2></div>", unsafe_allow_html=True)

    if len(st.session_state.history) == 0:
        st.info("Belum ada data evaluasi")
    else:

        df = pd.DataFrame(
            st.session_state.history,
            columns=["Nama Sampel", "OK", "NO", "Kepatuhan %"]
        )

        st.dataframe(df, use_container_width=True)

        st.markdown("### 📊 Statistik Riwayat")

        st.metric("Total Sampel", len(df))
        st.metric("Rata-rata Kepatuhan", f"{df['Kepatuhan %'].mean():.1f}%")
        def export_pdf(nama, df):

    buffer = BytesIO()

    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet

    doc = SimpleDocTemplate(buffer)
    elements = []

    styles = getSampleStyleSheet()
    title = Paragraph("Laporan AquaCek - Evaluasi Kualitas Air", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    sub = Paragraph(f"Nama Sampel: {nama}", styles["Normal"])
    elements.append(sub)
    elements.append(Spacer(1, 12))

    table_data = [df.columns.to_list()] + df.values.tolist()

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black)
    ]))

    elements.append(table)

    doc.build(elements)

    return buffer.getvalue()
# ==================================
# ROUTING
# ==================================
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
import plotly.express as px
def export_pdf(nama, df):

    buffer = BytesIO()

    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet

    doc = SimpleDocTemplate(buffer)
    elements = []

    styles = getSampleStyleSheet()
    title = Paragraph("Laporan AquaCek - Evaluasi Kualitas Air", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    sub = Paragraph(f"Nama Sampel: {nama}", styles["Normal"])
    elements.append(sub)
    elements.append(Spacer(1, 12))

    table_data = [df.columns.to_list()] + df.values.tolist()

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black)
    ]))

    elements.append(table)

    doc.build(elements)

    return buffer.getvalue()
