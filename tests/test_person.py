import json

def test_create_person(client):

        data = {"first_name":"testuser","last_name":"aaaa","identification":"192345","birthdate":"1990-03-01"}
        response = client.post("/store",json.dumps(data))
        assert response.status_code == 200
        assert response.json()["first_name"] == "testuser"


def test_check_person1(client):
    data = {"first_name": "ali", "last_name": "alavi", "identification": "192345", "birthdate": "1990-05-06"}
    response = client.post("/check", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["matches"][0]["first_name"] == "testuser"

def test_check_person2(client):
    data = {"first_name": "mohammad", "last_name": "aslani", "identification": "192346", "birthdate": "1990-07-08"}
    response = client.post("/check", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["matches"] == []