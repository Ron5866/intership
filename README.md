# 🎓 CLAT Mentor Recommendation System

This project recommends suitable mentors to CLAT aspirants based on their subject preferences, target college, preparation level, and learning style. It leverages cosine similarity to compute matches and offers an interactive Streamlit-based interface.

---

## 🧠 Features

- 🔍 Recommend top 3 mentors based on aspirant profiles  
- ✅ Uses `cosine_similarity` on encoded categorical data  
- 📊 Clean UI built using Streamlit  
- 📁 Pre-trained data stored in a `.pkl` file (no need to retrain every time)  

---

## 📂 Project Structure



---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/clat-mentor-recommender.git
cd clat-mentor-recommender
```

### 2. (Optional) Create a Virtual Environment
```bash
python -m venv venv
````

# Activate the virtual environment:

# On Windows:
```bash
.\venv\Scripts\activate
```
# On Mac/Linux:
```bash
source venv/bin/activate
```

### 3.Install Required Packages
```bash
python -m pip install --upgrade pip
pip install streamlit pandas scikit-learn
```

### 4. Make Sure .pkl File Is Present
Ensure that recommendation_model.pkl (generated via the notebook) is in the same directory as streamlit_app.py.

## 🚀 Running the App
streamlit run streamlit_app.py
Then open your browser and navigate to:
```bash
http://localhost:8501
````
## 🧪 Example Use Case

Select an Aspirant ID from the dropdown.

View the aspirant profile (subjects, college, level, learning style).

Click "Recommend Mentors" to get top 3 mentor matches with detailed info.

## 👤 Author
GitHub: @Ron5866


