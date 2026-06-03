essential_spices= ["ginger", "cardamom", "cinnamon"]
optional_spices= ["cloves", "ginger", "black paper"]

all_species= essential_spices + optional_spices
print(f"All spices: {all_species}")

common_spices= essential_spices & optional_spices
print(f"Common spices: {common_spices}")    

only_in_essential= essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")

print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")

