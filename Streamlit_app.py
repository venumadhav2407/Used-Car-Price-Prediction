import streamlit as st
import joblib
import pandas as pd

# load_dataset
car_data = pd.read_csv("./final_carDetails.csv")

# load final trained model
model = joblib.load('car_price_model.pkl') 

st.set_page_config(
    page_title="Used Car Price Prediction",
    page_icon=":material/directions_car:",
    layout='wide',
    menu_items={'About' : "# Used Car Price Prediction"}
)

st.markdown("# Used Car Price Prediction")


# define the columns
col1, col2 = st.columns([3, 1])

# input feilds 
with col1:  
    
    # define sub cols
    col11, col12 = st.columns([1, 1])
    
    with col11:  
        brand = st.selectbox("**Brand**",options=car_data['Brand'].unique(), placeholder="Select Brand", index=None)
        filter_models = car_data[car_data['Brand'] == brand]['model'].unique()
        model_car = st.selectbox("**Model**", options=filter_models, placeholder="Select Model", index=None)
        year = st.selectbox("**Year**", car_data['modelYear'].unique(), placeholder="Select Year", index=None)
        fuel_type = st.selectbox("**Fuel Type**", car_data['Fuel_Type'].unique(), placeholder="Select Fule Type", index=None)
        body_type = st.selectbox("**Body Type**", car_data['Body_Type'].unique(), placeholder="Select Body Type", index=None)
        transmission = st.selectbox("**Transmission**", car_data['transmission'].unique(), placeholder="Select Transmission", index=None)
        mileage = st.slider("**Mileage**", min_value=10.0, max_value=150.0)
    with col12:
        km_driven = st.slider("**Kms Driven**", min_value=1000, max_value=100000)
        engine_size = st.number_input("**Engine Size (CC)**", min_value=0, max_value=6000, step=50)
        previous_owner = st.selectbox("**Previous Owner**", car_data['ownerNo'].unique(), placeholder="Select Pre OwnerNo", index=None)

        city = st.selectbox("**City**", car_data['City'].unique(), placeholder="Select City", index=None)
        seats = st.selectbox("**Seats**", sorted(car_data['Seats'].unique()), placeholder="Select Seats", index=None)
        color = st.selectbox("**Color**", car_data['Color'].unique(), placeholder="Select Color", index=None)
        Insurance_validity = st.selectbox("**Insurance Validity**", car_data['Insurance_Validity'].unique(), placeholder="Select Insurance Validity", index=None)


with col2:
    # ḍefine the predict button
    prediction = st.button("Predict :material/search_insights:" ,type='secondary'  ,use_container_width=True) 

    if prediction:
        # create a dataframe with the input values
        input_df = pd.DataFrame({
            "Fuel_Type": [fuel_type],
            "Body_Type" : [body_type],
            "transmission" : [transmission],
            "ownerNo" : [previous_owner],
            "Brand" : [brand],
            "model" : [model_car],
            "modelYear" : [year],
            "Insurance_Validity" : [Insurance_validity],
            "Kms_Driven" : [km_driven],
            "Mileage" : [mileage],
            "Engine" : [engine_size],
            "Seats" : [seats],
            "Color": [color],
            "City" : [city]
        })
        
        # model prediction          
        predict = model.predict(input_df)
        
        # display the prediction value
        # st.success(f"The estimated price of the car is : {predict[0]:,.2f}")
        st.markdown(f"""
                    <div style="
                        display : flex;
                        justify-content: center;
                        align-items: center;
                        font-size: 20px;
                        font-weight: bold;
                        height: 200px;
                        width: 300px;
                        background-color: #f0f0f5;
                        border: 1px solid #00cc00;
                        border-radius: 10px;
                        padding: 20px;
                    ">
                    The estimated price of the car is : ₹ {predict[0]:,.2f}
                    </div>
                    """, unsafe_allow_html=True)
        
        st.info("Note: The estimated price is based on the given input values and may not reflect the actual market price of the car.")
        