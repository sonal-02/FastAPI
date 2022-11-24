# import json
# import unittest
# from fastapi.testclient import TestClient
# from unittest.mock import patch
# from main import app
# import pytest

# @pytest.fixture(scope="function")
# def test_create_user(client):
#     data = {"username":"testuser","email":"testuser@nofoobar.com","password":"testing"}
#     response = client.post("/login/",json.dumps(data))
#     assert response.status_code == 200 
#     assert response.json()["email"] == "testuser@nofoobar.com"
#     assert response.json()["is_active"] == True


# class DemoViewTestCase(unittest.TestCase):

#        def test_demo_api(self):
#            with patch('src.endpoints.demo_module.demo_api') as mocked_post:
#                mocked_post.return_value.status_code = 200
#                mocked_post.return_value.json = {
#                    "message": "request accepted",
#                    "success": True
#                    }
                # url = router.url_path_for('demo_api')   #fetch the api router
                # client = TestClient(app)
                # response = client.post(url, json={"id": "BXBksk8920", "name": "Pjp"})


# from starlette.testclient import TestClient


# def test_create_user(client: TestClient):
#     user_data = {
#         "username": "testUser",
#         "password": "testPassword",
#         "name": "testName",
#         "last_name": "testLastName",
#         "role": 1
#     }

#     response = client.post("/users/all")
#     assert response.status_code == 200

# from starlette.testclient import TestClient
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# def test_ping():
#     response = client.get("/login")
    # assert response.status_code == 200
    # assert response.json() == {"ping": "pong!"}