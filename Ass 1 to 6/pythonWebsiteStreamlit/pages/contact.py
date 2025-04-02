import streamlit as st

st.title("📩 Contact Us")

# Contact Form
name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

if st.button("Submit"):
    if name and email and message:
        st.success("✅ Thank you! Your message has been received.")
    else:
        st.error("⚠ Please fill in all fields.")
