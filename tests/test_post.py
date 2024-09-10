import pytest
import allure
from utils.posts import Posts
from utils.assertions import Assertions

@allure.feature('GET /posts')
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_posts(session, user_id):
    posts = Posts(session)
    response, posts_data = posts.get_posts(params={"userId": user_id})
    Assertions.assert_status_code(response.status_code, 200)
    Assertions.assert_all_posts_belong_to_user(posts_data, user_id)

@allure.feature('POST /posts - негативные сценарии - отсутствие полей')
@pytest.mark.parametrize("invalid_data, expected_error", [
    ({"body": "bar", "userId": 1}, "Required title"),
    ({"title": "foo", "userId": 1}, "Required body"),
    ({"title": "foo", "body": "bar"}, "Required userId"),
])
def test_create_post_with_invalid_data(session, invalid_data, expected_error):
    posts = Posts(session)
    response, _ = posts.create_post(invalid_data, validate=False)
    print(f"Response: {response.text}")
    Assertions.assert_status_code(response.status_code, 400)
    Assertions.assert_error_message(response, expected_error)

@allure.feature('POST /posts')
def test_create_post(session):
    posts = Posts(session)
    data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response, post = posts.create_post(data)
    print(f"Response: {response.text}")
    Assertions.assert_status_code(response.status_code, 201)
    Assertions.assert_post_data(post, data)
