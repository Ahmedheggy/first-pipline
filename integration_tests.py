import pytest
import redis
import psycopg2

def test_redis_integration():
    cache = redis.Redis(host='redis', port=6379)
    cache.set('test_key', 'test_value')
    value = cache.get('test_key')
    assert value.decode('utf-8') == 'test_value'
    cache.delete('test_key')

def test_postgres_integration():
    conn = psycopg2.connect(
        dbname='mydatabase',
        user='user',
        password='password',
        host='db',
        port=5432
    )
    cursor = conn.cursor()
    cursor.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'visits');")
    assert cursor.fetchone()[0] is True
    cursor.execute("INSERT INTO visits (visitor_name) VALUES (%s) RETURNING visit_time;", ('Test User',))
    visit_time = cursor.fetchone()[0]
    assert visit_time is not None
    cursor.execute("DELETE FROM visits WHERE visitor_name = 'Test User';")
    conn.commit()
    conn.close()