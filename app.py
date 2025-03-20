from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Client, Account

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
    if not client:
        return redirect(url_for('index'))
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
        Account.query.filter_by(client_id=client_id).delete()
        db.session.delete(client)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/client/<int:client_id>')
def client_details(client_id):
    client = Client.query.get_or_404(client_id)
    accounts = Account.query.filter_by(client_id=client_id).all()
    return render_template('client_details.html', client=client, accounts=accounts)

@app.route('/client/<int:client_id>/add_account', methods=['GET', 'POST'])
def add_account(client_id):
    if request.method == 'POST':
        account_number = request.form['account_number']
        deposit_amount = request.form['deposit_amount']
        deposit_term = request.form['deposit_term']
        deposit_date = request.form['deposit_date']
        interest_rate = request.form['interest_rate']

        new_account = Account(
            account_number=account_number,
            deposit_amount=deposit_amount,
            deposit_term=deposit_term,
            deposit_date=deposit_date,
            interest_rate=interest_rate,
            client_id=client_id
        )

        db.session.add(new_account)
        db.session.commit()
        return redirect(url_for('client_details', client_id=client_id))

    return render_template('add_account.html', client_id=client_id)

@app.route('/account/<int:account_id>')
def account_details(account_id):
    account = Account.query.get_or_404(account_id)
    return render_template('account_details.html', account=account)

@app.route('/account/<int:account_id>/edit', methods=['GET', 'POST'])
def update_account(account_id):
    account = Account.query.get_or_404(account_id)  
    if request.method == 'POST':
        account.account_number = request.form['account_number']
        account.deposit_amount = request.form['deposit_amount']
        account.deposit_term = request.form['deposit_term']
        account.deposit_date = request.form['deposit_date']
        account.interest_rate = request.form['interest_rate']
        db.session.commit()
        return redirect(url_for('account_details', account_id=account.account_id))
    return render_template('update_account.html', account=account)

@app.route('/account/<int:account_id>/delete', methods=['POST'])
def delete_account(account_id):
    account = Account.query.get_or_404(account_id)
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('client_details', client_id=account.client_id))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
