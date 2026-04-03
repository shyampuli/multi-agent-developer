import streamlit as st
from agents.dev_agent import DevAgent
from agents.test_agent import TestAgent
from agents.review_agent import ReviewAgent

st.set_page_config(page_title="Multi-Agent AI Developer", layout="wide")


st.markdown("""
<style>
/* Background */
body {
    background: linear-gradient(270deg, #7cff67, #B19EEF, #5227FF);
    background-size: 600% 600%;
    animation: gradient 12s ease infinite;
    color: white;
}

@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Glass Card */
.card {
    background: rgba(0, 0, 0, 0.65);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(15px);
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.1);
}

/* Title */
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 20px;
}

/* Input box */
input {
    border-radius: 10px !important;
}

/* Buttons */
.stButton > button {
    background: light grey;
    color: black;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


st.markdown('<div class="title">🤖 Multi-Agent AI Developer</div>', unsafe_allow_html=True)

task = st.text_input("Enter your task")

if st.button("Run Agents"):

    if task:
        dev = DevAgent()
        tester = TestAgent()
        reviewer = ReviewAgent()

        with st.spinner("👨‍💻 Dev Agent working..."):
            code = dev.run(task)

        with st.spinner("🧪 Test Agent working..."):
            tests = tester.run(code)

        with st.spinner("🕵️ Reviewer Agent optimizing..."):
            improved = reviewer.run(code)
            final_code = reviewer.run(improved)

        st.success("✅ All agents completed successfully!")

        
        col1, col2, col3 = st.columns(3)

       
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("👨‍💻 Developer")
            st.code(code, language="python")
            st.download_button(
                label="⬇️ Download Code",
                data=code,
                file_name="generated_code.py"
            )
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("🧪 Tester")
            st.code(tests, language="python")
            st.download_button(
                label="⬇️ Download Tests",
                data=tests,
                file_name="test_code.py"
            )
            st.markdown('</div>', unsafe_allow_html=True)

        with col3:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("🕵️ Reviewer")
            st.code(final_code, language="python")
            st.download_button(
                label="⬇️ Download Final Code",
                data=final_code,
                file_name="reviewed_code.py"
            )
            st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.warning("⚠️ Please enter a task")