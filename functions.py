import json
from json import JSONDecodeError


def load_posts():
    """Загружает файл с постами и преобразует из формата JSON"""
    try:
        with open('posts.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print('Файл posts.json отсутствует')
    except JSONDecodeError:
        print("Файл posts.json не удается преобразовать")


def get_search_result(key):
    """Из файла с постами получает список постов, содержащих поисковой запрос"""
    search_result = []
    for item in load_posts():
        if key.lower() in item['content'].lower():
            search_result.append(item)
    return search_result


def save_picture(picture):
    """Сохраняет изображение в папку images"""
    filename = picture.filename.replace(' ', '_')
    file_type = filename.split('.')[-1]
    if file_type not in ['jpg', 'jpeg', 'png']:
        return
    picture.save(f'./uploads/images/{filename}')
    return f'uploads/images/{filename}'


def add_post(post):
    """Добавляет в список постов новый пост"""
    posts = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)
    return post
