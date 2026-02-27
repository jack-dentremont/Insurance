"""
Investigation into when insurance is a good bet in Blackjack.
Jack d'Entremont
"""
import random
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns

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

            if math.floor(true_count) == true_count_target:
                count_matches += 1
                hole_card = shoe[0]
                if hole_card in [10, 11, 12, 13]:
                    insurance += 1
                break

    probability = (insurance/count_matches) if count_matches > 0 else 0
    return round(probability, 4)

def visualize_results(counts, probabilities):
    BREAKEVEN = 1/3

    sns.set_theme(style='whitegrid', font_scale=1.15)
    fig, ax = plt.subplots(figsize=(12,7))

    colors = ['#2ecc71' if p >= BREAKEVEN else '#c0392b' for p in probabilities]

    bars = ax.bar(counts, probabilities, color=colors, width=0.7,
                  edgecolor='white', linewidth=0.8, zorder=3)

    ax.axhline(y=BREAKEVEN, color = '#f39c12', linewidth=2.5,
               linestyle='--', zorder=4)

    ax.annotate(
        "Breakeven (33.3%)",
        xy=(-2,BREAKEVEN),
        xytext=(-3.5, BREAKEVEN + 0.04),
        fontsize=11, fontweight='bold', color='#f39c12',
        arrowprops=dict(arrowstyle='->', color='#f39c12', lw=1.5),
        zorder=5
    )

    for bar, prob in zip(bars, probabilities):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.005,
            f"{prob:.1%}",
            ha="center", va="bottom",
            fontsize=9, fontweight="medium", color="#2c3e50"
        )

    ax.text(-5, 0.41, "− EV (Bad Bet)", fontsize=13, fontweight="bold",
            color="#c0392b", ha="center", alpha=0.7)
    ax.text(5, 0.41, "+ EV (Good Bet)", fontsize=13, fontweight="bold",
            color="#2ecc71", ha="center", alpha=0.7)

    ax.set_xlabel("Hi-Lo True Count", fontsize=13, fontweight="bold", labelpad=10)
    ax.set_ylabel("Insurance Win Probability", fontsize=13, fontweight="bold", labelpad=10)
    ax.set_title("When Does Insurance Become a Good Bet in Blackjack?",
                 fontsize=16, fontweight="bold", pad=15)
    ax.set_xticks(counts)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=0))
    ax.set_ylim(0.18, 0.45)

    ax.tick_params(axis="both", labelsize=11)
    sns.despine(left=True, bottom=True)

    plt.tight_layout()
    plt.savefig("insurance_probability.png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.show()
    print("\nChart saved as insurance_probability.png")

def main():
    counts = []
    probabilities = []
    for count in range(-7, 8):
        probability = simulate_insurance(count)
        counts.append(count)
        probabilities.append(probability)
        print(f'Count: {count} -> {probability}')

    visualize_results(counts, probabilities)

if __name__ == "__main__":
    main()
