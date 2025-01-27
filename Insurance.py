"""
Investigation into when insurance is a good bet in Blackjack.
Jack d'Entremont
"""
import random
import math

def initialize_shoe(num_decks=6):
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    shoe = ranks * 4 * num_decks
    random.shuffle(shoe)
    return shoe
    
def simulate_insurance(true_count_target, num_trials=10000, num_decks=6):
    insurance = 0
    count_matches = 0

    for n in range(num_trials):
        shoe = initialize_shoe(num_decks)
        running_count = 0
        cards_dealt = 0
        
        while len(shoe) > 1:
            card = shoe.pop()
            cards_dealt += 1
            
            if card in [2, 3, 4, 5, 6]:
                running_count += 1
            elif card in [10, 11, 12, 13, 14]:
                running_count -= 1

            decks_remaining = num_decks - (cards_dealt // 52)
            true_count = running_count / decks_remaining

            if true_count == true_count_target:
                count_matches += 1
                hole_card = shoe[0]
                if hole_card in [10, 11, 12, 13]:
                    insurance += 1
                break

    probability = (insurance/count_matches) if count_matches > 0 else 0
    return round(probability, 4)

def main():
    results = {}
    for count in range(-7, 8):
        probability = simulate_insurance(count)
        results[count] = probability
        print(f'Count: {count} -> {probability}')

if __name__ == "__main__":
    main()
