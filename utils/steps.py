from utils.curl_utils import generate_and_attach_curl, measure_request_time
import allure

@allure.step("Отправляем GET запрос к {url} с параметрами {params}")
def send_get_request(session, url, params=None):
    print(f"GET Request to URL: {url}, with params: {params}")
    response = session.get(url, params=params)
    generate_and_attach_curl("GET", response.url, session.headers)  # Добавляем генерацию cURL
    allure.attach(response.text, name="Ответ", attachment_type=allure.attachment_type.JSON)
    return response

@allure.step("Отправляем POST запрос к {url} с телом {data}")
def send_post_request(session, url, data):
    response = session.post(url, json=data)

    generate_and_attach_curl("POST", response.url, session.headers, data)
    allure.attach(response.text, name="Ответ", attachment_type=allure.attachment_type.JSON)
    return response

@allure.step("Отправляем PUT запрос к {url} с телом {data}")
def send_put_request(session, url, data):
    response = session.put(url, json=data)
    response.raise_for_status()
    generate_and_attach_curl("PUT", response.url, session.headers, data)
    allure.attach(response.text, name="Ответ", attachment_type=allure.attachment_type.JSON)
    return response

@allure.step("Отправляем DELETE запрос к {url}")
def send_delete_request(session, url):
    response = session.delete(url)
    generate_and_attach_curl("DELETE", response.url, session.headers)
    allure.attach(response.text, name="Ответ", attachment_type=allure.attachment_type.JSON)
    return response
