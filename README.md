# AutoAnalytica

An AI-powered data analytics platform built with Streamlit.

# 🧠 AutoAnalytica – Your Personal Data Analyst

AutoAnalytica is an intelligent, GPT-powered, multi-module data analytics platform designed to automate Exploratory Data Analysis (EDA), generate insights, and interact with datasets conversationally — all in a clean Streamlit interface.

---

## 🚀 Features

🔹 **Upload & Clean** datasets with ease  
🔹 **Automated EDA**: Summary, distributions, correlations  
🔹 **AI Insights Generator** (powered by OpenAI & PandasAI)  
🔹 **Chat with Your Data** using natural language  
🔹 **Strategy Module** for business-oriented recommendations  
🔹 **Multi-page Streamlit app** with state management

---

## 📂 Folder Structure

AutoAnalytica_Starter/
├── .streamlit/
│ └── config.toml
├── pages/
│ ├── 1_Upload_Data.py
│ ├── 2_AutoEDA.py
│ ├── 3_Insights_AI.py
│ ├── 4_DataChatbot.py
│ └── 5_Strategy_Module.py
├── utils/
│ ├── cleaning.py
│ ├── eda_tools.py
│ ├── gpt_insights.py
│ ├── chatbot.py
│ └── strategy_models.py
├── main.py
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 💻 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/ummessh/AutoAnalytica_Starter.git
cd AutoAnalytica_Starter
2. Install dependencies
Make sure you have Python 3.9+ and run:

bash
Copy
Edit
pip install -r requirements.txt
3. Add your OpenAI API key
Create a .env file:

bash
Copy
Edit
OPENAI_API_KEY=your_openai_key_here
4. Run the app
bash
Copy
Edit
streamlit run main.py
🧠 Modules Explained
Module	Description
📁 Upload Data	Upload and clean your CSV/Excel datasets
📊 AutoEDA	Automatically perform EDA using Pandas and Plotly
🤖 GPT Insights	AI-generated insights using OpenAI GPT
💬 Data Chatbot	Ask your dataset anything using PandasAI
🎯 Strategy Module	Advanced recommendations for business insights

🧪 Tech Stack
Python 3.9+

Streamlit

Pandas

PandasAI

OpenAI GPT-3.5 / 4 (via API)

dotenv

Plotly / Seaborn / Matplotlib

📦 Deployment
You can deploy this app on:

Streamlit Community Cloud 🚀

Heroku, Railway, or Render (via Docker or WSGI)

🙌 Author
Umesh Tiwari
🧠 AI/ML Enthusiast | 📊 Data Science Explorer
📫 Connect on LinkedIn

📄 License
This project is open-source under the MIT License.

yaml
Copy
Edit

---

## 👉 Next Steps

- Save the content above as `README.md` inside your project
- Commit and push:
```bash
git add README.md
git commit -m "Add project README"
git push
