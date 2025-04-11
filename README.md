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

```bash
clat-mentor-recommender/
│
├── streamlit_app.py              # Streamlit UI to select aspirant & show recommendations
├── recommendation_model.pkl      # Pickled data + features generated in Google Colab
├── generate_model.ipynb          # Jupyter notebook to create and save the .pkl file
└── README.md                     # Project overview and setup instructions


## ⚙️ Setup Instructions
# 1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/clat-mentor-recommender.git
cd clat-mentor-recommender

# 2. (Optional) Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
.\venv\Scripts\activate          # For Windows
# OR
source venv/bin/activate        # For Mac/Linux

#3. Install Required Packages
bash
Copy
Edit
python -m pip install --upgrade pip
pip install streamlit pandas scikit-learn
4. Make Sure .pkl File Is Present
Ensure that recommendation_model.pkl (generated via the notebook) is in the same directory as streamlit_app.py.

## 🚀 Running the App
bash
Copy
Edit
streamlit run streamlit_app.py
Then open your browser and navigate to:
http://localhost:8501

## 🧪 Example Use Case
Select an aspirant ID from the dropdown.

View aspirant profile (subjects, college, level, learning style).

Click "Recommend Mentors" to get top 3 mentor matches with detailed info.

👤 Author
Your Name

GitHub: @your-username

