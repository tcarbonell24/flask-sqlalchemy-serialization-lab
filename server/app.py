from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Customer, CustomerSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab 2</h1>'

@app.route('/customers')
def customers():
    customers = Customer.query.all()
    print(customers)
    response_body = CustomerSchema().dumps(customers)
    print(response_body)
    return make_response(response_body)

@app.route('/customers/<int:id>')
def customer(id):
    customer = Customer.query.filter(Customer.id == id).first()
    response_body = CustomerSchema().dump(customer)
    print(response_body)
    return make_response(response_body)

if __name__ == '__main__':
    app.run(port=5555, debug=True)