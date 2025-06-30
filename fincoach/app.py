import streamlit as st
import requests

st.title("💬 FinCoach: Your Investment Reasoning Assistant")

# Maintain session state
if "user_input" not in st.session_state:
    st.session_state.user_input = {}

# Show current input fields
with st.form("advisor_form"):
    st.text("Initial question or clarification:")
    st.session_state.user_input["goal"] = st.text_input("Goal (e.g., retirement in 15 years)", st.session_state.user_input.get("goal", ""))
    st.session_state.user_input["age"] = st.number_input("Age", min_value=18, max_value=100, step=1, value=st.session_state.user_input.get("age", 45))
    st.session_state.user_input["income"] = st.number_input("Annual Income", min_value=100000, step=100000, value=st.session_state.user_input.get("income", 1000000))
    st.session_state.user_input["children"] = st.number_input("Number of Children", min_value=0, step=1, value=st.session_state.user_input.get("children", 0))
    submitted = st.form_submit_button("Get Advice")

# On submit, send full structured profile
if submitted:
    response = requests.post("http://localhost:8000/advise", json=st.session_state.user_input)
    print('Response: ', response)
    result = response.json()

    if "follow_up_questions" in result:
        st.warning("More info needed:")
        for field in result["follow_up_questions"]:
            st.text(f"Please provide: {field}")
    else:
        st.subheader("Step-by-Step Reasoning")
        for i, step in enumerate(result["reasoning_steps"]):
            st.markdown(f"**Step {i+1}:** {step}")

        st.subheader("Final Advice")
        st.success(result["advice"])
