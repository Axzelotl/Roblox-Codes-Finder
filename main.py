import requests, os
from bs4 import BeautifulSoup

unique = {"volleyball legends": "haikyuu-legends"}
folder = "Saved Codes"

if not os.path.exists(folder):
    os.makedirs(folder)

game = " ".join(input("Game: ").lower().split())
directory = "-".join(game.split())
roblox_prefix = False

while True:
    try:
        if game in unique:
            url = f"https://beebom.com/{unique[game]}-codes/"
        else:
            if not roblox_prefix:
                url = f"https://beebom.com/{directory}-codes/"
            else:
                url = f"https://beebom.com/roblox-{directory}-codes/"

        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        elements = soup.find_all("li")
        found = False
        filename = os.path.join(folder, f"{game.title()} Codes.txt")

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
            print("Found codes has been saved as Redeemed Codes in their respective file.")
        
        input("\nPress Enter to exit...")
        break
        
    except requests.exceptions.HTTPError:
        if not roblox_prefix and game not in unique:
            roblox_prefix = True
            continue
        else:
            print("Could not find page for given game. Check spelling or if page exists.")
            input("\nPress Enter to exit...")
            break