# app.py
# 🧠 Research Agentic AI - Streamlit App
# Summarizes research papers, finds gaps, suggests research directions
# Works with latest Transformers & Streamlit

import streamlit as st
from PyPDF2 import PdfReader
from transformers import pipeline

st.set_page_config(page_title="Research Agentic AI", layout="wide")
st.title("🧠 Research Agentic AI App")
st.write("Upload a research paper (PDF) and let the agent analyze gaps, suggest directions, and generate research questions!")

# -----------------------
# Load Hugging Face Models
# -----------------------

# Summarization (text2text-generation works with latest transformers)
summarizer = pipeline("text2text-generation", model="facebook/bart-large-cnn")

# Agent reasoning: Find gaps, suggest directions, answer questions
generator = pipeline("text-generation", model="gpt2")

# -----------------------
# UI: Upload PDF
# -----------------------

uploaded_file = st.file_uploader("Upload a research paper (PDF)", type=["pdf"])

if uploaded_file:
    try:
        pdf = PdfReader(uploaded_file)
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        if not text.strip():
            st.warning("⚠️ No text could be extracted from this PDF.")
        else:
            st.subheader("📄 Paper Extracted Text (Preview)")
            st.write(text[:1000] + "...")  # preview first 1000 chars

            # -----------------------
            # Summarize Paper
            # -----------------------
            st.write("🔄 Summarizing paper...")
            summary = summarizer(
                text, max_length=150, min_length=50, do_sample=False
            )[0]['generated_text']
            st.subheader("📝 Summary:")
            st.write(summary)

            # -----------------------
            # Analyze Gaps
            # -----------------------
            st.write("🔍 Agent analyzing research gaps...")
            gaps = generator(
                f"Analyze this research summary and list potential loopholes or gaps:\n{summary}",
                max_length=150,
                do_sample=True,
                temperature=0.7
            )[0]['generated_text']
            st.subheader("⚠️ Potential Research Gaps / Loopholes:")
            st.write(gaps)

            # -----------------------
            # Suggest Research Directions
            # -----------------------
            st.write("🚀 Agent suggesting research directions...")
            directions = generator(
                f"Based on the research gaps, suggest future research directions:\n{gaps}",
                max_length=150,
                do_sample=True,
                temperature=0.7
            )[0]['generated_text']
            st.subheader("🚀 Suggested Research Directions:")
            st.write(directions)

            # -----------------------
            # Generate Research Questions
            # -----------------------
            st.write("❓ Generate Research Questions")
            questions = generator(
                f"Generate 3 research questions based on the summary and gaps:\n{summary}\n{gaps}",
                max_length=150,
                do_sample=True,
                temperature=0.7
            )[0]['generated_text']
            st.subheader("❓ Research Questions:")
            st.write(questions)

            # -----------------------
            # Optional User Query
            # -----------------------
            st.write("💡 Optional: Ask a custom question about this paper")
            user_q = st.text_input("Ask a question about this research paper:")
            if user_q:
                answer = generator(
                    f"Answer this question based on the summary and gaps:\nSummary: {summary}\nGaps: {gaps}\nQuestion: {user_q}",
                    max_length=150,
                    do_sample=True,
                    temperature=0.7
                )[0]['generated_text']
                st.subheader("💡 Answer:")
                st.write(answer)

    except Exception as e:
        st.error(f"❌ Error reading PDF: {e}")
