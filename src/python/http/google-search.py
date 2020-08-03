# https://towardsdatascience.com/current-google-search-packages-using-python-3-7-a-simple-tutorial-3606e459e0d4

from googlesearch import search 

# to search 
query = "Geeksforgeeks"

for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
    print(j) 
