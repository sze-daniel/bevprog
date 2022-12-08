import requests


def main():

    nev = input("Pokemon neve: ")
    j = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nev}")
    data = j.json()

    n_of_abil = len(data["abilities"])
    move = data["moves"][0]["move"]["name"]

    def stats(n):
        return data["stats"][n]["base_stat"]

    health = stats(0)
    attack = stats(1)
    defense = stats(2)
    speed = stats(3)
    weight = data["weight"]

    print(f"Number of abilities: {n_of_abil}")
    print(f"First move: {move}")
    print(f"Health: {health}")
    print(f"Attack: {attack}")
    print(f"Defense: {defense}")
    print(f"Speed: {speed}")
    print(f"Weight: {weight}")


if __name__ == "__main__":
    main()