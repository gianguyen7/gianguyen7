import pytest
from fastapi.testclient import TestClient
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

from src.main import app


@pytest.fixture
def client():
    FastAPICache.init(InMemoryBackend())
    with TestClient(app) as c:
        yield c


def test_predict(client):
    data = {"text": ["I hate you.", "I love you."]}
    response = client.post(
        "/project/bulk-predict",
        json=data,
    )
    print(response.json())
    assert response.status_code == 200
    assert isinstance(response.json()["predictions"], list)
    assert isinstance(response.json()["predictions"][0], list)
    assert isinstance(response.json()["predictions"][0][0], dict)
    assert isinstance(response.json()["predictions"][1][0], dict)
    assert set(response.json()["predictions"][0][0].keys()) == {"label", "score"}
    assert set(response.json()["predictions"][0][1].keys()) == {"label", "score"}
    assert set(response.json()["predictions"][1][0].keys()) == {"label", "score"}
    assert set(response.json()["predictions"][1][1].keys()) == {"label", "score"}
    assert response.json()["predictions"][0][0]["label"] == "NEGATIVE"
    assert response.json()["predictions"][0][1]["label"] == "POSITIVE"
    assert response.json()["predictions"][1][0]["label"] == "POSITIVE"
    assert response.json()["predictions"][1][1]["label"] == "NEGATIVE"

def test_single_input(client):
    data = {"text": ["I love this!"]}
    response = client.post(
        "/project/bulk-predict",
        json=data,
    )
    assert response.status_code == 200
    assert isinstance(response.json()["predictions"], list)
    assert len(response.json()["predictions"]) == 1
    assert isinstance(response.json()["predictions"][0], list)
    assert isinstance(response.json()["predictions"][0][0], dict)
    assert set(response.json()["predictions"][0][0].keys()) == {"label", "score"}
    assert response.json()["predictions"][0][0]["label"] == "POSITIVE"

def test_empty_text(client):
    data = {"text": [""]}
    response = client.post(
        "/project/bulk-predict",
        json=data,
    )
    assert response.status_code == 200
    assert len(response.json()["predictions"]) == 1
    assert response.json()["predictions"][0] == []

def test_long_text(client):
    long_text = "A" * 10000 
    data = {"text": [long_text]}
    response = client.post(
        "/project/bulk-predict",
        json=data,
    )
    assert response.status_code == 200
    assert isinstance(response.json()["predictions"], list)
    assert len(response.json()["predictions"]) == 1
    assert isinstance(response.json()["predictions"][0], list)

def test_non_ascii_text(client):
    data = {"text": ["I ❤️ FastAPI!"]}
    response = client.post(
        "/project/bulk-predict",
        json=data,
    )
    assert response.status_code == 200
    assert isinstance(response.json()["predictions"], list)
    assert len(response.json()["predictions"]) == 1
    assert isinstance(response.json()["predictions"][0], list)

def test_multiple_empty_strings(client):
    data = {"text": ["", "", ""]}
    response = client.post(
        "/project/bulk-predict",
        json=data,
    )
    assert response.status_code == 200
    assert len(response.json()["predictions"]) == 3
    for prediction in response.json()["predictions"]:
        assert prediction == []

def test_mixed_inputs(client):
    data = {"text": ["I love you.", "", "12345", "This is great!"]}
    response = client.post(
        "/project/bulk-predict",
        json=data,
    )
    assert response.status_code == 200
    assert len(response.json()["predictions"]) == 4
    assert isinstance(response.json()["predictions"][0], list)
    assert isinstance(response.json()["predictions"][1], list)
    assert isinstance(response.json()["predictions"][2], list)
    assert isinstance(response.json()["predictions"][3], list)

def test_special_characters(client):
    data = {"text": ["!@#$%^&*()", ">>>???<<<", "[[[]]]]"]}
    response = client.post(
        "/project/bulk-predict",
        json=data,
    )
    assert response.status_code == 200
    assert len(response.json()["predictions"]) == 3
    for prediction in response.json()["predictions"]:
        assert isinstance(prediction, list)

def test_numerical_input(client):
    data = {"text": ["12345", "67890"]}
    response = client.post(
        "/project/bulk-predict",
        json=data,
    )
    assert response.status_code == 200
    assert len(response.json()["predictions"]) == 2
    assert isinstance(response.json()["predictions"][0], list)
    assert isinstance(response.json()["predictions"][1], list)

def test_null_input(client):
    data = {"text": [None]}
    response = client.post(
        "/project/bulk-predict",
        json=data,
    )
    assert response.status_code == 422 

def test_invalid_json(client):
    response = client.post("/project/bulk-predict", data="not a json")
    assert response.status_code == 422 

def test_missing_text_key(client):
    data = {"wrong_key": ["I love you."]}
    response = client.post(
        "/project/bulk-predict",
        json=data,
    )
    assert response.status_code == 422

def test_mixed_language_input(client):
    data = {"text": ["I love this!", "これはテストです", "C'est génial!"]}
    response = client.post(
        "/project/bulk-predict",
        json=data,
    )
    assert response.status_code == 200
    assert len(response.json()["predictions"]) == 3
    for prediction in response.json()["predictions"]:
        assert isinstance(prediction, list)

def test_repeated_words(client):
    data = {"text": ["happy happy happy", "sad sad sad"]}
    response = client.post(
        "/project/bulk-predict",
        json=data,
    )
    assert response.status_code == 200
    assert len(response.json()["predictions"]) == 2
    for prediction in response.json()["predictions"]:
        assert isinstance(prediction, list)

def test_no_payload(client):
    response = client.post(
        "/project/bulk-predict",
        json=None, 
    )
    assert response.status_code == 422 
