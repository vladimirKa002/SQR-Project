from streamlit.testing.v1 import AppTest
import pytest


def test_title():
    at = AppTest.from_file("../../frontend/app.py").run()
    assert at.title[0].value == "Inno Food Tier List"


if __name__ == "__main__":
    pytest.main()
