import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="AquaCheck",
    page_icon="💧",
    layout="wide"
)

# =========================
# SESSION STATE
# =========================
if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# CSS (CLEAN + ANIMATED WATER STYLE)
# =========================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#E3F2FD,#F5FBFF,#E0F7FA);
}

.header {
    text-align:center;
    padding:20px;
    background:white;
    border-radius:20px;
    box-shadow:0px 6px 20px rgba(0,0,0,0.1);
    margin-bottom:20px;
    animation: fadeIn 1s ease;
}

@keyframes fadeIn {
    from {opacity:0; transform:translateY(20px);}
    to {opacity:1; transform:translateY(0);}
}

.water {
    font-size:60px;
    text-align:center;
    animation: float 3s infinite;
}

@keyframes float {
    0% {transform:translateY(0px);}
    50% {transform:translateY(-10px);}
    100% {transform:translateY(0px);}
}

.card {
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
    margin-top:15px;
}

.stButton button {
    background: linear-gradient(90deg,#00B4DB,#0083B0)!important;
    color:white!important;
    border-radius:12px;
    height:50px;
    width:100%;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div class="header">
    <div class="water">💧</div>
    <h1>AQUACHECK</h1>
    <p>Evaluasi Kualitas Air - PP No. 22 Tahun 2021</p>
</div>
""", unsafe_allow_html=True)

# =========================
# MENU (ANTI DUPLICATE FIX)
# =========================
menu = st.sidebar.radio(
    "📂 Menu",
    [
        "🏠 Evaluasi",
        "📖 Baku Mutu",
        "📊 Interpretasi",
        "📜 Riwayat",
        "📚 Dasar Hukum",
        "👨‍💻 Pengembang"
    ]
)

# =========================
# PDF FUNCTION
# =========================
def generate_pdf(data):

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("AQUACHECK REPORT", styles["Title"]))
    elements.append(Spacer(1, 10))

    table_data = [["Parameter","Nilai"]]

    for k in ["pH","BOD","COD","DO","TSS","TDS"]:
        table_data.append([k, str(data[k])])

    table_data.append(["Skor", f"{data['Skor']:.0f}%"])
    table_data.append(["Status", data["Status"]])

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.lightblue),
        ("GRID",(0,0),(-1,-1),0.5,colors.grey)
    ]))

    elements.append(table)
    doc.build(elements)

    buffer.seek(0)
    return buffer

# =========================
# MENU 1 - EVALUASI
# =========================
if menu == "🏠 Evaluasi":

    st.title("💧 Evaluasi Kualitas Air")

    ph = st.number_input("pH",0.0,14.0,7.0)
    bod = st.number_input("BOD",0.0,100.0,2.0)
    cod = st.number_input("COD",0.0,200.0,10.0)
    do = st.number_input("DO",0.0,20.0,6.0)
    tss = st.number_input("TSS",0.0,500.0,40.0)
    tds = st.number_input("TDS",0.0,5000.0,1000.0)

    if st.button("🔍 Analisis"):

        hasil = {
            "pH": 6 <= ph <= 9,
            "BOD": bod <= 2,
            "COD": cod <= 10,
            "DO": do >= 6,
            "TSS": tss <= 40,
            "TDS": tds <= 1000
        }

        score = sum(hasil.values())/6*100
        status = "LAYAK" if score == 100 else "TIDAK LAYAK"

        data = {
            "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M"),
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

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.metric("Skor", f"{score:.0f}%")

        if score == 100:
            st.success("💧 AIR LAYAK")
        elif score >= 70:
            st.warning("⚠️ KURANG LAYAK")
        else:
            st.error("🚨 TIDAK LAYAK")

        st.markdown('</div>', unsafe_allow_html=True)

        # GRAFIK
        st.subheader("📈 Grafik")
        labels = ["pH","BOD","COD","DO","TSS","TDS"]
        values = [ph,bod,cod,do,tss,tds]

        fig, ax = plt.subplots()
        ax.plot(labels, values, marker="o")
        st.pyplot(fig)

        # PDF
        pdf = generate_pdf(data)

        st.download_button(
            "📄 Download PDF",
            pdf,
            "AquaCheck.pdf",
            "application/pdf"
        )

# =========================
# MENU 2
# =========================
elif menu == "📖 Baku Mutu":

    st.title("📖 Baku Mutu Air Kelas I")

    st.table(pd.DataFrame({
        "Parameter":["pH","BOD","COD","DO","TSS","TDS"],
        "Standar":["6-9","≤2","≤10","≥6","≤40","≤1000"]
    }))

# =========================
# MENU 3
# =========================
elif menu == "📊 Interpretasi":

    st.title("📊 Interpretasi")

    st.info("pH = keasaman air")
    st.info("BOD = oksigen biologis")
    st.info("COD = oksigen kimia")
    st.info("DO = oksigen terlarut")
    st.info("TSS = padatan")
    st.info("TDS = zat terlarut")

# =========================
# MENU 4
# =========================
elif menu == "📜 Riwayat":

    st.title("📜 Riwayat")

    if len(st.session_state.history) == 0:
        st.warning("Belum ada data")
    else:
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df)

        st.download_button(
            "⬇ CSV",
            df.to_csv(index=False),
            "riwayat.csv"
        )

# =========================
# MENU 5
# =========================
elif menu == "📚 Dasar Hukum":

    st.title("📚 Dasar Hukum")

    st.success("PP No. 22 Tahun 2021")

# =========================
# MENU 6
# =========================
elif menu == "👨‍💻 Pengembang":

    st.title("👨‍💻 Tentang Pengembang")

    st.markdown("""
    <div class="card">

    💧 AquaCheck Project  
    Prodi: Pengolahan Limbah Industri  
    AKA Bogor - Angkatan 11 (2026)

    </div>
    """, unsafe_allow_html=True)
