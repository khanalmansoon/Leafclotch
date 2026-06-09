flavours= ["ginger", "out of stock", "lemon"
           "discontinued", "tulsi"]

for flavour in flavours:
    if flavour == "out of stock":
        continue
    if flavour == "discontinued":
        break
    print(f"{flavour} item found")

print(f"out side of loop")    