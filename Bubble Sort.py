# Jamie Hilton
# 09/01/2015
# Bubble Sort



def bubble_sort(people):
   no_more_swaps = False
   while no_more_swaps == False:
       no_more_swaps = True
       for count in range(len(people)-1):
           if people[count] > people[count+1]:
               no_more_swaps = False
               temp = people[count]
               people[count] = people[count+1]
               people[count+1] = temp
               count + 1
  


# Main Program
people = ["Callum", "Kav", "George", "Euan", "Chris", "Jamie"]
bubble_sort(people)
print(people)
            
    
