from flask import Flask, jsonify # jsonify is to convert python dict to json
from flask_restful import Resource, Api

# initial the flask app and assign as an API
app = Flask(__name__)
api = Api(app)

'''
The class acts as an API resource
'''
class status(Resource):    
     def get(self):
         try:
            return {'data': 'Api running'}
         except(error): 
            return {'data': error}

class Sum(Resource):
    def get(self, a, b):
        return jsonify({'data': a+b})

# add it in the api resources
api.add_resource(status,'/')
api.add_resource(Sum,'/add/<int:a>,<int:b>')

'''
There is a concept of Cross-Origin in case of APIs’.
It means that even if we have developed our API with python,
Other origins(languages like Javascript, React) can also access our API.
So, we will also import CORS and assign our app as an CORS app.
'''

'''
If you are confused what procfile is:
google it, it is basically a file that works directly and specifically with Heroku
'''

if __name__ == '__main__':
    app.run(debug=True)