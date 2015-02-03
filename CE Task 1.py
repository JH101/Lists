# Jamie Hilton
# 12/12/2014
# class exercises Task 1

names = ['Jim', 'Bob', 'Alison', 'Jo', 'James']

element_sought = input('Enter the name you are searching for : ')
this_element = 0
found = False
while found == False:
       if names[this_element] == element_sought:
          Found = True
       else:
          this_element = this_element + 1

if Found == True:
   print('{0} was in element {1} in the list'.format(element_sought, this_element))
else:
   print('Not found')
