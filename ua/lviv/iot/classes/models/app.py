from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from ua.lviv.iot.classes.models.product import Product
from flask_marshmallow import Marshmallow
import os
import json
import copy


# with open('secrets.json') as f:
#     SECRET = json.load(f)

# SQLALCHEMY_TRACK_MODIFICATIONS = False
# DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
#     user=SECRET["user"],
#     password=SECRET["password"],
#     host=SECRET["host"],
#     port=SECRET["port"],
#     db=SECRET["db"]
#     )

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:J25k3l23@localhost:3306/labDB?use_pure=True'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class ExclusiveProduct(Product, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price_in_uah = db.Column(db.Float)
    producer = db.Column(db.String(100))
    shelf_life_in_days = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

    def __init__(self, price_in_uah=0.0, producer="not specified", shelf_life_in_days = 0, quantity = 0):
        super().__init__(price_in_uah, producer, shelf_life_in_days)
        self.quantity = quantity


class ExclusiveProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'price_in_uah', 'producer', 'shelf_life_in_days', 'quantity')


exclusive_product_schema = ExclusiveProductSchema()
exclusive_products_schema = ExclusiveProductSchema(many=True)


@app.route('/product', methods=['POST'])
def add_product():
    price_in_uah = request.json['price_in_uah']
    producer = request.json['producer']
    shelf_life_in_days = request.json['shelf_life_in_days']
    quantity = request.json['quantity']
    new_exclusive_product = ExclusiveProduct(price_in_uah, producer, shelf_life_in_days, quantity)
    db.session.add(new_exclusive_product)
    db.session.commit()
    return exclusive_product_schema.jsonify(new_exclusive_product)


@app.route('/product', methods=['GET'])
def get_products():
    all_products = ExclusiveProduct.query.all()
    result = exclusive_products_schema.dump(all_products)
    return jsonify({'all products': result})


@app.route("/product/<id_number>", methods=["GET"])
def get_product(id_number):
    exclusive_product = ExclusiveProduct.query.get(id_number)
    if not exclusive_product:
        abort(404)
    return exclusive_product_schema.jsonify(exclusive_product)


@app.route('/product/<id_number>', methods=['PUT'])
def update_product(id_number):
    exclusive_product = ExclusiveProduct.query.get(id_number)
    if not exclusive_product:
        abort(404)
    price_in_uah = request.json['price_in_uah']
    producer = request.json['producer']
    shelf_life_in_days = request.json['shelf_life_in_days']
    quantity = request.json['quantity']
    exclusive_product.price_in_uah = price_in_uah
    exclusive_product.producer = producer
    exclusive_product.shelf_life_in_days = shelf_life_in_days
    exclusive_product.quantity = quantity
    db.session.commit()
    return exclusive_product_schema.jsonify(exclusive_product)


@app.route('/product/<id_number>', methods=['DELETE'])
def delete_product(id_number):
    exclusive_product = ExclusiveProduct.query.get(id_number)
    if not exclusive_product:
        abort(404)
    db.session.delete(exclusive_product)
    db.session.commit()
    return exclusive_product_schema.jsonify(exclusive_product)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

