import streamlit as st
import joblib

# Load the trained model
model = joblib.load('model.pkl')

# App Title and Subtitle
st.title("🧠 Personality Checker App")
st.subheader("Discover whether you're an Introvert or Extrovert 🎭")

# Add a banner image (optional, if you have one in the same folder)
st.image("bannerimage.jpg", use_container_width=True)

# Introductory markdown
st.markdown("### 📝 Input Details")
st.markdown("Fill in the information below honestly to get your personality type.")

# Create two columns for cleaner input layout
col1, col2 = st.columns(2)

with col1:
    Time_spent_Alone = st.number_input("🕒 Time Spent Alone (hours/day)", min_value=0.0, step=0.5)
    Going_outside = st.number_input("🌤️ Hours Outside Daily", min_value=0.0, step=0.5)

with col2:
    Social_event_attendance = st.number_input("🎉 Social Events Attended Recently", min_value=0)
    Friends_circle_size = st.number_input("👥 Size of Friend Circle", min_value=0)

# Single field below the columns
Post_frequency = st.number_input("📱 Number of Posts Recently", min_value=0)

# Predict button
if st.button("Predict"):
    input_data = [[
        Time_spent_Alone,
        Social_event_attendance,
        Going_outside,
        Friends_circle_size,
        Post_frequency
    ]]
    prediction = model.predict(input_data)

    st.markdown("### 🔍 Result:")
    if prediction[0] == 1:
        st.success("🎧 You are likely an **Introvert**. You enjoy solitude, deep conversations, and introspection.")
    else:
        st.info("🎊 You are likely an **Extrovert**. You thrive in social situations and enjoy active engagement.")

# Disclaimer
st.markdown("---")
st.markdown(
    "> 🧠 **Disclaimer**: This is a fun personality check based on limited data and not a professional psychological assessment."
)
