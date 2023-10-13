from flask import Flask,jsonify,request
from models import db
from services import UserService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def say():
    return "hello"

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email=data.get('email')
    phone=data.get('phone')
    refer=data.get('refer')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Both username and password are required'}), 400

    user = UserService.create_user(username, password)
    return jsonify({'message': 'User created successfully', 'user': user}), 201

if __name__ == '__main__':
    app.run(debug=True)









# ===============================================================================

# from flask import Flask,jsonify,render_template

# app = Flask(__name__)


 
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# # Example of return a template



# # print(__name__)
# if __name__== "__main__":
#  app.run(debug=True,port=8001)

