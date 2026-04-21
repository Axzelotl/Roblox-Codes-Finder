import requests
from sys import exit
from bs4 import BeautifulSoup

unique = ["volleyball legends"]

game = input("Game: ").lower()

attempt_roblox = False

while True:
    try:
        if game in unique:
            url = f"https://beebom.com/haikyuu-legends-codes/"
        else:
            if not attempt_roblox:
                url = f"https://beebom.com/{game.replace(' ', '-')}-codes/"
            else:
                url = f"https://beebom.com/roblox-{game.replace(' ', '-')}-codes/"

        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        elements = soup.find_all("li")
        found = False
        if game not in unique:
            filename = f"{game.title()}.txt"
        else:
            filename = f"Volleyball Legends.txt"

        try:
            with open(filename) as file:
                redeemed = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            redeemed = []

        print(f"\033[1m\n{game.title()} Codes:\n")    

        for element in elements:
            text = element.get_text().strip()
            if "(NEW)" in text and text not in redeemed:
                print(f"{text}\n")
                found = True

                with open(filename, "a") as file:
                    file.write(f"{text}\n")
                
                redeemed.append(text)

        print("\033[0m", end="")

        if found == False:
            print("No NEW codes were found for this game.")
        else:
            print("Found codes has been saved as Redeemed Codes in their respective file and will not be shown again in program.")
        
        input("\nPress Enter to exit...")
        break
        
    except requests.exceptions.HTTPError:
        if not attempt_roblox and game not in unique:
            attempt_roblox = True
            continue
        else:
            print("Could not find page for given game. Check spelling or if page exists.")
            input("\nPress Enter to exit...")
            break