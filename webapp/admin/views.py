from flask import Blueprint, render_template
#from flask_login import current_user, login_required
from webapp.user.decorators import admin_required
from webapp.user.models import Users

blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@blueprint.route('/')
@admin_required
def admin_index():
    global users_list
    title = "Администрирование"
    users_list = Users.query.all()
    return render_template('admin/admin.html', page_title=title, users_list=users_list)
    #return render_template('login.html', page_title=title)

