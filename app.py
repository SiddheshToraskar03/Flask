from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
# Make sure to set your database URI here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    srno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    dse = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.srno} - {self.title}"

@app.route('/')
def hello_world():
    return render_template('index.html')
    #return 'Hello, World!'

@app.route('/product')
def product():
    return 'Hello Siddhesh This is Product'

if __name__ == "__main__":
    app.run(debug=True, port=7000)
