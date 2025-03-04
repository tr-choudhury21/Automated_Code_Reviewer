import streamlit as st
import requests


st.set_page_config(page_title="Automated Code Reviewer", page_icon="📝", layout="centered")


st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .stTextArea textarea {
            background-color: #eef;
            color: black;
            border-radius: 8px;
            padding: 10px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 5px;
            transition: 0.3s;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .stMarkdown h1 {
            color: #333;
        }
        .review-box {
            background-color: white;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #333;'>🚀 Automated Code Reviewer</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #666;'>Get AI-powered feedback on your code instantly</h4>", unsafe_allow_html=True)

st.divider()

# Code input area
st.markdown("### 📝 Enter Your Code Below")
code = st.text_area("", height=250, placeholder="Write or paste your Python code here...")

# Submit button
if st.button("🚀 Review My Code", use_container_width=True):
    if code.strip():
        with st.spinner("🔍 Analyzing your code... Please wait!"):
            response = requests.post("http://127.0.0.1:8000/review/", json={"code": code})

        if response.status_code == 200:
            review_text = response.json()["review"]
            
            # Review Output
            st.markdown("<h3 style='color: #333;'>🔍 Review Output</h3>", unsafe_allow_html=True)
            st.markdown('<div class="review-box">', unsafe_allow_html=True)

            # Format output into bullet points
            for line in review_text.split("\n"):
                if line.strip():
                    st.markdown(f"- {line.strip()}")

            st.markdown('</div>', unsafe_allow_html=True)

        else:
            st.error("❌ Error: Unable to get a response from the API")
    else:
        st.warning("⚠️ Please enter some code to review.")

st.divider()

# Footer
st.markdown("<p style='text-align: center; color: #888;'>Built with ❤️ using Streamlit & Gemini AI</p>", unsafe_allow_html=True)
