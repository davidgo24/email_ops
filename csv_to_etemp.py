import pandas as pd
from pathlib import Path



p = Path('/Users/david/desktop')

q = p / 'data.xlsx'

df = pd.read_excel(q)

print(df['Delivery Type?'])

row_data = df['Delivery Type?'] 

def deliveries_types():
    for i in row_data:
        outdoor_deliveries = 0
        if i == 'Outdoor':
            outdoor_deliveries += 1
    return outdoor_deliveries

print(deliveries_types())

        


#practice with pandas - nba

'''

data = {'Name': ['Kobe', 'Antetekoumpo', 'LeBron'], 'Championships': [5, 1, 4]}
df_people = pd.DataFrame(data, index=['first', 'second', 'third'])

print(df_people.to_string(justify='right', float_format='${:,.2f}'.format))


## most common and efficient way to convert the data into an array (numpy array)
new_array = df_people.values

#print(new_array)


##accessing the row "index" objects - will return an integer unless you create the index using the index in the dataframe construction

rank_name = df_people.index
#print(row_index)

##accessing the column "index" objects

col_index = df_people.columns
#print(col_index)

## in order to address "index objects" aka column and row labels, we will use pandas index objects


# i want to print every name and age in the dataframe i created


'''

'''for position, (player_name, player_championships) in enumerate(new_array):
    custom_index_name = row_index[position]
    print(f"NBA GOATS in order: {custom_index_name}===== Name: {player_name} ==== Championships: {player_championships}")
'''
'''
rank_max = max(len(label) for label in rank_name)
player_name_max = max(len(player[0]) for player in new_array)
championships_max = max(len(str(player[1])) for player in new_array)

for position, (player_name, player_championships) in enumerate(new_array):
    print(f"NBA GOATS in order: {rank_name[position]:{rank_max}}===== Name: {player_name:{player_name_max}} ==== Championships: {player_championships:{championships_max}}")
'''


'''# Accessing by label (Index) - should print Noelia
print(df.loc['A'])
# Accessing by position - should print Noelia
print(df.iloc[0])

'''