from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, Client

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/banktop2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from flask import Flask, render_template, request, redirect, url_for
from models import db, Client

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/banktop2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    clients = Client.query.all()
    return render_template('index.html', clients=clients)

@app.route('/add_client', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        surname = request.form['surname']
        name = request.form['name']
        middle_name = request.form['middle_name']
        new_client = Client(surname=surname, name=name, middle_name=middle_name)
        db.session.add(new_client)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_client.html')

@app.route('/update_client/<int:client_id>', methods=['GET', 'POST'])
def update_client(client_id):
    client = Client.query.get(client_id)
    if request.method == 'POST':
        client.surname = request.form['surname']
        client.name = request.form['name']
        client.middle_name = request.form['middle_name']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update_client.html', client=client)

@app.route('/delete_client/<int:client_id>', methods=['POST'])
def delete_client(client_id):
    client = Client.query.get(client_id)
    if client:
        db.session.delete(client)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


@app.route('/')
def index():
    clients = Client.query.all()
    return render_template('index.html', clients=clients)

@app.route('/add_client', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        surname = request.form['surname']
        name = request.form['name']
        middle_name = request.form['middle_name']
        new_client = Client(surname=surname, name=name, middle_name=middle_name)
        db.session.add(new_client)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_client.html')

@app.route('/update_client/<int:client_id>', methods=['GET', 'POST'])
def update_client(client_id):
    client = Client.query.get(client_id)
    if request.method == 'POST':
        client.surname = request.form['surname']
        client.name = request.form['name']
        client.middle_name = request.form['middle_name']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update_client.html', client=client)


@app.route('/delete_client/<int:client_id>', methods=['POST'])
def delete_client(client_id):
    client = Client.query.get(client_id)
    if client:
        db.session.delete(client)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
