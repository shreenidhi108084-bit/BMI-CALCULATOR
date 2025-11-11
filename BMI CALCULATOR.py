# bmi_cli.py
import time

def get_float(prompt, min_val=None, max_val=None):
    while True:
        try:
            s = input(prompt).strip()
            if s.lower() in ('q', 'quit', 'exit'):
                return None
            val = float(s)
            if min_val is not None and val < min_val:
                print(f"Value must be >= {min_val}. Try again or type 'q' to quit.")
                continue
            if max_val is not None and val > max_val:
                print(f"Value must be <= {max_val}. Try again or type 'q' to quit.")
                continue
            return val
        except ValueError:
            print("Invalid number. Please enter a numeric value (or 'q' to quit).")

def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def bmi_category(bmi):
    # Standard categories (WHO-ish)
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Simple BMI Calculator (type 'q' to quit at any prompt)\n")
    while True:
        w = get_float("Enter weight in kilograms (e.g. 65): ", min_val=10, max_val=500)
        if w is None: break
        h = get_float("Enter height in meters (e.g. 1.70): ", min_val=0.5, max_val=2.5)
        if h is None: break

        bmi = calculate_bmi(w, h)
        category = bmi_category(bmi)
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}\n")

        # Optional extra info
        print("BMI ranges (approx): Underweight <18.5 | Normal 18.5–24.9 | Overweight 25–29.9 | Obese >=30")
        again = input("\nCalculate again? (y/n): ").strip().lower()
        if again not in ('y', 'yes'):
            print("Goodbye — stay healthy!")
            time.sleep(0.4)
            break

if __name__ == "__main__":
    main()
