def discount_rate(total, vip=False):
    if total < 0:
        raise ValueError("Order total cannot be negative.")

    if total >= 200:
        rate = 0.15
    elif total >= 100:
        rate = 0.10
    elif total >= 50:
        rate = 0.05
    else:
        rate = 0.00

    if vip:
        rate += 0.05

    return min(rate, 0.20)

def final_price(total, vip=False):
    return total * (1 - discount_rate(total, vip))

if __name__ == "__main__":
    total = float(input("Order total: "))
    vip = input("VIP customer? (y/n): ").strip().lower() == "y"
    print(f"Discount rate: {discount_rate(total, vip):.0%}")
    print(f"Final price: {final_price(total, vip):.2f}")
