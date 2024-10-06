<h1 align="center" style="font-family: Arial, sans-serif; color: #2C3E50;">🏡 HomePricePro 🏡</h1>

<p align="center" style="font-family: Arial; font-size: 18px; color: #34495E;">
  <strong>Predict house prices in Bangalore and Delhi using machine learning models and Flask.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-v3.8-blue" alt="Python 3.8">
  <img src="https://img.shields.io/badge/flask-v2.0.1-green" alt="Flask">
</p>

<h2 style="color: #2980B9;">✨ Features</h2>
<ul style="font-family: Arial; color: #7F8C8D;">
  <li>Predict house prices in multiple cities using trained models.</li>
  <li>Flask-based backend with machine learning model integration.</li>
  <li>Input parameters include: city, square footage, number of bathrooms, BHK, and location.</li>
  <li>Supports price prediction for Bangalore and Delhi.</li>
</ul>

<h2 style="color: #2980B9;">🚀 Demo</h2>
<p>You can run the application locally by following the <a href="#installation">Installation</a> instructions below.</p>

<h2 style="color: #2980B9;">💻 Technologies Used</h2>
<ul style="font-family: Arial; color: #7F8C8D;">
  <li><strong>Frontend:</strong> HTML, CSS, JavaScript, Bootstrap</li>
  <li><strong>Backend:</strong> Flask, NumPy, Pickle</li>
  <li><strong>Machine Learning Models:</strong> Pre-trained models for Bangalore and Delhi</li>
</ul>

<h2 id="installation" style="color: #2980B9;">⚙️ Installation</h2>
<h3 style="font-family: Arial; color: #34495E;">Prerequisites</h3>
<ul style="font-family: Arial; color: #7F8C8D;">
  <li>Python 3.x</li>
  <li>pip (Python package manager)</li>
</ul>

<h3 style="font-family: Arial; color: #34495E;">Steps</h3>
<ol style="font-family: Arial; color: #7F8C8D;">
  <li><strong>Clone the repository:</strong></li>
  <pre><code>git clone https://github.com/your-username/HomePricePro.git
cd HomePricePro</code></pre>

  <li><strong>Backend Setup:</strong></li>
  <pre><code># Create a virtual environment and install dependencies:
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt</code></pre>

  <p>Place the model files (<code>banglore_price_prediction_model.pickle</code>, <code>delhi_price_prediction_model.pickle</code>) and their respective columns files (<code>banglore_columns.json</code>, <code>delhi_columns.json</code>) in the <code>model/</code> directory.</p>

  <li><strong>Run the Flask Application:</strong></li>
  <pre><code>python app.py</code></pre>
  <p>The Flask server should be running at <code>http://127.0.0.1:5000</code>.</p>
</ol>

<h2 style="color: #2980B9;">📊 API Endpoints</h2>

<h3><code>/get_location_names</code> [GET]</h3>
<p>Fetches available location names for a given city.</p>
<ul style="font-family: Arial; color: #7F8C8D;">
  <li><strong>Parameters:</strong> <code>city</code> (e.g., 'benglore', 'delhi')</li>
</ul>
<pre><code>{
  "locations": ["location1", "location2", "location3"]
}</code></pre>

<h3><code>/predict_price</code> [POST]</h3>
<p>Predicts the price of a house based on user inputs.</p>
<ul style="font-family: Arial; color: #7F8C8D;">
  <li><strong>Parameters (form-data):</strong></li>
  <ul>
    <li><code>city</code>: City name</li>
    <li><code>sqft</code>: Square footage of the property</li>
    <li><code>location</code>: Location within the city</li>
    <li><code>bhk</code>: Number of bedrooms</li>
    <li><code>bath</code>: Number of bathrooms</li>
  </ul>
</ul>
<pre><code>{
  "estimated_price": 120.45
}</code></pre>

<h2 style="color: #2980B9;">📂 File Structure</h2>
<pre><code>HomePricePro/
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
│   └── script.js            # JavaScript with AJAX requests
├── requirements.txt         # Python dependencies
└── README.md                # This README file</code></pre>

<h2 style="color: #2980B9;">🔧 Future Improvements</h2>
<ul style="font-family: Arial; color: #7F8C8D;">
  <li>Add more cities for prediction.</li>
  <li>Improve models with more data.</li>
  <li>Deploy the app to a cloud platform (Heroku, AWS).</li>
  <li>Add input validation and error handling.</li>
</ul>


<h2>SCREENSHOTS</h2>
<h3 style="color: #2980B9;">📜 License</h3>
<p style="font-family: Arial; color: #7F8C8D;">This project is licensed under the MIT License.</p>
