import pytest
import threading
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_concurrent_waves(client):
    def wave():
        client.post('/wave', json={'name': 'Test User'})

    threads = [threading.Thread(target=wave) for _ in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    response = client.get('/get_count')
    assert response.status_code == 200
    data = response.get_json()
    assert data['count'] == 10