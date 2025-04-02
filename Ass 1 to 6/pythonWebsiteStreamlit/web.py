import streamlit as st

# Set page configuration
st.set_page_config(page_title="My Streamlit Website", page_icon="🌍", layout="wide")

# Sidebar Navigation
st.sidebar.title("🔗 Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Home Page
if page == "Home":
    st.title("🏡 Welcome to My Website!")
    st.write("This is a simple multi-page website built using Streamlit.")
    #st.image("https://source.unsplash.com/800x400/?technology", use_container_width=True)

    st.subheader("✨ Features:")
    st.markdown("- ✅ Fast & Interactive UI")
    st.markdown("- ✅ Lightweight Web App")
    st.markdown("- ✅ Fully Responsive")
    st.markdown("- ✅ Multipage Navigation")

# About Page
elif page == "About":
    st.title("📖 About Us")
    st.write("This website is created using **Streamlit**, a Python framework for building web apps.")

# Contact Page
elif page == "Contact":
    st.title("📩 Contact Us")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Submit"):
        if name and email and message:
            st.success("✅ Thank you! We will get back to you soon.")
        else:
            st.error("⚠ Please fill in all fields.")
