from flask import Flask, jsonify, request, g, Response, current_app
from flask_cors import CORS

users = {
	1: {
		'id' : 1,
		'name': 'tl',
		'age': 27,
		'account_type': 'premium'
	},
	2: {
		'id':2,
		'name': 'tina',
		'age':21,
		'account_type':'vip'
	}
}

def create_app():
	app = Flask(__name__)
	CORS(app)

	@app.route('/ping', methods=['GET'])
	def ping():
		return "pong"

	#fetch all the user data 	
	@app.route('/users', methods=['GET'])
	def all_users():
		return jsonify(list(users.values()))
	
	#fecth user with a specific id
	@app.route('/user/<int:id>', methods=['GET'])
	def get_user(id):
		return jsonify(users[id]) if id in users else ('', 404)
	
	#create user 
	@app.route('/user', methods=['POST'])
	def create_user():
		new_user = request.json
		users[int(new_user['id'])] = new_user
		return jsonify(users)
	
	#delete user
	@app.route('/user', methods=['DELETE'])
	def remove_user():
		delete_user = request.json
		del users[int(delete_user['id'])]
		return jsonify(users)
	
	#update user
	@app.route('/user/<int:id>', methods=['PUT'])
	def update_user(id):
		if id in users:
			update_user = request.json
			users[id] = update_user
			users[id]['id'] = id
			return jsonify(users)	
		else:
			return ('', 404)
	return app
