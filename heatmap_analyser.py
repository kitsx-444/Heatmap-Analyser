import pandas as pd

currency_dict = {'currencies':{'EURUSD':87,
			  'GBPUSD':134,
			  'USDJPY':210,
			  'AUDUSD':63,
			  'USDCAD':95,
			  'USDCHF':78,
			  'NZDUSD':110}}

header = {'Pair': currency_dict['currencies'].keys(), 'Pips':currency_dict['currencies'].values()}
df = pd.DataFrame(header)
# Adding a new column. New concept for me.
df['Strength'] = df['Pips'].apply(lambda x: 'Strong' if x > 100 else 'Weak')

strong_row_index = df['Pips'].idxmax()
weak_row_index = df['Pips'].idxmin()
strong_row = df.loc[strong_row_index]
weak_row = df.loc[weak_row_index]

print(df)
print(f'\nThe strongest currency is: {strong_row["Pair"]} with {strong_row["Pips"]} pips.')
print(f'The weakest currency is: {weak_row["Pair"]} with {weak_row["Pips"]} pips.')

# Two equal signs for comparison.
# The inner df checks the strength row only for the string 'Strong'.
# The outer df  returns the entire row if the 'Strong' string is in its Strength column
strong_rows = df[df['Strength'] == 'Strong']
print(strong_rows)
