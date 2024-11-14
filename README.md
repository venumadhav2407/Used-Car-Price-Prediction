# CarDekho Used Car Price Prediction

## Introduction
This project aims to enhance customer experience and optimize the pricing process for used cars. Using historical car data and features such as make, model, year, fuel type, and transmission type, we developed a machine learning model to predict used car prices. 
The model is integrated into a Streamlit web application, allowing users to input car details and receive real-time price predictions.

The final model is deployed as an interactive web application using Streamlit, allowing users to input specific car features and receive real-time price predictions.

## Project Workflow
1. **Data Collection**: Loaded and cleaned a dataset containing used car details.
2. **Data Preprocessing**: Processed unstructured data, handled missing values, and encoded categorical features.
3. **Feature Engineering**: Enhanced the dataset with additional features for improved model accuracy.
4. **Model Training**: Trained multiple regression models, with Random Forest chosen as the best model based on evaluation metrics.
5. **Hyperparameter Tuning**: Optimized the model using `GridSearchCV` to improve accuracy.
6. **Deployment**: Developed a Streamlit application for easy user interaction and price predictions.

### Model Deployment - Streamlit
- Developed an interactive application for price prediction:
   - **User Input Interface**: Allows users to input details (e.g., make, model, year).
   - **Real-time Prediction**: Displays predicted price using the trained Random Forest model.
   - **Backend**: Loaded model and scalers with `pickle`, ensuring preprocessing consistency.

## App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://redbus-app.streamlit.app/)


![image](https://github.com/user-attachments/assets/ee1ae5ba-bee4-41b2-b7ce-75e9322a820f)


## Getting Started
To run this project locally, follow the setup instructions below.

### Prerequisites
- Python 3.x
- Libraries: `pandas`, `numpy`, `scikit-learn`, `streamlit`, `pickle`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/venumadhav2407/Used-Car-Price-Prediction.git
   cd used-car-price-prediction
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Data Preprocessing and Model Training
1. Run the `data_preprocessing.ipynb` notebook to clean and preprocess the dataset.
2. Use the notebook to train the model and save the trained model as `model.pkl` using `pickle`.

## Deployment with Streamlit
1. Run the Streamlit app with:
   ```bash
   streamlit run app.py
   ```
2. Go to `http://localhost:8501` in your browser to access the app.

--- 

## Approach

### Data Processing
1. **Data Import and Wrangling**:
   - Loaded datasets from multiple cities in unstructured formats (Excel files, JSON-like structures).
   - Used `pandas` and `ast.literal_eval` to parse and flatten nested JSON data.
   - Combined city-specific data into a single unified dataframe for model training.

2. **Data Cleaning**:
   - Removed symbols, units, and unnecessary whitespace; converted values to numerical format.
   - Handled missing values using `dropna` and processed text fields for modeling.

3. **Exploratory Data Analysis (EDA)**:
   - Examined feature relationships and detected outliers using a correlation matrix and IQR.
   - Identified key patterns and outliers that influenced the target variable, `price`.

4. **Feature Selection**:
   - Selected categorical features (e.g., fuel type, body type) and numerical features (e.g., kms driven, mileage).

5. **Encoding and Scaling**:
   - Applied OneHot Encoding for categorical data and Standard Scaler for numerical features to standardize scales.

### Model Development
1. **Train-Test Split**: Divided data into training and testing sets (e.g., 70-30 split).

2. **Model Selection**:
   - **Linear Regression**: Baseline model with Ridge and Lasso regularization.
   - **Gradient Boosting Regressor**: Ensemble model for residual-based fitting.
   - **Decision Tree Regressor**: Nonlinear model with pruning to prevent overfitting.
   - **Random Forest Regressor**: Ensemble model that averaged predictions across trees, selected as the final model due to performance.

3. **Model Evaluation**:
   - Used Mean Squared Error (MSE), Mean Absolute Error (MAE), and R² Score.
   - Random Forest Regressor achieved the best performance, with the lowest MSE and highest R².

4. **Pipeline**:
   - Structured modular pipeline for data preprocessing and model training, ensuring consistency and reproducibility.
   - Integrated Column Transformer to handle both categorical and numerical data.


## Results
- **Random Forest Model**: Highest accuracy with best MSE and R² metrics.
- **Hyperparameter Tuning**: Improved model performance through Grid Search on parameters like `n_estimators` and `max_depth`.

## Project Impact
This tool provides CarDekho customers with real-time, data-driven price predictions for used cars, enabling informed decisions and enhancing customer experience. 
For sales representatives, it simplifies the pricing process, ensuring consistent and efficient valuation.

## Limitations
- **Data Quality**: Model accuracy depends on input data quality.
- **Feature Selection**: Relevant features might be missing, affecting predictions.
- **Market Variability**: The model may not account for external factors like economic conditions.

## Future Work
- **Feature Expansion**: Incorporate features like service history and car condition.
- **Advanced Models**: Explore deep learning methods for better accuracy.
- **Real-time Market Data**: Integrate dynamic market data for adaptive pricing.


## Conclusion
The deployment of this model through a Streamlit app provides users and sales reps with quick, reliable used car price estimates. It also opens opportunities for future enhancements, such as real-time data integration and personalized recommendations.

---



