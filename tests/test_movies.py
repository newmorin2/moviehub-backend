def test_get_movies(test_client):
    response = test_client.get("/movies")

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_movie(test_client):
    response = test_client.get("/movies/1")

    assert response.status_code in [200, 404]