from webapp import create_app
from webapp.users_db import users_list

app = create_app()
with app.app_context():
    users_list()