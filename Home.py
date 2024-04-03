import streamlit as st
import pickle
from PIL import Image
from datetime import datetime, time
import pandas as pd

# Load the trained model and data
data = pd.read_csv('updated_nutri.csv', encoding='ISO-8859-1')

# Define the main definition link
main_definition_link = "https://www.who.int/news-room/fact-sheets/detail/polycystic-ovary-syndrome"
About_PCOS_link = "https://www.nhs.uk/conditions/polycystic-ovary-syndrome-pcos/"
PCOS_NutritionPlan_link = "https://www.healthline.com/health/pcos-diet"
Mood_link = "https://www.fertilityfamily.co.uk/blog/pcos-and-mood-swings-how-does-pcos-affect-your-mood/"

# Define a session state to keep track of the current page
class SessionState:
    def __init__(self):
        self.page = "Home"

# Create an instance of the session state
session_state = SessionState()

# Define functions for each page
def home_page():
    st.title("Home")

    # Open the first image
    image1 = Image.open("PCOS img.png")

    # Open the second image
    image2 = Image.open("Abt PCOS.png")

    # Display the images side by side
    col1, _, col2 = st.columns([1, 0.3, 1])  # Add a column of width 0.1 for spacing

    # Display the first image and markdown
    with col1:
        st.image(image1, width=400)
        # Create a hyperlink for "About PCOS" in the second column
        st.markdown(f"[PCOS]({main_definition_link})", unsafe_allow_html=True)

    # Display the second image and markdown
    with col2:
        # Create a hyperlink for "About PCOS" in the second column
        st.image(image2, width=286)
        st.markdown(f"[About PCOS]({About_PCOS_link})", unsafe_allow_html=True)

    st.write("This homepage is dedicated to supporting individuals with Polycystic Ovary Syndrome (PCOS). It serves as a welcoming gateway to resources, information, and assistance tailored to the unique needs of PCOS patients. The goal is to provide a supportive and informative environment for those navigating the challenges of PCOS.")

# Define the paths to the saved models
MOOD_MODEL_PATH = 'mood_model.sav'
NUTRI_MODEL_PATH = 'nutri_model.sav'

def load_models():
    with open(MOOD_MODEL_PATH, 'rb') as mood_file:
        mood_model = pickle.load(mood_file)

    with open(NUTRI_MODEL_PATH, 'rb') as nutri_file:
        nutri_modl = pickle.load(nutri_file)
    
    return mood_model, nutri_modl


def Nutrition_Recommendation(mood_weight, data):
    recommendations = []  # Initialize an empty list to store recommendations
    if mood_weight in [1, 2, 3]:  # Check if mood_weight is 1, 2, or 3
        filtered_data = data[data["Mood_Weight"] == mood_weight]  # Assuming "Mood_Weight" is the correct column name
        if "Category" in filtered_data.columns:  # Check if the column "categories" exists
            unique_categories = set(filtered_data["Category"].tolist())
            recommendations = {interpret_recommendation(category) for category in unique_categories}
        else:
            st.error("The column 'Category' does not exist in the data.")
    else:
        st.error("Invalid mood_weight. Please provide a valid value (1, 2, or 3).")
    
    return recommendations
# Define basic nutrition recommendations based on mood
    nutrition_dict = {
        "Happy": "Include more fruits, vegetables, and whole grains in your diet. Stay hydrated!",
        "Sad": "Focus on comfort foods, but also ensure a balanced intake of nutrients.",
        "In Between": "Maintain a well-balanced diet with a mix of proteins, carbs, and fats."
    }

    # Return the nutrition recommendation for the given mood
    return nutrition_dict.get(mood, "Nutrition recommendation not available.")


def interpret_recommendation(value):
    # Define a mapping of numerical categories to words
    category_mapping = {
        0: "Dairy Products",
        1: "Dessert Sweets",
        2: "Drinks",
        3: "Fat food",
        4: "Meat",
        5: "Poultry",
        6: "Seeds and Nuts",
        7: "Vegetable"
    }
    # Return the corresponding word for the numerical category
    return category_mapping.get(value, "Unknown Recommendation")

def interpret_recommendation(value):
    if value == 0:
        return "Dairy Products"
    elif value == 1:
        return "Dessert Sweets"
    elif value == 2:
        return "Drinks"
    elif value == 3:
        return "Fat food"
    elif value == 4:
        return "Meat"
    elif value == 5:
        return "Poultry"
    elif value == 6:
        return "Seeds and Nuts"
    elif value == 7:
        return "Vegetable"
    else:
        return "Unknown Recommendation"

# Function to display the nutrition recommendation page
def nutrimood_page():
    st.title("Nutrition & Mood")
    st.write("This focuses on optimizing nutrition to positively impact the mood of individuals with Polycystic Ovary Syndrome (PCOS). It involves tailored dietary approaches, identifying nutritional deficiencies, and understanding how specific nutrients influence mood in PCOS patients. The aim is to enhance overall well-being through targeted nutritional strategies.")

    # Display the images side by side
    nutri, _, mood = st.columns([1, 0.3, 1])  # Add a column of width 0.1 for spacing

    # Display the first image and markdown
    with nutri:
        st.image("PCOS nutri.png", width=300)
        # Display the hyperlinks one below the other
        st.markdown(f"[Nutrition Plan]({PCOS_NutritionPlan_link})", unsafe_allow_html=True)

    # Display the second image and markdown
    with mood:
        st.image("PCOS Mood.png", width=350)
        # Display the hyperlinks one below the other
        st.markdown(f"[Mood]({Mood_link})", unsafe_allow_html=True)
       

    # Get user input for mood
    st.header("Mood")
    mood = st.selectbox("How do you feel today?", ["Sad", "In Between", "Happy"])

    # Convert mood to Mood_Weight
    mood_mapping = {"Sad": 1, "In Between": 2, "Happy": 3}
    Mood_Weight = mood_mapping.get(mood, None)

    if Mood_Weight:
        # Display nutrition recommendation based on mood
        recommendation = Nutrition_Recommendation(Mood_Weight, data)
        st.header("Nutrition Recommendation")
        st.write(recommendation)
        
        # Display encouragement based on mood
        st.header("Encouragement")
        if mood == "Sad":
            st.write("It's okay to feel down sometimes. Remember to take care of yourself, stay hydrated and prioritize your well-being.")
        elif mood == "Happy":
            st.write("Great job! Keep up the positive energy and continue to nourish your body with healthy foods.")
        else:
            st.write("Stay balanced, hydrated and focused. You're doing great!")

# Load the saved models
mood_model, nutri_modl = load_models()

def flexible_time_page():
    st.title("Flexible Working Time")
    st.write("Consideration for flexible working time is crucial for individuals with PCOS. Understanding and accommodating their unique needs can contribute to a more supportive work environment.")
    
    # Get user input for flexible working time
    session_state.flexible_time = st.selectbox("Select Flexible Working Time", ["Full-time", "Part-time", "Flexible Hours"])
    
    st.title("Book Availability")
    
    # Get user input for working hours
    working_hours = st.time_input("Select Working Hours:", time(9, 0))  # Default to 9:00 AM
    
    # Display selected working hours
    st.write("Selected Working Hours:", working_hours)
    
    # Display the calendar
    selected_dates = st.date_input("Select dates for availability:", [datetime.now()])
    
    # Update the availability dates in the session state
    session_state.availability_dates = selected_dates

    # Display the selected dates
    st.write("Selected Dates:", session_state.availability_dates)
    
# Create the Streamlit app
def main():
    st.sidebar.title("Navigation")
    pages = ["Home", "Nutrition & Mood", "Working Time"]
    selected_page = st.sidebar.radio("Go to", pages, index=pages.index(session_state.page))

    # Update the current page in the session state
    session_state.page = selected_page

    # Render the selected page
    if selected_page == "Home":
        home_page()
    elif selected_page == "Nutrition & Mood":
        nutrimood_page()
    elif selected_page == "Working Time":
        flexible_time_page()


if __name__ == "__main__":
    main()
