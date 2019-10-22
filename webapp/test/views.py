from flask import Blueprint
from flask_login import current_user, login_required
#from webapp.test.models import Depart

blueprint = Blueprint('test', __name__, url_prefix='/test')

@blueprint.route("/test")
def test_index():
    title = "Работа с тестами"
    if current_user.is_authenticated:
        return "Меню работы с тестами!"
        if current_user.is_admin:
            users_list = Users.query.all()
        else:
            users_list =''
    return render_template('test.html', page_title=title)