from webapp.test.models import Tests

@app.route("/test")
def index():
    title = "On-line тестирование"
    if current_user.is_authenticated:
        global users_list
        if current_user.is_admin:
            users_list = Users.query.all()
        else:
            users_list =''
    return render_template('test.html', page_title=title, users_list=users_list)