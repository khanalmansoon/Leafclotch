maala_species= ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = maala_species

print(f"Main masala spices are {spice1}, {spice2} and {spice3}")

ginger_ratio, cardamom_ratio= 2,1
print(f"Ratio is ginger {ginger_ratio} and cardamom {cardamom_ratio}" )
ginger_ratio, cardamom_ratio= cardamom_ratio, ginger_ratio
print(f"Ratio is ginger {ginger_ratio} and cardamom {cardamom_ratio}" )

#member ship

print(f"Is ginger in masala spices? {'ginger' in maala_species}")
print(f"Is cardamom in masala spices? {'cardamom' in maala_species}")