import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(page_title="Hygiea", page_icon="hygiea_1-removebg-preview.png", layout="wide")

# Load Local Dataset (diabetes.csv)
@st.cache_data  # Cache the dataset to improve performance
def load_data():
    # Replace this with the path to your local dataset
    data = pd.read_csv("diabetes.csv")
    return data

data = load_data()

# Custom CSS for styling
st.markdown("""
<style>
    /* Custom Cursor (Stethoscope) */
    body, button, a { cursor: url('https://cdn-icons-png.flaticon.com/512/427/427735.png'), auto; }

    /* Global Styles */
    .stApp { background-color: #11263d; }
    .stHeader { color: #53c89b; font-family: 'Poppins', sans-serif; }
    .stMarkdown { color: white; }

    /* Hero Section */
    .hero-section { 
        position: relative;
         margin-top:35px;
        height: 100vh; 
        display: flex; 
        flex-direction: column; 
        justify-content: center; 
        background: linear-gradient(rgba(8,0,58,0.7), rgba(8,0,58,0.7)), url("https://t4.ftcdn.net/jpg/05/50/83/61/360_F_550836159_9ZAJDg8t9F7WOqrMbrD0Wlp7BAaWRrw4.jpg");
        align-items: center; 
        text-align: center; 
        color: white; 
        overflow: hidden;
        background-size: cover;
        background-position: center;
    }
    .hero-content {
        position: relative;
        z-index: 1;
    }
    .hero-section h1 { 
        font-size: 64px; 
        font-weight: bold; 
        margin-bottom: 20px; 
    }
    .hero-section p { 
        font-size: 24px; 
        margin-bottom: 40px; 
    }
    .hero-section button { 
        background-color: #53c89b; 
        color: white; 
        border: none; 
        padding: 15px 30px; 
        border-radius: 50px; 
        font-size: 18px; 
        transition: transform 0.3s ease, box-shadow 0.3s ease; 
    }
    .hero-section button:hover { 
        transform: translateY(-5px); 
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2); 
    }

    /* About Section */
    .about-section { 
        margin-top: 20px;
        background-color: #F0F0F0; 
        padding: 50px 20px; 
        border-radius: 20px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .about-section:hover {
        transform: scale(1.05); 
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    }

    .about-section p { color: #11263d;
            font-size: 20px; }

    /* How It Works Section */
    .how-it-works-section { 
        background-color: white; 
        padding: 50px 20px; 
        margin-top: 20px;
        border-radius: 20px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .how-it-works-section:hover {
        transform: scale(1.05); 
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    }
    .how-it-works-section p { color: #11263d; 
            font-size: 20px;}

    /* Key Features Section */
    .features-section { 
        margin-top: 20px;
        border-radius: 20px;
        background: linear-gradient(to right, #53c89b, #11263d); 
        padding: 50px 20px; 
    }
    .features-section:hover {
        transform: scale(1.05); 
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    }
    .features-section h2 { color: white; }
    .feature-card { 
        background-color: white; 
        border-radius: 10px; 
        padding: 20px; 
        margin: 10px; 
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); 
        transition: transform 0.3s ease, box-shadow 0.3s ease; 
    }
    .feature-card:hover { 
        transform: scale(1.05); 
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); 
    }
    .feature-card h3 { color: #11263d; }
    .feature-card p { color: #11263d; }
        
      .heading-section {
        background-color: none;
        color: white;
        padding: 5px 5px;
        margin-top: 10px;
        border-radius: 20px;
        text-align:center;
        
    }
            
    .visual-section{
            background-color: #53c89b;
        color: white;
        padding: 5px 5px;
        margin-top: 10px;
        border-radius: 20px;
        text-align:center;
        
            }
                        
   .nav-bar {
    height: 50px; /* Adjust height as needed */
    width: 100%;
    display: flex;
    align-items: center; /* Center items vertically */
    padding: 0 10px; /* Add padding */
    
}

.nav-bar  img {
    width: 30px; /* Adjust width as needed */
    height: 30px; /* Adjust height as needed */
    margin-right: 10px; /* Add spacing between logo and text */
}

.nav-bar h2 {
    color: white;
    margin: 0; /* Remove default margin */
}

    /* Dataset Section */
    .dataset-section {
        background-color: none;
        color: white;
        padding: 10px 10px;
        margin-top: 20px;
        border-radius: 20px;
    }
    .dataset-section h2 {
        color: #FFFF;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Testimonials Section */
    .testimonials-section { 
        background-color: #F0F0F0; 
        padding: 50px 20px; 
        margin-top: 20px;
        border-radius: 20px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .testimonials-section:hover { 
        transform: scale(1.05); 
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); 
    }
    .testimonials-section h2 { color: #11263d; }
    .testimonial-card { 
        background-color: white; 
        border-radius: 10px; 
        padding: 20px; 
        margin: 10px; 
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); 
        transition: transform 0.3s ease, box-shadow 0.3s ease; 
        text-align: center;
    }
    .testimonial-card:hover { 
        transform: scale(1.05); 
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); 
    }
    .testimonial-card img {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        margin-bottom: 15px;
        object-fit: cover;
    }
    .testimonial-card h3 { color: #11263d; }
    .testimonial-card p { color: #11263d; }

    /* FAQ Section */
    .faq-section {
        background-color: white;
        padding: 50px 20px;
        margin-top: 20px;
        background: linear-gradient(to right, #53c89b, #11263d);
        border-radius: 20px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .faq-section:hover { 
        transform: scale(1.05); 
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); 
    }
    .faq-section h2 {
        color: #11263d;
        text-align: center;
        margin-bottom: 30px;
    }
    .faq-container {
        display: flex;
        justify-content: space-between;
        gap: 20px;
    }
    .faq-block {
        background-color: #F0F0F0;
        border-radius: 10px;
        padding: 20px;
        flex: 1;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .faq-block:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    }
    .faq-block h3 {
        color: #11263d;
        margin-bottom: 10px;
    }
    .faq-block p {
        color: #11263d;
    }

    /* Call-to-Action Section */
    .cta-section { 
        background-color: #11263d; 
        padding: 30px 10px; 
        text-align: center; 
        margin-top: 40px;
        border: solid 2px #53c89b;
        border-top-left-radius:20px;
        border-top-right-radius:20px;
    }
    .cta-section h2 { color: white; }
    .cta-section .button { 
        background-color: #53c89b; 
        color: white; 
        border: none; 
        padding: 10px 20px; 
        border-radius: 10px; 
        margin: 10px; 
        text-decoration:none;
        cursor:pointer;
        transition: background-color 0.3s ease; 
    }
    .cta-section button:hover { background-color: #3aa87f; }

    /* Footer */
    .footer { 
        
        background-color: #11263d; 
        padding: 20px; 
        text-align: center; 
    }
    .footer p { color: white; }
</style>
""", unsafe_allow_html=True)

# Navbar with Hosted Image URL
st.markdown(
    """
    <style>
        .nav-bar {
            display: flex;
            align-items: center;
        }
        .nav-bar img {
            width: 50px;  /* Adjust size as needed */
            height: auto;
            margin-right: 10px;
        }
        .nav-bar h2 {
            margin: 0;
            font-size: 24px;
        }
    </style>
    <div class="nav-bar">
        <img src="https://res.cloudinary.com/dcscwh33t/image/upload/v1741415925/hygiea_1-removebg-preview_rapzjl.png" alt="Logo">
        <h2>HYGIEA</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# Hero Section
st.markdown(
    """
    <div class="hero-section">
        <div class="hero-content">
            <h1>Hygiea</h1>
            <p>Empowering Health, One Drop at a Time.</p>
            <p>Hygiea is revolutionizing healthcare with urine analysis for early disease detection.</p>
            <button>Learn More</button>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# About Section
st.markdown(
    """
     <div class="heading-section" >
        <h2 style="font-size: 2rem;" >About Us</h2>
    </div>
    <div class="about-section">
        <p>Hygiea is not just a device—it’s a groundbreaking innovation that transforms your everyday toilet seat into a powerful health-monitoring system. Designed with cutting-edge technology, Hygiea seamlessly integrates into your bathroom routine, providing real-time health insights without disrupting your daily life. It’s the future of proactive health management, right in the comfort of your home</p>
    </div>
    """,
    unsafe_allow_html=True
)

# How It Works Section
st.markdown(
    """
      <div class="heading-section" >
        <h2 >Working</h2>
    </div>
    <div class="how-it-works-section">
         <p>1. <strong>Sample Collection</strong>: Hygiea’s advanced sensors seamlessly collect health data during your daily bathroom routine. No needles, no extra steps—just use your toilet as you normally would</p>
        <p>2. <strong>AI Analysis</strong>: Hygiea’s cutting-edge AI algorithms process the collected data in real-time. By leveraging machine learning and predictive analytics, the system identifies potential health risks, tracks trends, and detects early warning signs of conditions like diabetes, kidney issues, or dehydration</p>
        <p>3. <strong>Insights & Recommendations</strong>: Hygiea delivers personalized health insights directly to your smartphone via its user-friendly app. From hydration reminders to dietary suggestions and early warnings about potential health issues</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Key Features Section
st.markdown(
    """
    <div class="heading-section" >
        <h2 >Why Choose Hygiea?</h2>
    </div>
    <div class="features-section">
        <div style="display: flex; justify-content: space-between;">
            <div class="feature-card">
                <h3>🤖 AI-Powered Analysis</h3>
                <p>Accurate and fast results powered by state-of-the-art AI.</p>
            </div>
            <div class="feature-card">
                <h3>🩺 Early Disease Detection</h3>
                <p>Proactive health management through early detection of diseases.</p>
            </div>
            <div class="feature-card">
                <h3>📱 User-Friendly Interface</h3>
                <p>Designed for ease of use, ensuring accessibility for everyone.</p>
            </div>
            <div class="feature-card">
                <h3>🔒 Data Privacy</h3>
                <p>Your data is secure and confidential, with end-to-end encryption.</p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Dataset Section
st.markdown(
    """
    <div class="heading-section">
        <h2>Diabetes Dataset</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# Display the Diabetes Dataset
st.dataframe(data)

# Graphs Section
st.markdown(
    """
    <div class="visual-section">
        <h2>Data Visualizations</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# Graph 1: Histogram of Age
st.markdown(
    """
    <div class="heading-section">
        <h2>Age Distribution</h2>
    </div>
    """,
    unsafe_allow_html=True
)
fig1, ax1 = plt.subplots()
sns.histplot(data['Age'], bins=20, kde=True, ax=ax1, color='#53c89b')
ax1.set_xlabel("Age")
ax1.set_ylabel("Frequency")
st.pyplot(fig1)

# Graph 2: Scatter Plot of Glucose vs BMI
st.markdown(
    """
    <div class="heading-section">
        <h2>Glucose vs BMI</h2>
    </div>
    """,
    unsafe_allow_html=True
)
fig2, ax2 = plt.subplots()
sns.scatterplot(x=data['Glucose'], y=data['BMI'], hue=data['Outcome'], palette='coolwarm', ax=ax2)
ax2.set_xlabel("Glucose")
ax2.set_ylabel("BMI")
st.pyplot(fig2)

# Graph 3: Bar Chart of Outcome Distribution
st.markdown(
    """
    <div class="heading-section">
        <h2>Outcome Distribution</h2>
    </div>
    """,
    unsafe_allow_html=True
)
fig3, ax3 = plt.subplots()
sns.countplot(x=data['Outcome'], palette='viridis', ax=ax3)
ax3.set_xlabel("Outcome (0: No Diabetes, 1: Diabetes)")
ax3.set_ylabel("Count")
st.pyplot(fig3)

# Graph 4: Correlation Heatmap
st.markdown(
    """
    <div class="heading-section">
        <h2>Correlation Heatmap</h2>
    </div>
    """,
    unsafe_allow_html=True
)
fig4, ax4 = plt.subplots()
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax4)
st.pyplot(fig4)

# Testimonials Section
st.markdown(
    """
    <div class="heading-section" >
        <h2 >Testimonials</h2>
    </div>
    <div class="testimonials-section">
        <div style="display: flex; justify-content: space-between;">
            <div class="testimonial-card">
                <img src="https://media.istockphoto.com/id/1293373291/photo/portrait-of-confident-ethnic-female-doctor.jpg?s=612x612&w=0&k=20&c=CJsw6IgTecJZoBeVXqZdvh2BI-NyVa-8VcQM3fPhbYc=" alt="Dr. Madhu Sagdeo">
                <h3>Dr. Madhu Sagdeo</h3>
                <p>"Hygiea is a game-changer in preventive healthcare. Its real-time biomarker analysis is revolutionary, it will help people to stay more healthy as prevention is better than cure!"</p>
                <p>⭐⭐⭐⭐⭐</p>
            </div>
            <div class="testimonial-card">
                <img src="https://st.depositphotos.com/49005766/54607/i/450/depositphotos_546075462-stock-photo-indian-female-doctor-portrait-south.jpg" alt="Dr. Mohini Singh">
                <h3>Dr. Mohini Singh</h3>
                <p>"Hygiea simplifies health monitoring in the most user-friendly way. It’s been a great tool for tracking my hydration and understanding how lifestyle impacts health. A must-have for anyone interested in preventive care!"</p>
                <p>⭐⭐⭐⭐</p>
            </div>
            <div class="testimonial-card">
                <img src="https://t4.ftcdn.net/jpg/06/47/16/29/360_F_647162966_SFu8GP6awkeW0OnFnAxPjiGXSoeme4ht.jpg" alt="Dr. Ananya Pandey">
                <h3>Dr. Ananya Pandey</h3>
                <p>"Hygiea has been a lifesaver during my exams, helping me monitor hydration and stress levels. It’s amazing how it combines AI and health insights—truly inspiring for the future of medicine!"</p>
                <p>⭐⭐⭐⭐⭐</p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# FAQ Section
st.markdown(
    """
    <div class="heading-section" >
        <h2 >Frequently Asked Questions</h2>
    </div>
    <div class="faq-section">
        <div class="faq-container">
            <div class="faq-block">
                <h3>What is Hygiea?</h3>
                <p>Hygiea is a platform that uses AI to analyze blood test results for early disease detection.</p>
            </div>
            <div class="faq-block">
                <h3>How does Hygiea work?</h3>
                <p>Hygiea collects blood test data, analyzes it using AI, and provides personalized health insights.</p>
            </div>
            <div class="faq-block">
                <h3>Is my data secure?</h3>
                <p>Yes, Hygiea uses end-to-end encryption to ensure your data is secure and confidential.</p>
            </div>
            <div class="faq-block">
                <h3>Can I trust the results?</h3>
                <p>Hygiea's AI algorithms are state-of-the-art and provide accurate and reliable results.</p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Call-to-Action Section
st.markdown(
    """
    <div class="cta-section">
        <h2>Join the Health Revolution Today!</h2>
        <a class="button" href = "https://www.linkedin.com/company/emissionzeroindia/">Join Us</a>
        <a class="button" href = "https://www.linkedin.com/in/yashvant-singh-90787a290/">Contact Us</a> 
         <div class="footer">
        <p>© 2023 Hygiea. All rights reserved.</p>
    </div>
    </div>
    """,
    unsafe_allow_html=True
)

