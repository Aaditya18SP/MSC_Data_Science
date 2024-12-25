fruits_dict = {
        "apple": "green",
        "banana": "yellow",
        "cherry": "red"
        }

fruits_dict["apple"] = "red"
fruits_dict["guava"] = "green"

fruits_dict.pop("cherry")
# del fruits_dict["cherry"]
print(fruits_dict)

print("===============================")
name = "Monty"
title = "Python"
full_name = name + " " + title
print(full_name)
first_name = full_name.split(" ")[0]
print("first name", first_name, "len:", len(first_name)) 

is_f = "f" in full_name
print("Full_name:", full_name , "is f present:", is_f)
