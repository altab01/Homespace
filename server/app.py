from flask import Flask, request, jsonify
import controller

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    city = request.args.get('city')
    print(city)
    response = jsonify({
        'locations': controller.get_location_names(city)    
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_price', methods=['POST'])
def predict_price():
    city = request.form['city']
    sqft = float(request.form['sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': controller.predict_price(city, location, sqft, bath, bhk)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Server started")
    controller.load_saved_data()
    app.run(debug=True)


# from flask import Flask, request, jsonify
# import util

# app = Flask(__name__)

# @app.route('/get_location_names')
# def get_location_names():
#     try:
#         locations = util.get_location_names()
#         response = jsonify({'locations': locations})
#         response.headers.add('Access-Control-Allow-Origin', '*')
#         return response
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# @app.route('/predict_price', methods=['POST'])
# def predict_price():
#     try:
#         sqft = float(request.form['sqft'])
#         location = request.form['location']
#         bhk = int(request.form['bhk'])
#         bath = int(request.form['bath'])

#         estimated_price = util.predict_price(location, sqft, bath, bhk)
#         response = jsonify({'estimated_price': estimated_price})
#         response.headers.add('Access-Control-Allow-Origin', '*')
#         return response
#     except KeyError as e:
#         return jsonify({'error': f'Missing key: {str(e)}'}), 400
#     except ValueError as e:
#         return jsonify({'error': f'Invalid value: {str(e)}'}), 400
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == "__main__":
#     print("Server started")
#     try:
#         util.load_saved_data()
#         app.run()
#     except Exception as e:
#         print(f"Error: {str(e)}")
