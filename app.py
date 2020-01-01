#!/usr/bin/env python 
from flask import Flask, jsonify, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

acronymnList = [
	{
		'acronymn': 'SSDS',
		'description': 'Ship Self Defense System'
	},
	{
		'acronymn': 'SEWIP',
		'description': 'Surface Electronic Warefare Improvement Program'
	},
	{
		'acronymn': 'PDASCM',
		'description': 'Pulse Doppler Anti Ship Cruise Missile'
	},
	{
		'acronymn': 'RAM',
		'description': 'Rolling Airframe Missile'
	},
	{
		'acronymn': 'ESSM',
		'description': 'Evolved Sea Sparrow Missile'
	}	
]

# ['SSDS', 'SEWIP', 'PDASCM', 'RAM', 'ESSM']
# @app.route('/acronymnList', methods=['GET'])
# def get_acronyms():
#     return jsonify({'list': acronymnList})


@app.route('/acronymnList/<string:acronymn>', methods=['GET'])
def get_acronym(acronymn): 
    found_acronymn_description = [this_acronymn['description'] for this_acronymn in acronymnList if this_acronymn['acronymn'] == acronymn]

    if found_acronymn_description == []:
    	return jsonify({'acronymn': ''})

    return jsonify({'acronymn': found_acronymn_description[0]})


if __name__ == '__main__':
	app.run(debug=True)

