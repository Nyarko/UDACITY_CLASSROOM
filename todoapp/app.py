from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:66Oh!6My!6@localhost:5432/todoapp'
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

db.create_all()

@app.route('/todos/create', methods=['POST'])
def create_todo():
    description = request.get_json()['description']

    #USING description ABOVE TO CREATE A NEW TODO OBJECT
    todo = Todo(description=description)

    ##THIS STARTS CREATING OBJECT, AS A PENDING CHANGE
    db.session.add(todo)

    ##THIS ONE FINALY MAKES THE CHANGE REFLECT ON THE DB
    db.session.commit()

    ##SINCE WE'RE USING JSON NOW, JSONIFY FROM FLAS WILL BE USED
    ##JSONIFY FROM FLASK WILL TAKE CARE OF LOADING PAGES ON CHANGES MADE
    return jsonify()


@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())

##Just in case you wanna use python to run
if __name__ == '__main__':
   app.run(host="0.0.0.0", port=3000)