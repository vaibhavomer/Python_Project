import html
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqllite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    #return 'Hello, World!'
    return render_template('index.html')

@app.route('/products')
def products():
    return 'This is product page'

if __name__ == "__main__":
    app.run(debug=True)
    
