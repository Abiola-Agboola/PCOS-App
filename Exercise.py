import streamlit as st
import pickle
import pandas as pd
import os  # Add this line to import the os module

exercise_data = pd.read_csv('cleaned_features.csv')
# Define a session state to keep track of the current page
class SessionState:
    def __init__(self):
        self.page = "Lightweight Exercise"

# Create an instance of the session state
session_state = SessionState()

# Declare all necessary features
features = [('Weight (Kg)', 'weight'), ('Height(Cm)', 'height'), ('Age (yrs)', 'age'),  ('Cycle(R/I)', 'cycle'), ('hair growth(Y/N)', 'hair_growth'), ('BMI', 'BMI')]

# Load the trained model
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

# Function to calculate BMI
def calculate_bmi(weight, height):
    height_m = height / 100
    return weight / (height_m ** 2)

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

# Function to determine exercise intensity based on BMI
def determine_exercise_intensity(BMI):
    if BMI < 18.5:  # Underweight
        return 'Light'
    elif 18.5 <= BMI < 25:  # Normal weight
        return 'Moderate'
    elif 25 <= BMI < 30:  # Overweight
        return 'Intense'
    else:  # Obese
        return 'Intense'

# Function to recommend lightweight exercises based on BMI
def recommend_lightweight_exercise(BMI):
    if BMI < 18.5:  # Underweight
        if BMI < 18.0:
            return "Yoga"
        elif BMI < 18.3:
            return "Pilates"
        else:
            return "Stretching"
    elif 18.5 <= BMI < 25:  # Normal weight
        if BMI < 20.0:
            return "Walking"
        elif BMI < 21.5:
            return "Cycling"
        else:
            return "Swimming"
    elif 25 <= BMI < 30:  # Overweight
        if BMI < 27.0:
            return "Water Aerobics"
        elif BMI < 28.5:
            return "Elliptical Training"
        else:
            return "Dancing"
    else:  # Obese
        if BMI < 35.0:
            return "Tai Chi"
        elif BMI < 38.0:
            return "Chair Yoga"
        else:
            return "Resistance Band Training"

        # Function to display exercise instructions
def display_exercise_instructions(exercise):
    if exercise == "Yoga":
        return st.markdown("[Yoga Exercise](https://www.bing.com/videos/riverview/relatedvideo?q=PCOS+patient+cycling+exercise+on+you+tube&&view=riverview&mmscn=mtsc&mid=B7BF90BE7113A697E45BB7BF90BE7113A697E45B&&aps=0&FORM=VMSOVR)")
    elif exercise == "Pilates":
        return st.markdown("[Pilates Exercise](https://www.bing.com/videos/riverview/relatedvideo?&q=pilates+exercise+on+you+tube&&mid=AE6B3A58EE85A0CCBB8BAE6B3A58EE85A0CCBB8B&&FORM=VRDGAR)")
    elif exercise == "Stretching":
        return st.markdown("[Stretching Exercise](https://www.bing.com/videos/riverview/relatedvideo?&q=Stretching+exercise+on+you+tube&&mid=5B6A56849BB02AA23B935B6A56849BB02AA23B93&&FORM=VRDGAR)")
    elif exercise == "Walking":
        return st.markdown("[Walking Exercise](https://www.bing.com/videos/riverview/relatedvideo?&q=PCOS+patient+walking+exercise+on+you+tube&&mid=E40FE169CC8F07127BD9E40FE169CC8F07127BD9&&FORM=VRDGAR)")
    elif exercise == "Cycling":
        return st.markdown("[Cycling Exercise](https://www.bing.com/videos/riverview/relatedvideo?q=PCOS+patient+cycling+exercise+on+you+tube&&view=riverview&mmscn=mtsc&mid=1103F357AA3E17DB50601103F357AA3E17DB5060&&aps=11&FORM=VMSOVR)")
    elif exercise == "Swimming":
        return st.markdown("[Swimming Exercise](https://www.bing.com/videos/riverview/relatedvideo?q=swimming%20exercise%20on%20you%20tube&mid=FFAC85F42AD9078892C1FFAC85F42AD9078892C1&ajaxhist=0)")
    elif exercise == "Water Aerobics":
        return st.markdown("[Water Aerobics Exercise](https://www.bing.com/videos/riverview/relatedvideo?q=Water+Aerobics+exercise+for+PCOS+patient+on+you+tube&&view=riverview&mmscn=mtsc&mid=C92BC62E2001BF52DFF6C92BC62E2001BF52DFF6&&aps=11&FORM=VMSOVR)")
    elif exercise == "Elliptical Training":
        return st.markdown("[Elliptical Training](https://www.bing.com/videos/riverview/relatedvideo?&q=Elliptical+Training+exercise+for+PCOS+patient+on+you+tube&&mid=63F99E10ED8907AB4E9563F99E10ED8907AB4E95&&FORM=GVRPTV)")
    elif exercise == "Dancing":
        return st.markdown("[Dancing Exercise](https://www.bing.com/videos/riverview/relatedvideo?&q=dancing+exercise&&mid=88AC333CB71118A7542E88AC333CB71118A7542E&&FORM=VRDGAR)")
    elif exercise == "Tai Chi":
        return st.markdown("[Tai Chi Exercise](https://www.bing.com/videos/riverview/relatedvideo?&q=+Tai+Chi+exercise+for+PCOS+&&mid=900CF16B2B69C4B3A4A2900CF16B2B69C4B3A4A2&&FORM=VRDGAR)")
    elif exercise == "Chair Yoga":
        return st.markdown("[Chair Yoga Exercise](https://www.youtube.com/watch?v=-rBDxFKJtlE)")
    elif exercise == "Resistance Band Training":
        return st.markdown("[Resistance Band Training](https://www.bing.com/videos/riverview/relatedvideo?q=Resistance+Band+Training+exercise+for+PCOS+patient+on+you+tube&&view=riverview&mmscn=mtsc&mid=626E244C4C0E859517AB626E244C4C0E859517AB&&aps=0&FORM=VMSOVR)")

# Function to display the Yoga page
def Yoga_page():
    st.title("Yoga")
    st.markdown("[Yoga Exercise Instructions](https://www.bing.com/videos/riverview/relatedvideo?q=PCOS+patient+cycling+exercise+on+you+tube&&view=riverview&mmscn=mtsc&mid=B7BF90BE7113A697E45BB7BF90BE7113A697E45B&&aps=0&FORM=VMSOVR)")
    st.write("Here are the steps to perform Yoga:")
    st.write("- Step 1: Find a quiet space.")
    st.write("- Step 2: Roll out your yoga mat.")
    st.write("- Step 3: Start with breathing exercises (pranayama).")
    st.write("- Step 4: Begin with a gentle warm-up, such as neck rolls and shoulder shrugs.")
    st.write("- Step 5: Move into standing poses like Mountain Pose (Tadasana) and Forward Bend (Uttanasana).")
    st.write("- Step 6: Transition to seated poses like Seated Forward Bend (Paschimottanasana) and Butterfly Pose (Baddha Konasana).")
    st.write("- Step 7: Include balancing poses such as Tree Pose (Vrksasana) and Eagle Pose (Garudasana).")
    st.write("- Step 8: Practice backbends like Cobra Pose (Bhujangasana) and Bridge Pose (Setu Bandhasana).")
    st.write("- Step 9: Perform inversions like Downward-Facing Dog (Adho Mukha Svanasana) and Shoulder Stand (Sarvangasana).")
    st.write("- Step 10: Conclude your practice with relaxation poses such as Corpse Pose (Savasana) and Seated Meditation.")
    st.write("- Step 11: Take a moment to reflect on your practice and express gratitude for your body and mind.")
    st.write("- Step 12: Hydrate yourself and enjoy the sense of peace and well-being that comes from your yoga practice.")

# Function to display the Pilates page
def Pilates_page():
    st.title("Pilates")
    st.markdown("[Pilates Exercise Instructions](https://www.bing.com/videos/riverview/relatedvideo?&q=pilates+exercise+on+you+tube&&mid=AE6B3A58EE85A0CCBB8BAE6B3A58EE85A0CCBB8B&&FORM=VRDGAR)")
    st.write("Here are the steps to perform Pilates:")
    st.write("- Step 1: Find a comfortable surface to lie on.")
    st.write("- Step 2: Engage your core muscles.")
    st.write("- Step 3: Follow a series of controlled movements.")
    st.write("- Step 4: Start with a warm-up, focusing on breathing and gentle stretches.")
    st.write("- Step 5: Move into core-strengthening exercises like the Hundred and the Roll-Up.")
    st.write("- Step 6: Incorporate exercises that target other muscle groups, such as leg circles and side leg lifts.")
    st.write("- Step 7: Transition into exercises that challenge balance and coordination, such as the Swan Dive and the Teaser.")
    st.write("- Step 8: Pay attention to your form and alignment throughout the workout.")
    st.write("- Step 9: Include stretching exercises to improve flexibility and prevent muscle tightness.")
    st.write("- Step 10: Conclude your session with a cool-down, focusing on deep breathing and relaxation.")
    st.write("- Step 11: Reflect on your practice and any improvements in strength, flexibility, or overall well-being.")
    st.write("- Step 12: Stay hydrated and enjoy the benefits of your Pilates practice.")

# Function to display the Stretching page
def Stretching_page():
    st.title("Stretching")
    st.markdown("[Stretching Exercise Instructions](https://www.bing.com/videos/riverview/relatedvideo?&q=Stretching+exercise+on+you+tube&&mid=5B6A56849BB02AA23B935B6A56849BB02AA23B93&&FORM=VRDGAR)")
    st.write("Here are the steps to perform Stretching:")
    st.write("- Step 1: Warm up your muscles.")
    st.write("- Step 2: Hold each stretch for 15-30 seconds.")
    st.write("- Step 3: Breathe deeply and slowly.")
    st.write("- Step 4: Focus on the muscle groups you want to stretch.")
    st.write("- Step 5: Stretch slowly and gently, avoiding any sudden movements.")
    st.write("- Step 6: Relax into each stretch, feeling the tension release.")
    st.write("- Step 7: Listen to your body and avoid overstretching or causing pain.")
    st.write("- Step 8: Incorporate a variety of stretches for different muscle groups.")
    st.write("- Step 9: Include dynamic stretches to improve flexibility and range of motion.")
    st.write("- Step 10: Stretch both sides of your body evenly to maintain balance.")
    st.write("- Step 11: Pay attention to your posture and alignment during each stretch.")
    st.write("- Step 12: Conclude your stretching routine with a cooldown to relax your muscles.")

# Function to display the Walking page
def Walking_page():
    st.title("Walking")
    st.markdown("[Walking Exercise Instructions](Walking Exercise](https://www.bing.com/videos/riverview/relatedvideo?&q=PCOS+patient+walking+exercise+on+you+tube&&mid=E40FE169CC8F07127BD9E40FE169CC8F07127BD9&&FORM=VRDGAR)")
    st.write("Here are the steps to perform Walking:")
    st.write("- Step 1: Wear comfortable shoes.")
    st.write("- Step 2: Start with a brisk pace.")
    st.write("- Step 3: Swing your arms naturally.")
    st.write("- Step 4: Keep your back straight and shoulders relaxed.")
    st.write("- Step 5: Engage your core muscles for stability.")
    st.write("- Step 6: Take regular and even strides.")
    st.write("- Step 7: Land on your heels and roll through to your toes.")
    st.write("- Step 8: Maintain a steady breathing rhythm.")
    st.write("- Step 9: Keep your head up and eyes forward.")
    st.write("- Step 10: Be aware of your surroundings and any obstacles.")
    st.write("- Step 11: Stay hydrated by drinking water before, during, and after your walk.")
    st.write("- Step 12: Cool down with a slower pace and stretches after your walk.")

# Function to display the Cycling page
def Cycling_page():
    st.title("Cycling")
    st.markdown("[Cycling Exercise Instructions](https://www.bing.com/videos/riverview/relatedvideo?q=PCOS+patient+cycling+exercise+on+you+tube&&view=riverview&mmscn=mtsc&mid=1103F357AA3E17DB50601103F357AA3E17DB5060&&aps=11&FORM=VMSOVR)")
    st.write("Here are the steps to perform Cycling:")
    st.write("- Step 1: Adjust your bike seat to the correct height.")
    st.write("- Step 2: Start pedaling with a smooth, steady rhythm.")
    st.write("- Step 3: Keep your upper body relaxed and stable.")
    st.write("- Step 4: Focus on the muscle groups you want to stretch.")
    st.write("- Step 5: Stretch slowly and gently, avoiding any sudden movements.")
    st.write("- Step 6: Relax into each stretch, feeling the tension release.")
    st.write("- Step 7: Listen to your body and avoid overstretching or causing pain.")
    st.write("- Step 8: Incorporate a variety of stretches for different muscle groups.")
    st.write("- Step 9: Include dynamic stretches to improve flexibility and range of motion.")
    st.write("- Step 10: Stretch both sides of your body evenly to maintain balance.")
    st.write("- Step 11: Pay attention to your posture and alignment during each stretch.")
    st.write("- Step 12: Conclude your stretching routine with a cooldown to relax your muscles.")

# Function to display the Swimming page
def Swimming_page():
    st.title("Swimming")
    st.markdown("[Swimming Exercise Instructions](https://www.bing.com/videos/riverview/relatedvideo?q=swimming%20exercise%20on%20you%20tube&mid=FFAC85F42AD9078892C1FFAC85F42AD9078892C1&ajaxhist=0)")
    st.write("Here are the steps to perform Swimming:")
    st.write("- Step 1: Choose a stroke (e.g., freestyle, breaststroke).")
    st.write("- Step 2: Get into the water and start swimming.")
    st.write("- Step 3: Practice breathing techniques.")
    st.write("- Step 4: Keep your body streamlined to reduce drag.")
    st.write("- Step 5: Use your arms and legs to propel yourself through the water.")
    st.write("- Step 6: Rotate your body while swimming to improve efficiency.")
    st.write("- Step 7: Keep your head in line with your body and look forward or slightly down.")
    st.write("- Step 8: Exhale underwater and inhale when your face is above the water surface.")
    st.write("- Step 9: Kick from your hips and use a flutter or dolphin kick to propel yourself forward.")
    st.write("- Step 10: Coordinate your breathing with your stroke technique.")
    st.write("- Step 11: Practice bilateral breathing to improve balance and symmetry.")
    st.write("- Step 12: Cool down with a few easy laps and stretches after your swimming session.")

# Function to display the Water Aerobics page
def Water_Aerobics_page():
    st.title("Water Aerobics")
    st.markdown("[Water Aerobics Exercise Instructions](https://www.bing.com/videos/riverview/relatedvideo?&q=Water+Aerobics+exercise+for+PCOS+patient+on+you+tube&&view=riverview&mmscn=mtsc&mid=C92BC62E2001BF52DFF6C92BC62E2001BF52DFF6&&aps=11&FORM=VMSOVR)")
    st.write("Here are the steps to perform Water Aerobics:")
    st.write("- Step 1: Stand in waist-deep water.")
    st.write("- Step 2: Perform a variety of movements (e.g., leg lifts, arm circles).")
    st.write("- Step 3: Enjoy the buoyancy of the water.")
    st.write("- Step 4: Focus on maintaining good posture and engaging your core muscles.")
    st.write("- Step 5: Move your arms and legs through the water with control and intention.")
    st.write("- Step 6: Vary the intensity of your movements to challenge yourself.")
    st.write("- Step 7: Incorporate equipment like water dumbbells or noodles for added resistance.")
    st.write("- Step 8: Stay hydrated by drinking water before, during, and after your workout.")
    st.write("- Step 9: Pay attention to your breathing and exhale during exertion.")
    st.write("- Step 10: Listen to your body and modify exercises as needed to avoid strain or injury.")
    st.write("- Step 11: Cool down with gentle stretches in the water to improve flexibility.")
    st.write("- Step 12: Enjoy the social aspect of water aerobics and have fun with your workout!")

# Function to display the Elliptical Training page
def Elliptical_Training_page():
    st.title("Elliptical Training")
    st.markdown("[Elliptical Training Instructions](https://www.bing.com/videos/riverview/relatedvideo?&q=Elliptical+Training+exercise+for+PCOS+patient+on+you+tube&&mid=63F99E10ED8907AB4E9563F99E10ED8907AB4E95&&FORM=GVRPTV)")
    st.write("Here are the steps to perform Elliptical Training:")
    st.write("- Step 1: Adjust the resistance and incline as desired.")
    st.write("- Step 2: Start pedaling with a smooth motion.")
    st.write("- Step 3: Keep your posture upright and engage your core.")
    st.write("- Step 4: Focus on maintaining a consistent cadence throughout your workout.")
    st.write("- Step 5: Use the handlebars for support, but avoid leaning too heavily on them.")
    st.write("- Step 6: Experiment with different hand positions to alleviate pressure and prevent fatigue.")
    st.write("- Step 7: Keep your shoulders relaxed and avoid tensing up.")
    st.write("- Step 8: Pay attention to your breathing and try to synchronize it with your pedaling.")
    st.write("- Step 9: Monitor your heart rate to gauge the intensity of your workout.")
    st.write("- Step 10: Incorporate interval training by alternating between periods of high intensity and recovery.")
    st.write("- Step 11: Stay hydrated by drinking water throughout your workout.")
    st.write("- Step 12: Cool down with a few minutes of easy pedaling and gentle stretches.")

# Function to display the Dancing page
def Dancing_page():
    st.title("Dancing")
    st.markdown("[Dancing Exercise Instructions](https://www.bing.com/videos/riverview/relatedvideo?&q=dancing+exercise&&mid=88AC333CB71118A7542E88AC333CB71118A7542E&&FORM=VRDGAR)")
    st.write("Here are the steps to perform Dancing:")
    st.write("- Step 1: Choose your favorite music and style of dance.")
    st.write("- Step 2: Move your body to the rhythm of the music.")
    st.write("- Step 3: Have fun and express yourself through dance.")
    st.write("- Step 4: Start with a warm-up to loosen up your muscles and joints.")
    st.write("- Step 5: Practice basic dance steps and movements to build confidence.")
    st.write("- Step 6: Focus on proper posture and alignment to avoid strain or injury.")
    st.write("- Step 7: Pay attention to the beat and timing of the music.")
    st.write("- Step 8: Engage your core muscles for stability and balance.")
    st.write("- Step 9: Experiment with different dance styles and techniques to challenge yourself.")
    st.write("- Step 10: Incorporate jumps, turns, and other dynamic movements for variety.")
    st.write("- Step 11: Listen to your body and take breaks as needed to rest and hydrate.")
    st.write("- Step 12: Cool down with some gentle stretching to relax your muscles.")
# Function to display the Tai Chi page
def Tai_Chi_page():
    st.title("Tai Chi")
    st.markdown("[Tai Chi Exercise Instructions](https://www.bing.com/videos/riverview/relatedvideo?&q=+Tai+Chi+exercise+for+PCOS+&&mid=900CF16B2B69C4B3A4A2900CF16B2B69C4B3A4A2&&FORM=VRDGAR)")
    st.write("Here are the steps to perform Tai Chi:")
    st.write("- Step 1: Find a quiet outdoor or indoor space.")
    st.write("- Step 2: Follow a series of flowing, slow movements.")
    st.write("- Step 3: Focus on your breath and maintain balance.")
    st.write("- Step 4: Begin with a warm-up to loosen your muscles and joints.")
    st.write("- Step 5: Stand in a relaxed posture with feet shoulder-width apart.")
    st.write("- Step 6: Start with basic Tai Chi movements, such as 'Ward Off' or 'Grasp the Sparrow's Tail'.")
    st.write("- Step 7: Coordinate your movements with deep, slow breathing.")
    st.write("- Step 8: Pay attention to the alignment of your body and maintain a straight spine.")
    st.write("- Step 9: Flow smoothly from one movement to the next, maintaining a sense of fluidity.")
    st.write("- Step 10: Keep your mind calm and focused, letting go of any distractions or tension.")
    st.write("- Step 11: Practice regularly to improve your technique and deepen your understanding of Tai Chi.")
    st.write("- Step 12: End with a cool-down, incorporating gentle stretches and relaxation techniques.")
# Function to display the Chair Yoga page
def Chair_Yoga_page():
    st.title("Chair Yoga")
    st.markdown("[Chair Yoga Exercise Instructions](https://www.youtube.com/watch?v=-rBDxFKJtlE)")
    st.write("Here are the steps to perform Chair Yoga:")
    st.write("- Step 1: Sit comfortably in a sturdy chair.")
    st.write("- Step 2: Perform gentle stretches and movements.")
    st.write("- Step 3: Focus on your breath and relax your body.")
    st.write("- Step 4: Start with deep breathing exercises to center yourself.")
    st.write("- Step 5: Gently stretch your neck by tilting your head from side to side.")
    st.write("- Step 6: Rotate your shoulders in circles to release tension.")
    st.write("- Step 7: Extend your arms overhead and stretch towards the ceiling.")
    st.write("- Step 8: Bring your hands to your heart center and take a moment to set an intention for your practice.")
    st.write("- Step 9: Incorporate seated twists to improve spinal mobility.")
    st.write("- Step 10: Engage your core muscles by lifting one knee at a time towards your chest.")
    st.write("- Step 11: Relax into forward folds, allowing your upper body to hang loosely.")
    st.write("- Step 12: Conclude your practice with a few moments of seated meditation or relaxation.")

# Function to display the Resistance Band Training page
def Resistance_Band_Training_page():
    st.title("Resistance Band Training")
    st.markdown("[Resistance Band Training Instructions](https://www.bing.com/videos/riverview/relatedvideo?q=Resistance+Band+Training+exercise+for+PCOS+patient+on+you+tube&&view=riverview&mmscn=mtsc&mid=626E244C4C0E859517AB626E244C4C0E859517AB&&aps=0&FORM=VMSOVR)")
    st.write("Here are the steps to perform Resistance Band Training:")
    st.write("- Step 1: Secure the resistance band under your feet or around a stable object.")
    st.write("- Step 2: Perform various exercises targeting different muscle groups.")
    st.write("- Step 3: Maintain proper form and control throughout each movement.")
    st.write("- Step 4: Begin with a dynamic warm-up to prepare your muscles for exercise.")
    st.write("- Step 5: Incorporate compound movements such as squats, lunges, and rows to work multiple muscle groups simultaneously.")
    st.write("- Step 6: Adjust the resistance level of the band as needed to challenge yourself.")
    st.write("- Step 7: Focus on controlled, deliberate movements to maximize muscle engagement.")
    st.write("- Step 8: Take breaks as needed to prevent fatigue and ensure safety.")
    st.write("- Step 9: Gradually increase the intensity and duration of your workouts as you build strength and endurance.")
    st.write("- Step 10: Incorporate stretching exercises at the end of your session to improve flexibility and prevent muscle soreness.")
    st.write("- Step 11: Listen to your body and avoid overexertion or discomfort.")
    st.write("- Step 12: Stay consistent with your training routine to see progress and achieve your fitness goals.")

def User_BMI_calculation_page():
    st.title("Lightweight Exercise")
    st.write("Enter your details below to get personalized exercise recommendations.")

    weight = st.number_input("Enter your weight (kg):", value=0.0)
    height = st.number_input("Enter your height (cm):", value=0.0)
    age = st.number_input("Enter your age (years):", value=0)
    cycle = st.selectbox("Select menstrual cycle type:", ["Regular", "Irregular"])
    hair_growth = st.selectbox("Is there hair growth issue?", ["Yes", "No"])

    if st.button("Calculate BMI"):
        BMI = calculate_bmi(weight, height)
        st.write(f"Your BMI is: {BMI:.2f}")

        if 'scaler' in globals():
            cycle_encoded = 1 if cycle == "Regular" else 0
            hair_growth_encoded = 1 if hair_growth == "Yes" else 0
            scaled_bmi = scaler.transform([[weight, height, age, cycle_encoded, hair_growth_encoded, BMI]])[0][0]
            st.write(f"Scaled BMI: {scaled_bmi}")

            if 'model' in globals() and scaled_bmi is not None:
                input_features = [[scaled_bmi, height, age, cycle_encoded, hair_growth_encoded, scaled_bmi]]
                input_data = pd.DataFrame(input_features)
                weight_gain_prob = model.predict_proba(input_data)[0][1]  # Probability of weight gain
                
                if weight_gain_prob >= 0.5:
                    st.write("It seems you have gained weight.")
                elif weight_gain_prob <= 0.3:
                    st.write("Your weight seems stable.")
                else:
                    st.write("You seem to have lost weight.")
            else:
                st.warning("Model or input feature not found.")

            bmi_category = categorize_bmi(BMI)
            exercise_intensity = determine_exercise_intensity(BMI)
            lightweight_exercise = recommend_lightweight_exercise(BMI)

            st.write(f"BMI Category: {bmi_category}")
            st.write(f"Exercise Intensity: {exercise_intensity}")
            st.write(f"Based on your BMI, we recommend {lightweight_exercise}. Please click the exercise.")
                               
           # Display exercise instructions when the user clicks on the recommended exercise link
        if lightweight_exercise:
            st.subheader("Exercise Instructions:")
            display_exercise_instructions(lightweight_exercise)

# Streamlit app
def main():
    st.sidebar.title(" ")
    pages = ["Lightweight Exercise", "Yoga", "Pilates", "Stretching", "Walking", "Cycling", "Swimming", "Water Aerobics", "Elliptical Training", "Dancing", "Tai Chi", "Chair Yoga", "Resistance Band Training"]
    selected_page = st.sidebar.radio("Go to", pages, index=pages.index(session_state.page) if session_state.page in pages else 0)

    # Update the current page in the session state
    session_state.page = selected_page

    # Render the selected page
    if selected_page == "Lightweight Exercise":
        User_BMI_calculation_page()
    if selected_page == "Yoga":
        Yoga_page()
    elif selected_page == "Pilates":
        Pilates_page()
    elif selected_page == "Stretching":
        Stretching_page()
    elif selected_page == "Walking":
        Walking_page()
    elif selected_page == "Cycling":
        Cycling_page()
    elif selected_page == "Swimming":
        Swimming_page()
    elif selected_page == "Water Aerobics":
        Water_Aerobics_page()
    elif selected_page == "Elliptical Training":
        Elliptical_Training_page()
    elif selected_page == "Dancing":
        Dancing_page()
    elif selected_page == "Tai Chi":
        Tai_Chi_page()
    elif selected_page == "Chair Yoga":
        Chair_Yoga_page()
    elif selected_page == "Resistance Band Training":
        Resistance_Band_Training_page()

if __name__ == "__main__":
    main()
