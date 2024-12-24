import streamlit as st
from fpdf import FPDF
from PIL import Image

st.set_page_config(
    page_title="PDF Converter",
    page_icon="✨",
    layout="wide",
)


def convertTextToPdf(text, filename):
    pdfobj = FPDF()
    pdfobj.add_page()
    pdfobj.set_font("Arial", size=12)
    pdfobj.multi_cell(0, 10, text)
    pdfobj.output(filename)


def convertImageToPdf(image, output_pdf):
    img = Image.open(image)
    img.save(output_pdf, "PDF", resolution=100.0)


st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to bottom, lightblue 95%, red 5%);
        height: 100vh; /* Full viewport height */
        padding: 0;
        margin: 0;
    }
    </style>
    
    
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>PDF Convertor</h1>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose a file", label_visibility="collapsed")

if uploaded_file is not None:
    # Handle text files
    if uploaded_file.type == "text/plain":
        content = uploaded_file.read().decode("utf-8")
        if st.button("Convert to PDF"):
            outputPdf = "converted_file.pdf"
            convertTextToPdf(content, outputPdf)
            with open(outputPdf, "rb") as f:
                st.download_button(
                    label="Download PDF",
                    data=f,
                    file_name="converted_file.pdf",
                    mime="application/pdf",
                )

    # Handle image files
    elif uploaded_file.type in ["image/jpeg", "image/png", "image/jpg"]:
        if st.button("Convert Image to PDF"):
            outputPdf = "converted_image.pdf"
            convertImageToPdf(uploaded_file, outputPdf)
            with open(outputPdf, "rb") as f:
                st.download_button(
                    label="Download Image as PDF",
                    data=f,
                    file_name="converted_image.pdf",
                    mime="application/pdf",
                )

st.markdown("<hr style='border: 1px solid #000; width: 80%; margin: 20px auto;'>", unsafe_allow_html=True)

st.markdown("""
    <style>
        .info-box {
            border: 2px solid #ddd;
            padding: 20px;
            border-radius: 8px;
            background-color: #f9f9f9;
            text-align: center;
            font-size: 16px;
            color: #333;
            margin-top: 20px;
        }
        .info-box p {
            margin: 10px 0;
        }
    </style>
    <div class="info-box">
        <p>✅Convert to and from PDF on Mac, Windows, and mobile</p>
        <p>✅Free, no-hassle PDF Converter</p>
        <p>✅30+ PDF tools trusted by 1 billion people</p>
    </div>
 
""", unsafe_allow_html=True)

st.markdown("""
    <style>
         .card-container {
            display: flex;
            justify-content: space-around;
            margin-top: 70px;
            gap: 20px;
        }
        .card {
            width: 250px;
            height: 200;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0px 4px 12px rgba(0, 0, 255, 0.2); /* Blue shadow */
            padding: 20px;
            background-color: #e6f0ff; /* Light blue background */
            text-align: center;
        }
        .card h3 {
            margin-bottom: 15px;
            font-size: 18px;
            color: #007bff; /* Blue text color */
        }
        .card p {
            font-size: 14px;
            color: #333;
        }
    </style>

     <!-- Card container -->
    <div class="card-container">
        <div class="card">
            <h3>Easy Conversion</h3>
            <p>Convert PDFs quickly and easily without installation.</p>
        </div>
        <div class="card">
            <h3>Secure Processing</h3>
            <p>Your data is safe with us—secure file handling and processing.</p>
        </div>
        <div class="card">
            <h3>Fast Results</h3>
            <p>Get your files converted instantly with no delays.</p>
        </div>
    </div>
""", unsafe_allow_html=True)
