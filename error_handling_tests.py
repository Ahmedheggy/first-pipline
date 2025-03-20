import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_invalid_json(client):
    response = client.post('/wave', data='invalid json', content_type='application/json')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_empty_name(client):
    response = client.post('/wave', json={'name': ''})
    assert response.status_code == 400
    data = response.get_json()
    assert data['message'] == '👋 Please enter your name!'