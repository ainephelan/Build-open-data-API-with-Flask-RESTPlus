from flask import Flask, g, request, jsonify
from flask_restplus import Api, Resource, fields
import sqlite3

app = Flask(__name__)
api = Api(app)

#Database helper
def connect_db():
    sql = sqlite3.connect('NSW_BIRTH_RATE.sqlite')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@api.route('/all')
class Language(Resource):
    def get(self):
        db = get_db()
        details_cur = db.execute('select YEAR, LOCALITY, SUBURB, STATE, POSTCODE, COUNT from NSW_BIRTH_RATE')
        details = details_cur.fetchall()

        return_values = []

        for detail in details:
            detail_dict = {}
            detail_dict['YEAR'] = detail['YEAR']
            detail_dict['LOCALITY'] = detail['LOCALITY']
            detail_dict['SUBURB'] = detail['SUBURB']
            detail_dict['STATE'] = detail['STATE']
            detail_dict['POSTCODE'] = detail['POSTCODE']
            detail_dict['COUNT'] = detail['COUNT']

            return_values.append(detail_dict)

        print(return_values)
        return return_values

@app.route('/details', methods=['GET'])
def get_details():
    db = get_db()
    details_cur = db.execute('select YEAR, LOCALITY, SUBURB, STATE, POSTCODE, COUNT from NSW_BIRTH_RATE')
    details = details_cur.fetchall()

    return_values = []

    for detail in details:
        detail_dict = {}
        detail_dict['YEAR']      = detail['YEAR']
        detail_dict['LOCALITY']  = detail['LOCALITY']
        detail_dict['SUBURB']    = detail['SUBURB']
        detail_dict['STATE']     = detail['STATE']
        detail_dict['POSTCODE']  = detail['POSTCODE']
        detail_dict['COUNT']     = detail['COUNT']

        return_values.append(detail_dict)

    return jsonify({'details' : return_values})

@app.route('/details/<string:SUBURB>', methods=['GET'])
def get_detail(SUBURB):
    db = get_db()
    details_cur = db.execute('select YEAR, LOCALITY, SUBURB, STATE, POSTCODE, COUNT from NSW_BIRTH_RATE where SUBURB = ?', [SUBURB])
    details = details_cur.fetchall()

    return_values = []

    for detail in details:
        detail_dict = {}
        detail_dict['YEAR']      = detail['YEAR']
        detail_dict['LOCALITY']  = detail['LOCALITY']
        detail_dict['SUBURB']    = detail['SUBURB']
        detail_dict['STATE']     = detail['STATE']
        detail_dict['POSTCODE']  = detail['POSTCODE']
        detail_dict['COUNT']     = detail['COUNT']

        return_values.append(detail_dict)

    return jsonify({'details' : return_values})


if __name__ == '__main__':
    app.run()