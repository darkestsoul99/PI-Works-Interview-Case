#############################################################
#                                                           #
# Interview case solution for P.I. Works Job Application    #
#                                                           #
# Author : Berke Kocadere                                   #
#                                                           #
#                                                           #
#############################################################

# Imports
import pandas as pd
import os

string = "10/08/2016" # Date condition

df = pd.read_csv("exhibitA-input.csv", sep='\t') # Read CSV file

df = df.convert_dtypes() # Convert to convenient data types

df = df[df['PLAY_TS'].str.contains(string)] # If it contains the string, create a new dataframe with this condition

print(df)

df = df.groupby('CLIENT_ID') # Group by CLIENT_ID

data = [] # Empty list

# Iterate over each group (client) and find unique songs for each client
for client, group in df:
    print(client)
    print(group)
    print(type(group))
    print("\n")

    series = group['SONG_ID'].nunique()
    print(series)
    print(type(series))

    data.append([series, client])

df2 = pd.DataFrame(data, columns=['DISTINCT_PLAY_COUNT', 'CLIENT_ID']) # Create the output dataframe

print(df2)

csv_data = df2.to_csv('{}/output.csv'.format(os.getcwd())) # Save to a CSV File

print(df2[df2['DISTINCT_PLAY_COUNT'] == 346])
print(df2[df2['DISTINCT_PLAY_COUNT'] == 346].count()) # Number of users who listened 346 distinct songs

print(df2.max(axis = 0)) # Max number of distincts songs played