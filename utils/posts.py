from config import BASE_URL
from utils.steps import send_get_request, send_post_request, send_put_request, send_delete_request
from models.post import Post
import allure
from pydantic import ValidationError

class Posts:
    def __init__(self, session):
        self.session = session
        self.url = f"{BASE_URL}/posts"
        print(f"Base URL is set to: {self.url}")

    @allure.step("Получаем посты с параметром {params}")
    def get_posts(self, params=None, validate=True):
        """
        Получаем посты и опционально проверяем их на валидацию с помощью Pydantic.
        Параметр validate управляет проверкой.
        """
        print(f"GET Request to URL: {self.url}, with params: {params}")
        response = send_get_request(self.session, self.url, params=params)

        if validate:
            try:
                posts = [Post(**post_data) for post_data in response.json()]
            except ValidationError as e:
                raise AssertionError(f"Ошибка валидации постов: {e}")
            return response, posts

        return response, response.json()  # Если валидация отключена, возвращаем просто JSON-ответ

    @allure.step("Создаем новый пост")
    def create_post(self, data, validate=True):
        """
        Создаем пост и опционально проверяем ответ на валидацию с помощью Pydantic.
        Параметр validate управляет проверкой.
        """
        response = send_post_request(self.session, self.url, data)

        if validate:
            try:
                post = Post(**response.json())
            except ValidationError as e:
                raise AssertionError(f"Ошибка валидации созданного поста: {e}")
            return response, post

        return response, response.json()  # Если валидация отключена, возвращаем просто JSON-ответ

    @allure.step("Обновляем пост с ID={post_id}")
    def update_post(self, post_id, data, validate=True):
        """
        Обновляем пост и опционально проверяем ответ на валидацию с помощью Pydantic.
        Параметр validate управляет проверкой.
        """
        response = send_put_request(self.session, f"{self.url}/{post_id}", data)

        if validate:
            try:
                post = Post(**response.json())
            except ValidationError as e:
                raise AssertionError(f"Ошибка валидации обновленного поста: {e}")
            return response, post

        return response, response.json()  # Если валидация отключена, возвращаем просто JSON-ответ

    @allure.step("Удаляем пост с ID={post_id}")
    def delete_post(self, post_id):

        response = send_delete_request(self.session, f"{self.url}/{post_id}")
        return response
