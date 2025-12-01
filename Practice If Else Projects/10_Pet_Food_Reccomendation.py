pet = input("Enter a pet: ")
pet_age = input("Enter a pet age: ")

if pet == "Dog" and (pet_age.isdigit() == True):
    age = int(pet_age)
    if (age <= 2):
        print("Give Him Puppy Food")
    else:
        print("Give Him Dog Food")
        exit()

if pet == "Cat" and (pet_age.isdigit() == True):
    age = int(pet_age)
    if (age <= 2):
        print("Give Him Little Cab Food")
    else:
        print("Give Him Normal Cat Food")
        exit()

