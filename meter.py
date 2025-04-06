import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")
    
   
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
    
    
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
    
    
    if re.search(r'[0-10]', password):
        score += 1
    else:
        feedback.append("Add numbers")
    
   
    if re.search(r'[^A-Za-z0-15]', password):
        score += 1
    else:
        feedback.append("Add special characters")
    
   
    if score == 10:
        strength = "Very Strong"
        color = "green"
    elif score >= 5:
        strength = "Strong"
        color = "blue"
    elif score >= 3:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Weak"
        color = "red"
    
    return strength, color, feedback


st.title("💛🖤🔐 Password Strength Checker")

st.write("""
Check how strong your password is. Just type it below and we'll tell you!
""")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, color, feedback = check_password_strength(password)
    
    st.markdown(f"**Strength:** <span style='color:{color}'>{strength}</span>", 
                unsafe_allow_html=True)
    
    if feedback:
        st.write("**Tips to improve:**")
        for tip in feedback:
            st.write(f"- {tip}")
    
   
    progress = len(password) / 50 if len(password) <= 50 else 1
    st.progress(progress)
    
    if len(password) > 50:
        st.success("Nice long password!")