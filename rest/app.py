from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SECRET_KEY'] = "123456"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:123456@localhost/car_bd"
db = SQLAlchemy(app)
ma = Marshmallow(app)

class ChemistryItem(db.Model):
    __tablename__ = 'chemistry'
    id = db.Column(db.Integer, primary_key=True)
    type_of_object = db.Column(db.Integer, unique=False, nullable=False)
    name = db.Column(db.String(64), unique=False, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)
    balance_in_stock = db.Column(db.Integer, unique=False, nullable=False)
    brand = db.Column(db.String(64), unique=False, nullable=False)

class ChemistryItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'type_of_object', 'name', 'price', 'balance_in_stock', 'brand')


@app.route("/", methods=["GET"])
def get_chemistryItems():
    chemistryItems = ChemistryItem.query.all()
    return jsonify(ChemistryItemSchema(many=True).dump(chemistryItems))


@app.route("/<id>", methods=["GET"])
def get_chemistryItem(id):
    chemistryItem = ChemistryItem.query.get(id)
    if not chemistryItem:
        abort(404)
    return jsonify(ChemistryItemSchema().dump(chemistryItem))


@app.route("/", methods=["POST"])
def add_chemistryItem():
    chemistryItem = ChemistryItem(type_of_object=request.json["type_of_object"],
                                  name=request.json["name"],
                                  price=request.json["price"],
                                  balance_in_stock=request.json["balance_in_stock"],
                                  brand=request.json["brand"])
    db.session.add(chemistryItem)
    db.session.commit()
    return jsonify(ChemistryItemSchema().dump(chemistryItem))


@app.route("/<id>", methods=["DELETE"])
def delete_chemistryItem(id):
    chemistryItem = ChemistryItem.query.get(id)
    if not chemistryItem:
        abort(404)
    db.session.delete(chemistryItem)
    db.session.commit()
    return jsonify(success=True)


@app.route("/<id>", methods=["PUT"])
def update_chemistryItem(id):
    chemistryItem = ChemistryItem.query.get(id)
    if not chemistryItem:
        abort(404)
    chemistryItem.type_of_object = request.json["type_of_object"]
    chemistryItem.name = request.json["name"]
    chemistryItem.price = request.json["price"]
    chemistryItem.balance_in_stock = request.json["balance_in_stock"]
    chemistryItem.brand = request.json["brand"]
    db.session.commit()
    return jsonify(success=True)


if __name__ == '__main__':
    app.run(debug=True)