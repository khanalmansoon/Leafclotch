menu= ["green", "lemon", "spiced", "mint"]

for m in menu:
    print(f"menu item is {m}")


for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item} chai")    