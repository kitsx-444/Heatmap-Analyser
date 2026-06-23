# Heatmap-Analyser

## What is it?
This is a Forex heatmap analyser. It tabulates the pip strength of different currencies for data analysis, prints out the strongest rows, and the strongest and weakest currencies.

## What did I learn:
1. A new structure to dictionaries. Instead of basic key:value pairs, I created a key that has a dictionary assigned to it. This made referencing the keys and values simpler for me.
2. Using a comparison operator inside DataFrame indexing - df[df['Strength'] == 'Strong'].
3. Using lambda to assign strings based on a condition inside apply().
4. Creating a new column with new syntax.

## Future goals:
Using pandas to score the strength of macroeconomic data for directional macro bias.
