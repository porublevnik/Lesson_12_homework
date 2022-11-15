import logging
from flask import Blueprint, render_template, request
from functions import get_search_result

logging.basicConfig(filename="basic.log", level=logging.INFO)

main = Blueprint('main', __name__, template_folder='templates', url_prefix='/')


@main.route('/')
def page_index():
    """Главная страница"""
    return render_template('index.html')


@main.route('/search')
def page_post_list():
    """страница с результатом поиска"""
    substr = request.args['s']
    search_result = get_search_result(substr)
    logging.info(f"Поиск по запросу {substr}")
    return render_template('post_list.html', s=substr, search_result=search_result)


