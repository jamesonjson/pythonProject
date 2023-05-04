# This is a sample Python script.
import requests;


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


url = "https://ultimate-tennis1.p.rapidapi.com/player_stats/atp/su87"

headers = {
    "X-RapidAPI-Key": "e29c745549mshe442ba2aed3947cp197e44jsn38d9a0a3ade3",
    "X-RapidAPI-Host": "ultimate-tennis1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
