print("*********************")
print("Discount Calculator")
print("*********************")

shopping_amt = float(input("Enter shopping amount: "))

if shopping_amt >= 500 and shopping_amt < 2000:
    print(f"Final amount: {shopping_amt - (0.1 * shopping_amt)}")
elif shopping_amt >= 2000 and shopping_amt < 5000:
    print(f"Final amount: {shopping_amt - (0.25 * shopping_amt)}")
elif shopping_amt >= 5000:
    print(f"Final amount: {shopping_amt - (0.5 * shopping_amt)}")
else:
    print(f"Not eligible for discount. Final amount: {shopping_amt}")

