from flask import Blueprint
from dataaccess import DataAccess
import utils as ut
import json


product_api = Blueprint('product_api', __name__)


@product_api.route('/product/get')
def getProducts():
    conf = ut.getConfig()
    da = DataAccess(conf)

    query = "select * from products"
    result = da.select_row(query)
    # print type(json.dumps(result))
    return json.dumps(result)

@product_api.route('/product/create', methods=['POST'])
def createProduct():
    p_name = request.json['name']
    p_desc = request.json['description']
    p_price = request.json['price']
    
    p_obj = dict(name=p_name, description=p_desc, price=p_price, status="ok")

    return json.dumps(p_obj)