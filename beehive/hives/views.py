from flask import Blueprint, render_template

from .models import Hive

hives = Blueprint('hives', __name__, template_folder='templates')

@hives.route('/')
def hive_list():
    hives = Hive.query.all()
    return render_template('hive_list.html', hives=hives)