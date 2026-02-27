# 🃏 Monte Carlo Simulation of Insurance in Blackjack

A Python simulation that investigates when the insurance side bet in Blackjack becomes profitable, using the Hi-Lo card counting system and true count analysis across a standard six-deck shoe.

## Overview

In Blackjack, when the dealer shows an Ace, players are offered the opportunity to buy "insurance": a side wager that pays 2:1 if the dealer has a natural 21, "Blackjack". Game theory says that insurance is a sucker bet, but card counters know the math shifts at higher true counts as the shoe becomes rich in tens and face cards.

This project uses a Monte Carlo simulation to answer the question: **At what true count does insurance become a positive expected value (+EV) bet?**

## Key Finding

The simulation confirms that insurance becomes profitable around a **true count of +3**, aligning with established card counting theory. At this threshold, the density of tens and face cards remaining in the shoe pushes the probability of a dealer natural 21 above the ~33.3% breakeven point required for insurance to have a positive expected value.

## How It Works

1. **Shoe Initialization** — A standard six-deck shoe (312 cards) is shuffled
2. **Card Counting** — Cards are dealt one at a time using the Hi-Lo system:
   - Cards 2–6: +1 (running count)
   - Cards 7–9: 0 (no impact on running count)
   - Cards 10–Ace: −1 (running count)
3. **True Count Conversion** — Running count is divided by decks remaining in the shoe to get the true count
4. **Insurance Check** — When the true count hits a target value, the simulation checks whether the dealer's hole card is a ten-value card (10, J, Q, K)
5. **Aggregation** — This process repeats across 10,000 trials per true count, and the probability of a winning insurance bet is calculated for true counts ranging from −7 to +7

## Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Core language |
| **random** | Shoe shuffling and simulation randomness |
| **math** | Numerical operations |
| **matplotlib** | Chart rendering and plot customizations |
| **seaborn** | Statistical visualization styling and themes |

## Results

| True Count | Insurance Win Probability |
|:----------:|:------------------------:|
| −7 | Low (~20–24%) |
| −3 | Below breakeven (~25-30%) |
| 0 | ~30% (neutral shoe) |
| **+3** | **~33-35% (breakeven)** |
| +5 | ~35–38% |
| +7 | High (~38–40%) |

> *Exact values vary by simulation run. The 33.3% breakeven corresponds to the 2:1 insurance payout — above this threshold, the bet has positive expected value.*

**Output:** A printout of insurance win probability at each true count from −7 to +7 and png file of barchart visualization.
