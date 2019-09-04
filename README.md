# Top Baby Suburbs

<h6>NSWBirthRateDatabasePrep.py</h6>
Basic Python program which prepares the database containing NSW birthrate information per suburb.

<h6>app.py</h6>

Flask program which uses Flask-RESTPlus to produce APIs which exposes NSW birth rate data residing in the database.



  
  
1. Data Extraction from data.nsw.gov.au (NSWBirthRate.txt)  
2. Data Ingestion to SQLite database (PyCharm, DB Broswer for SQLite, NSWBirthRateDatabasePrep.py)  
    - Clone gitlab repo in PyCharm
    - Delete existing DB
    - Connect python interpreter
    - Run the NSWBirthRateDatabasePrep.py to create and load text file data

3. Build an API using Flask-RESTPlus (PyCharm, app.py)  
    - Run app.py to expose the api

4. Data Consumption (swagger, ngrok, Postman)
    - Url in the results (http://127.0.0.1:5000/) to access the data (swagger.json flask-restplus data service that allows a client to consume the api)
    - In terminal run the below to establish secure tunnel from a public endpoint to my locally running network service while capturing all traffic for detailed inspection and replay
      ./ngrok http 5000
        - Paste the generated public endpoint url/all or e.g. url/all/leichhardt into browser to get the data
        - Postman, get: above-generated url/all
