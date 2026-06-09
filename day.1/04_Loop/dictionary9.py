users= [
    {"id": 1, "total: 100", "coopon":P20}
    {"id": 2, "total: 150", "coopon":P10}
    {"id": 3, "total: 80", "coopon":P50}
]

discount= {
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0, 10),
}

for user in users:
    percent, fixed= discounts.get(user["coopon"], (0,0))
    discount= user["total"] * precent + fixed
    print(f"{user["id"]} paid {user["total"]} and got discount for next viit of rs {discount}")