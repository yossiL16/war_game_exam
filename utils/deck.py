import random


def create_card(rank:str,suite:str) -> dict:

    dicti_card = {}
    while True:
        if rank ==  "2" or rank == "3" or rank == "4" or rank == "5" or rank == "6" or rank == "7" or rank == "8" or rank == "9" or rank == "10" or rank == "J" or rank == "Q" or rank ==  "K" or rank ==  "A" :

            dicti_card["rank"] = rank
            dicti_card["suite"] = suite

            listi_of_num = ["2","3","4","5","6","7","8","9","10"]

            for number in listi_of_num:
                if number == rank:
                    dicti_card["value"] = int(number)
                    break


            if rank == "J":
                dicti_card["value"] = 11
            elif rank == "Q":
                dicti_card["value"] = 12
            elif rank == "K":
                dicti_card["value"] = 13
            elif rank == "A":
                dicti_card["value"] = 14

            print(dicti_card)
            break
        else:

            break

    return dicti_card



def compare_cards(p1_card:dict, p2_card:dict) -> str:


    if p1_card.get("value") > p2_card.get("value"):

        return "p1"
    elif p1_card.get("value") < p2_card.get("value"):

        return "p2"

    else:
        return "WAR"




def create_deck() -> list[dict]:

    list_dict_card = []
    for i in range(10):
        if i < 10:
            dicti = create_card(str(i +1), "H")
            list_dict_card.append(dicti)

    for i in range(10):
        if i < 10:
            dicti = create_card(str(i + 1), "D")
            list_dict_card.append(dicti)

    for i in range(10):
        if i < 10:
            dicti = create_card(str(i + 1), "C")
            list_dict_card.append(dicti)

    for i in range(10):
        if i < 10:
            dicti = create_card(str(i + 1), "S")
            list_dict_card.append(dicti)



    list_letter = ["H","D", "C", "S"]
    list_special = ["J", "Q", "K", "A"]
    for i in list_letter:
        for j in list_special:
                dicti = create_card(i, j)
                list_dict_card.append(dicti)

    return list_dict_card



def shuffle(deck:list[dict]) -> list[dict]:


    for i in range(1):
        list_cards = deck
        list_numbers = []
        randomaly = random.randrange(2,11)
        list_numbers.append(randomaly)
        randomaly = random.randrange(2, 11)
        list_numbers.append(randomaly)

        if list_numbers[0] == list_numbers[1]:
            continue
        else:
            list_cards[list_numbers[0]], list_cards[list_numbers[1]] = list_cards[list_numbers[1]], list_cards[list_numbers[0]]

        return list_cards


