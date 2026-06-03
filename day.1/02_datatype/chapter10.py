chai_order= dict("Masala Chai", size="Large", sugar_level=3)
print(f"Order: {chai_order}")

chai_recipe= {}
chai_recipe["base"]= "black tea"
chai_recipe["liquid"]= "milk"

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe: {chai_recipe}")
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order= {"type": "ginger chai", "size": "medium", "sugar_level": 2}

#print(f"order details(keys): {chai_order.keys()}")
#print(f"order details(values): {chai_order.values()}")
#print(f"order details(items): {chai_order.items()}")

last_item= chai_order.popitem()
print(f" RemovedLast item: {last_item}")

extra_spices= {"cardamom": "crushed", "ginger": "sliced"}
chai_order.update(extra_spices)

print(f"Updated order: {chai_order}")

Chai_note= chai_order.get("size", "NO NOTE")
print(f"Customer_note: {Customer_note}")
