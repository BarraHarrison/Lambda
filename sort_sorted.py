list_of_numbers = [34, 11, 23, 68, 98, 58473]
squared_numbers_list = [3, 5, 9, 12, 18, 23]

print(filter(lambda x:x % 2 == 0, list_of_numbers))
print(filter(lambda x: x**3, squared_numbers_list))
print("---------------------")
print(list_of_numbers)
print(squared_numbers_list)