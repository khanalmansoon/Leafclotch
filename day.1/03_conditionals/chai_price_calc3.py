cup_size = input("Choose your cup size (small/medium/large): ").lower()

if cup_size == "small":
    print("Price is Rs10")
elif cup_size == "medium":
    print("Price is Rs15")
elif cup_size == "large":
    print("Price is Rs20")
else:
    print("Unknown cup size. Please choose small, medium, or large.")