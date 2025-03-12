from flask import Flask
from models.user import User
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretKey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

@app.route("/helloworld", methods=["GET"])
def helloWorld():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)

