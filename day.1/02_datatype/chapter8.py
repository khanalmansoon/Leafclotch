ingridents=["water", "milk", "black tea"]
ingridents.append("sugar")
print(f"Ingridents are: {ingridents}")
ingridents.remove("water")
print(f"Ingridents are: {ingridents}")

spice_options= ["ginger", "cardamom", "cinnamon"]
chai_ingridents= ["water", "milk"]

chai_ingridents.extend(spice_options)
print(f"Chai: {chai_ingridents}")
chai_ingridents.insert(2, "black tea")
print(f"Chai: {chai_ingridents}")

last_added= chai_ingridents.pop()
print(f"{last_added}")
print(f"chai: {chai_ingridents}")
chai_ingridents.remove()
print(f"chai: {chai_ingridents}")
chai_ingridents.sort()
print(f"chai: {chai_ingridents}")

sugar_levels= [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")  

base_liquid=["water", "milk"]
extra_flavor= ["ginger"]

full_liquid_mix= base_liquid + extra_flavor
print(f"liquid mix: {full_liquid_mix}")

strong_brew= ["black tea"] * 3
print(f"strong brew: {strong_brew}")

raw_spice_data= bytearray(b"cardamom")
raw_spice_data = raw_spice_data.replace(b"cinnamon", b"cardamom")
print(f"Bytes:{raw_spice_data}")