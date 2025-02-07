# import os
# import pickle
# import streamlit as st
# from streamlit_option_menu import option_menu

# # Set page configuration
# st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="⚕️")

# # Getting the working directory of the script
# working_dir = os.path.dirname(os.path.abspath(__file__))

# # Loading the saved models
# diabetes_model = pickle.load(open(os.path.join(working_dir, 'C:/Users/vinee/Documents/MCA PROJECT/Internship Project/multidiseaseprediction-main/saved models/diabetes_model.sav'), 'rb'))
# heart_disease_model = pickle.load(open(os.path.join(working_dir, 'C:/Users/vinee/Documents/MCA PROJECT/Internship Project/multidiseaseprediction-main/saved models/heart_disease_model.sav'), 'rb'))
# parkinsons_model = pickle.load(open(os.path.join(working_dir, 'C:/Users/vinee/Documents/MCA PROJECT/Internship Project/multidiseaseprediction-main/saved models/parkinsons_model.sav'), 'rb'))

# # Sidebar for navigation
# with st.sidebar:
#     selected = option_menu(
#         'Multiple Disease Prediction System',
#         ['Diabetes Prediction', 'Heart Disease Prediction', "Parkinson's Prediction"],
#         menu_icon='hospital-fill',
#         icons=['activity', 'heart', 'person'],
#         default_index=0
#     )

# # Diabetes Prediction Page
# if selected == 'Diabetes Prediction':
#     st.title('Diabetes Prediction using ML')

#     col1, col2, col3 = st.columns(3)
#     with col1:
#         Pregnancies = st.text_input('Number of Pregnancies')
#     with col2:
#         Glucose = st.text_input('Glucose Level')
#     with col3:
#         BloodPressure = st.text_input('Blood Pressure value')
#     with col1:
#         SkinThickness = st.text_input('Skin Thickness value')
#     with col2:
#         Insulin = st.text_input('Insulin Level')
#     with col3:
#         BMI = st.text_input('BMI value')
#     with col1:
#         DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
#     with col2:
#         Age = st.text_input('Age of the Person')

#     if st.button('Diabetes Test Result'):
#         user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
#         user_input = [float(x) for x in user_input]

#         diab_prediction = diabetes_model.predict([user_input])
#         result = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
#         st.success(result)

# # Heart Disease Prediction Page
# elif selected == 'Heart Disease Prediction':
#     st.title('Heart Disease Prediction using ML')

#     col1, col2, col3 = st.columns(3)
#     with col1:
#         age = st.text_input('Age')
#     with col2:
#         sex = st.text_input('Sex')
#     with col3:
#         cp = st.text_input('Chest Pain types')
#     with col1:
#         trestbps = st.text_input('Resting Blood Pressure')
#     with col2:
#         chol = st.text_input('Serum Cholesterol in mg/dl')
#     with col3:
#         fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
#     with col1:
#         restecg = st.text_input('Resting Electrocardiographic results')
#     with col2:
#         thalach = st.text_input('Maximum Heart Rate achieved')
#     with col3:
#         exang = st.text_input('Exercise Induced Angina')
#     with col1:
#         oldpeak = st.text_input('ST depression induced by exercise')
#     with col2:
#         slope = st.text_input('Slope of the peak exercise ST segment')
#     with col3:
#         ca = st.text_input('Major vessels colored by fluoroscopy')
#     with col1:
#         thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

#     if st.button('Heart Disease Test Result'):
#         user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
#         user_input = [float(x) for x in user_input]

#         heart_prediction = heart_disease_model.predict([user_input])
#         result = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
#         st.success(result)

# # Parkinson's Prediction Page
# elif selected == "Parkinson's Prediction":
#     st.title("Parkinson's Disease Prediction using ML")

#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         fo = st.text_input('MDVP:Fo(Hz)')
#     with col2:
#         fhi = st.text_input('MDVP:Fhi(Hz)')
#     with col3:
#         flo = st.text_input('MDVP:Flo(Hz)')
#     with col4:
#         Jitter_percent = st.text_input('MDVP:Jitter(%)')
#     with col5:
#         Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
#     with col1:
#         RAP = st.text_input('MDVP:RAP')
#     with col2:
#         PPQ = st.text_input('MDVP:PPQ')
#     with col3:
#         DDP = st.text_input('Jitter:DDP')
#     with col4:
#         Shimmer = st.text_input('MDVP:Shimmer')
#     with col5:
#         Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
#     with col1:
#         APQ3 = st.text_input('Shimmer:APQ3')
#     with col2:
#         APQ5 = st.text_input('Shimmer:APQ5')
#     with col3:
#         APQ = st.text_input('MDVP:APQ')
#     with col4:
#         DDA = st.text_input('Shimmer:DDA')
#     with col5:
#         NHR = st.text_input('NHR')
#     with col1:
#         HNR = st.text_input('HNR')
#     with col2:
#         RPDE = st.text_input('RPDE')
#     with col3:
#         DFA = st.text_input('DFA')
#     with col4:
#         spread1 = st.text_input('Spread1')
#     with col5:
#         spread2 = st.text_input('Spread2')
#     with col1:
#         D2 = st.text_input('D2')
#     with col2:
#         PPE = st.text_input('PPE')

#     if st.button("Parkinson's Test Result"):
#         user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
#                       Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE,
#                       DFA, spread1, spread2, D2, PPE]
#         user_input = [float(x) for x in user_input]

#         parkinsons_prediction = parkinsons_model.predict([user_input])
#         result = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
#         st.success(result)

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="⚕️")

# Getting the working directory of the script
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved models
diabetes_model = pickle.load(open(os.path.join(working_dir, '"C:/Users/sai/Downloads/multidiseaseprediction-main/multidiseaseprediction-main/datasets/diabetes.csv"'), 'rb'))
heart_disease_model = pickle.load(open(os.path.join(working_dir, '"C:/Users/sai/Downloads/multidiseaseprediction-main/multidiseaseprediction-main/datasets/heart.csv"'), 'rb'))
parkinsons_model = pickle.load(open(os.path.join(working_dir, '"C:/Users/sai/Downloads/multidiseaseprediction-main/multidiseaseprediction-main/datasets/parkinsons.csv"'), 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', "Parkinson's Prediction"],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    if st.button('Diabetes Test Result'):
        try:
            user_input = [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
                          float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]
            
            diab_prediction = diabetes_model.predict([user_input])
            result = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
            st.success(result)
        except ValueError:
            st.error("Please enter valid numerical values.")

# Heart Disease Prediction Page
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.selectbox('Sex', ['Male', 'Female'])  # Dropdown for categorical variable
    with col3:
        cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3])
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl')
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])
    with col1:
        restecg = st.selectbox('Resting Electrocardiographic results', [0, 1, 2])
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.selectbox('Exercise Induced Angina', [0, 1])
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.selectbox('Slope of the peak exercise ST segment', [0, 1, 2])
    with col3:
        ca = st.selectbox('Major vessels colored by fluoroscopy', [0, 1, 2, 3, 4])
    with col1:
        thal = st.selectbox('Thalassemia', [0, 1, 2, 3])

    if st.button('Heart Disease Test Result'):
        try:
            # Encode categorical variables before conversion
            sex = 1 if sex == 'Male' else 0

            user_input = [float(age), sex, cp, float(trestbps), float(chol), fbs,
                          restecg, float(thalach), exang, float(oldpeak), slope, ca, thal]

            heart_prediction = heart_disease_model.predict([user_input])
            result = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
            st.success(result)
        except ValueError:
            st.error("Please enter valid numerical values.")

# Parkinson's Prediction Page
elif selected == "Parkinson's Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('Spread1')
    with col5:
        spread2 = st.text_input('Spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    if st.button("Parkinson's Test Result"):
        try:
            user_input = [float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs),
                          float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB),
                          float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR),
                          float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)]

            parkinsons_prediction = parkinsons_model.predict([user_input])
            result = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
            st.success(result)
        except ValueError:
            st.error("Please enter valid numerical values.")
