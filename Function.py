#def function get_value return first character name
def get_value(name):
    value = name[0:1]
    return value

#prompt user to enter firstname
first_name = input("Please enter a firstname\n")

#assign get_value function to first_name
first_name_value = get_value(first_name)

#output first character name
print(first_name_value)