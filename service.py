from flask import Blueprint, request
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
    try:
        p_name = request.json['name']
        p_desc = request.json['description']
        p_price = request.json['price']

        p_int_price = float(p_price)

        conf = ut.getConfig()
        da = DataAccess(conf)

        query = "INSERT INTO products (`name`, `description`, `price`) VALUES ('{0}', '{1}', {2})".format(p_name, p_desc, str(p_price))
        print query
        da.execute_query(query)

        p_obj = dict(success=True, error="")
    except Exception as ex:
        p_obj = dict(success=False, error=str(ex))

    return json.dumps(p_obj)