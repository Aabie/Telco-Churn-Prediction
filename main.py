import streamlit as st
import joblib
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Telco Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    body, .main {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #f6f9fc 0%, #ffffff 100%);
        color: #2D3748;
        margin: 0;
        padding: 0;
    }

    .main {
        padding: 25px;
        animation: fadeIn 1s ease-in-out;
    }

    @keyframes fadeIn {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }

    /* Card styling for sections */
    .main > div {
        background: linear-gradient(135deg, #ffffff 0%, #f8faff 100%);
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 4px 15px rgba(66, 153, 225, 0.1);
        transition: transform 0.3s ease-in-out;
        border: 1px solid rgba(66, 153, 225, 0.1);
    }

    .main > div:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 20px rgba(66, 153, 225, 0.15);
    }

    /* Button styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%);
        color: white;
        font-weight: 500;
        padding: 15px;
        border-radius: 10px;
        border: none;
        transition: all 0.4s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #4F46E5 0%, #4338CA 100%);
        box-shadow: 0 5px 15px rgba(79, 70, 229, 0.3);
        transform: translateY(-3px);
    }

    /* Title styling */
    h1.title {
        background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 2.5em;
        font-weight: 600;
        margin: 25px 0;
        text-shadow: 2px 2px 4px rgba(79, 70, 229, 0.1);
    }

    /* Subheader styling */
    .stSubheader {
        color: #4F46E5;
        font-size: 1.2em;
        font-weight: 500;
        padding-bottom: 10px;
        border-bottom: 2px solid #E2E8F0;
        margin-bottom: 15px;
    }

    /* Divider styling */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(to right, transparent, #6366F1, transparent);
        margin: 25px 0;
    }

    /* Select box styling */
    .stSelectbox {
        background-color: #f8fafc;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
        padding: 5px;
    }

    /* Number input styling */
    .stNumberInput {
        background-color: #f8fafc;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
    }

    /* Prediction result styles */
    .prediction-message {
        padding: 20px;
        border-radius: 10px;
        font-weight: 500;
        margin-top: 20px;
    }

    .high-risk {
        background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%);
        color: #DC2626;
        border-left: 6px solid #EF4444;
    }

    .low-risk {
        background: linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%);
        color: #16A34A;
        border-left: 6px solid #22C55E;
    }

    /* Widget labels */
    .stSelectbox > label, .stNumberInput > label {
        color: #4A5568;
        font-weight: 500;
    }

    /* Input field styling */
    input[type="number"] {
        border: 2px solid #E2E8F0;
        border-radius: 8px;
        padding: 8px 12px;
        transition: all 0.3s ease;
    }

    input[type="number"]:focus {
        border-color: #6366F1;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
    }

    /* Dropdown styling */
    select {
        border: 2px solid #E2E8F0;
        border-radius: 8px;
        padding: 8px 12px;
        background: white;
        transition: all 0.3s ease;
    }

    select:focus {
        border-color: #6366F1;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
    }
    </style>
""", unsafe_allow_html=True)


# Title and description
st.markdown("<h1 class='title'>Telco Customer Churn Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>This app predicts the likelihood of a customer churning based on various customer features. Please input customer details and hit 'Predict Customer Churn' to get the result.</p>", unsafe_allow_html=True)
st.markdown("---")

# Load model
model = joblib.load(r'logreg_model.pkl')

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Personal Information")
    gender_mapping = {"Female": 0, "Male": 1}
    gender_label = st.selectbox("👤 Gender", gender_mapping)
    gender_encoded = gender_mapping[gender_label]

    senior_mapping = {"Yes": 1, "No": 0}
    senior = st.selectbox("👴 Senior Citizen", senior_mapping)
    senior_encoded = senior_mapping[senior]

    Partner_mapping = {"Yes": 1, "No": 0}
    Partner = st.selectbox("💑 Partner", Partner_mapping)
    Partner_encoded = Partner_mapping[Partner]

    Dependents_mapping = {"Yes": 1, "No": 0}
    Dependents = st.selectbox("👨‍👩‍👧‍👦 Dependents", Dependents_mapping)
    Dependents_encoded = Dependents_mapping[Dependents]

    tenure = st.number_input("📅 Tenure (months)", min_value=0, max_value=72)

with col2:
    st.subheader("Services")
    PhoneService_mapping = {"Yes": 1, "No": 0}
    PhoneService = st.selectbox("📱 Phone Service", PhoneService_mapping)
    PhoneService_encoded = PhoneService_mapping[PhoneService]

    MultipleLines_mapping = {"Yes": 2, "No": 0, "No phone service": 1}
    MultipleLines = st.selectbox("📞 Multiple Lines", MultipleLines_mapping)
    MultipleLines_encoded = MultipleLines_mapping[MultipleLines]

    InternetService_mapping = {"DSL": 0, "Fiber optic": 1, "No": 2}
    InternetService = st.selectbox("🌐 Internet Service", InternetService_mapping)
    InternetService_encoded = InternetService_mapping[InternetService]

    OnlineSecurity_mapping = {"Yes": 2, "No": 0, "No internet service": 1}
    OnlineSecurity = st.selectbox("🔒 Online Security", OnlineSecurity_mapping)
    OnlineSecurity_encoded = OnlineSecurity_mapping[OnlineSecurity]

    OnlineBackup_mapping = {"Yes": 2, "No": 0, "No internet service": 1}
    OnlineBackup = st.selectbox("💾 Online Backup", OnlineBackup_mapping)
    OnlineBackup_encoded = OnlineBackup_mapping[OnlineBackup]

with col3:
    st.subheader("Additional Features")
    TechSupport_mapping = {"Yes": 2, "No": 0, "No internet service": 1}
    TechSupport = st.selectbox("🛠️ Tech Support", TechSupport_mapping)
    TechSupport_encoded = TechSupport_mapping[TechSupport]

    StreamingTV_mapping = {"Yes": 2, "No": 0, "No internet service": 1}
    StreamingTV = st.selectbox("📺 Streaming TV", StreamingTV_mapping)
    StreamingTV_encoded = StreamingTV_mapping[StreamingTV]

    StreamingMovies_mapping = {"Yes": 2, "No": 0, "No internet service": 1}
    StreamingMovies = st.selectbox("🎬 Streaming Movies", StreamingMovies_mapping)
    StreamingMovies_encoded = StreamingMovies_mapping[StreamingMovies]

    DeviceProtection_mapping = {"Yes": 2, "No": 0, "No internet service": 1}
    DeviceProtection = st.selectbox("🛡️ Device Protection", DeviceProtection_mapping)
    DeviceProtection_encoded = DeviceProtection_mapping[DeviceProtection]

st.markdown("---")
col4, col5 = st.columns(2)
with col4:
    st.subheader("Contract Details")
    Contract_mapping = {"Month-to-month": 0, "One year": 1, "Two year": 2}
    Contract = st.selectbox("📄 Contract", Contract_mapping)
    Contract_encoded = Contract_mapping[Contract]

    PaperlessBilling_mapping = {"Yes": 1, "No": 0}
    PaperlessBilling = st.selectbox("📱 Paperless Billing", PaperlessBilling_mapping)
    PaperlessBilling_encoded = PaperlessBilling_mapping[PaperlessBilling]

with col5:
    st.subheader("Payment Information")
    PaymentMethod_mapping = {
        "Electronic check": 2,
        "Mailed check": 3,
        "Bank transfer (automatic)": 0,
        "Credit card (automatic)": 1
    }
    PaymentMethod = st.selectbox("💳 Payment Method", PaymentMethod_mapping)
    PaymentMethod_encoded = PaymentMethod_mapping[PaymentMethod]
    MonthlyCharges = st.number_input("💰 Monthly Charges ($)", min_value=0.0, max_value=120.0)

data = {
    "gender": [gender_encoded],
    "SeniorCitizen": [senior_encoded],
    "Partner": [Partner_encoded],
    "Dependents": [Dependents_encoded],
    "tenure": [tenure],
    "PhoneService": [PhoneService_encoded],
    "MultipleLines": [MultipleLines_encoded],
    "InternetService": [InternetService_encoded],
    "OnlineSecurity": [OnlineSecurity_encoded],
    "OnlineBackup": [OnlineBackup_encoded],
    "DeviceProtection": [DeviceProtection_encoded],
    "TechSupport": [TechSupport_encoded],
    "StreamingTV": [StreamingTV_encoded],
    "StreamingMovies": [StreamingMovies_encoded],
    "Contract": [Contract_encoded],
    "PaperlessBilling": [PaperlessBilling_encoded],
    "PaymentMethod": [PaymentMethod_encoded],
    "MonthlyCharges": [MonthlyCharges]
}

st.markdown("---")
col6, col7, col8 = st.columns([1, 2, 1])
with col7:
    if st.button("🔮 Predict Customer Churn"):
        result = model.predict(pd.DataFrame(data))
        if result == 1:
            message = """
                <div class="prediction-container">
                    <div class="prediction-message high-risk">
                        <span class="prediction-icon">⚠️</span>
                        <h3 class="prediction-title">High Risk of Churn</h3>
                        <p class="prediction-text">This customer is likely to churn. Immediate attention required.</p>
                        <div class="additional-info">
                            Recommended: Schedule a customer retention call within 24 hours
                        </div>
                    </div>
                </div>
                <style>
                    .prediction-container {
                        padding: 20px;
                        border-radius: 8px;
                        background-color: #ffe0e0;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    }
                    .prediction-message {
                        text-align: center;
                    }
                    .high-risk {
                        color: #b00020;
                        background-color: #ffcccc;
                    }
                    .prediction-title {
                        font-size: 24px;
                        font-weight: bold;
                    }
                    .prediction-text {
                        font-size: 16px;
                        margin-bottom: 15px;
                    }
                    .additional-info {
                        font-size: 14px;
                        font-style: italic;
                    }
                    .prediction-icon {
                        font-size: 40px;
                    }
                </style>
            """
            st.markdown(message, unsafe_allow_html=True)
        else:
            message = """
                <div class="prediction-container">
                    <div class="prediction-message low-risk">
                        <span class="prediction-icon">✅</span>
                        <h3 class="prediction-title">Low Risk of Churn</h3>
                        <p class="prediction-text">This customer is likely to stay. Keep up the good service!</p>
                        <div class="additional-info">
                            Recommended: Continue monitoring satisfaction levels
                        </div>
                    </div>
                </div>
                <style>
                    .prediction-container {
                        padding: 20px;
                        border-radius: 8px;
                        background-color: #e8f7e3;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    }
                    .prediction-message {
                        text-align: center;
                    }
                    .low-risk {
                        color: #2e7d32;
                        background-color: #a5d6a7;
                    }
                    .prediction-title {
                        font-size: 24px;
                        font-weight: bold;
                    }
                    .prediction-text {
                        font-size: 16px;
                        margin-bottom: 15px;
                    }
                    .additional-info {
                        font-size: 14px;
                        font-style: italic;
                    }
                    .prediction-icon {
                        font-size: 40px;
                    }
                </style>
            """
            st.markdown(message, unsafe_allow_html=True)


st.markdown("""
    <style>
        .footer {
            text-align: center;
            padding: 15px;
            font-size: 16px;
            background-color: #282c34;
            color: white;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            border-top: 1px solid #444;
        }
        .footer a {
            color: #61dafb;
            text-decoration: none;
            font-weight: bold;
        }
        .footer a:hover {
            color: #ffffff;
            text-decoration: underline;
        }
    </style>
    <div class='footer'>
        Made with Streamlit by <a href="https://www.linkedin.com/in/abienugraha" target="_blank">Abie Nugraha</a>
    </div>
""", unsafe_allow_html=True)
