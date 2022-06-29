from flask import Flask, jsonify, request # jsonify is to convert python dict to json
from flask_restful import Resource, Api

# initial the flask app and assign as an API
app = Flask(__name__)
api = Api(app)

'''
The class acts as an API resource
'''
@app.route('/', methods=['GET'])  
def getStatus():
    try:
        return {'data': 'Api running'}
    except(error): 
        return {'data': error}

@app.route('/add/', methods=['POST'])
def getAdd():
    req_json = request.json
    num1 = req_json['num1']
    num2 = req_json['num2']
    return jsonify({"result": num1.type()})

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