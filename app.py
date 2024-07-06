from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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

    def __repr__(self):
        return f"{self.srno} - {self.title}"

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form['title']
        dse = request.form['dse']
        todo = Todo(title=title, dse=dse)
        db.session.add(todo)
        db.session.commit()
    
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)

@app.route('/show')
def product():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'Hello Siddhesh, This is Product'

@app.route('/update/<int:srno>', methods=['GET', 'POST'])
def update(srno):
    if request.method == 'POST':
        title = request.form['title']
        dse = request.form['dse']
        todo = Todo.query.filter_by(srno=srno).first()
        todo.title=title
        todo.dse=dse
        db.session.add(todo)
        db.session.commit()
        return redirect("/")


    todo = Todo.query.filter_by(srno=srno).first()
    return render_template('update.html', todo=todo)


@app.route('/delete/<int:srno>')
def delete(srno):
    todo = Todo.query.filter_by(srno=srno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=7000)
