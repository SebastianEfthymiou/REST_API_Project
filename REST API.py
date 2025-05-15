from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'productdb'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_PORT'] = 3307

mysql = MySQL(app)

# ------------------ GET Requests ------------------

@app.route('/products', methods=['GET'])
def get_products():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    return jsonify(products)

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products WHERE id = %s", (id,))
    product = cur.fetchone()
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

# ------------------ POST Requests ------------------

@app.route('/products/add', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get("name")
    price = data.get("price")
    stock = data.get("stock")

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", (name, price, stock))
    mysql.connection.commit()
    return jsonify({"message": "Product added successfully"}), 201

@app.route('/products/addbulk', methods=['POST'])
def add_products_bulk():
    data = request.get_json()
    cur = mysql.connection.cursor()
    for item in data:
        cur.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)",
                    (item["name"], item["price"], item["stock"]))
    mysql.connection.commit()
    return jsonify({"message": "Bulk products added"}), 201

# ------------------ PUT Requests ------------------

@app.route('/products/update/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    name = data.get("name")
    price = data.get("price")
    stock = data.get("stock")

    cur = mysql.connection.cursor()
    cur.execute("UPDATE products SET name=%s, price=%s, stock=%s WHERE id=%s", (name, price, stock, id))
    mysql.connection.commit()
    return jsonify({"message": "Product updated"})

@app.route('/products/update/<int:id>/stock', methods=['PUT'])
def update_stock(id):
    data = request.get_json()
    stock = data.get("stock")

    cur = mysql.connection.cursor()
    cur.execute("UPDATE products SET stock=%s WHERE id=%s", (stock, id))
    mysql.connection.commit()
    return jsonify({"message": "Stock updated"})

# ------------------ DELETE Requests ------------------

@app.route('/products/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM products WHERE id=%s", (id,))
    mysql.connection.commit()
    return jsonify({"message": "Product deleted"})

@app.route('/products/delete/all', methods=['DELETE'])
def delete_all_products():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM products")
    mysql.connection.commit()
    return jsonify({"message": "All products deleted"})

# ------------------ Run App ------------------

if __name__ == "__main__":
    app.run(debug=True)
