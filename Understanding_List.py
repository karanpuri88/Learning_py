# understanding list , it always use square bracket

from typing_extensions import Annotated


list1 = ["Cisco", "Junper", "Velo_Cloud", "Cloudginix"]

print(list1[0]) # this will print first item of list

# If you want to print all items , use for loop

for items in list1:
     print(items)

# Items in list can have list of lists

list2 = [["ipsec" , 50] , ["gre" , 47], ["bfd_tunnels", 51]]

for new_items , numbers in list2:
    print(new_items , " and its protocol number is", numbers) # This is to print items in list separately 


list3 = ["Test", 2, 5, 111, "Test 2", "Test3"]

for items_1 in list3:
    if str(items_1).isnumeric() and items_1> 10:
        print(items_1)