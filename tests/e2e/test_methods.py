from tests.TestProject import TestProject


class TestMethods(TestProject):

    def test_get_all_templates(self):
        response = self.client.get("/template/all")
        assert response.status_code == 200
        assert isinstance(response.json(), list)  # Ensuring the response is a list of templates

    def test_get_template(self):
        template_id = 1  # Example ID that should exist
        response = self.client.get(f"/template/get/{template_id}")
        assert response.status_code == 200
        assert response.json()['id'] == template_id  # Ensure the correct template is fetched

    def test_get_template_not_found(self):
        template_id = 9999  # Non-existing ID
        response = self.client.get(f"/template/get/{template_id}")
        assert response.status_code == 404

    def test_get_item(self):
        item_id = 1  # Example item ID
        response = self.client.get(f"/item/get/{item_id}")
        assert response.status_code == 200
        assert response.json()['id'] == item_id

    def test_item_not_found(self):
        item_id = 9999  # This item does not exist
        response = self.client.get(f"/item/get/{item_id}")
        assert response.status_code == 404
