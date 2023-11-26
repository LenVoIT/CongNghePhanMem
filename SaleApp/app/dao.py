#File để truy vấn database
from app.models import Category, Product, User
from app import app
import hashlib


def load_categories():
    return Category.query.all()


def load_products(kw=None, cate_id=None, page=None):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))

    if page:
        page = int(page) #ép về kiểu int
        page_size = app.config['PAGE_SIZE']
        start = (page - 1) * page_size #vị trí bắt đầu
        return products.slice(start, start + page_size) #lấy từ vị trí start đến n phần tử đã được xác định

    return products.all()


def get_user_by_id(id):
    return User.query.get(id)


def count_products():
    return Product.query.count()

def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()),
                            User.password.__eq__(password)).first()