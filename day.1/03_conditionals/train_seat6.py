seat_type= input("Enter seat type (sleeper/AC/general/luxury): ").lower()


match seat_type:
    case "sleeper":
        print("sleeper - No AC, bead available")
    case"AC":
        print("AC - Air Conditioned, comfy ride")
    case"general":
        print("General - Cheaper option, no reservation")
    case"luxury":
        print("Luxury - Primum seat with meals")
    case"sofa":
print("Invalide seat type")                