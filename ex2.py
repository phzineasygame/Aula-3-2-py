def avalieAnimes():
    mikadono_sisters = input("Avalie Mikadono Sisters (de 0 a 10): "))
    horimiya = input("Avalie Horimiya (de 0 a 10): "))
    the_quintuplets = input("Avalie The Quintuplets (de 0 a 10): "))

    if mikadono_sisters > 6:
        print("Mikadono Sisters: Anime bom!")
    else:
        print("Mikadono Sisters: Anime ruim...")

    if horimiya > 6:
        print("Horimiya: Anime bom!")
    else:
        print("Horimiya: Anime ruim...")

    if the_quintuplets > 6:
        print("The Quintuplets: Anime bom!")
    else:
        print("The Quintuplets: Anime ruim...")
