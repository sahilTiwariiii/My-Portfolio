from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "burakork-resume.pdf"
profile_pic = current_dir / "p.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Sahil Tiwari"
PAGE_ICON = ":wave:"
NAME = "Sahil Tiwari"
DESCRIPTION = """
Data Scientist | ML Engineer | MLOps Engineer | AI Engineer | Data Analyst | Deep Learning | NLP.
"""
EMAIL = "sahiltiwari1222@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sahil-tiwari-b2269b27a/",
    "GitHub": "https://github.com/sahilTiwariiii",
    "Twitter": "https://twitter.com/sahil_tiwa96610",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].markdown(f"[![{platform}](https://img.shields.io/badge/-{platform}-blue?style=flat-square&logo={platform.lower()}&logoColor=white)]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Experience in extracting actionable insights from data
- ✔️ Strong hands-on experience and knowledge in Python and Data Science
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.subheader("Hard Skills")
st.write("""
- **Data Science** 📊: Comprehensive knowledge and application of statistics, data analysis, and data visualization techniques.
- **Machine Learning** 🤖: Proficient in developing and implementing machine learning models using various algorithms.
- **Deep Learning** 🧠: Skilled in building and training deep neural networks for complex pattern recognition and predictive analytics.
- **Natural Language Processing (NLP)** 💬: In-depth understanding of NLP techniques for text analysis, sentiment analysis, and language modeling.
- **Data Analysis** 📈: Expertise in data wrangling, cleaning, and exploratory data analysis to extract meaningful insights.
- **Libraries & Frameworks** 🛠️:
  - **scikit-learn**: Machine learning library for Python.
  - **NumPy**: Fundamental package for scientific computing with Python.
  - **Seaborn**: Statistical data visualization library based on matplotlib.
  - **Pandas**: Data manipulation and analysis library.
  - **TensorFlow**: Open-source platform for machine learning.
- **Programming Languages** 💻:
  - **Python**: Advanced proficiency in Python for data science and machine learning.
  - **JavaScript**: Competence in JavaScript for web development.
- **Databases** 🛢️:
  - **MongoDB**: Experience with NoSQL databases for scalable data storage.
  - **SQL**: Proficiency in SQL for relational database management.
- **MLOps Tools** 🚀:
  - **MLflow**: Tool for managing the end-to-end machine learning lifecycle.
  - **DVC (Data Version Control)**: Version control system for machine learning projects.
  - **Github Actions**: Automation tool for CI/CD pipelines.
  - **AWS Cloud**: Knowledge of deploying and managing applications on AWS cloud infrastructure.
- **Other Tools** 🔧:
  - **Evidently AI**: Platform for managing and deploying AI models.
""")

# Function to create project section
def create_project_section(title, description, tools, link):
    st.subheader(title)
    st.write(description)
    st.write("**Tools Used:**")
    for tool in tools:
        st.markdown(f"- {tool}")
    if link:
        st.markdown(f'<a href="{link}" target="_blank"><button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Project Link</button></a>', unsafe_allow_html=True)

# Streamlit App Layout
st.title("🚀 My Machine Learning and MLOps Projects")
st.write("Welcome to my portfolio of machine learning and MLOps projects. Below is an overview of my completed projects, each with detailed descriptions, tools used, and links to the project repositories. I've also included an animated sequence to visually guide you through my projects.")

# Project 1: Student Performance Indicator
create_project_section(
    "🎓 Project 1: Student Performance Indicator",
    "This is a complete end-to-end machine learning and MLOps project. It involves predicting student performance using various machine learning techniques and deploying the model using MLOps tools.",
    ["Python 🐍", "MySQL 🛢️", "Docker 🐳", "Flask 🌐", "dotenv 🔐", "Machine Learning 🧠", "Statistics 📊", "Numpy 🔣", "Scikit-learn 🔍", "Pandas 🐼", "Seaborn 📈", "PyMySQL 🛠️", "DVC 🗂️", "MLflow 🚀", "AWS ☁️", "Streamlit 🌐"],
    "https://github.com/sahilTiwariiii/Dssp"
)

# Project 2: Email Spam Classifier
create_project_section(
    "📧 Project 2: Email Spam Classifier",
    "A classification project to identify spam emails using natural language processing and machine learning algorithms.",
    ["Python 🐍", "NLTK 📚", "Pandas 🐼", "Numpy 🔣", "Scikit-learn 🔍", "Streamlit 🌐"],
    "https://github.com/sahilTiwariiii/Email-Spam-Classifier"
)

# Project 3: Laptop Price Predictor
create_project_section(
    "💻 Project 3: Laptop Price Predictor",
    "A regression project to predict laptop prices based on various features such as brand, RAM, storage, etc.",
    ["Python 🐍", "Pandas 🐼", "Numpy 🔣", "Scikit-learn 🔍", "Streamlit 🌐"],
    "https://github.com/sahilTiwariiii/Laptop-Price-Predictor"
)

# Project 4: Diwali Sale Analysis
create_project_section(
    "🛒 Project 4: Diwali Sale Analysis",
    "Diwali Sale Analysis for an Ecommerce Organization",
    ["Python 🐍", "Pandas 🐼", "Numpy 🔣", "Matplotlib 📊", "Seaborn 📈", "Jupyter Notebook 📓"],
    "https://github.com/sahilTiwariiii/Diwali-analysis"
)

# Project 5: E-commerce Web Application (MERN Stack)
create_project_section(
    "🛒 Project 5: E-commerce Web Application (MERN Stack)",
    "A full-stack web application for an e-commerce platform built using the MERN (MongoDB, Express, React, Node.js) stack.",
    ["MongoDB 🍃", "Express 🏢", "React ⚛️", "Node.js 🟢", "JavaScript 📜", "CSS 🎨", "HTML 📝"],
    "https://github.com/sahilTiwariiii/Ecommerce-famous-MERN-app"
)

# Project 6: Unio Marketplace
create_project_section(
    "📈 Project 6: Unio Marketplace Real Estate Website",
    "A web application for real estate listings using Unio Marketplace.",
    ["Python 🐍", "Django 🌐", "JavaScript 📜", "HTML 📝", "CSS 🎨"],
    "https://github.com/sahilTiwariiii/UnioMarketPlace"
)

# Animation Section
st.subheader("🔄 Animation of Project Sequence")
st.write("To give you a better understanding of the sequence and flow of my projects, here is an animated overview:")
st.image("https://your-animation-link.com/animation.gif")




# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")

# Internship at Bambhari
st.markdown("### Bambhari (Frontend Developer)")
st.write("""
During my internship at Bambhari, I gained valuable experience as a Frontend Developer and contributed to various aspects of web development projects. My responsibilities included:
- Collaborating with team members to design and develop user-friendly interfaces.
- Utilizing React.js, HTML, and CSS to create responsive and dynamic frontend applications.
- Implementing interactive features and ensuring cross-browser compatibility.
- Participating in agile development processes and contributing to team discussions and brainstorming sessions.
""")

# Link to Bambhari website
st.markdown("[Bambhari Website](https://www.linkedin.com/company/bambhari/mycompany/)")



# Connect with me
st.markdown("---")
st.write("**Connect with me:**")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].markdown(f"[![{platform}](https://img.shields.io/badge/-{platform}-blue?style=flat-square&logo={platform.lower()}&logoColor=white)]({link})")






