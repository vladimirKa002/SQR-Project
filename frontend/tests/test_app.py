from streamlit.testing.v1 import AppTest


def test_markdown():
    at = AppTest.from_file("../app.py").run()
    # print(at.title[0].value)
    # assert "Inno Food Tier List - A Delicious Journey of Exploration" in at.markdown[0].value