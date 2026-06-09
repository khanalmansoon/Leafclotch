name= ["mune", "sam", "smit", "shin", "grac"]
bills= [50, 70, 100, 55]

for name, amount in zip(name, bills):
    print(f"{name} paid {amount} rupees")