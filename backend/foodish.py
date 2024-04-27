import requests


def get_random_food_image():
    url = "https://foodish-api.com/api"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError if the response status is not 200

        data = response.json()
        image_url = data['image']
        return image_url
    except requests.exceptions.RequestException as e:
        print("Failed to fetch image:", e)
        return None
