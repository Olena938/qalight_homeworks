# Домашнє завдання: API Testing з Python (`requests`)
## Мета
# Навчитися працювати з REST API через Python, виконувати HTTP-запити, перевіряти відповіді сервера та писати базові API тести.
# ## API для роботи

import requests
from utils.constants import BASE_URL
from utils.helpers import check_status_code

## 1. GET — отримання даних
### Отримати всі posts
response = requests.get(f"{BASE_URL}/posts/1")
print(response.headers["Content-Type"])
print("--------------------------------------------------------------------")
# print(response)
# print("--<Response [200]>-----------------------------------------------")
# print(response.status_code)
# print("-200----------------------------------------------------------")
# print(response.text)
# print("---{-----------------------------------------------")
# print("---"userId": 1,-----------------------------------------------")
# print("---"id": 1,-----------------------------------------------")
# print("---"title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",-----------------------------------------------")
# print("---"body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"--------------")
# print("---}------------------------------------------------------------")
# print(response.json())
# print("--{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}----------")
# print(type(response))
# print("-------<class 'requests.models.Response'>-------------------------------")
# print(type(response.json()))
# print("---------------<class 'dict'>---------------------------------")

# response = requests.get(f"{BASE_URL}")
# print(response.headers["Content-Type"])
# print("--------------------------------------------------------------------")
# print(response)
# print("--------------------------------------------------------------------")
# print(response.status_code)
# print("--------------------------------------------------------------------")
# print(response.text)
# print("--------------------------------------------------------------------")
# print(response.json())
# print("--------------------------------------------------------------------")
# print(type(response))
# print("--------------------------------------------------------------------")
# print(type(response.json()))
# print("--------------------------------------------------------------------")


def test_get_post_status_code():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    data=response.json()
    assert isinstance(data,dict)

# ### Отримати post по id
# ```http
# GET /posts/1
# ```
# Очікування:
# * status code = 200
# * `id == 1`

def test_get_post_id():
    response = requests.get(f"{BASE_URL}/posts/1")
    check_status_code(response, 200)
    data = response.json()
    assert data["id"] == 1

# ### Query parameters
# ```http
# GET /posts?userId=1
# ```
# Приклад:
# ```python
# response = requests.get(
#     "https://jsonplaceholder.typicode.com/posts",
#     params={"userId": 1}
# )
# ```
# Очікування:
# * всі записи мають `userId == 1`
def test_get_post_query():
    response = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId": 1})
    data=response.json()
    assert isinstance(data, list)
    for post in data:
        assert post["userId"]==1

# ## 2. POST — створення ресурсу
# ```http
# POST /posts
# Body:
# ```json
# {
#   "title": "my title",
#   "body": "my body",
#   "userId": 1
# }
# ```
# Приклад:
# ```python
# payload = {
#     "title": "my title",
#     "body": "my body",
#     "userId": 1
# }
# response = requests.post(
#     "https://jsonplaceholder.typicode.com/posts",
#     json=payload
# )
# ```
# Очікування:
# * status code = 201
# * response body містить створені поля
# * згенерований `id`

def test_post():
    payload = {"title": "my title", "body": "my body", "userId": 1}
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code==201

# ## 3. PUT — повне оновлення
# ```http
# PUT /posts/1
# ```
# Body:
# ```json
# {
#   "id": 1,
#   "title": "updated title",
#   "body": "updated body",
#   "userId": 1
# }
# ```
# Очікування:
# * status code = 200
# * title оновився

def test_put():
    payload = {"id": 1, "title": "updated title", "body": "updated body", "userId": 1}
    response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=payload)
    assert response.status_code==200

# ## 4. PATCH — часткове оновлення
# ```http
# PATCH /posts/1
# ```
# Body:
# ```json
# {
#   "title": "patched title"
# }
# ```
# Очікування:
# * status code = 200
# * змінилось тільки поле `title`

def test_patch():
    payload = {"title": "patched title"}
    response = requests.patch(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code==200
    data=response.json()
    assert isinstance(data, dict)
    assert data["title"]=="patched title"

# ## 5. DELETE — видалення
# ```http
# DELETE /posts/1
# ```
# Очікування:
# * status code = 200 або 204

def test_delete():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code in [200, 204]

# # Завдання
# ## Частина 1. Базові запити
# ### Завдання 1
# Написати скрипт, який:
# 1. отримує всі posts
# 2. перевіряє:
#    * статус 200
#    * кількість записів = 100

def test_count():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code in [200, 204]
    data=response.json()
    assert isinstance(data, list)
    assert len(data)==100

# ### Завдання 2
# Отримати post з id=10.
# Перевірити:
# * status code 200
# * `id == 10`
# * є поля:
#   * userId
#   * id
#   * title
#   * body

def test_get_get_id10():
    response = requests.get(f"{BASE_URL}/posts/10")
    assert response.status_code==200
    data = response.json()
    assert data["id"] == 10
    assert "userId" in data
    assert "title" in data
    assert "body" in data

# ### Завдання 3
# Отримати всі todos користувача 2:
# ```http
# GET /todos?userId=2
# ```
# Перевірити:
# * всі `userId == 2`
# ## Частина 2. CRUD

def test_get_user_id2():
    response = requests.get(f"{BASE_URL}/todos?userId=2")
    assert response.status_code==200
    data = response.json()

    for post in data:
        assert post["userId"] ==2

# ### Завдання 4 — Create
# Створити новий post.
# Перевірити:
# * status 201
# * title збігається
# * body збігається

def test_get_post_id():
    payload = {"title": "my title", "body": "my body", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code==201
    data = response.json()
    assert "title" in data
    assert "body" in data

# ### Завдання 5 — Update через PUT
# Оновити post id=5.
# Перевірити:
# * status 200
# * нові дані повернулись у response

def test_get_put_id5():
    payload = {
        "id": 5,
        "title": "my new title",
        "body": "updated body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/5", json=payload)
    assert response.status_code==200
    data = response.json()
    assert data["title"] == "my new title"
    assert data["body"] == "updated body"
  
# ### Завдання 6 — Partial Update через PATCH
# Оновити тільки title.
# Перевірити:
# * status 200
# * title змінився

def test_get_PATCH_id():
    payload = {
        "title": "my new title",
    }
    response = requests.patch(f"{BASE_URL}/posts/5", json=payload)
    assert response.status_code==200
    data = response.json()
    assert data["title"] == "my new title"


# ### Завдання 7 — Delete
# Видалити post id=5.
# Перевірити:
# * status 200/204
# ## Частина 3. Негативні сценарії

def test_delete_7():
    response = requests.delete(f"{BASE_URL}/posts/5")
    assert response.status_code in [200, 204]

# ### Завдання 8
# Отримати неіснуючий post:
# ```http
# GET /posts/999999
# ```
# Перевірити:
# * status 404 або пустий response

def test_get_8():
    response = requests.get(f"{BASE_URL}/posts/999999")
    assert response.status_code == 404


# ### Завдання 9
# Відправити POST без required полів.
# ```json
# {}
# ```
# Перевірити поведінку API.

def test_post_empty_body():
    payload = {}
    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload
    )
    assert response.status_code == 201
    data = response.json()
    assert "id" in data


# ## Частина 4. Робота з headers
# ### Завдання 10
# Відправити GET з custom headers:
# ```python
# headers = {
#     "User-Agent": "QA Student"
# }
# ```
# Переконатися:
# * request виконався успішно
# ## Bonus ⭐

def test_get10():
    payload = {}
    headers = {
     "User-Agent": "QA Student"
    }
    response = requests.get(
        f"{BASE_URL}/posts",
        headers=headers,
    )
    assert response.status_code == 200

# ### Завдання 11
# Створити універсальну функцію:
# ```python
# def make_request(method, endpoint, **kwargs):
#     ...
# ```
# Щоб можна було викликати:
# ```python
# make_request("GET", "/posts")
# make_request("POST", "/posts", json=data)
# ```

def make_request(method, endpoint, **kwargs):
    url = f"{BASE_URL}{endpoint}"
    response = requests.request(method, url, **kwargs)
    return response   

def test_11():
    response = make_request(
    "PUT",
    "/posts/1",
    json={"title": "new title"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "new title"

# ### Завдання 12
# Додати assertions через `pytest`
# Приклад:
# ```python
# def test_get_post():
#     response = requests.get(BASE_URL + "/posts/1")
#     assert response.status_code == 200
# ```

def test_get_post():
    response = requests.get(BASE_URL + "/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    assert "userId" in data

# # Критерії оцінювання

# | Критерій              | Бали |
# | --------------------- | ---- |
# | GET tests             | 20   |
# | POST/PUT/PATCH/DELETE | 40   |
# | Negative tests        | 20   |
# | Code quality          | 10   |
# | Bonus                 | 10   |

# Максимум: **100 балів**

# ## Що здати

# 1. GitHub repository
# 2. файл `requirements.txt`
# 3. файл `README.md` з інструкцією запуску

# ```bash
# pip install -r requirements.txt
# pytest
# ```

# додатковий челендж: оформити це як маленький API framework з папками:

# ```text
# project/
#     tests/
#     api/
#     utils/
#     conftest.py
# ```
