def main():
    print("Enter SalesPerson Name")
    s_name = input()
    print("Enter Customer Name")
    c_name = input()
    print("Product type (x, y or z)")
    p_type = input()
    print("Number of units")
    units = float(input())
    discount = sale = vat = 0
    price = 80 if p_type == "x" else 95 if p_type == "y" else 135 if p_type == "y" else 0
    sale = units * price
    if sale > 10000:
        percent = 0.1 if p_type == "x" else 0.05 if p_type == "y" or "z" else 0
        discount = sale * percent
    vat = (sale-discount)*0.16 if p_type == "x" else 0
    to_pay = sale - discount + vat
    print(f"The total purchase for {c_name} is: ksh {sale}")
    print(f"Discount: {discount}")
    print(f"VAT: {vat}")
    print(f"Amount to pay: {to_pay}")
    print(f"Sales Person: {s_name}")


if __name__ == "__main__":
    main()

