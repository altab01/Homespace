<h1 align="center">HomePricePro</h1>

<p align="center">
  <strong>A Web Application for Predicting House Prices</strong><br>
  Predict house prices in Bangalore and Delhi using machine learning models and Flask.
</p>

<h2>Features</h2>
<ul>
  <li>Predict house prices in multiple cities.</li>
  <li>Flask backend with machine learning model integration.</li>
  <li>Input parameters: city, square footage, number of bathrooms, BHK, location.</li>
  <li>Supports price prediction for cities like Bangalore and Delhi.</li>
</ul>

<h2>Demo</h2>
<p>You can run the application locally by following the <a href="#installation">Installation</a> instructions.</p>

<h2>Technologies Used</h2>
<ul>
  <li><strong>Frontend:</strong> HTML, CSS, JavaScript, Bootstrap</li>
  <li><strong>Backend:</strong> Flask, NumPy, Pickle</li>
  <li><strong>Machine Learning Models:</strong> Pre-trained models for Bangalore and Delhi</li>
</ul>

<h2 id="installation">Installation</h2>
<h3>Prerequisites</h3>
<ul>
  <li>Python 3.x</li>
  <li>pip (Python package manager)</li>
</ul>

<h3>Steps</h3>
<ol>
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

<h2>Usage</h2>
<ol>
  <li>Once the server is running, open <code>http://127.0.0.1:5000</code> in your browser.</li>
  <li>Fill in the form by selecting a city, square footage, number of bathrooms, BHK, and location.</li>
  <li>Click on the "Predict Price" button to get the estimated price of the house.</li>
</ol>

<h2>API Endpoints</h2>

<h3>1. <code>/get_location_names</code> [GET]</h3>
<p>Fetches the available location names for a given city.</p>
<p><strong>Parameters:</strong></p>
<ul>
  <li><code>city</code>: The city for which you want to fetch locations (e.g., <code>benglore</code>, <code>delhi</code>).</li>
</ul>

<p><strong>Response:</strong></p>
<pre><code>{
  "locations": ["location1", "location2", "location3"]
}</code></pre>

<h3>2. <code>/predict_price</code> [POST]</h3>
<p>Predicts the price of a house based on user inputs.</p>
<p><strong>Parameters (form-data):</strong></p>
<ul>
  <li><code>city</code>: City name (<code>benglore</code>, <code>delhi</code>)</li>
  <li><code>sqft</code>: Square footage of the property</li>
  <li><code>location</code>: Location within the city</li>
  <li><code>bhk</code>: Number of bedrooms</li>
  <li><code>bath</code>: Number of bathrooms</li>
</ul>

<p><strong>Response:</strong></p>
<pre><code>{
  "estimated_price": 120.45
}</code></pre>

<h2>File Structure</h2>
<pre><code>HomePricePro/
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
│   └── script.js            # JavaScript with AJAX requests
├── requirements.txt         # Python dependencies
└── README.md                # This README file</code></pre>

<h2>Future Improvements</h2>
<ul>
  <li>Add more cities for prediction.</li>
  <li>Improve models with more data.</li>
  <li>Deploy the app to a cloud platform (Heroku, AWS).</li>
  <li>Add input validation and error handling.</li>
</ul>

<h2>License</h2>
<p>This project is licensed under the MIT License.</p>
