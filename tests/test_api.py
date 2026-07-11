import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_generate():
    response = client.post(
        "/generate",
        json={
            "event": "AI for Sustainable Cities",
            "interest": "Climate Change"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "keywords" in data
    assert "conversation_starter" in data


def test_fact_check():
    response = client.get("/fact-check/Artificial intelligence")

    assert response.status_code == 200

    data = response.json()

    assert "summary" in data


def test_history():
    response = client.get("/history")

    assert response.status_code == 200