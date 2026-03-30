import random

while True:

        käyttäjän_valinta = input('Valitse: \nkivi \npaperi \nsakset \n')

        mahdolliset_liikkeet = ["kivi", "paperi", "sakset"]

        vastustajan_liike = random.choice(mahdolliset_liikkeet)

        print(f'\nValitsit {käyttäjän_valinta}, vastustaja valitsi {vastustajan_liike}.\n')

        if käyttäjän_valinta == vastustajan_liike:
                print(f'valitsitte molemmat saman, tasapeli!')

        elif käyttäjän_valinta == "kivi":
                if vastustajan_liike == "sakset":
                        print('Kivi voittaa sakset, voitit!')
                else:
                        print('Paperi peittää kiven, hävisit.')

        elif käyttäjän_valinta == "sakset":
                if vastustajan_liike == "paperi":
                        print('Sakset leikkaa paperin, voitit!')
                else:
                        print('Kivi rikkoo sakset, hävisit.')

        elif käyttäjän_valinta == "paperi":
                if vastustajan_liike == "kivi":
                        print('Paperi peittää kiven, voitit!')
                else:
                        print("Sakset leikkaa paperin, hävisit.")

        play_again = input("\nPelaatko uudestaan? (y/n): ")
        if play_again.lower() != "y":
                break