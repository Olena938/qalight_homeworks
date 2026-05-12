def check_status_code(response, expected_code):
    assert response.status_code == expected_code