from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

video_put_arq = reqparse.RequestParser()
video_put_arq.add_argument("name", type=str, help="Name")

names = {"tim": {"age": 19, "gen": "masc"}, "tm": {"age": 24, "gen": "masc"}}

class HelloWord(Resource):
    def get(self, name, age):
        print(request.form['add'])
        return names[name]

    def post(self, name, age):
        arqs = video_put_arq.parse_args()
        return {"data": "Post"}
        
class HomePage(Resource):
    def get(self):
        return {"Hello": "From flask"}

api.add_resource(HelloWord, "/helloworld/<string:name>/<int:age>")
api.add_resource(HomePage, "/")

if __name__ == "__main__":
    app.run(debug=True)
