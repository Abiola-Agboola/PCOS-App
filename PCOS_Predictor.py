import streamlit as st
import pandas as pd
import pickle as pickle
import plotly.graph_objects as go
import numpy as np
# Load the trained model and data
data = pd.read_csv(r'C:\Users\User\Downloads\cleaned.csv', encoding='ISO-8859-1')

st.set_page_config(page_title="PCOS Predictor", page_icon="🧊", layout="wide")

def add_sidebar():
    st.sidebar.header("Health Metrics Assessment")

    num_slider_labels = [("Follicle No. (R)", "Follicle No. (R)"), ("Follicle No. (L)", "Follicle No. (L)"),("AMH(ng/mL)", "AMH(ng/mL)"),
                         ("Weight (Kg)", "Weight (Kg)")]
    int_values = [("Cycle(R/I)", "Cycle(R/I)")]

    char_selectbox_labels = ["Skin darkening (Y/N)", "hair growth(Y/N)", 
                             "Weight gain(Y/N)","Fast food (Y/N)", "Pimples(Y/N)"]
    
    slider_values = {}
    selectbox_values = {}

    for n_label, key in num_slider_labels:
        slider_values[key] = st.sidebar.slider(n_label, min_value=float(0), max_value=float(data[key].max()),
                                               value=float(data[key].mean()))
    for int_label, key in int_values:
        slider_values[key] = st.sidebar.slider(int_label, min_value=int(0), max_value=int(data[key].max()),
                                               value=int(data[key].mean()))

    for ch_label in char_selectbox_labels:
        options = ['Yes', 'No']
        selected_value = 'Yes' if data[ch_label].mean() == 1 else 'No'  # Adjust this logic based on your data
        selectbox_values[ch_label] = st.sidebar.selectbox(ch_label, options, index=options.index(selected_value))

    return slider_values, selectbox_values

def get_scaled_values(slider_values, selectbox_values):
    X = data.drop(['PCOS (Y/N)'], axis=1)
    scaled_dict_N = {}
    scaled_dict_Ch = {}

    for key, value in slider_values.items():
        max_val_n = X[key].max()
        min_val_n = X[key].min()
        scaled_value_N = (value - min_val_n) / (max_val_n - min_val_n)
        scaled_dict_N[key] = scaled_value_N

    for key, value in selectbox_values.items():
        # Convert "Yes" to 1 and "No" to 0
        numerical_value = 1 if value == "Yes" else 0
        max_val_ch = X[key].max()
        min_val_ch = X[key].min()
        scaled_value_Ch = (numerical_value - min_val_ch) / (max_val_ch - min_val_ch)
        scaled_dict_Ch[key] = scaled_value_Ch

    return scaled_dict_N, scaled_dict_Ch

def get_radar_chart(slider_vals, selectbox_vals):
    scaled_slider_vals, scaled_selectbox_vals = get_scaled_values(slider_vals, selectbox_vals)
    n_categories = ['Follicle No. (R)', 'Follicle No. (L)', 'AMH(ng/mL)', 'Weight (Kg)', 'Cycle(R/I)']
    ch_categories = ['Skin darkening (Y/N)', 'hair growth(Y/N)', 'Weight gain(Y/N)', 'Fast food (Y/N)', 'Pimples(Y/N)']

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(r=[slider_vals['Follicle No. (R)'], slider_vals['Follicle No. (L)'],
                                     slider_vals['AMH(ng/mL)'], slider_vals['Weight (Kg)'], slider_vals['Cycle(R/I)']],
                                  theta=n_categories,
                                  fill='toself',
                                  name='Product N'
                                    ))

    fig.add_trace(go.Scatterpolar(r=[selectbox_vals['Skin darkening (Y/N)'], selectbox_vals['hair growth(Y/N)'], 
                                     selectbox_vals['Weight gain(Y/N)'], selectbox_vals['Fast food (Y/N)'],
                                     selectbox_vals['Pimples(Y/N)']], 
                                  theta=ch_categories,
                                  fill='toself',
                                  name='Product CH'
                                    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )),
        showlegend=True
    )

    return fig

def add_predictions(slider_vals, selectbox_vals):
    with open('final_model.sav', 'rb') as model_file:
        PCOSmodel = pickle.load(model_file)
        
        # Combine the slider and selectbox values
        input_dict = {**slider_vals, **selectbox_vals}

        # Convert categorical variables to numeric values
        for key, value in input_dict.items():
            if value == 'Yes':
                input_dict[key] = 1
            elif value == 'No':
                input_dict[key] = 0

        # Convert the input dictionary to a DataFrame
        input_df = pd.DataFrame([input_dict])

        #st.dataframe(input_df)

        # Extract the numeric values from the DataFrame
        input_array = input_df.values.astype(float)

        # Load the scaler
    with open('scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)

        # Scale the input features
        scaled_input_array = scaler.transform(input_array)

        # Make predictions
        prediction = PCOSmodel.predict(scaled_input_array)
        
        st.subheader("Medical Insight")
        st.write("Hello Damsel! your medical insight is:")
        
        
        if prediction[0] == 0:
            st.write("No evidence of PCOS")
    # No need to direct to the nutrition page
        else:
            st.error("Confirmation of PCOS is evident")
            # Directly link to the nutrition page
            st.markdown("[Go to Nutrition Page](http://localhost:8501/Home)")
            st.markdown("[Go to Exercise Page](http://localhost:8501/Exercise)")
            
        st.write("Probability of being no evidence of PCOS: ", PCOSmodel.predict_proba(scaled_input_array)[0][0])
        st.write("Probability confirmation of PCOS is evident: ", PCOSmodel.predict_proba(scaled_input_array)[0][1])
        
        st.write("While this application can aid healthcare professionals in the diagnostic process, it should not serve as a replacement for a professional diagnosis. It is recommended to consult with your General Practitioner (GP) for confirmation, especially if the app indicates a probability of PCOS.")
        
def main():
    st.set_page_config(page_title='PCOS Predictor',
                   page_icon=':female-doctor:',
                   layout='wide',
                   initial_sidebar_state='expanded')
    
slider_vals, selectbox_vals = add_sidebar()
#st.write(slider_vals, selectbox_vals)
get_radar_chart(slider_vals, selectbox_vals)

# Add a pink background color
st.markdown(
    """
    <style>
        body {
            background-color: #FFC0CB;  /* Pink color code */
        }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.title('PCOS Predictor')
    st.write("Please connect your result from on this app with your Doctor, gynecologists or endocrinologists because this PCOS Predictor                App accurately evaluates PCOS markers. It examines user data, lab reports, and provides expert-driven proactive health                      management. Users can update measurements manually for precise analysis using intuitive sliders in the sidebar.")
    
    col1, col2 = st.columns([4,1])
    
    with col1:
        radar_chart = get_radar_chart(slider_vals, selectbox_vals)
        st.plotly_chart(radar_chart)
    with col2:
        add_predictions(slider_vals, selectbox_vals)
        
        
        
#if _name_ == '_main_':
    #main()
    