import streamlit as st
from agent import chat

st.set_page_config(
    page_title="CareerLens AI Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 CareerLens AI Agent")
st.markdown("*Your personal AI career coach — ask me anything!*")

# Example questions
# ── Role + Location selectors ─────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    role = st.selectbox(
        "Select Target Role",
        [
            "GenAI Engineer",
            "ML Engineer",
            "Data Scientist",
            "Data Engineer",
            "AI Research Engineer",
            "NLP Engineer",
            "LLM Engineer",
            "Backend Engineer (Python)",
            "Full Stack Engineer",
            "DevOps / MLOps Engineer",
            "Cloud Engineer (AWS/GCP)",
            "Software Engineer",
            "Product Manager (AI)",
            "Test Lead",
            "Embedded Testing",
            "Python Developer",
            "Java Developer",
            "Software Engineer"
        ]
    )

with col2:
    location = st.selectbox(
        "Select Location",
        [
            "Chennai",
            "Bangalore",
            "Hyderabad",
            "Mumbai",
            "Pune",
            "Delhi / NCR",
            "Noida"
            "Remote",
            "Pan India",
        ]
    )

# ── Dynamic quick buttons ─────────────────────────────────────
col1, col2, col3 = st.columns(3)
with col1:
    if st.button(f"🔍 Find {role} jobs in {location}"):
        st.session_state.example = (
            f"Find {role} jobs in {location} "
            f"India 2026 with salary details"
        )
with col2:
    if st.button(f"📚 Skills for {role}"):
        st.session_state.example = (
            f"What are the most important skills "
            f"needed for {role} role in India 2026? "
            f"Include tools, frameworks and salary range."
        )
with col3:
    if st.button("📈 Latest AI trends"):
        st.session_state.example = (
            "What is trending in AI/tech industry "
            "this week in India? Include new tools, "
            "frameworks and hiring trends."
        )


st.divider()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle example button clicks
if "example" in st.session_state:
    prompt = st.session_state.example
    del st.session_state.example

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            response = chat(prompt)
            st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
    st.rerun()

# Chat input
if prompt := st.chat_input("Ask your career question..."):
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            response = chat(prompt)
            st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
    st.rerun()

st.divider()
st.markdown( "*CareerLens AI Agent — LangChain + "
    "LangGraph + NVIDIA LLM + Streamlit — by Raj Kumar*"
)
