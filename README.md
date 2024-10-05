HomePricePro
HomePricePro is a web application that predicts house prices based on inputs like city, square footage, number of bathrooms, and bedrooms. The application uses a Flask-based backend and a machine learning model to estimate prices for cities like Bangalore and Delhi.

Features
Dynamic form for user inputs (City, BHK, Square Feet, Number of Bathrooms, Location)
Predict house prices in different cities
Backend API using Flask and pre-trained machine learning models
Supports multiple cities (currently Bangalore and Delhi)
Table of Contents
Demo
Technologies Used
Installation
Usage
API Endpoints
File Structure
Future Improvements
Contributing
License
Demo
You can run the application locally by following the installation instructions below.

Technologies Used
Frontend:
HTML
CSS
JavaScript (AJAX)
Bootstrap 5
Backend:
Flask
NumPy
Pickle
Machine Learning Models:
Pre-trained models for Bangalore and Delhi
Installation
Prerequisites
Python 3.x
pip (Python package manager)
Node.js (Optional for frontend build tools)
Steps
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/HomePricePro.git
cd HomePricePro
Backend Setup:

Create a virtual environment and install dependencies:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
Place the model files (banglore_price_prediction_model.pickle, delhi_price_prediction_model.pickle) and their respective columns files (banglore_columns.json, delhi_columns.json) in the model/ directory.

Frontend Setup: No additional setup is needed for the frontend. The necessary JavaScript and Bootstrap files are already linked in the HTML.

Run the Flask Application:

bash
Copy code
python app.py
The Flask server should be running at http://127.0.0.1:5000.

Usage
Once the server is running, navigate to http://127.0.0.1:5000 in your browser.
Select a city, square footage, number of bathrooms, BHK, and location from the form.
Click on the "Predict Price" button to get the estimated price.
API Endpoints
1. /get_location_names [GET]
Fetches the available location names for a given city.

Parameters:

city: The city for which you want to fetch locations (e.g., benglore, delhi).
Response:

json
Copy code
{
  "locations": ["location1", "location2", "location3"]
}
2. /predict_price [POST]
Predicts the price of a house based on the inputs.

Parameters (form-data):

city: City name (benglore, delhi)
sqft: Square footage of the property
location: Location within the city
bhk: Number of bedrooms
bath: Number of bathrooms
Response:

json
Copy code
{
  "estimated_price": 120.45
}
File Structure
graphql
Copy code
HomePricePro/
│
├── app.py                  # Main Flask application
├── controller.py            # Controller with prediction logic and location fetch
├── model/
│   ├── banglore_price_prediction_model.pickle
│   ├── delhi_price_prediction_model.pickle
│   ├── banglore_columns.json
│   └── delhi_columns.json
├── templates/
│   └── index.html           # Frontend HTML
├── static/
│   ├── style.css            # CSS for frontend
│   ├── script.js            # JavaScript with AJAX requests
├── requirements.txt         # Python dependencies
└── README.md                # This README file
Future Improvements
Add more cities to the prediction model
Improve machine learning models with updated datasets
Add validation for user inputs
Deployment on a cloud platform (e.g., Heroku, AWS)
