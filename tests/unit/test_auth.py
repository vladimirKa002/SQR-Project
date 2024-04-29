from unittest.mock import patch

from backend.schemas import UserCreate, UserResponse
from tests.TestProject import TestProject


class TestAuth(TestProject):
    def setUp(self):
        super(TestAuth, self).setUp()
        self.user_create = UserCreate(**{
            'email': 'test@example.com',
            'name': 'Test User',
            'password': 'password'
        })
        self.user_response = UserResponse(**{
            'id': 1,
            'email': 'test@example.com',
            'name': 'Test User'
        })

    @patch('auth.get_user')
    @patch('auth.create_user')
    def test_register_new_user(self, create_user_mock, get_user_mock):
        # Mock the necessary functions
        get_user_mock.return_value = None
        create_user_mock.return_value = self.user_response

        # Send a request to register a new user
        response = self.client.post('/auth/register', json={
            'email': 'test@example.com',
            'password': 'password',
            'name': 'Test User'
        })

        assert response.status_code == 200
        assert response.json() == {
            'id': 1,
            'email': 'test@example.com',
            'name': 'Test User'
        }
        create_user_mock.assert_called_once()

    @patch('auth.get_user')
    def test_register_existing_user(self, get_user_mock):
        # Mock the necessary function
        get_user_mock.return_value = self.user_response

        # Send a request to register an existing user
        response = self.client.post('/auth/register', json={
            'email': 'test@example.com',
            'password': 'password',
            'name': 'Test User'
        })

        assert response.status_code == 400
        assert response.json() == {'detail': 'A user with this email already exists'}
        get_user_mock.assert_called_once()

    @patch('auth.get_user')
    @patch('auth.verify_password')
    @patch('auth.manager.create_access_token')
    def test_login_successful(self, create_access_token_mock, verify_password_mock, get_user_mock):
        # Mock the necessary functions
        get_user_mock.return_value = self.user_create
        verify_password_mock.return_value = True
        create_access_token_mock.return_value = 'test_access_token'

        # Send a request to login
        response = self.client.post('/auth/token', data={
            'username': 'test@example.com',
            'password': 'password'
        })

        assert response.status_code == 200
        assert response.json() == {
            'access_token': 'test_access_token',
            'token_type': 'Bearer'
        }
        create_access_token_mock.assert_called_once_with(data={'sub': 'test@example.com'})

    @patch('auth.get_user')
    @patch('auth.verify_password')
    def test_login_invalid_credentials(self, verify_password_mock, get_user_mock):
        # Mock the necessary functions
        get_user_mock.return_value = self.user_create
        verify_password_mock.return_value = False

        # Send a request to login with invalid credentials
        response = self.client.post('/auth/token', data={
            'username': 'test@example.com',
            'password': 'password'
        })

        assert response.status_code == 401
        assert response.json() == {'detail': 'Invalid credentials'}
        verify_password_mock.assert_called_once()

    @patch('auth.get_user')
    def test_login_nonexistent_user(self, get_user_mock):
        # Mock the necessary function
        get_user_mock.return_value = None

        # Send a request to login with a non-existent user
        response = self.client.post('/auth/token', data={
            'username': 'test@example.com',
            'password': 'password'
        })

        assert response.status_code == 401
        assert response.json() == {'detail': 'Invalid credentials'}
        get_user_mock.assert_called_once()
