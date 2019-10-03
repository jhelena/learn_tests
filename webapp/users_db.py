import requests
from webapp.model import db, Users
from bs4 import BeautifulSoup

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print ("Сетевая ошибка")
        return False

def users_list():
    #html = get_html("localhost:5000/templates/sign_up.html")
    #if html:
    username = request.form.get('login')
    password = request.form.get('password')
    role = request.form.get('role')
    full_name = request.form.get('full_name')
    major = request.form.get('major')
    prof = request.form.get('prof')
    depart = request.form.get('depart')
    save_users(username, password, role, full_name, major, prof, depart)
	
def save_users(username, password, role, full_name, major, prof, depart):
    new_users = Users(username=username, password=password, role=role, full_name=full_name, id_major=major, id_prof=prof, id_depart=depart)
    db.session.add(new_users)
    db.session.commit()