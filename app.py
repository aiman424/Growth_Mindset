import random
import streamlit as st

st.set_page_config(page_title="Grrowth Mindeset Assignment", page_icon="📈")
st.title("Grrowth Mindset")

st.header("🧭My journey")
st.write("Life is a journey of learning, challenges, and continuous growth. Adopting a growth mindset has transformed the way I approach difficulties, failures, and success.")

quotes = [
    "Challenges are what make life interesting. Overcoming them is what makes life meaningful.",
    "Failure is simply the opportunity to begin again, this time more intelligently.",
    "Effort and persistence lead to mastery.",
]
st.subheader("💬 Mindset Quote:")
st.write((quotes))

st.subheader("🌟Daily Reflection")
reflection = st.text_area("What challenge did you face today and how did you handle it?")
if st.button("Save Reflection"):
    st.success("Reflection saved!")

st.subheader("💪 What's your Challenge Today?")
st.text_area("Describe Your Challenge...")
  
st.subheader("�� What's Your Growth Mindset?")
st.write("""1. I believe in the power of hard work, perseverance, and resilience.,
 2. I believe in the importance of setting realistic goals and breaking them down into manageable tasks.,
 3. Success comes from hard work, practice, and consistency.""")

# Achievement
st.title("🏆 Your Achievements")
achievement = st.text_input("Record a new achievement:")

if st.button("Add Achievement"):
    st.balloons()
    st.success("Achievement added!")
else:
    st.write("Add your achievement here.") 

#Footer

st.subheader("��About Growth Mindset")
st.write("""Growth mindset is a mindset that encourages people to view challenges as opportunities for learning and growth rather than as failures. It helps people see that success is a journey, not a destination.""")

st.write("---")
st.write("�� 2023 Growth Mindset")  
st.write("keep believing in yourself. Growth is a journey not a destination.🌟")
st.write("🔴 Created by Aiman Rizwan")   


