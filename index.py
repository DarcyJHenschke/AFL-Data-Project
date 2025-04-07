import pandas as pd
import googlemaps
from datetime import datetime

df = pd.read_excel('/Users/darcyhenschke/Downloads/afl.xlsx', sheet_name=0, skiprows=1)

df = df[['Date', 'Kick Off (local)', 'Home Team', 'Away Team', 'Venue', 'Home Score', 'Away Score', 'Play Off Game?', 'Home Odds Close', 'Away Odds Close']]


def get_winner(row):
    if row['Home Score'] > row['Away Score']:
        return row['Home Team']
    elif row['Home Score'] < row['Away Score']:
        return row['Away Team']
    else:
        return "Draw"  # Or any other value to indicate a tie

# Apply the function to each row to create the new column
df['Winning Team'] = df.apply(get_winner, axis=1)

# Display the first few rows to verify the new column
df = df[
    ((df['Winning Team'] == df['Home Team']) & (df['Home Odds Close'] > 3)) |
    ((df['Winning Team'] == df['Away Team']) & (df['Away Odds Close'] > 3))
]

unique_values = df['Venue'].unique()

gmaps = googlemaps.Client(key='AIzaSyD973IqdvJn_w-n03RS8DHgE8mNhnPBk7c')

geocode_result = gmaps.geocode('Marvel Stadium')
print(geocode_result)
