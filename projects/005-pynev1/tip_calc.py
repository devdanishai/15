def calculate_tip(bill: float, tip_percent: float, people: int) -> dict:
    tip_total = bill * (tip_percent / 100)
    grand_total = bill + tip_total
    per_person = grand_total / people
    return {
        "tip_total": round(tip_total, 2),
        "grand_total": round(grand_total, 2),
        "per_person": round(per_person, 2),
    }

def main():
    print("=== Tip Calculator ===")
    bill = float(input("Bill amount: $"))
    tip = float(input("Tip % (e.g. 15): "))
    people = int(input("Number of people: "))

    result = calculate_tip(bill, tip, people)
    print(f"\nTip:         ${result['tip_total']}")
    print(f"Total:       ${result['grand_total']}")
    print(f"Per person:  ${result['per_person']}")

if __name__ == "__main__":
    main()
