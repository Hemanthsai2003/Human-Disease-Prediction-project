Health Assistant: A Multi-Disease Prediction Web Application

Overview
Health Assistant is a web-based application that leverages machine learning to predict the likelihood of developing three common diseases: Diabetes, Heart Disease, and Parkinson's Disease. The system provides an accessible, non-invasive approach for individuals to assess their health risks and take proactive measures.

Features
- User-friendly Interface: Developed using Streamlit, making it easy for anyone to use.
- Disease Prediction: Predicts the risk of Diabetes, Heart Disease, and Parkinson's Disease based on user input.
- Machine Learning Models: Utilizes trained models to provide accurate risk assessments.
- Informative Visualizations: Displays clear results and insights to help users understand their health risks.

Technologies Used
- Programming Language: Python
- Web Framework: Streamlit
- Machine Learning Libraries: scikit-learn, NumPy, Pandas
- Development Environments: Google Colab, Spyder (Anaconda)

Installation & Setup
To run this project locally, follow these steps:

Prerequisites
Ensure you have Python installed (version 3.7 or higher). You can download it from [python.org](https://www.python.org/downloads/).

Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/health-assistant.git
   cd health-assistant
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   streamlit run app.py
   ```
5. Open the provided localhost URL in your browser.

Usage
1. Select a disease prediction category from the sidebar:
   - Diabetes Prediction
   - Heart Disease Prediction
   - Parkinson's Disease Prediction
2. Enter the required medical details.
3. Click the "Predict" button to view the results.
4. The system will analyze the input data and display the likelihood of having the selected disease.

Model Details
- Diabetes Prediction: Uses a Support Vector Machine (SVM) model trained on a diabetes dataset.
- Heart Disease Prediction: Utilizes a Logistic Regression model to assess heart disease risk.
- Parkinson's Disease Prediction: Implements a Support Vector Machine model trained on voice and movement-related data.

Limitations
- This application does not provide medical diagnoses; it serves as an informative tool.
- Predictions are based on machine learning models and should be validated by a healthcare professional.

Future Enhancements
- Integration with Wearable Devices: Real-time health monitoring using fitness trackers.
- Chatbot Support: AI-powered chatbot to guide users.
- Enhanced Model Accuracy: Incorporate additional datasets and deep learning techniques.

Contribution Guidelines
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature-branch
   ```
3. Make your changes and commit them:
   ```sh
   git commit -m "Added new feature"
   ```
4. Push to your fork and submit a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For any queries, contact Devika Sanjay Jonjale at [your-email@example.com](mailto:your-email@example.com).

Result snaps
https://github.com/Hemanthsai2003/Human-Disease-Prediction-project/blob/master/images/image1.jpg?raw=true
https://github.com/Hemanthsai2003/Human-Disease-Prediction-project/blob/master/images/image2.jpg?raw=true
https://github.com/Hemanthsai2003/Human-Disease-Prediction-project/blob/master/images/image3.jpg?raw=true
https://github.com/Hemanthsai2003/Human-Disease-Prediction-project/blob/master/images/image4.jpg?raw=true
