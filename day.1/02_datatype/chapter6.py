chai_type= "Ginger chai"
customer_name= "Preeti"

print(f"Order for {customer_name} is {chai_type}")

chai_description= "Aeo,atic and Bold"
print(f"First word: {chai_description[0:8]}")
print(f"Last word: {chai_description[12:]}")
print(f"Last word: {chai_description[::-1]}")

lable_text= "chai Special"
ecoded_label= labele_text.encode("utf-8")
print(f"Non Encoded label: {lable_text}")
print(f"Encoded label: {ecoded_label}")
decoded_label= encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")