# Jamie Hilton
# 09/01/2015
# Search list

def linear_search (search_list, search_person):
    found = False
    count = 0
    while not found and count < len(search_list):
        if search_list[count] == search_person:
           found = True
        else:
           count + 1 
        
        return found

def output(found):
    if found == True:
        print("Found")
    else:
        print("Not Found")
   
    
# Main Program

search_list = ["Bob", "Jim", "Terry", "Mark", "Alex", "Sam"]

search_person = input("Please enter the name you are looking for: ")


found = linear_search(search_list, search_person)

output(found)
