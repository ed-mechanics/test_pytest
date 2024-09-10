import allure

class Assertions:

    @staticmethod
    @allure.step("Проверяем статус код: ожидаемый {expected_status}, фактический {actual_status}")
    def assert_status_code(actual_status, expected_status):
        assert actual_status == expected_status, (
            f"Ожидался статус {expected_status}, но получен {actual_status}"
        )

    @staticmethod
    @allure.step("Проверяем, что все посты принадлежат userId={user_id}")
    def assert_all_posts_belong_to_user(posts, user_id):
        for post in posts:
            assert post.userId == user_id, (
                f"Ожидалось, что post с ID={post.id} будет иметь userId={user_id}, но получен userId={post.userId}"
            )

    @staticmethod
    @allure.step("Проверяем содержимое поста")
    def assert_post_data(post, expected_data):
        assert post.title == expected_data["title"], (
            f"Ожидался заголовок '{expected_data['title']}', но получен '{post.title}'"
        )
        assert post.body == expected_data["body"], (
            f"Ожидалось содержимое '{expected_data['body']}', но получено '{post.body}'"
        )
        assert post.userId == expected_data["userId"], (
            f"Ожидался userId {expected_data['userId']}, но получен {post.userId}"
        )

    @classmethod
    def assert_error_message(cls, response, expected_error):
        pass
