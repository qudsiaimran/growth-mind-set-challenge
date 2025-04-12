import streamlit as st
import datetime

# App Title
st.title("Growth Mindset Challenge")

# Sidebar Navigation
st.sidebar.header("Menu")
section = st.sidebar.radio("Select a section:", ["Home", "About", "Services", "Contact", "Feedback"])

# Home Section
if section == "Home":
    st.header("Hello! 👋")
    st.write("Explore the features of this Streamlit app.")
    
    # User Name Input
    username = st.text_input("Your Name:", value="")  # Fix: Default value added
    if username:
        st.write(f"Hello, {username}! Glad to have you here.")
    
    # Upload Image Feature
    img_file = st.file_uploader("Select an image file:", type=["jpg", "png", "jpeg"])
    if img_file is not None:
        try:
            st.image(img_file, caption="Uploaded Image", use_column_width=True)
        except Exception as e:
            st.error(f"Error displaying image: {e}") 

    # Date & Time
    st.write("Current Date & Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # Age Calculator
    st.subheader("Calculate Your Age")
    birth_year = st.number_input("Enter your birth year:", min_value=1900, max_value=datetime.datetime.now().year, step=1)
    current_year = datetime.datetime.now().year
    if birth_year:
        calculated_age = current_year - birth_year
        st.write(f"Hello, {username}! Your age is: {calculated_age} years")

# About Section
elif section == "About":
    st.header("About This App")
    st.write("This web app is built using Streamlit.")

# Services Section
elif section == "Services":
    st.header("What We Offer")
    st.markdown("""
    - ✅ Web Development  
    - ✅ Mobile App Development  
    - ✅ Data Science & AI  
    - ✅ Automation Solutions  
    """)

# Contact Section
elif section == "Contact":
    st.header("Get in Touch")
    st.write("📧 Email: example@example.com")
    st.write("📞 Phone: +123456789")
    
    
    # Feedback Form
    st.subheader("We Appreciate Your Feedback")
    user_feedback = st.text_area("Share your thoughts:", value="")  # Fix: Default value added
    if st.button("Submit Feedback"):
        st.success("Thanks for your valuable feedback!")

# Feedback Section
elif section == "Feedback":
    st.header("Your Opinion Matters")
    feedback_text = st.text_area("Provide your feedback:", value="")  # Fix: Default value added
    if st.button("Submit"):
        st.success("Your feedback has been recorded.")