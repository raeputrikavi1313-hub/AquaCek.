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
# CSS SEDERHANA
# ==================================
st.markdown("""
<style>
.stApp{
background: linear-gradient(135deg,#E3F2FD,#F5FBFF);
}

.stButton button{
background: #00B4DB;
color: white;
border-radius: 10px;
height: 45px;
width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ==================================
# SIDEBAR MENU
# ==================================
st.sidebar.title("💧 AquaCheck")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "🏠 Evaluasi Kualitas Air",
        "📖 Baku Mutu Air Kelas I",
        "📊 Interpretasi Parameter",
        "📚 Dasar Hukum",
        "👨‍💻 Tentang Pengembang"
    ]
)

# ==================================
# EVALUASI (VERSI DASAR)
# ==================================
if menu == "🏠 Evaluasi Kualitas Air":

    st.title("💧 Evaluasi Kualitas Air")

    ph = st.number_input("pH", 0.0, 14.0, 7.0)
    bod = st.number_input("BOD (mg/L)", 0.0, 100.0, 2.0)
    cod = st.number_input("COD (mg/L)", 0.0, 200.0, 10.0)
    do = st.number_input("DO (mg/L)", 0.0, 20.0, 6.0)
    tss = st.number_input("TSS (mg/L)", 0.0, 500.0, 40.0)
    tds = st.number_input("TDS (mg/L)", 0.0, 5000.0, 1000.0)

    if st.button("🔍 Analisis"):

        if 6 <= ph <= 9 and bod <= 2 and cod <= 10 and do >= 6 and tss <= 40 and tds <= 1000:
            st.success("💧 AIR LAYAK (Kelas I)")
        else:
            st.error("⚠️ AIR TIDAK LAYAK (Kelas I)")

# ==================================
# BAKU MUTU
# ==================================
elif menu == "📖 Baku Mutu Air Kelas I":

    st.title("📖 Baku Mutu Air Kelas I")

    df = pd.DataFrame({
        "Parameter": ["pH","BOD","COD","DO","TSS","TDS"],
        "Baku Mutu": ["6-9","≤2","≤10","≥6","≤40","≤1000"]
    })

    st.table(df)

    st.info("Acuan: PP No. 22 Tahun 2021")

# ==================================
# INTERPRETASI
# ==================================
elif menu == "📊 Interpretasi Parameter":

    st.title("📊 Interpretasi Parameter")

    st.write("pH = tingkat keasaman air")
    st.write("BOD = kebutuhan oksigen biologis")
    st.write("COD = kebutuhan oksigen kimia")
    st.write("DO = oksigen terlarut")
    st.write("TSS = padatan tersuspensi")
    st.write("TDS = zat terlarut total")

# ==================================
# DASAR HUKUM
# ==================================
elif menu == "📚 Dasar Hukum":

    st.title("📚 Dasar Hukum")

    st.success("Peraturan Pemerintah Republik Indonesia No. 22 Tahun 2021")

    st.write("""
    Air Kelas I adalah air yang dapat digunakan sebagai
    air baku air minum dan kebutuhan lain dengan standar mutu tinggi.
    """)

# ==================================
# TENTANG PENGEMBANG
# ==================================
elif menu == "👨‍💻 Tentang Pengembang":

    st.title("👨‍💻 Tentang Pengembang")

    st.info("Menu ini akan diisi data pengembang aplikasi")
    import streamlit as st
import pandas as pd

# ==================================
# CONFIG
# ==================================
st.set_page_config(
    page_title="AquaCheck",
    page_icon="💧",
    layout="wide"
)

# ==================================
# CSS SIMPLE
# ==================================
st.markdown("""
<style>
.stApp{
background: linear-gradient(135deg,#E3F2FD,#F5FBFF);
}

.stButton button{
background: #00B4DB;
color: white;
border-radius: 10px;
height: 45px;
width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ==================================
# SIDEBAR
# ==================================
st.sidebar.title("💧 AquaCheck")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "🏠 Evaluasi Kualitas Air",
        "📖 Baku Mutu Air Kelas I",
        "📊 Interpretasi Parameter",
        "📚 Dasar Hukum",
        "👨‍💻 Tentang Pengembang"
    ]
)

# ==================================
# EVALUASI 1B (UPGRADE)
# ==================================
if menu == "🏠 Evaluasi Kualitas Air":

    st.title("💧 Evaluasi Kualitas Air")

    ph = st.number_input("pH", 0.0, 14.0, 7.0)
    bod = st.number_input("BOD (mg/L)", 0.0, 100.0, 2.0)
    cod = st.number_input("COD (mg/L)", 0.0, 200.0, 10.0)
    do = st.number_input("DO (mg/L)", 0.0, 20.0, 6.0)
    tss = st.number_input("TSS (mg/L)", 0.0, 500.0, 40.0)
    tds = st.number_input("TDS (mg/L)", 0.0, 5000.0, 1000.0)

    if st.button("🔍 Analisis"):

        hasil = {
            "pH": 6 <= ph <= 9,
            "BOD": bod <= 2,
            "COD": cod <= 10,
            "DO": do >= 6,
            "TSS": tss <= 40,
            "TDS": tds <= 1000
        }

        total = len(hasil)
        lulus = sum(hasil.values())
        score = (lulus / total) * 100

        st.subheader("📊 Hasil Evaluasi")

        for k, v in hasil.items():
            if v:
                st.success(f"{k} ✔ memenuhi")
            else:
                st.error(f"{k} ❌ tidak memenuhi")

        st.metric("📊 Skor Kelayakan", f"{score:.0f}%")

        if score == 100:
            st.success("💧 AIR SANGAT LAYAK (Kelas I)")
        elif score >= 70:
            st.warning("⚠️ AIR KURANG LAYAK")
        else:
            st.error("🚨 AIR TIDAK LAYAK")

# ==================================
# BAKU MUTU
# ==================================
elif menu == "📖 Baku Mutu Air Kelas I":

    st.title("📖 Baku Mutu Air Kelas I")

    df = pd.DataFrame({
        "Parameter": ["pH","BOD","COD","DO","TSS","TDS"],
        "Baku Mutu": ["6-9","≤2","≤10","≥6","≤40","≤1000"]
    })

    st.table(df)

# ==================================
# INTERPRETASI
# ==================================
elif menu == "📊 Interpretasi Parameter":

    st.title("📊 Interpretasi Parameter")

    st.write("pH = keasaman air")
    st.write("BOD = kebutuhan oksigen biologis")
    st.write("COD = kebutuhan oksigen kimia")
    st.write("DO = oksigen terlarut")
    st.write("TSS = padatan tersuspensi")
    st.write("TDS = zat terlarut total")

# ==================================
# DASAR HUKUM
# ==================================
elif menu == "📚 Dasar Hukum":

    st.title("📚 Dasar Hukum")

    st.success("PP No. 22 Tahun 2021")

    st.write("""
    Air Kelas I digunakan sebagai air baku air minum
    dan kebutuhan lain dengan standar mutu tinggi.
    """)

# ==================================
# TENTANG PENGEMBANG
# ==================================
elif menu == "👨‍💻 Tentang Pengembang":

    st.title("👨‍💻 Tentang Pengembang")

    st.info("Menu ini akan diisi profil pengembang nanti")
    import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# ==================================
# CONFIG
# ==================================
st.set_page_config(
    page_title="AquaCheck",
    page_icon="💧",
    layout="wide"
)

# ==================================
# SESSION STATE (RIWAYAT)
# ==================================
if "history" not in st.session_state:
    st.session_state.history = []

# ==================================
# CSS SIMPLE
# ==================================
st.markdown("""
<style>
.stApp{
background: linear-gradient(135deg,#E3F2FD,#F5FBFF);
}

.stButton button{
background: #00B4DB;
color: white;
border-radius: 10px;
height: 45px;
width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ==================================
# SIDEBAR
# ==================================
st.sidebar.title("💧 AquaCheck")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "🏠 Evaluasi Kualitas Air",
        "📖 Baku Mutu Air Kelas I",
        "📊 Interpretasi Parameter",
        "📜 Riwayat Analisis",
        "📚 Dasar Hukum",
        "👨‍💻 Tentang Pengembang"
    ]
)

# ==================================
# EVALUASI 1C
# ==================================
if menu == "🏠 Evaluasi Kualitas Air":

    st.title("💧 Evaluasi Kualitas Air")

    ph = st.number_input("pH", 0.0, 14.0, 7.0)
    bod = st.number_input("BOD (mg/L)", 0.0, 100.0, 2.0)
    cod = st.number_input("COD (mg/L)", 0.0, 200.0, 10.0)
    do = st.number_input("DO (mg/L)", 0.0, 20.0, 6.0)
    tss = st.number_input("TSS (mg/L)", 0.0, 500.0, 40.0)
    tds = st.number_input("TDS (mg/L)", 0.0, 5000.0, 1000.0)

    if st.button("🔍 Analisis"):

        hasil = {
            "pH": 6 <= ph <= 9,
            "BOD": bod <= 2,
            "COD": cod <= 10,
            "DO": do >= 6,
            "TSS": tss <= 40,
            "TDS": tds <= 1000
        }

        total = len(hasil)
        lulus = sum(hasil.values())
        score = (lulus / total) * 100

        status = "LAYAK" if score == 100 else "TIDAK LAYAK"

        # SIMPAN RIWAYAT
        st.session_state.history.append({
            "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "pH": ph,
            "BOD": bod,
            "COD": cod,
            "DO": do,
            "TSS": tss,
            "TDS": tds,
            "Skor": score,
            "Status": status
        })

        st.subheader("📊 Hasil Evaluasi")

        for k, v in hasil.items():
            if v:
                st.success(f"{k} ✔")
            else:
                st.error(f"{k} ❌")

        st.metric("📊 Skor Kelayakan", f"{score:.0f}%")

        if score == 100:
            st.success("💧 AIR SANGAT LAYAK (Kelas I)")
        else:
            st.error("⚠️ AIR TIDAK LAYAK (Kelas I)")

        # GRAFIK
        st.subheader("📈 Grafik Kualitas Air")

        labels = ["pH","BOD","COD","DO","TSS","TDS"]
        values = [ph,bod,cod,do,tss,tds]

        fig, ax = plt.subplots()
        ax.bar(labels, values)
        st.pyplot(fig)

# ==================================
# RIWAYAT
# ==================================
elif menu == "📜 Riwayat Analisis":

    st.title("📜 Riwayat Analisis")

    if len(st.session_state.history) == 0:
        st.warning("Belum ada data analisis")
    else:
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df)

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇ Download CSV",
            csv,
            "riwayat_aquacheck.csv",
            "text/csv"
        )

# ==================================
# BAKU MUTU
# ==================================
elif menu == "📖 Baku Mutu Air Kelas I":

    st.title("📖 Baku Mutu Air Kelas I")

    st.table(pd.DataFrame({
        "Parameter": ["pH","BOD","COD","DO","TSS","TDS"],
        "Baku Mutu": ["6-9","≤2","≤10","≥6","≤40","≤1000"]
    }))

# ==================================
# INTERPRETASI
# ==================================
elif menu == "📊 Interpretasi Parameter":

    st.title("📊 Interpretasi Parameter")

    st.write("pH = keasaman air")
    st.write("BOD = kebutuhan oksigen biologis")
    st.write("COD = kebutuhan oksigen kimia")
    st.write("DO = oksigen terlarut")
    st.write("TSS = padatan tersuspensi")
    st.write("TDS = zat terlarut total")

# ==================================
# DASAR HUKUM
# ==================================
elif menu == "📚 Dasar Hukum":

    st.title("📚 Dasar Hukum")

    st.success("PP No. 22 Tahun 2021")

# ==================================
# TENTANG PENGEMBANG
# ==================================
elif menu == "👨‍💻 Tentang Pengembang":

    st.title("👨‍💻 Tentang Pengembang")
    st.info("Profil pengembang akan ditambahkan nanti")
    import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# ==================================
# CONFIG
# ==================================
st.set_page_config(
    page_title="AquaCheck",
    page_icon="💧",
    layout="wide"
)

# ==================================
# SESSION STATE
# ==================================
if "history" not in st.session_state:
    st.session_state.history = []

# ==================================
# PDF FUNCTION
# ==================================
def generate_pdf(data):

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("AQUACHECK - LAPORAN ANALISIS KUALITAS AIR", styles["Title"]))
    elements.append(Spacer(1, 12))

    table_data = [["Parameter", "Nilai"]]

    for k in ["pH","BOD","COD","DO","TSS","TDS"]:
        table_data.append([k, str(data[k])])

    table_data.append(["Skor", f"{data['Skor']:.0f}%"])
    table_data.append(["Status", data["Status"]])
    table_data.append(["Waktu", data["Waktu"]])

    table = Table(table_data)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightblue),
        ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
        ("PADDING", (0,0), (-1,-1), 6)
    ]))

    elements.append(table)

    doc.build(elements)
    buffer.seek(0)
    return buffer

# ==================================
# CSS
# ==================================
st.markdown("""
<style>
.stApp{
background: linear-gradient(135deg,#E3F2FD,#F5FBFF);
}

.stButton button{
background: #00B4DB;
color: white;
border-radius: 10px;
height: 45px;
width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ==================================
# SIDEBAR
# ==================================
st.sidebar.title("💧 AquaCheck")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "🏠 Evaluasi Kualitas Air",
        "📖 Baku Mutu Air Kelas I",
        "📊 Interpretasi Parameter",
        "📜 Riwayat Analisis",
        "📚 Dasar Hukum",
        "👨‍💻 Tentang Pengembang"
    ]
)

# ==================================
# EVALUASI
# ==================================
if menu == "🏠 Evaluasi Kualitas Air":

    st.title("💧 Evaluasi Kualitas Air")

    ph = st.number_input("pH", 0.0, 14.0, 7.0)
    bod = st.number_input("BOD", 0.0, 100.0, 2.0)
    cod = st.number_input("COD", 0.0, 200.0, 10.0)
    do = st.number_input("DO", 0.0, 20.0, 6.0)
    tss = st.number_input("TSS", 0.0, 500.0, 40.0)
    tds = st.number_input("TDS", 0.0, 5000.0, 1000.0)

    if st.button("🔍 Analisis"):

        hasil = {
            "pH": 6 <= ph <= 9,
            "BOD": bod <= 2,
            "COD": cod <= 10,
            "DO": do >= 6,
            "TSS": tss <= 40,
            "TDS": tds <= 1000
        }

        total = len(hasil)
        lulus = sum(hasil.values())
        score = (lulus / total) * 100

        status = "LAYAK" if score == 100 else "TIDAK LAYAK"

        data = {
            "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "pH": ph,
            "BOD": bod,
            "COD": cod,
            "DO": do,
            "TSS": tss,
            "TDS": tds,
            "Skor": score,
            "Status": status
        }

        st.session_state.history.append(data)

        st.subheader("📊 Hasil")

        for k, v in hasil.items():
            if v:
                st.success(f"{k} ✔")
            else:
                st.error(f"{k} ❌")

        st.metric("Skor", f"{score:.0f}%")

        if score == 100:
            st.success("💧 AIR SANGAT LAYAK")
        else:
            st.error("⚠️ AIR TIDAK LAYAK")

        # GRAFIK
        st.subheader("📈 Grafik")

        labels = ["pH","BOD","COD","DO","TSS","TDS"]
        values = [ph,bod,cod,do,tss,tds]

        fig, ax = plt.subplots()
        ax.bar(labels, values)
        st.pyplot(fig)

        # PDF DOWNLOAD
        pdf = generate_pdf(data)

        st.download_button(
            "📄 Download PDF Laporan",
            pdf,
            file_name="AquaCheck_Laporan.pdf",
            mime="application/pdf"
        )

# ==================================
# RIWAYAT
# ==================================
elif menu == "📜 Riwayat Analisis":

    st.title("📜 Riwayat Analisis")

    if len(st.session_state.history) == 0:
        st.warning("Belum ada data")
    else:
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df)

        st.download_button(
            "⬇ Download CSV",
            df.to_csv(index=False),
            "riwayat.csv"
        )

# ==================================
# BAKU MUTU
# ==================================
elif menu == "📖 Baku Mutu Air Kelas I":

    st.title("📖 Baku Mutu")

    st.table(pd.DataFrame({
        "Parameter":["pH","BOD","COD","DO","TSS","TDS"],
        "Baku Mutu":["6-9","≤2","≤10","≥6","≤40","≤1000"]
    }))

# ==================================
# INTERPRETASI
# ==================================
elif menu == "📊 Interpretasi Parameter":

    st.title("📊 Interpretasi")

    st.write("pH = keasaman air")
    st.write("BOD = kebutuhan oksigen biologis")
    st.write("COD = kebutuhan oksigen kimia")
    st.write("DO = oksigen terlarut")
    st.write("TSS = padatan tersuspensi")
    st.write("TDS = zat terlarut total")

# ==================================
# DASAR HUKUM
# ==================================
elif menu == "📚 Dasar Hukum":

    st.title("📚 Dasar Hukum")

    st.success("PP No. 22 Tahun 2021")

# ==================================
# TENTANG PENGEMBANG
# ==================================
elif menu == "👨‍💻 Tentang Pengembang":

    st.title("👨‍💻 Tentang Pengembang")

    st.info("Profil pengembang akan ditambahkan nanti")
    import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# ==================================
# CONFIG
# ==================================
st.set_page_config(
    page_title="AquaCheck",
    page_icon="💧",
    layout="wide"
)

# ==================================
# SESSION STATE
# ==================================
if "history" not in st.session_state:
    st.session_state.history = []

# ==================================
# PDF FUNCTION
# ==================================
def generate_pdf(data):

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("AQUACHECK - LAPORAN ANALISIS KUALITAS AIR", styles["Title"]))
    elements.append(Spacer(1, 12))

    table_data = [["Parameter", "Nilai"]]

    for k in ["pH","BOD","COD","DO","TSS","TDS"]:
        table_data.append([k, str(data[k])])

    table_data.append(["Skor", f"{data['Skor']:.0f}%"])
    table_data.append(["Status", data["Status"]])
    table_data.append(["Waktu", data["Waktu"]])

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.lightblue),
        ("GRID",(0,0),(-1,-1),0.5,colors.grey),
        ("PADDING",(0,0),(-1,-1),6)
    ]))

    elements.append(table)

    doc.build(elements)
    buffer.seek(0)
    return buffer

# ==================================
# UI STYLE AESTHETIC
# ==================================
st.markdown("""
<style>
.stApp{
background: linear-gradient(135deg,#E3F2FD,#F5FBFF,#E0F7FA);
}

.header{
text-align:center;
padding:20px;
background:white;
border-radius:20px;
box-shadow:0px 6px 20px rgba(0,0,0,0.1);
margin-bottom:20px;
}

.card{
background:white;
padding:20px;
border-radius:20px;
box-shadow:0px 4px 15px rgba(0,0,0,0.08);
margin-top:15px;
}

.stButton button{
background: linear-gradient(90deg,#00B4DB,#0083B0)!important;
color:white!important;
border-radius:12px;
height:50px;
width:100%;
font-size:16px!important;
font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# ==================================
# HEADER (LOGO + TITLE)
# ==================================
st.markdown("""
<div class="header">
    <h1>💧 AQUACHECK</h1>
    <p>Sistem Evaluasi Kualitas Air Berbasis PP No. 22 Tahun 2021</p>
</div>
""", unsafe_allow_html=True)

# ==================================
# SIDEBAR
# ==================================
st.sidebar.title("💧 AquaCheck")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "🏠 Evaluasi Kualitas Air",
        "📖 Baku Mutu Air Kelas I",
        "📊 Interpretasi Parameter",
        "📜 Riwayat Analisis",
        "📚 Dasar Hukum",
        "👨‍💻 Tentang Pengembang"
    ]
)

# ==================================
# EVALUASI
# ==================================
if menu == "🏠 Evaluasi Kualitas Air":

    st.title("🏠 Evaluasi Kualitas Air")

    ph = st.number_input("pH", 0.0, 14.0, 7.0)
    bod = st.number_input("BOD (mg/L)", 0.0, 100.0, 2.0)
    cod = st.number_input("COD (mg/L)", 0.0, 200.0, 10.0)
    do = st.number_input("DO (mg/L)", 0.0, 20.0, 6.0)
    tss = st.number_input("TSS (mg/L)", 0.0, 500.0, 40.0)
    tds = st.number_input("TDS (mg/L)", 0.0, 5000.0, 1000.0)

    if st.button("🔍 Analisis Kualitas Air"):

        hasil = {
            "pH": 6 <= ph <= 9,
            "BOD": bod <= 2,
            "COD": cod <= 10,
            "DO": do >= 6,
            "TSS": tss <= 40,
            "TDS": tds <= 1000
        }

        total = len(hasil)
        lulus = sum(hasil.values())
        score = (lulus / total) * 100

        status = "LAYAK" if score == 100 else "TIDAK LAYAK"

        data = {
            "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "pH": ph,
            "BOD": bod,
            "COD": cod,
            "DO": do,
            "TSS": tss,
            "TDS": tds,
            "Skor": score,
            "Status": status
        }

        st.session_state.history.append(data)

        # ==========================
        # HASIL CARD
        # ==========================
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("📊 Hasil Evaluasi")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Skor Kelayakan", f"{score:.0f}%")

        with col2:
            if score == 100:
                st.success("LAYAK")
            elif score >= 70:
                st.warning("KURANG")
            else:
                st.error("TIDAK LAYAK")

        with col3:
            st.info("PP 22/2021")

        st.markdown("</div>", unsafe_allow_html=True)

        # DETAIL PARAMETER
        st.subheader("📌 Detail Parameter")

        for k, v in hasil.items():
            if v:
                st.success(f"{k} ✔ memenuhi")
            else:
                st.error(f"{k} ❌ tidak memenuhi")

        # GRAFIK
        st.subheader("📈 Grafik Kualitas Air")

        labels = ["pH","BOD","COD","DO","TSS","TDS"]
        values = [ph,bod,cod,do,tss,tds]

        fig, ax = plt.subplots()
        ax.plot(labels, values, marker="o")
        ax.set_title("Profil Kualitas Air")
        st.pyplot(fig)

        # PDF DOWNLOAD
        pdf = generate_pdf(data)

        st.download_button(
            "📄 Download PDF Laporan",
            pdf,
            file_name="AquaCheck_Laporan.pdf",
            mime="application/pdf"
        )

# ==================================
# RIWAYAT
# ==================================
elif menu == "📜 Riwayat Analisis":

    st.title("📜 Riwayat Analisis")

    if len(st.session_state.history) == 0:
        st.warning("Belum ada data analisis")
    else:
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df)

        st.download_button(
            "⬇ Download CSV",
            df.to_csv(index=False),
            "riwayat.csv"
        )

# ==================================
# BAKU MUTU
# ==================================
elif menu == "📖 Baku Mutu Air Kelas I":

    st.title("📖 Baku Mutu Air Kelas I")

    st.table(pd.DataFrame({
        "Parameter":["pH","BOD","COD","DO","TSS","TDS"],
        "Baku Mutu":["6-9","≤2","≤10","≥6","≤40","≤1000"]
    }))

# ==================================
# INTERPRETASI
# ==================================
elif menu == "📊 Interpretasi Parameter":

    st.title("📊 Interpretasi Parameter")

    st.info("pH = tingkat keasaman air")
    st.info("BOD = kebutuhan oksigen biologis")
    st.info("COD = kebutuhan oksigen kimia")
    st.info("DO = oksigen terlarut")
    st.info("TSS = padatan tersuspensi")
    st.info("TDS = zat terlarut total")

# ==================================
# DASAR HUKUM
# ==================================
elif menu == "📚 Dasar Hukum":

    st.title("📚 Dasar Hukum")

    st.success("PP No. 22 Tahun 2021")
    
# ==================================
# TENTANG PENGEMBANG
# ==================================
elif menu == "👨‍💻 Tentang Pengembang":

    st.title("👨‍💻 Tentang Pengembang")

    st.markdown("""
    <div style="
        background:white;
        padding:25px;
        border-radius:20px;
        box-shadow:0px 6px 20px rgba(0,0,0,0.1);
    ">

    <h3>💧 AquaCheck Project Team</h3>

    <p><b>Program Studi:</b> Pengolahan Limbah Industri</p>
    <p><b>Semester:</b> 2</p>
    <p><b>Instansi:</b> AKA Bogor</p>
    <p><b>Angkatan:</b> 11</p>
    <p><b>Tahun:</b> 2026</p>

    <hr>

    <h4>👥 Tim Pengembang</h4>

    <ul>
        <li>Dela Rahayu Putri (2530606)</li>
        <li>Mutiara Shifwah A (2530640)</li>
        <li>Putri Bilqis Aliyyu N (2530647)</li>
        <li>Rae Putri Kavi (2530648)</li>
        <li>Salsabila Putri (2530650)</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)
