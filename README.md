#Web service Machine Learning using scikit-learn and Flask | Model Iris | Database using PostgreSQL

This repository is the code for the web service machine learning using scikit-learn and Flask. The model used is the Iris dataset. The database used is PostgreSQL.

## Installation
1. Install the required libraries
```bash
pip install -r requirements.txt
```

2. Install PostgreSQL
```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```

3. Start PostgreSQL
```bash
sudo service postgresql start
```

4. Login to PostgreSQL
```bash
sudo -u postgres psql
```

5. Create a database
```bash
CREATE DATABASE iris;
```

6. Create a table
```bash
CREATE TABLE iris_data (
    id SERIAL PRIMARY KEY,
    sepal_length FLOAT NOT NULL,
    sepal_width FLOAT NOT NULL,
    petal_length FLOAT NOT NULL,
    petal_width FLOAT NOT NULL,
    species VARCHAR(50) NOT NULL
);
```

7. Exit PostgreSQL
```bash
\q
```

8. Run the application
```bash
python app.py
```

9. Open your browser and go to `http://localhost:5000`

## Usage
1. Open your browser and go to `http://localhost:5000`
2. Enter the sepal length, sepal width, petal length, and petal width
3. Click `Predict` button
4. The predicted species will be shown

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgements
- [Building a Machine Learning Web API with Flask and scikit-learn](https://www.youtube.com/watch?v=UbCWoMf80PY)
- [How to install PostgreSQL on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)


