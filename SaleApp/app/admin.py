from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from app import app, db
from app.models import Category, Product

admin = Admin(app=app, name='Trang Admin', template_mode='bootstrap4')


class MyProductView(ModelView):
    column_list = ['id', 'name', 'price', 'category']
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['price', 'name']
    column_editable_list = ['name', 'price']
    details_modal = True
    edit_modal = True
    can_view_details = True

class MyCategoryView(ModelView):
    column_list = ['name', 'products']


class StatsView(BaseView):
    @expose("/")
    def index(self):
        return self.render('admin/stats.html')



admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(StatsView(name='Thống kê báo cáo'))