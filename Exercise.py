import streamlit as st
import pickle

# Load the saved model
with open('final_model.sav', 'rb') as file:
    model = pickle.load(file)

# Define a function to calculate calories
def calculate_calories(height, age, weight):
    # Perform necessary calculations using the model
    # Replace this with your actual calculations based on your model
    # Example:
    calories = model.predict([[height, age, weight]])
    return calories

# Define a function to suggest exercises based on exercise intensity
def suggest_exercises(exercise_intensity):
    # Perform necessary calculations or look up a database of exercises
    # based on the exercise intensity
    # Example:
    if exercise_intensity == 'Low':
        exercises = ['Walking', 'Yoga', 'Swimming']
    elif exercise_intensity == 'Moderate':
        exercises = ['Cycling', 'Pilates', 'Light weight training']
    else:
        exercises = ['Aerobics', 'Dancing', 'Squats']
    return exercises

# Main function to create the Streamlit app
def main():
    st.title('PCOS Exercise Recommendation')
    
    # User input section
    height = st.slider('Enter your height (cm)', 100, 250, 150)
    age = st.slider('Enter your age', 10, 100, 25)
    weight = st.slider('Enter your weight (kg)', 30, 200, 60)
    
    # Calculate calories
    calories = calculate_calories(height, age, weight)
    st.write(f'Calories burned per day: {calories}')
    
    # Determine exercise intensity based on calories
    if calories < 1500:
        exercise_intensity = 'Low'
    elif 1500 <= calories < 2500:
        exercise_intensity = 'Moderate'
    else:
        exercise_intensity = 'High'
    
    st.write(f'Exercise Intensity: {exercise_intensity}')
    
    # Suggest exercises based on exercise intensity
    exercises = suggest_exercises(exercise_intensity)
    
    st.write('Recommended exercises:')
    for exercise in exercises:
        st.write(exercise)

# Run the app
if __name__ == '__main__':
    main()