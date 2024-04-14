from flask import Flask, render_template, request
from iris_predict import predict_iris
import psycopg2

app = Flask(__name__)

# Global database connection
connection = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="127.0.0.1",
    port="5432"
)

def get_data_from_postgresql():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM iris_data")
    data = cursor.fetchall()
    cursor.close()
    return data

@app.route('/')
def index():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form data
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        # Make prediction
        features = [sepal_length, sepal_width, petal_length, petal_width]
        prediction = predict_iris(features)

        # Connect to the database
        cursor = connection.cursor()

        # Insert form data and predicted species into the database
        cursor.execute("INSERT INTO iris_data (sepal_length, sepal_width, petal_length, petal_width, species) VALUES (%s, %s, %s, %s, %s)",
                       (sepal_length, sepal_width, petal_length, petal_width, prediction))
        connection.commit()
        cursor.close()

        return render_template('index.html', prediction=prediction)

    except Exception as e:
        # Handle any errors
        return render_template('error.html', error=str(e))

@app.route('/show')
def show():
    data = get_data_from_postgresql()
    return render_template('show.html', data=data)

@app.route('/remove', methods=['POST'])
def remove_data():
    try:
        # Get ID of the row to be removed
        id = int(request.form['id'])

        # Connect to the database
        cursor = connection.cursor()

        # Execute SQL query to delete the row
        cursor.execute("DELETE FROM iris_data WHERE id = %s", (id,))
        connection.commit()

        cursor.close()
        
        # Get updated data
        data = get_data_from_postgresql()
        
        return render_template('show.html', data=data)
    

    except Exception as e:
        # Handle any errors
        return render_template('error.html', error=str(e))




if __name__ == '__main__':
    app.run(debug=True)
