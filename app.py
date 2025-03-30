import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import random
import time
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Finance Quiz App",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    /* Main heading colors */
    h1 {
        color: #FF4081 !important;
        font-weight: 700 !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    h2 {
        color: #E91E63 !important;
        font-weight: 600 !important;
    }
    
    h3 {
        color: #D81B60 !important;
        font-weight: 600 !important;
    }
    
    h4 {
        color: #C2185B !important;
        font-weight: 600 !important;
    }
    
    /* Container text colors */
    .profile-container {
        color: #880E4F !important;
    }
    
    .quiz-container {
        color: #AD1457 !important;
    }
    
    .game-container {
        color: #C2185B !important;
    }
    
    .leaderboard-container {
        color: #D81B60 !important;
    }
    
    .insight-container {
        color: #E91E63 !important;
    }
    
    /* Text colors for different sections */
    p {
        color: #4A148C !important;
        font-weight: 500 !important;
    }
    
    li {
        color: #4A148C !important;
        font-weight: 500 !important;
    }
    
    /* Profile text colors */
    .profile-text {
        color: #6A1B9A !important;
    }
    
    /* Quiz text colors */
    .quiz-text {
        color: #4A148C !important;
    }
    
    /* Game text colors */
    .game-text {
        color: #311B92 !important;
    }
    
    /* Leaderboard text colors */
    .leaderboard-text {
        color: #1A237E !important;
    }
    
    /* Insights text colors */
    .insight-text {
        color: #0D47A1 !important;
    }
    
    /* Button text color */
    .stButton>button {
        color: white !important;
    }
    
    /* Metric text colors */
    .metric-value {
        color: #1E88E5 !important;
        font-weight: 700 !important;
    }
    
    .metric-label {
        color: #0D47A1 !important;
        font-weight: 500 !important;
    }
    
    /* Main app styling */
    .stApp {
        background-color: #f0f4f8;
    }
    
    /* Main content padding */
    .main {
        padding-bottom: 120px;
    }
    
    /* Enhanced footer */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(135deg, #2c3e50, #3498db);
        color: white;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 -4px 12px rgba(0,0,0,0.1);
        z-index: 1000;
        font-weight: 500;
    }
    
    /* Profile container styling */
    .profile-container {
        background: linear-gradient(135deg, #ffffff, #f8f9fa);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        margin: 1rem 0;
        transition: all 0.3s ease;
        border: 1px solid rgba(0,0,0,0.05);
        position: relative;
        overflow: hidden;
    }
    
    .profile-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.2), transparent);
        transform: translateX(-100%);
        transition: 0.5s;
    }
    
    .profile-container:hover::before {
        transform: translateX(100%);
    }
    
    .profile-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }
    
    /* Quiz container styling */
    .quiz-container {
        background: linear-gradient(135deg, #ffffff, #f8f9fa);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        margin: 1rem 0;
        transition: all 0.3s ease;
        border: 1px solid rgba(0,0,0,0.05);
        position: relative;
        overflow: hidden;
    }
    
    .quiz-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.2), transparent);
        transform: translateX(-100%);
        transition: 0.5s;
    }
    
    .quiz-container:hover::before {
        transform: translateX(100%);
    }
    
    .quiz-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }
    
    /* Game container styling */
    .game-container {
        background: linear-gradient(135deg, #ffffff, #f8f9fa);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        margin: 1rem 0;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .game-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.2), transparent);
        transform: translateX(-100%);
        transition: 0.5s;
    }
    
    .game-container:hover::before {
        transform: translateX(100%);
    }
    
    .game-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }
    
    /* Button styling */
    .stButton>button {
        width: 100%;
        margin: 0.5rem 0;
        background: linear-gradient(135deg, #2c3e50, #3498db);
        color: white;
        border: none;
        padding: 0.8rem 1.5rem;
        border-radius: 8px;
        transition: all 0.3s ease;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        position: relative;
        overflow: hidden;
    }
    
    .stButton>button::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.2), transparent);
        transform: translateX(-100%);
        transition: 0.5s;
    }
    
    .stButton>button:hover::before {
        transform: translateX(100%);
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #3498db, #2c3e50);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(135deg, #2c3e50, #3498db);
    }
    
    /* Success message styling */
    .stSuccess {
        background: linear-gradient(135deg, #27ae60, #2ecc71);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        animation: slideIn 0.5s ease;
    }
    
    /* Error message styling */
    .stError {
        background: linear-gradient(135deg, #e74c3c, #c0392b);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        animation: slideIn 0.5s ease;
    }
    
    /* Warning message styling */
    .stWarning {
        background: linear-gradient(135deg, #f39c12, #e67e22);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        animation: slideIn 0.5s ease;
    }
    
    /* Info message styling */
    .stInfo {
        background: linear-gradient(135deg, #3498db, #2980b9);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        animation: slideIn 0.5s ease;
    }
    
    /* Profile image styling */
    .profile-image {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #3498db;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    /* Leaderboard styling */
    .leaderboard-container {
        background: linear-gradient(135deg, #ffffff, #f8f9fa);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .leaderboard-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }
    
    .leaderboard-item {
        background: linear-gradient(135deg, #ffffff, #f8f9fa);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
        border-left: 4px solid #3498db;
    }
    
    .leaderboard-item:hover {
        transform: translateX(10px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Quiz questions
questions = [
    {
        "question": "You just got your first job with a monthly salary of $3,000. What's the smartest way to handle your first paycheck?",
        "options": [
            "Spend it all on new clothes and gadgets",
            "Save 20% for emergencies, pay bills, then use the rest for fun",
            "Put it all in a savings account and don't touch it",
            "Give it all to your parents to manage"
        ],
        "correct": 1
    },
    {
        "question": "Your friend wants to borrow $500 and promises to pay it back next month. What should you do?",
        "options": [
            "Lend them the money since they're your friend",
            "Ask for a written agreement and set a repayment schedule",
            "Tell them to get a loan from the bank instead",
            "Give them the money as a gift"
        ],
        "correct": 1
    },
    {
        "question": "You see a new smartphone on sale for $200 off. Your current phone works fine. What's the best decision?",
        "options": [
            "Buy it immediately since it's a great deal",
            "Check your budget and savings first",
            "Put it on your credit card and pay later",
            "Ask your parents to buy it for you"
        ],
        "correct": 1
    },
    {
        "question": "Your car needs repairs that will cost $1,000. You have $500 in savings. What's the best approach?",
        "options": [
            "Put the repairs on your credit card",
            "Take out a personal loan",
            "Save up the remaining amount before getting repairs",
            "Ignore the repairs until you have more money"
        ],
        "correct": 2
    },
    {
        "question": "You receive a $1,000 tax refund. What's the smartest way to use it?",
        "options": [
            "Treat yourself to a shopping spree",
            "Put it in your emergency fund",
            "Invest it in stocks",
            "Use it to pay minimum payments on your credit card"
        ],
        "correct": 1
    },
    {
        "question": "Your friend tells you about a 'guaranteed' investment that will double your money in a week. What should you do?",
        "options": [
            "Invest all your savings immediately",
            "Research the investment thoroughly first",
            "Tell your other friends about the opportunity",
            "Borrow money to invest more"
        ],
        "correct": 1
    },
    {
        "question": "You're planning a vacation that will cost $2,000. What's the best way to save for it?",
        "options": [
            "Put it on your credit card and pay later",
            "Open a separate savings account and save monthly",
            "Take out a personal loan",
            "Ask family members to help pay for it"
        ],
        "correct": 1
    },
    {
        "question": "Your employer offers to match your 401(k) contributions up to 6%. What should you do?",
        "options": [
            "Contribute nothing since retirement is far away",
            "Contribute at least 6% to get the free money",
            "Contribute more than 6% to save extra",
            "Wait until you're older to start contributing"
        ],
        "correct": 1
    },
    {
        "question": "You find a $100 bill on the street. What's the best way to use it?",
        "options": [
            "Spend it on something fun",
            "Put it in your emergency fund",
            "Give it to charity",
            "Split it with friends"
        ],
        "correct": 1
    },
    {
        "question": "Your credit card bill is due in a week, but you don't have enough money to pay it. What should you do?",
        "options": [
            "Ignore it until you have more money",
            "Pay the minimum amount",
            "Call the credit card company to discuss options",
            "Get a cash advance from another card"
        ],
        "correct": 2
    }
]

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False
if 'game_score' not in st.session_state:
    st.session_state.game_score = 0
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = []
if 'user_profiles' not in st.session_state:
    st.session_state.user_profiles = {}
if 'current_user' not in st.session_state:
    st.session_state.current_user = None
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = None
if 'initial_score' not in st.session_state:
    st.session_state.initial_score = 0

# Navigation menu
with st.sidebar:
    selected = option_menu(
        menu_title="Finance Quiz",
        options=["Home", "Profile", "Quiz", "Game", "Results", "Leaderboard", "Insights"],
        icons=["house", "person", "question-circle", "gamepad", "graph-up", "trophy", "lightbulb"],
        menu_icon="cast",
        default_index=0,
    )

# Home page
if selected == "Home":
    st.markdown("<h1 style='color: #FF4081; text-align: center;'>Welcome to the Personal Finance Quiz! 📊</h1>", unsafe_allow_html=True)
    
    # Add a header image - Modern financial dashboard
    st.image("https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", width=800)
    
    st.markdown("""
    # :blue[Test your financial knowledge and learn more about personal finance!]
    
    ### This interactive quiz will help you:
    
    * 📚 Assess your financial literacy
    * 💡 Learn important financial concepts
    * 📈 Track your progress
    * 🎮 Have fun while learning!
    
    ## :blue[Features:]
    
    * 👤 Personal profile management
    * 📝 10 multiple-choice questions
    * 🎮 Interactive financial literacy game
    * 📈 Performance tracking
    * 💡 Educational insights
    * 🏆 Global leaderboard
    * 📊 Interactive charts and graphs
    
    ### :violet[Ready to begin? Create your profile and start the quiz!]
    """)
    
    # Add a quick stats section
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Questions", len(questions))
    with col2:
        st.metric("Topics Covered", "10+")
    with col3:
        st.metric("Interactive Features", "7+")

# Profile page
elif selected == "Profile":
    st.markdown("<h1 style='color: #FF4081; text-align: center;'>👤 Profile Management</h1>", unsafe_allow_html=True)
    
    # User selection section
    st.markdown("""
    <div class="profile-container">
        <h3 style='color: #D81B60;'>Select or Create Profile</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        if st.session_state.user_profiles:
            profiles_list = list(st.session_state.user_profiles.keys())
            selected_user = st.selectbox("Select Existing Profile:", 
                                       ["Create New Profile"] + profiles_list,
                                       index=0 if st.session_state.current_user is None else 
                                       profiles_list.index(st.session_state.current_user) + 1)
            
            if selected_user != "Create New Profile":
                st.session_state.current_user = selected_user
                st.session_state.user_profile = st.session_state.user_profiles[selected_user]
            else:
                st.session_state.current_user = None
                st.session_state.user_profile = None
        else:
            st.info("No profiles exist yet. Create your first profile!")
            st.session_state.current_user = None
            st.session_state.user_profile = None
    
    with col2:
        if st.session_state.current_user and st.button("Delete Profile", type="secondary"):
            user_to_delete = st.session_state.current_user
            if st.session_state.user_profiles.pop(user_to_delete, None):
                # Remove from leaderboard
                st.session_state.leaderboard = [entry for entry in st.session_state.leaderboard 
                                              if entry["name"] != user_to_delete]
                st.session_state.current_user = None
                st.session_state.user_profile = None
                st.success(f"Profile '{user_to_delete}' deleted successfully!")
                st.rerun()
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.session_state.user_profile is None:
        st.markdown("""
        <div class="profile-container">
            <h3 style='color: #D81B60;'>Create New Profile</h3>
            <p>Fill in your details to get started!</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Profile creation form
        with st.form("profile_form"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Full Name")
                age = st.number_input("Age", min_value=18, max_value=100)
                occupation = st.text_input("Occupation")
                education = st.selectbox("Education Level", 
                    ["High School", "Bachelor's Degree", "Master's Degree", "PhD"])
            
            with col2:
                email = st.text_input("Email")
                location = st.text_input("Location")
                financial_goals = st.multiselect("Financial Goals",
                    ["Retirement", "Home Purchase", "Investment", "Debt Management", "Emergency Fund"])
                experience_level = st.selectbox("Financial Experience Level",
                    options=["Beginner", "Intermediate", "Advanced"])
            
            submitted = st.form_submit_button("Create Profile")
            
            if submitted:
                if not name:
                    st.error("Please enter your name!")
                elif name in st.session_state.user_profiles:
                    st.error("A profile with this name already exists!")
                else:
                    # Create profile
                    new_profile = {
                        "name": name,
                        "age": age,
                        "occupation": occupation,
                        "education": education,
                        "email": email,
                        "location": location,
                        "financial_goals": financial_goals,
                        "experience_level": experience_level,
                        "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
                    }
                    
                    # Add to user profiles
                    st.session_state.user_profiles[name] = new_profile
                    st.session_state.current_user = name
                    st.session_state.user_profile = new_profile
                    
                    # Add to leaderboard with initial score
                    st.session_state.leaderboard.append({
                        "name": name,
                        "score": st.session_state.initial_score,
                        "date": time.strftime("%Y-%m-%d %H:%M:%S")
                    })
                    
                    st.success("Profile created successfully! 🎉")
                    st.rerun()
    else:
        # Display profile information
        st.markdown(f"""
        <div style="color: #FF4081; font-size: 24px; font-weight: 700; margin-bottom: 20px;">
            {st.session_state.user_profile['name']}
        </div>
        <div style="color: #4A148C;">
        - <strong>Age:</strong> {st.session_state.user_profile['age']}<br>
        - <strong>Occupation:</strong> {st.session_state.user_profile['occupation']}<br>
        - <strong>Education:</strong> {st.session_state.user_profile['education']}<br>
        - <strong>Location:</strong> {st.session_state.user_profile['location']}<br>
        - <strong>Experience Level:</strong> {st.session_state.user_profile['experience_level']}<br>
        - <strong>Financial Goals:</strong> {', '.join(st.session_state.user_profile['financial_goals'])}<br>
        - <strong>Member Since:</strong> {st.session_state.user_profile['created_at']}
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Switch to New Profile"):
            st.session_state.current_user = None
            st.session_state.user_profile = None
            st.rerun()

# Quiz page
elif selected == "Quiz":
    st.markdown("<h1 style='color: #FF4081; text-align: center;'>Personal Finance Quiz</h1>", unsafe_allow_html=True)
    
    # Add quiz page image - Financial education
    st.image("https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", width=800)
    
    # Add restart quiz button at the top
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🔄 Restart Quiz", type="primary"):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.quiz_completed = False
            st.rerun()
    
    if not st.session_state.quiz_completed:
        current_q = questions[st.session_state.current_question]
        
        with st.container():
            st.markdown(f"""
            <div class="quiz-container">
                <h3 style='color: #D81B60;'>Question {st.session_state.current_question + 1}/10</h3>
                <p style='color: #4A148C;'>{current_q['question']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            for i, option in enumerate(current_q['options']):
                if st.button(option, key=f"option_{i}"):
                    if i == current_q['correct']:
                        st.session_state.score += 1
                        st.success("Correct! 🎉")
                    else:
                        st.error(f"Wrong! The correct answer was: {current_q['options'][current_q['correct']]}")
                    
                    time.sleep(1)
                    st.session_state.current_question += 1
                    
                    if st.session_state.current_question >= len(questions):
                        st.session_state.quiz_completed = True
                        # Update leaderboard score
                        if st.session_state.user_profile:
                            for entry in st.session_state.leaderboard:
                                if entry["name"] == st.session_state.user_profile["name"]:
                                    entry["score"] = st.session_state.score
                                    entry["date"] = time.strftime("%Y-%m-%d %H:%M:%S")
                                    break
                        
                        st.success("Quiz completed! Check your results in the Results page! 🎉")
                        st.rerun()
                    else:
                        st.rerun()
        
        # Progress bar
        progress = (st.session_state.current_question + 1) / len(questions)
        st.progress(progress)
        
        # Score display
        st.sidebar.markdown(f"### Current Score: {st.session_state.score}/{st.session_state.current_question + 1}")
    else:
        st.title("Quiz Completed! 🎉")
        st.markdown(f"""
        ### Your Final Score: {st.session_state.score}/{len(questions)}
        
        Percentage: {(st.session_state.score/len(questions))*100:.1f}%
        
        Well done! You've completed the quiz. Check out the Results page to see your performance analysis.
        """)
        
        # Add restart button after completion
        if st.button("📝 Take Quiz Again", type="primary"):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.quiz_completed = False
            st.rerun()

# Game page
elif selected == "Game":
    st.markdown("<h1 style='color: #FF4081; text-align: center;'>Financial Literacy Game</h1>", unsafe_allow_html=True)
    
    # Add game page image - Interactive learning
    st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", width=800)
    
    with st.container():
        st.markdown("""
        <div class="game-container">
            <h3>Quick Math Challenge</h3>
            <p>Test your financial calculation skills!</p>
        </div>
        """, unsafe_allow_html=True)
        
        if 'game_question' not in st.session_state:
            st.session_state.game_question = {
                'num1': random.randint(10, 100),
                'num2': random.randint(10, 100),
                'operation': random.choice(['+', '-', '*'])
            }
        
        st.write(f"Calculate: {st.session_state.game_question['num1']} {st.session_state.game_question['operation']} {st.session_state.game_question['num2']}")
        
        answer = st.number_input("Your answer:", key="game_answer")
        
        if st.button("Submit"):
            correct_answer = eval(f"{st.session_state.game_question['num1']} {st.session_state.game_question['operation']} {st.session_state.game_question['num2']}")
            if answer == correct_answer:
                st.session_state.game_score += 1
                st.success("Correct! 🎉")
            else:
                st.error(f"Wrong! The correct answer was: {correct_answer}")
            
            st.session_state.game_question = {
                'num1': random.randint(10, 100),
                'num2': random.randint(10, 100),
                'operation': random.choice(['+', '-', '*'])
            }
            st.rerun()
        
        st.sidebar.markdown(f"### Game Score: {st.session_state.game_score}")

# Results page
elif selected == "Results":
    st.markdown("<h1 style='color: #FF4081; text-align: center;'>Your Performance Analysis</h1>", unsafe_allow_html=True)
    
    # Add results page image - Data visualization
    st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", width=800)
    
    if st.session_state.quiz_completed:
        # Create multiple charts
        col1, col2 = st.columns(2)
        
        with col1:
            # Gauge chart
            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=st.session_state.score,
                title={'text': "Quiz Score"},
                domain={'x': [0, 1], 'y': [0, 1]},
                gauge={'axis': {'range': [0, len(questions)]},
                      'bar': {'color': "darkblue"},
                      'steps': [{'range': [0, len(questions)], 'color': "lightgray"}],
                      'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': st.session_state.score}}
            ))
            st.plotly_chart(fig_gauge, use_container_width=True)
        
        with col2:
            # Pie chart
            fig_pie = px.pie(
                values=[st.session_state.score, len(questions) - st.session_state.score],
                names=['Correct', 'Incorrect'],
                title='Score Distribution'
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        
        # Performance insights
        st.markdown("### Performance Insights")
        percentage = (st.session_state.score/len(questions))*100
        
        if percentage >= 80:
            st.success("Excellent! You have a strong understanding of personal finance! 🌟")
        elif percentage >= 60:
            st.info("Good job! You have a solid foundation in personal finance. Keep learning! 📚")
        else:
            st.warning("Keep practicing! There's always room to improve your financial knowledge. 💪")
        
        # Additional statistics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Quiz Score", f"{st.session_state.score}/{len(questions)}")
        with col2:
            st.metric("Game Score", st.session_state.game_score)
        with col3:
            st.metric("Success Rate", f"{percentage:.1f}%")
    else:
        st.warning("Please complete the quiz first to see your results!")

# Leaderboard page
elif selected == "Leaderboard":
    st.markdown("<h1 style='color: #FF4081; text-align: center;'>🏆 Global Leaderboard</h1>", unsafe_allow_html=True)
    
    # Add leaderboard page image - Achievement and competition
    st.image("https://images.unsplash.com/photo-1567427017947-545c5f8d16ad?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", width=800)
    
    # Sort leaderboard by score
    sorted_leaderboard = sorted(st.session_state.leaderboard, key=lambda x: x['score'], reverse=True)
    
    # Create a DataFrame for better display
    df = pd.DataFrame(sorted_leaderboard)
    
    # Display leaderboard with enhanced styling
    st.markdown("""
        <div class="leaderboard-container">
            <h3 style='color: #D81B60;'>🌟 Top Performers</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Display all players with special styling
    if not df.empty:
        for i, row in df.iterrows():
            medal = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else "⭐"
            
            st.markdown(f"""
                <div class="leaderboard-item" style="background: linear-gradient(135deg, #ffffff, #f8f9fa); padding: 15px; border-radius: 10px; margin: 10px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: all 0.3s ease;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="flex-grow: 1;">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <h4 style="margin: 0; color: #FF4081; font-size: 1.2em; font-weight: 600;">{medal} {row['name']}</h4>
                                <span style="font-weight: bold; color: #D81B60;">Score: {row['score']}/10</span>
                            </div>
                            <p style="margin: 5px 0 0 0; color: #4A148C; font-size: 0.9em;">Date: {row['date']}</p>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        # Create statistics cards
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
            <div style="background: linear-gradient(135deg, #ffffff, #f8f9fa); padding: 20px; border-radius: 15px; margin-top: 20px;">
                <h3 style="color: #FF4081; margin-bottom: 20px; font-weight: 700; font-size: 24px; text-align: center;">📊 Leaderboard Statistics</h3>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
                <div style="text-align: center; background: linear-gradient(135deg, #ffffff, #f8f9fa); padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    <p style="color: #FF4081; font-size: 20px; font-weight: 600; margin-bottom: 10px;">Average Score</p>
                    <h2 style="color: #D81B60; margin: 0; font-size: 32px; font-weight: 700;">{df['score'].mean():.1f}</h2>
                    <p style="color: #4A148C; font-size: 16px; margin-top: 10px;">{df['score'].mean() - 5:.1f} from average</p>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div style="text-align: center; background: linear-gradient(135deg, #ffffff, #f8f9fa); padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    <p style="color: #FF4081; font-size: 20px; font-weight: 600; margin-bottom: 10px;">Highest Score</p>
                    <h2 style="color: #D81B60; margin: 0; font-size: 32px; font-weight: 700;">{df['score'].max()}</h2>
                    <p style="color: #4A148C; font-size: 16px; margin-top: 10px;">{df['score'].max() - df['score'].mean():.1f} from average</p>
                </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
                <div style="text-align: center; background: linear-gradient(135deg, #ffffff, #f8f9fa); padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    <p style="color: #FF4081; font-size: 20px; font-weight: 600; margin-bottom: 10px;">Total Players</p>
                    <h2 style="color: #D81B60; margin: 0; font-size: 32px; font-weight: 700;">{len(df)}</h2>
                    <p style="color: #4A148C; font-size: 16px; margin-top: 10px;">Active participants</p>
                </div>
            """, unsafe_allow_html=True)
        
        # Add charts
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        with col1:
            # Bar chart of top scores with improved styling
            fig_bar = px.bar(
                df.head(10),
                x='name',
                y='score',
                title='Top 10 Scores',
                color='score',
                color_continuous_scale=['#FF4081', '#E91E63', '#D81B60', '#C2185B', '#880E4F'],
                labels={'name': 'Player', 'score': 'Score'}
            )
            fig_bar.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                showlegend=False,
                title_x=0.5,
                title_font_size=20,
                title_font_color='#D81B60',
                xaxis_title_font_size=14,
                yaxis_title_font_size=14,
                xaxis=dict(
                    tickfont=dict(color='#4A148C'),
                    title_font=dict(color='#4A148C')
                ),
                yaxis=dict(
                    tickfont=dict(color='#4A148C'),
                    title_font=dict(color='#4A148C')
                )
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        
        with col2:
            # Line chart showing score trends with improved styling
            df['date'] = pd.to_datetime(df['date'])
            fig_line = px.line(
                df,
                x='date',
                y='score',
                title='Score Trends Over Time',
                markers=True,
                labels={'date': 'Date', 'score': 'Score'}
            )
            fig_line.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                title_x=0.5,
                title_font_size=20,
                title_font_color='#D81B60',
                xaxis_title_font_size=14,
                yaxis_title_font_size=14,
                xaxis=dict(
                    tickfont=dict(color='#4A148C'),
                    title_font=dict(color='#4A148C')
                ),
                yaxis=dict(
                    tickfont=dict(color='#4A148C'),
                    title_font=dict(color='#4A148C')
                )
            )
            fig_line.update_traces(
                line_color='#FF4081',
                marker=dict(color='#D81B60')
            )
            st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.info("No players have completed the quiz yet. Be the first to take the challenge! 🎯")

# Insights page
elif selected == "Insights":
    st.markdown("<h1 style='color: #FF4081; text-align: center;'>💡 Financial Insights</h1>", unsafe_allow_html=True)
    
    # Add insights page image - Financial planning
    st.image("https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", width=800)
    
    # Create tabs for different insights
    tab1, tab2, tab3 = st.tabs(["Budgeting Tips", "Investment Strategies", "Debt Management"])
    
    with tab1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ffffff, #f8f9fa); padding: 20px; border-radius: 15px; margin: 20px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style='color: #FF1493; font-size: 28px; font-weight: 700; margin-bottom: 15px; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);'>Smart Budgeting Tips</h3>
            <ul style='color: #000000; font-size: 20px; font-weight: 500; line-height: 1.8;'>
                <li>Track your expenses daily</li>
                <li>Use the 50/30/20 rule</li>
                <li>Set up automatic savings</li>
                <li>Review and adjust monthly</li>
                <li>Use budgeting apps</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Add a budget calculator
        st.markdown("<h3 style='color: #FF1493; font-size: 28px; font-weight: 700; margin: 20px 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);'>Budget Calculator</h3>", unsafe_allow_html=True)
        income = st.number_input("Monthly Income:", min_value=0.0)
        if income > 0:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(f"""
                    <div style="text-align: center; background: linear-gradient(135deg, #ffffff, #f8f9fa); padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                        <p style="color: #FF1493; font-size: 22px; font-weight: 600; margin-bottom: 10px;">Needs (50%)</p>
                        <h3 style="color: #000000; margin: 0; font-size: 26px; font-weight: 700;">${income * 0.5:.2f}</h3>
                    </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown(f"""
                    <div style="text-align: center; background: linear-gradient(135deg, #ffffff, #f8f9fa); padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                        <p style="color: #FF1493; font-size: 22px; font-weight: 600; margin-bottom: 10px;">Wants (30%)</p>
                        <h3 style="color: #000000; margin: 0; font-size: 26px; font-weight: 700;">${income * 0.3:.2f}</h3>
                    </div>
                """, unsafe_allow_html=True)
            with col3:
                st.markdown(f"""
                    <div style="text-align: center; background: linear-gradient(135deg, #ffffff, #f8f9fa); padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                        <p style="color: #FF1493; font-size: 22px; font-weight: 600; margin-bottom: 10px;">Savings (20%)</p>
                        <h3 style="color: #000000; margin: 0; font-size: 26px; font-weight: 700;">${income * 0.2:.2f}</h3>
                    </div>
                """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ffffff, #f8f9fa); padding: 20px; border-radius: 15px; margin: 20px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style='color: #FF1493; font-size: 28px; font-weight: 700; margin-bottom: 15px; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);'>Investment Strategies</h3>
            <ul style='color: #000000; font-size: 20px; font-weight: 500; line-height: 1.8;'>
                <li>Start early and invest regularly</li>
                <li>Diversify your portfolio</li>
                <li>Consider index funds</li>
                <li>Stay informed about market trends</li>
                <li>Review and rebalance annually</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Add an investment calculator
        st.markdown("<h3 style='color: #FF1493; font-size: 28px; font-weight: 700; margin: 20px 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);'>Investment Growth Calculator</h3>", unsafe_allow_html=True)
        initial_investment = st.number_input("Initial Investment:", min_value=0.0)
        monthly_contribution = st.number_input("Monthly Contribution:", min_value=0.0)
        years = st.slider("Investment Period (Years):", 1, 40, 10)
        interest_rate = st.slider("Expected Annual Return (%):", 1.0, 15.0, 7.0, 0.1)
        
        if initial_investment > 0:
            future_value = initial_investment * (1 + interest_rate/100) ** years
            st.markdown(f"""
                <div style="text-align: center; background: linear-gradient(135deg, #ffffff, #f8f9fa); padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-top: 20px;">
                    <p style="color: #FF1493; font-size: 22px; font-weight: 600; margin-bottom: 10px;">Future Value</p>
                    <h2 style="color: #000000; margin: 0; font-size: 32px; font-weight: 700;">${future_value:,.2f}</h2>
                </div>
            """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ffffff, #f8f9fa); padding: 20px; border-radius: 15px; margin: 20px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style='color: #FF1493; font-size: 28px; font-weight: 700; margin-bottom: 15px; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);'>Debt Management Tips</h3>
            <ul style='color: #000000; font-size: 20px; font-weight: 500; line-height: 1.8;'>
                <li>Create a debt repayment plan</li>
                <li>Pay more than minimum payments</li>
                <li>Consider debt consolidation</li>
                <li>Build an emergency fund</li>
                <li>Seek professional advice when needed</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Add a debt calculator
        st.markdown("<h3 style='color: #FF1493; font-size: 28px; font-weight: 700; margin: 20px 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);'>Debt Repayment Calculator</h3>", unsafe_allow_html=True)
        debt_amount = st.number_input("Total Debt:", min_value=0.0)
        interest_rate = st.number_input("Interest Rate (%):", min_value=0.0)
        monthly_payment = st.number_input("Monthly Payment:", min_value=0.0)
        
        if debt_amount > 0 and monthly_payment > 0:
            monthly_rate = interest_rate / 12 / 100
            if monthly_rate > 0:
                months = -np.log(1 - (monthly_payment / (debt_amount * monthly_rate))) / np.log(1 + monthly_rate)
                st.markdown(f"""
                    <div style="text-align: center; background: linear-gradient(135deg, #ffffff, #f8f9fa); padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-top: 20px;">
                        <p style="color: #FF1493; font-size: 22px; font-weight: 600; margin-bottom: 10px;">Months to Pay Off</p>
                        <h2 style="color: #000000; margin: 0; font-size: 32px; font-weight: 700;">{months:.1f}</h2>
                    </div>
                """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer" style="color: white !important;">
        <p>Created with ❤️ for financial education | © 2024 Finance Quiz App</p>
    </div>
""", unsafe_allow_html=True) 