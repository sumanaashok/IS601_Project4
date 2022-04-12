def test_request_index(client):
    """This tests the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

    def test_request_page_not_found(client):
        """This tests a 404 page"""
        response = client.get("/page5")
        assert response.status_code == 404