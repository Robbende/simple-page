from flask import Flask, render_template, request
from service import *
from dataaccess import DataAccess
import json

app = Flask(__name__, static_url_path='', static_folder='contents', template_folder='templates')

# register the api
app.register_blueprint(product_api, url_prefix="/api")


@app.route('/')
def main():
    prod_res = get_products()
    return render_template('index.html', products=prod_res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
