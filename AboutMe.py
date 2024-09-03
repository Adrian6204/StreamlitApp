import streamlit as st
import pandas as pd

st.markdown("""
    <style>
    .stApp {
        background-color: #6482AD;
    }

    [data-testid="stSidebar"] > div:first-child {
        background-color: #E2DAD6;
    }

    [data-testid="stSidebar"] * {
        color: black; 
    }

    .stApp p, 
    .stApp li,
    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stApp h4,
    .stApp h5,
    .stApp h6 {
        color: white;
    }

    a {
        color: #1E90FF;
    }

    img {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

def show_about_me():
    st.title("About Me: Adrian AJ R. De Leon")
    st.write("""
    Welcome to my personal Streamlit app! I'm an Information Technology student from Cebu Institute of Technology - U. My interests within my field are Data Analytics, Quality Assurance, and Project Management.
    While my personal interests are gaming, rides, photography, and chess. In regards to why I chose this course, simply because this field is constantly advancing and being updated in technologies and such is important for me.
    I'm ready to accept any job I can get after graduating, but I'm hoping to become a Project Manager in my later years.
    """)
    st.write("""
    In my free time, I enjoy exploring new technologies, working on creative projects like game development on Roblox, and learning new skills to expand my professional toolkit.
    """)

def show_basic_details():
    st.title("Basic Details")
    st.write(f"**Name**: Adrian AJ R. De Leon")
    st.write(f"**Age**: 22")
    st.write(f"**Location**: Cebu City, Philippines")
    st.write(f"**Favorite Food**: Sinigang")
    st.write(f"**Favorite Color**: Blue")

def show_resume():
    st.title("Resume")
    st.image("Images/resume.jpg", caption="My Resume", use_column_width=True)

def show_map():
    st.title("Map: Cebu City")
    map_data = pd.DataFrame({
        'lat': [10.3157],
        'lon': [123.8854]
    })
    st.map(map_data)

def show_activities():
    st.title("Personality Test")

    st.subheader("1. Favorite Programming Language")
    language = st.selectbox(
        "Choose your favorite programming language:",
        ["Python", "JavaScript", "C++", "Java", "C#"]
    )
    st.write(f"You selected: {language}")

    st.subheader("2. Daily Routine")
    st.write("What does your typical day look like?")
    morning_activity = st.text_input("Morning Activity", "Coding")
    afternoon_activity = st.text_input("Afternoon Activity", "Learning new tech")
    evening_activity = st.text_input("Evening Activity", "Relaxing or gaming")
    st.write(f"Morning: {morning_activity}")
    st.write(f"Afternoon: {afternoon_activity}")
    st.write(f"Evening: {evening_activity}")

    st.subheader("3. Goal Setting")
    goal = st.text_area("Set a goal for yourself:")
    if st.button("Submit Goal"):
        st.write(f"Your goal is: {goal}")

    st.subheader("4. Inspirational Quote")
    quote = st.text_input("Share an inspirational quote you like:")
    if st.button("Share Quote"):
        st.write(f"Your favorite quote: {quote}")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "About Me", "Basic Details", "Resume", "Map", "Activities"])

if page == "Home":
    st.title("Welcome to My Streamlit App")
    
    st.write("""
    Hi! I'm Adrian AJ R. De Leon. Welcome to my interactive portfolio.
    This app showcases my background, interests, and some of the projects I've worked on.
    Use the sidebar to explore different sections of the app.
    """)

    st.image("Images/profpic.jpg", caption="Adrian AJ R. De Leon", width=200)

    st.header("Explore the App")
    st.write("""
    - **About Me**: Learn more about my educational background, passions, and hobbies.
    - **Basic Details**: Get to know some basic details about me, like my favorite food and color.
    - **Resume**: View my professional resume.
    - **Map**: See a map focusing on my hometown, Cebu City.
    - **Activities**: Engage in interactive activities to know more about my daily routine, goals, and inspirations.
    """)

    st.header("Recent Projects")
    st.write("Here are a few highlights of my recent work:")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("FoodMatch")
        st.image("Images/foodmatch.PNG", use_column_width=True)
        st.write("An application for managing recipes.")

    with col2:
        st.subheader("EcoWatch")
        st.image("Images/ecowatch.jpg", use_column_width=True)
        st.write("A web application for managing electricity and water consumption in an office setting.")

    st.header("Skills and Expertise")
    st.write("""
    - **Web Development**: JavaScript, React, Node.js, Firebase
    - **Backend Development**: Java, BootStrap, Python
    - **Project Management**: EcoWatch
    """)

    st.header("Get in Touch")
    st.write("You can reach me via [LinkedIn](https://www.linkedin.com) or email at adrianajdeleon@gmail.com.")

elif page == "About Me":
    show_about_me()
elif page == "Basic Details":
    show_basic_details()
elif page == "Resume":
    show_resume()
elif page == "Map":
    show_map()
elif page == "Activities":
    show_activities()
