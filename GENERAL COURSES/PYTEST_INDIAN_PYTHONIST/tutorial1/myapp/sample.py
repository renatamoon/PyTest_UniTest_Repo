from tutorial1.myapp.dice import roll_dice
import requests


def guess_number(num):
    result = roll_dice()
    if result == num:
        return "You won!"
    else:
        return "You lost!"


def get_ip():
    response = requests.get("https://meuip.com.br/")
    if response.status_code == 200:
        return response.json()
