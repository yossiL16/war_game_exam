


def create_card(rank:str,suite:str) -> dict:

    dicti_card = {}
    while True:
        if rank ==  "2" or rank == "3" or rank == "4" or rank == "5" or rank == "6" or rank == "7" or rank == "8" or rank == "9" or rank == "10" or rank == "J" or rank == "Q" or rank ==  "K" or rank ==  "A" :

            dicti_card["rank"] = rank
            dicti_card["suite"] = suite

            listi_of_num = ["2","3","4","5","6","7","8","9","10"]
            list_letter = ["J","Q", "K", "A"]
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




create_card("J", "S")



def compare_cards(p1_card:dict, p2_card:dict) -> str:
    pass

def create_deck() -> list[dict]:
    pass

def shuffle(deck:list[dict]) -> list[dict]:
    pass