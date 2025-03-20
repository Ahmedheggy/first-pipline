import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_wave_endpoint(client):
    response = client.post('/wave', json={'name': 'Test User'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert 'visit_time' in data
    assert 'count' in data

def test_get_count_endpoint(client):
    response = client.get('/get_count')
    assert response.status_code == 200
    data = response.get_json()
    assert 'count' in data