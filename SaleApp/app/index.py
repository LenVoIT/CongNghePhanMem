import math

from flask import render_template, request, redirect, session, jsonify
import dao
import utils
from app import app, login
from flask_login import login_user


@app.route('/')
def index():
    kw = request.args.get('kw')

    cate_id = request.args.get('cate_id')
    # # cates = dao.load_categories()
    page = request.args.get('page')
    #
    total = dao.count_products()  # tổng số lượng trên database
    pages= app.config["PAGE_SIZE"] #số lượng trên 1 trang
    products = dao.load_products(kw=kw, cate_id=cate_id, page=page)
    #
    return render_template('index.html', products=products,
                           pages=math.ceil(total / app.config['PAGE_SIZE']))  # số lượng trên 1 trang


# @app.route('/admin/login', methods=['post'])
# def admin_login():
#      = request.form.get('username')
#      request.form.get('password')
#
#     user= dao.auth_user(username=username,password=password)
#     if user: # khác null
#         login_user(user=user)
#     return redirect('/admin')
@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)


@app.route('/api/cart', methods=['post'])
def add_cart():
    cart = session.get('cart')  # Lấy giỏ
    if cart is None:  # kiểm tra có giỏ chưa
        cart = {}

    data = request.json
    id = str(data.get('id'))

    if id in cart:  # sản phẩm đã có trong giỏ
        cart[id]["quantity"] = cart[id]["quantity"] + 1
    else:  # sản phẩm chưa có trong giỏ
        cart[id] = {
            "id": id,
            "name": data.get('name'),
            "price": data.get('price'),
            "quantity": 1
        }
    # lưu vô session
    session['cart'] = cart

    return jsonify(utils.count_cart(cart))

@app.route('/cart')
def cart_list():
    return render_template('cart.html')


@app.context_processor  # gắn tất cả response => danh mục Mobile, Tablet lên header
def common_res():
    return {
        'categories': dao.load_categories(),
        'cart': utils.count_cart(session.get('cart'))
    }


@app.route('/admin/login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.auth_user(username=username, password=password)
    if user:  # khác null
        login_user(user=user)
    return redirect('/admin')


if __name__ == '__main__':
    from app import admin

    app.run(debug=True)  # xuất lỗi ra
