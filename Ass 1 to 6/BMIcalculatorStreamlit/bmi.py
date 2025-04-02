import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    """
    Calculates BMI using the formula:
    BMI = weight (kg) / (height (m) ** 2)
    """
    height_m = height / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)  # BMI formula
    return round(bmi, 2)

# Function to determine BMI category
def bmi_category(bmi):
    """
    Returns the BMI category based on the calculated BMI value.
    """
    if bmi < 18.5:
        return "Underweight 🟡"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight ✅"
    elif 25 <= bmi < 29.9:
        return "Overweight 🟠"
    else:
        return "Obese 🔴"

# Streamlit UI
def main():
    st.title("💪 BMI Calculator Web App")
    st.write("Calculate your Body Mass Index (BMI) and check your health category in just a few seconds.")
    st.write("🎯 Take the first step towards a healthier lifestyle today!")
    st.write("👉 Enter your details below to begin!")

    # User Inputs
    weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1, format="%.1f")
    height = st.number_input("Enter your height (cm):", min_value=40.0, step=0.1, format="%.1f")

    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            category = bmi_category(bmi)
            st.success(f"📊 Your BMI is: **{bmi}**")
            st.info(f"🏷️ Category: **{category}**")
        else:
            st.error("⚠ Please enter valid weight and height!")

# Run the app
if __name__ == "__main__":
    main()
