first_name = input("Introduceți prenumele: ")
last_name = input("Introduceți numele: ")

# Inițialele
initials = first_name[0].upper() + '.' + last_name[0].upper() + '.'
print("Inițialele sunt:", initials)

# Numele din agendă
full_name = first_name.capitalize() + ' ' + last_name.capitalize()
print("Numele din agendă este:", full_name)

# Numele de utilizator
username = (first_name[0] + last_name).lower()
print("Numele de utilizator este:", username)
