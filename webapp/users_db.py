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
    username = request.form.get('login')
    password = request.form.get('password')
    role = request.form.get('role')
    full_name = request.form.get('full_name')
    major = request.form.get('major')
    prof = request.form.get('prof')
    depart = request.form.get('depart')
