# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 20:01:36 2024

@author: Acer
"""

import pandas as pd

#Importing the data

# Specify the path to your Excel file
# excel_file = 'D:\\data.xlsx'
excel_file = 'C:\\Users\\Jebeto\\OneDrive\\Career\\Economist\\University\\MA\\Central European University\\Administrative\\Research Assistantship Application\\data.xlsx'


# Use pandas' ExcelFile class to load the entire Excel file
xls = pd.ExcelFile(excel_file)

# Parse each sheet into a separate DataFrame
sheet_names = xls.sheet_names
dfs = {}  # Dictionary to hold DataFrames for each sheet
for sheet_name in sheet_names:
    dfs[sheet_name] = pd.read_excel(xls, sheet_name)
    

#Task 1

# Count the number of tenders per city
tenders_per_city = dfs['tender'].groupby('location')['tender_id'].nunique().reset_index()

# Rename the columns for clarity

tenders_per_city.columns = ['City', 'Number of Tenders']

print(tenders_per_city)

#Task 2

# Count the number of bidders per tenders
bidders_per_tenders = dfs['bid'].groupby('tender_id')['bidder_id'].nunique().reset_index()

# Rename the columns for clarity
bidders_per_tenders.columns = ['Tender', 'Number of Bidders']

print(bidders_per_tenders)

#Task 3

# Accessing the bidder dataframe
bidder_df = dfs['bidder']
#print("Bidder DataFrame:")
#print(bidder_df)

# Accessing the tender dataframe
tender_df = dfs['tender']
#print("\nTender DataFrame:")
#print(tender_df)

# Accessing the bid dataframe
bid_df = dfs['bid']
#print("\nBid DataFrame:")
#print(bid_df)

# Merge bid dataframe with bidder dataframe to get bidder city
bid_with_city = bid_df.merge(bidder_df, on='bidder_id')

# Merge bid_with_city with tender dataframe to get tender location
bid_with_city_tender = bid_with_city.merge(tender_df, on='tender_id')

# Filter out only the necessary columns
bid_with_city_tender = bid_with_city_tender[['city', 'location']]

# Group by city pairs and count the number of bids
city_pair_counts = bid_with_city_tender.groupby(['city', 'location']).size().reset_index(name='bid_count')

# Rename the columns for clarity
city_pair_counts.columns = ['City', 'Location', 'Bid Count']

# Display the result
print(city_pair_counts)

#Task 4

# Expand the potential bidder and potential tender combinations
potential_bids = pd.merge(bidder_df.assign(key=1), tender_df.assign(key=1), on='key').drop('key', axis=1)

# Initialize an empty list to store local_experience values
local_experience_list = []

# Iterate over each potential bidder and each potential tender combination
for index, row in potential_bids.iterrows():
    bidder_id = row['bidder_id']
    tender_id = row['tender_id']
    city = row['city']
    location = row['location']
    year = row['year']
    
    # Check if the bidder has bid in the same city as the tender before the year of the tender
    has_local_experience = bid_df[(bid_df['bidder_id'] == bidder_id) & 
                                  (bid_df['tender_id'] != tender_id) & 
                                  (bid_df['bidder_id'].isin(bidder_df[bidder_df['city'] == location]['bidder_id'])) & 
                                  (tender_df['year'] < year)].shape[0] > 0
    
    # Append 1 if the bidder has local experience, 0 otherwise
    local_experience_list.append(1 if has_local_experience else 0)

# Add the local_experience list as a new column in potential_bids dataframe
potential_bids['local_experience'] = local_experience_list

# Cross-tabulate the frequency distribution of local_experience with the year of the tender
cross_tab = pd.crosstab(potential_bids['local_experience'], potential_bids['year'], margins=True)

print(cross_tab)
