import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_full_flow(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome Fixed Intern Team' in response.data

    response = client.post('/wave', json={'name': 'Test User'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == '👋 Hello, Test User!'
    assert data['count'] == 1

    response = client.get('/get_count')
    assert response.status_code == 200
    data = response.get_json()
    assert data['count'] == 1