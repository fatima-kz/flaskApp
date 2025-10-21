



from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_health():
    client = app.test_client()
    response = client.get('/health')
    assert b"OK" in response.data

def test_post_data():
    client = app.test_client()
    response = client.post('/data', json={"name": "Aqsa"})
    assert response.status_code == 200
    assert b"Data received successfully" in response.data
