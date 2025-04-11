import streamlit as st
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Load model and data
with open("recommendation_model.pkl", "rb") as f:
    data = pickle.load(f)

aspirants = data["aspirants"]
mentors = data["mentors"]
aspirant_features = data["aspirant_features"]
mentor_features = data["mentor_features"]

st.title("🔍 CLAT Mentor Recommender")

# Dropdown for aspirant selection
aspirant_ids = aspirants["id"].tolist()
aspirant_option = st.selectbox("Select your Aspirant ID", aspirant_ids)

# Show selected aspirant's details
aspirant_info = aspirants[aspirants["id"] == aspirant_option].iloc[0]
st.subheader("🧑‍🎓 Aspirant Profile")
st.write(f"**Subjects:** {', '.join(aspirant_info['preferred_subjects'])}")
st.write(f"**Target College:** {aspirant_info['target_college']}")
st.write(f"**Prep Level:** {aspirant_info['prep_level']}")
st.write(f"**Learning Style:** {aspirant_info['learning_style']}")

# Recommend mentors
if st.button("Recommend Mentors"):
    index = aspirants[aspirants["id"] == aspirant_option].index[0]
    similarities = cosine_similarity([aspirant_features.iloc[index]], mentor_features)[0]
    top_indices = similarities.argsort()[::-1][:3]

    st.subheader("🎓 Top 3 Mentor Recommendations")
    for idx in top_indices:
        mentor = mentors.iloc[idx]
        st.markdown(f"""
        **👨‍🏫 {mentor['name']}**
        - Subjects: {', '.join(mentor['expertise_subjects'])}
        - College: {mentor['college']}
        - Teaching Style: {mentor['teaching_style']}
        - Mastery Level: {mentor['prep_level_mastery']}
        """)
