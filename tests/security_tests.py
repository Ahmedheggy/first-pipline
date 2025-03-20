import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_sql_injection(client):
    response = client.post('/wave', json={'name': "'; DROP TABLE visits; --"})
    assert response.status_code == 200

    response = client.get('/get_count')
    assert response.status_code == 200