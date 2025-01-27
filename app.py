import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
@st.cache_data
def load_data():
    file_path = 'data (3).csv'  # Adjust the path if needed
    return pd.read_csv(file_path)

# Initialize Dataset
dataset = load_data()

# Streamlit App
#st.title("Patient Analysis: Adrenal/Thyroid Disorders & Chronic Kidney Disease")
st.markdown(
    """
    <style>
    @keyframes color-change {
        0% { color: #ff4b1f; }
        25% { color: #ff9068; }
        50% { color: #1fddff; }
        75% { color: #6a11cb; }
        100% { color: #ff4b1f; }
    }
    .animated-title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        animation: color-change 5s infinite;
    }
    </style>
    <h1 class="animated-title">Patient Analysis: Adrenal/Thyroid Disorders & Chronic Kidney Disease</h1>
    """,
    unsafe_allow_html=True
)



# Tabs for organization
tab1, tab2, tab3 = st.tabs(["Dataset Overview", "Patient Lookup", "Predictive Analysis"])

# Tab 1: Dataset Overview
with tab1:
    st.subheader("Dataset Overview")
    st.write("### Preview of the Dataset:")
    st.write(dataset.head(10))  # Display the first 10 rows
    
    #st.write("### Dataset Statistics:")
    #st.write(dataset.describe())

    # Display correlation heatmap
    #st.write("### Correlation Heatmap:")
    #fig, ax = plt.subplots()
    #sns.heatmap(dataset.corr(), annot=True, cmap="coolwarm", ax=ax)
    #st.pyplot(fig)

# Tab 2: Patient Lookup
with tab2:
    st.subheader("Patient Lookup")
    
    # Input for Patient_Number
    patient_number = st.number_input(
        "Enter Patient_Number to check:",
        min_value=int(dataset['Patient_Number'].min()),
        max_value=int(dataset['Patient_Number'].max()),
        step=1,
        key="patient_lookup_number"
    )
    
    # Input fields for other features
    Blood_Pressure_Abnormality = st.selectbox("Blood Pressure Abnormality (0 = No, 1 = Yes):", [0, 1], key="lookup_blood_pressure")
    Level_of_Hemoglobin = st.number_input("Level of Hemoglobin (g/dL):", min_value=0.0, step=0.1, key="lookup_hemoglobin")
    Genetic_Pedigree_Coefficient = st.number_input("Genetic Pedigree Coefficient:", min_value=0.0, step=0.01, key="lookup_genetic_pedigree")
    Age = st.number_input("Age:", min_value=0, step=1, key="lookup_age")
    BMI = st.number_input("BMI (kg/m^2):", min_value=0.0, step=0.1, key="lookup_bmi")
    Sex = st.selectbox("Sex (0 = Female, 1 = Male):", [0, 1], key="lookup_sex")
    Pregnancy = st.selectbox("Pregnancy (0 = No, 1 = Yes):", [0, 1], key="lookup_pregnancy")
    Smoking = st.selectbox("Smoking (0 = No, 1 = Yes):", [0, 1], key="lookup_smoking")
    Physical_activity = st.number_input("Physical Activity (Hours per week):", min_value=0.0, step=0.1, key="lookup_physical_activity")
    salt_content_in_the_diet = st.number_input("Salt Content in Diet (g/day):", min_value=0.0, step=0.1, key="lookup_salt_content")
    alcohol_consumption_per_day = st.number_input("Alcohol Consumption (units/day):", min_value=0.0, step=0.1, key="lookup_alcohol")
    Level_of_Stress = st.number_input("Level of Stress (0-10):", min_value=0, max_value=10, step=1, key="lookup_stress")

    # Button to check results
    if st.button("Search Patient"):
        # Filter the dataset for the given Patient_Number
        patient_row = dataset[dataset['Patient_Number'] == patient_number]

        if not patient_row.empty:
            # Extract details for the patient
            row = patient_row.iloc[0]
            st.write(f"### Patient Details for Patient_Number {patient_number}:")
            st.write(row)

            # Display specific results
            chronic_kidney_disease = row['Chronic_kidney_disease']
            adrenal_thyroid_disorders = row['Adrenal_and_thyroid_disorders']

            st.write("### Diagnosis:")
            #st.write(f"- **Chronic Kidney Disease**: {'Yes' if chronic_kidney_disease == 1 else 'No'}")
            #st.write(f"- **Adrenal and Thyroid Disorders**: {'Yes' if adrenal_thyroid_disorders == 1 else 'No'}")
            st.markdown(
                f"""
                <p><b>Chronic Kidney Disease:</b> 
                <span style="color:{'red' if chronic_kidney_disease == 1 else 'green'};">
                {'Yes' if chronic_kidney_disease == 1 else 'No'}
                </span>
                </p>
                <p><b>Adrenal and Thyroid Disorders:</b> 
                <span style="color:{'red' if adrenal_thyroid_disorders == 1 else 'green'};">
                {'Yes' if adrenal_thyroid_disorders == 1 else 'No'}
                </span>
                </p>
                """,
                unsafe_allow_html=True
            )

        else:
            st.warning("No patient found with the given Patient_Number.")

# Tab 3: Predictive Analysis
with tab3:
    st.subheader("Predictive Analysis")
    
    # Input Fields
    Blood_Pressure_Abnormality = st.selectbox("Blood Pressure Abnormality (0 = No, 1 = Yes):", [0, 1], key="predict_blood_pressure")
    Level_of_Hemoglobin = st.number_input("Level of Hemoglobin (g/dL):", min_value=0.0, step=0.1, key="predict_hemoglobin")
    Genetic_Pedigree_Coefficient = st.number_input("Genetic Pedigree Coefficient:", min_value=0.0, step=0.01, key="predict_genetic_pedigree")
    Age = st.number_input("Age:", min_value=0, step=1, key="predict_age")
    BMI = st.number_input("BMI (kg/m^2):", min_value=0.0, step=0.1, key="predict_bmi")
    Sex = st.selectbox("Sex (0 = Female, 1 = Male):", [0, 1], key="predict_sex")
    Pregnancy = st.selectbox("Pregnancy (0 = No, 1 = Yes):", [0, 1], key="predict_pregnancy")
    Smoking = st.selectbox("Smoking (0 = No, 1 = Yes):", [0, 1], key="predict_smoking")
    Physical_activity = st.number_input("Physical Activity (Hours per week):", min_value=0.0, step=0.1, key="predict_physical_activity")
    salt_content_in_the_diet = st.number_input("Salt Content in Diet (g/day):", min_value=0.0, step=0.1, key="predict_salt_content")
    alcohol_consumption_per_day = st.number_input("Alcohol Consumption (units/day):", min_value=0.0, step=0.1, key="predict_alcohol")
    Level_of_Stress = st.number_input("Level of Stress (0-10):", min_value=0, max_value=10, step=1, key="predict_stress")

    # Predict disorders
    if st.button("Check for Disorders"):
        # Example thresholds for simplicity
        Adrenal_and_thyroid_disorders = (
            Blood_Pressure_Abnormality == 1 and 
            Level_of_Hemoglobin < 12 and 
            Level_of_Stress > 7
        )
        Chronic_kidney_disease = (
            BMI > 30 and 
            salt_content_in_the_diet > 5 and 
            Smoking == 1
        )

        st.write("### Diagnosis:")
        #st.write(f"- **Adrenal/Thyroid Disorder**: {'Likely' if Adrenal_and_thyroid_disorders else 'Unlikely'}")
        #st.write(f"- **Chronic Kidney Disease**: {'Likely' if Chronic_kidney_disease else 'Unlikely'}")
        st.markdown(
           f"""
           <p><b>Adrenal/Thyroid Disorder:</b> 
           <span style="color:{'red' if Adrenal_and_thyroid_disorders else 'green'};">
           {'Likely' if Adrenal_and_thyroid_disorders else 'Unlikely'}
           </span>
           </p>
           <p><b>Chronic Kidney Disease:</b> 
           <span style="color:{'red' if Chronic_kidney_disease else 'green'};">
           {'Likely' if Chronic_kidney_disease else 'Unlikely'}
           </span>
           </p>
           """,
           unsafe_allow_html=True
        )


# Footer
st.markdown('<span style="color:#838b99;">Project completed by MCA (2023-25), BCREC (Group-19)</span>', unsafe_allow_html=True)

