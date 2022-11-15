import logging
from flask import Blueprint, render_template, request, send_from_directory
from functions import save_picture, add_post

logging.basicConfig(filename="basic.log", level=logging.INFO)

loader = Blueprint('loader', __name__, template_folder='templates', url_prefix='/')


@loader.route("/post")
def page_post_form():
    """Страница с формой добавления поста"""
    return render_template('post_form.html')


@loader.route("/post", methods=["POST"])
def page_post_upload():
    """Страница, отображающая добавление поста"""
    post_content = request.form['content']
    post_picture = request.files.get('picture')

    if not post_picture or not post_content:
        logging.info(f"Ошибка при загрузке файла")
        return f"Данные не загружены! {render_template('post_form.html')}"

    picture_path = save_picture(post_picture)
    if not picture_path:
        logging.info("Не изображение!")
        return f"Не изображение! {render_template('post_form.html')}"

    post = {"pic": picture_path, "content": post_content}
    post = add_post(post)

    return render_template('post_uploaded.html', post=post)


@loader.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory('uploads', path)