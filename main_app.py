import streamlit as st
import PyPDF2
from modules.resume_parser import extract_skills
from modules.job_matcher import match_jobs

st.set_page_config(page_title="AI Resume Parser & Job Matcher", page_icon="🤖", layout="centered")

st.title("🤖 AI Resume Parser & Job Matcher")
st.markdown("Upload your resume and find the best-matching job roles!")

uploaded_file = st.file_uploader("📄 Upload your Resume (PDF/TXT)", type=["pdf", "txt"])

if uploaded_file is not None:
    # Extract text from resume
    if uploaded_file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(uploaded_file)
        resume_text = ""
        for page in reader.pages:
            resume_text += page.extract_text()
    else:
        resume_text = uploaded_file.read().decode("utf-8")

    st.subheader("🧠 Extracted Skills")
    skills = extract_skills(resume_text)
    st.write(", ".join(skills) if skills else "No skills detected.")

    if st.button("🔍 Match Jobs"):
        with st.spinner("Matching jobs..."):
            matches = match_jobs(skills)

        st.subheader("🎯 Top Matching Jobs")
        st.dataframe(matches)

        # Display best match
        if not matches.empty:
            top = matches.iloc[0]
            st.success(f"✅ Best Match:  ({top['Category']}) — Score: {round(top['Match_Score'], 2)}")

st.markdown("---")
st.caption("Developed BY Anvith Shetty And Apoorva")
