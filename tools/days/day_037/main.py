# Copyright (c) 2024 Jarid Prince

from days.day_037.files.helpers import *


def day_037():
    title("PIXELA TRACKER")
    load_dotenv()

    PIXELA_USER = os.getenv("PIXELA_USER")
    PIXELA_AUTH_TOKEN = os.getenv("PIXELA_AUTH_TOKEN")
    pixela_endpoint = "https://pixe.la/v1/users"
    headers = {"X-USER-TOKEN": PIXELA_AUTH_TOKEN}

    nls("This day is API based. Uncomment code to run each section.")

    # Uncomment to create your account ===============
    # user_params = {
    #     "token": PIXELA_AUTH_TOKEN,
    #     "username": PIXELA_USER,
    #     "agreeTermsOfService": "yes",
    #     "notMinor": "yes",
    # }

    # response = requests.post(url=pixela_endpoint, json=user_params)
    # print(response.text)

    # UNCOMMENT TO CREATE A GRAPH ================
    # graph_endpoint = f"{pixela_endpoint}/{PIXELA_USER}/graphs"

    # graph_config = {
    #     "id": "calories",
    #     "name": "Food",
    #     "unit": "calory",
    #     "type": "float",
    #     "color": "momiji",
    # }

    # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    # print(response.text)

    # UNCOMMENT TO CREATE CALORIES GRAPH ==========================
    # pixel_creation_endpoint = f"{pixela_endpoint}/{PIXELA_USER}/graphs/calories"

    # today = dt.now()
    # print(today.strftime("%Y%m%d"))
    # pixel_data = {
    #     "date": today.strftime("%Y%m%d"),
    #     "quantity": input("How many calories did you eat?\n"),
    # }

    # response = requests.post(
    #     url=pixel_creation_endpoint, json=pixel_data, headers=headers
    # )
    # print(
    #     f"{response.text}\n Navigate to https://pixe.la/@{PIXELA_USER} to see your charts."
    # )

    # UNCOMMENT TO UPDATE GRAPH ==========================

    # update_endpoint = f"{pixela_endpoint}/{USER}/graphs/calories/{today.strftime('%Y%m%d')}"
    # new_pixel_data = {
    #     "quantity": input("How many calories did you eat?")
    # }

    # response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
    # print(response.text)

    # UNCOMMENT TO DELETE GRAPH ==========================

    # delete_endpoint = (
    #     f"{pixela_endpoint}/{PIXELA_USER}/graphs/calories/{today.strftime('%Y%m%d')}"
    # )

    # response = requests.delete(url=delete_endpoint, headers=headers)
    # print(response.text)
