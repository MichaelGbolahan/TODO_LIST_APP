from flask import Flask,render_template,redirect,url_for,flash,session,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config.from_pyfile('config.cfg')
app.config.from_pyfile('config.cfg')
app.config.from_pyfile('config.cfg')
db=SQLAlchemy(app)


class todo(db.Model):
    id=db.Column('todo_id',db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    done=db.Column(db.Boolean)


def __init__(self,name,done):
    self.name=name
    self.done=done

@app.route('/')
def home():
    todo_list=todo.query.all()
    return render_template('index.html',todo_list=todo_list)

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='POST':
        name=request.form['todo']
        add_name=todo(name=name,done=False)
        db.session.add(add_name)
        db.session.commit()
        return redirect(url_for('home'))


@app.route('/update/<int:id>')
def update(id):
    todos=todo.query.get(id)
    todos.done=not todos.done
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete(id):
    deletes=todo.query.get(id)
    db.session.delete(deletes)
    db.session.commit()
    return redirect(url_for('home'))



if __name__=='__main__':
    db.create_all()
    app.run(debug=False)