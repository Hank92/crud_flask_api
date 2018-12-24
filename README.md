# crud_flask_api

# Set up

Create virtual environment using conda

	conda create --name test python=3.6

Download httpie in mac os

	brew install httpie
	
# Call apis on terminal using httpie

Fetch all users

	http -v get localhost:5000/users 

Fetch user data with user id 1
	
	http -v get localhost:5000/user/1

Create user 
	
	http -v post localhost:5000/user id=3 name='sam' age=3 account_type= 'vip'

Remove user with user id 1

	http -v delete localhost:5000/user id=1 

Update user data with user id 2

	http -v put localhost:5000/user/2 name='sam' age=3 account_type='vip' 

 

