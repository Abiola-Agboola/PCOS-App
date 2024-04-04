import streamlit as st
import pickle
import pandas as pd
import os

# Add navigation links to the four pages
st.title("")
st.markdown("[Home](https://pcos-app-home.streamlit.app/)")
st.markdown("[Exercise Page](https://pcos-app-pcos-exercise.streamlit.app/)")
st.markdown("[PCOS Predictor](https://pcos-app-pcos-predictor.streamlit.app/)")

# Load the data and model
exercise_data = pd.read_csv('cleaned_features.csv', encoding='ISO-8859-1')
model_file = 'exercise_model.sav'
scaler_file = 'scaledexer.pkl'

if os.path.exists(model_file):
    with open(model_file, 'rb') as file:
        model = pickle.load(file)
else:
    st.error(f"Model file '{model_file}' not found. Please upload the model file.")

if os.path.exists(scaler_file):
    with open(scaler_file, 'rb') as file:
        scaler = pickle.load(file)
else:
    st.error(f"Scaler file '{scaler_file}' not found. Please upload the scaler file.")

# Function to categorize BMI
def categorize_bmi(BMI):
    if BMI < 18.5:
        return 'Underweight'
    elif 18.5 <= BMI < 25:
        return 'Normal'
    elif 25 <= BMI < 30:
        return 'Overweight'
    else:
        return 'Obese'

        return 'Intense' if BMI >= 30 else 'Light'

# Function to recommend lightweight exercises based on BMI
def recommend_exercises(BMI):
    if BMI < 18.5:
        return ["Yoga", "Pilates", "Stretching"]
    elif 18.5 <= BMI < 25:
        return ["Walking", "Cycling", "Swimming"]
    else:
        return ["Water Aerobics", "Elliptical Training", "Dancing"]

# Function to display exercise instructions
def display_exercise_instructions(exercise):
    instructions = {
        "Yoga": "https://www.bing.com/videos/riverview/relatedvideo?q=PCOS+patient+cycling+exercise+on+you+tube&&view=riverview&mmscn=mtsc&mid=B7BF90BE7113A697E45BB7BF90BE7113A697E45B&&aps=0&FORM=VMSOVR",
        "Pilates": "https://www.bing.com/videos/riverview/relatedvideo?&q=pilates+exercise+on+you+tube&&mid=AE6B3A58EE85A0CCBB8BAE6B3A58EE85A0CCBB8B&&FORM=VRDGAR",
        "Stretching": "https://www.bing.com/videos/riverview/relatedvideo?&q=Stretching+exercise+on+you+tube&&mid=5B6A56849BB02AA23B935B6A56849BB02AA23B93&&FORM=VRDGAR",
        "Walking": "https://www.bing.com/videos/riverview/relatedvideo?&q=PCOS+patient+walking+exercise+on+you+tube&&mid=E40FE169CC8F07127BD9E40FE169CC8F07127BD9&&FORM=VRDGAR",
        "Cycling": "https://www.bing.com/videos/riverview/relatedvideo?q=PCOS+patient+cycling+exercise+on+you+tube&&view=riverview&mmscn=mtsc&mid=1103F357AA3E17DB50601103F357AA3E17DB5060&&aps=11&FORM=VMSOVR",
        "Swimming": "https://www.bing.com/videos/riverview/relatedvideo?q=swimming%20exercise%20on%20you%20tube&mid=FFAC85F42AD9078892C1FFAC85F42AD9078892C1&ajaxhist=0",
        "Water Aerobics": "https://www.bing.com/videos/riverview/relatedvideo?q=Water+Aerobics+exercise+for+PCOS+patient+on+you+tube&&view=riverview&mmscn=mtsc&mid=C92BC62E2001BF52DFF6C92BC62E2001BF52DFF6&&aps=11&FORM=VMSOVR",
        "Elliptical Training": "https://www.bing.com/videos/riverview/relatedvideo?&q=Elliptical+Training+exercise+for+PCOS+patient+on+you+tube&&mid=63F99E10ED8907AB4E9563F99E10ED8907AB4E95&&FORM=GVRPTV",
        "Dancing": "https://www.bing.com/videos/riverview/relatedvideo?&q=dancing+exercise&&mid=88AC333CB71118A7542E88AC333CB71118A7542E&&FORM=VRDGAR",
        "Tai Chi": "https://www.bing.com/videos/riverview/relatedvideo?&q=+Tai+Chi+exercise+for+PCOS+&&mid=900CF16B2B69C4B3A4A2900CF16B2B69C4B3A4A2&&FORM=VRDGAR",
        "Chair Yoga": "https://www.youtube.com/watch?v=-rBDxFKJtlE",
        "Resistance Band Training": "https://www.bing.com/videos/riverview/relatedvideo?q=Resistance+Band+Training+exercise+for+PCOS+patient+on+you+tube&&view=riverview&mmscn=mtsc&mid=626E244C4C0E859517AB626E244C4C0E859517AB&&aps=0&FORM=VMSOVR"
    }
    return st.markdown(f"[{exercise}]({instructions.get(exercise, '')})")

# Define the main function to create the app
def main():
    st.title("Device Readings")
    
    # Define a list of BMI values
    bmi_values = [i / 10 for i in range(100, 501)]  # BMI values from 10.0 to 50.0
    
    # Get user's BMI
    BMI = st.selectbox("Select your BMI:", bmi_values, index=10)  # Default index for 20.0 BMI
    
    # Calculate BMI category and exercise intensity
    bmi_category = categorize_bmi(BMI)
    
    # Recommend exercises
    exercises = recommend_exercises(BMI)
    
    # Display BMI category and exercise intensity
    st.write(f"**BMI Category:** {bmi_category}")
    
    # Define three columns for Health, Nutrition, and Fitness feedback
    #col1, col2, col3 = st.columns(3)
    
     #Display the content for health, nutrition, and fitness columns with different column widths
    col1, _, col2, col3 = st.columns([4, 0.1, 2.2, 2])  # Adjust the widths as needed
    
    # Health feedback
    with col1:
        st.subheader("Health")
        if bmi_category == "Underweight":
            st.write("For underweight individuals, adopting healthy lifestyle habits can help improve overall health and well-being. Here are some guidelines:")
            st.write("- Eat frequent, nutrient-rich meals and snacks throughout the day to increase calorie intake")
            st.write("- Choose foods that are high in protein, healthy fats, and complex carbohydrates")
            st.write("- Incorporate strength training exercises into your workout routine to build muscle mass")
            st.write("- Get adequate rest and prioritize quality sleep to support muscle recovery and overall health")
        elif bmi_category == "Normal":
            st.write("Maintaining a healthy lifestyle is important for individuals with a normal BMI to prevent future health problems. Consider these guidelines:")
            st.write("- Eat a balanced diet consisting of a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats")
            st.write("- Engage in regular physical activity such as walking, jogging, or cycling for at least 30 minutes most days of the week")
            st.write("- Practice stress-reducing techniques like meditation, deep breathing exercises, or yoga to promote mental well-being")
            st.write("- Limit alcohol consumption and avoid smoking to reduce the risk of chronic diseases")
        elif bmi_category in ["Overweight", "Obese"]:
            st.write("For individuals who are overweight or obese, making positive lifestyle changes is key to achieving and maintaining a healthy weight. Here are some recommendations:")
            st.write("- Focus on portion control and mindful eating to reduce calorie intake and promote weight loss")
            st.write("- Increase physical activity levels by incorporating aerobic exercises such as brisk walking, swimming, or cycling into your daily routine")
            st.write("- Aim for gradual, sustainable weight loss by setting realistic goals and making small changes to your diet and exercise habits")
            st.write("- Seek support from friends, family, or a health professional to stay motivated and accountable on your weight loss journey")
    
    # Nutrition feedback
    with col2:
        st.subheader("Nutrition")
        if bmi_category == "Underweight":
            st.write("In addition to regular meals, consider adding high-calorie, nutrient-dense foods to your diet, such as:")
            st.write("- Whole milk")
            st.write("- Cheese")
            st.write("- Nuts and seeds")
            st.write("- Nut butters")
            st.write("- Dried fruits")
            st.write("- Granola and trail mix")
        elif bmi_category == "Normal":
            st.write("Aim for a balanced diet with a variety of foods from all food groups. Consider the following tips:")
            st.write("- Choose whole grains over refined grains")
            st.write("- Include plenty of fruits and vegetables in your meals")
            st.write("- Opt for lean sources of protein")
            st.write("- Limit added sugars and unhealthy fats")
        elif bmi_category in ["Overweight", "Obese"]:
            st.write("To support weight loss efforts, focus on filling your plate with nutrient-dense foods while reducing calorie-dense options. Some examples include:")
            st.write("- Leafy greens and other non-starchy vegetables")
            st.write("- Lean proteins such as poultry, fish, and tofu")
            st.write("- Whole grains like quinoa, brown rice, and oats")
            st.write("- Fruits in moderation")
            st.write("- Low-fat or non-fat dairy products")

    # Fitness feedback
    with col3:
        st.subheader("Fitness")
        st.write("For this individual, engaging in exercises below can be beneficial.")
        for exercise in exercises:
            display_exercise_instructions(exercise)
        if bmi_category == "Underweight":
            st.write("Exercise Intensity: Light")
            
        elif bmi_category == "Normal":
            st.write("Exercise Intensity: Moderate")
            
        elif bmi_category in ["Overweight", "Obese"]:
            st.write("Exercise Intensity: Intense")
    
if __name__ == "__main__":
    main()
