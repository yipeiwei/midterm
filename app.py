from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 模擬商品資料
products = [
    {"product": "商品 A", "price": 100, "content": "這是一個不錯的商品"},
    {"product": "商品 B", "price": 200, "content": "這是另一個不錯的商品"}
]

@app.route("/")
def index():
    return render_template("index.html", products=products)

@app.route("/product/<int:product_id>")
def product(product_id):
    if 0 <= product_id < len(products):
        return render_template("product.html", product=products[product_id])
    return "商品不存在", 404

@app.route("/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        product_name = request.form["product"]
        price = request.form["price"]
        content = request.form["content"]
        products.append({"product": product_name, "price": int(price), "content": content})
        return redirect(url_for("index"))
    return render_template("add_product.html")

if __name__ == "__main__":
    app.run(debug=True)
    
#yipeiwei@weipeiyideMacBook-Air blog_1014 % python3 app.py
#yipeiwei@weipeiyideMacBook-Air blog_1014 % cd ../midterm 
#yipeiwei@weipeiyideMacBook-Air midterm % ls -l
#yipeiwei@weipeiyideMacBook-Air midterm % python3 app.py

