import allure
import time
from functools import wraps

def generate_and_attach_curl(method, url, headers=None, data=None):
    curl_command = f"curl -X {method} '{url}'"
    if headers:
        for header, value in headers.items():
            curl_command += f" -H '{header}: {value}'"
    if data:
        curl_command += f" -d '{data}'"
    allure.attach(curl_command, name="cURL командa", attachment_type=allure.attachment_type.TEXT)

def measure_request_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with args: {args} and kwargs: {kwargs}")

        start_time = time.time()
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"Error during function execution: {e}")
            raise
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Function {func.__name__} took {elapsed_time:.3f} seconds")
        allure.attach(f"{elapsed_time:.3f} секунд", name="Время выполнения запроса", attachment_type=allure.attachment_type.TEXT)

        return result
    return wrapper
