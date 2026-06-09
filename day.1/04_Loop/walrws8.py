#value= 13
#remainder= value % 5

#if remainder:
#   print(f"no divisible, remainder is {remainder}")


vakue= 13

if remainder:= value % 5:
    print(f"no divisible, remainder is {remainder}")


#available_size= ["small", "medium", "large"]

#if (requested_size := input(enter your chai cup size:)) in available_sizes:
#print(f"serving {request_size} chai")
#else:
#print(f"size is unavailable - {requested_size}")


flavour= ["masala", "ginger", "lemon", "mint"]

print("available flavour: ", flavour)


while (flavour := input("choose your flavour:")) not in flavour:
    print(f"sorry,{flavour} is not available")
print(f"you choose {flavour} chai")    