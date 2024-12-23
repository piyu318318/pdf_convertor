import streamlit as st
from fpdf import FPDF

st.set_page_config(
    page_title="PDF Convertor",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("Choose Your File Type")



def convertTextToPdf(text, filename):
    pdfobj = FPDF()
    pdfobj.add_page()
    pdfobj.set_font("Arial", size=12)
    pdfobj.multi_cell(0, 10, text)
    pdfobj.output(filename)

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: lightblue;
    }
    </style>
    """, unsafe_allow_html=True)
st.title("Upload Your File and Effortlessly Convert It to PDF")

uploaded_file = st.file_uploader("Choose a file", label_visibility="collapsed")

if uploaded_file is not None:
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





# st.markdown("""
#     <style>
#     .card-container {
#         display: flex;
#         flex-wrap: wrap;
#         gap: 20px;
#         justify-content: center;
#         padding: 20px;
#     }
#     .card {
#         background-color: white;
#         border-radius: 10px;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#         padding: 20px;
#         width: 300px;
#         text-align: center;
#     }
#     .card h3 {
#         margin: 0;
#         color: #333;
#     }
#     .card p {
#         color: #666;
#     }
#     .card button {
#         background-color: #007bff;
#         color: white;
#         border: none;
#         padding: 10px 20px;
#         border-radius: 5px;
#         cursor: pointer;
#     }
#     .card button:hover {
#         background-color: #0056b3;
#     }
#     </style>
#     """, unsafe_allow_html=True)
#
# # Add cards
# st.markdown("""
#     <div class="card-container">
#         <div class="card">
#             <h3>Card 1</h3>
#             <p>Please click the card to convert image into PDF</p>
#             <button>Click Here</button>
#         </div>
#         <div class="card">
#             <h3>Card 2</h3>
#             <p>Please click the card to convert file into PDF.</p>
#             <button>Click Here</button>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)


