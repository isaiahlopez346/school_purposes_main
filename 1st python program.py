print("="*54)
print("Walang Lusot, May Resibo — A Fund Transparency System")
print("         CREATED BY: ISAIAH MOSES B. LOPEZ")
print("                      ACT-1F")
print("="*54)
print('')

while True:
    money = input("Enter starting money: ")

    if money == "":
        print("NO AMOUNT ADDED")
        print("TRY AGAIN")
        exit()

    if not money.replace(".", "", 1).isdigit():
        print("INVALID INPUT")
        print("TRY AGAIN")
        exit()

    money = float(money)

    if money <= 0:
        print("INSUFFICIENT FUNDS")
        print("TRY AGAIN")
        exit()
    else:
        print(f"FUNDS: P{money:.2f}")
        break

expense = input("\nWhat was the money used for? ")
amount = float(input("How much was spent? P"))

if amount <= 0:
    print("INVALID AMOUNT")
    print("TRY AGAIN")
    exit()

if amount > money:
    print("Insufficient funds.")
    print("TRY AGAIN")
    exit()

elif amount < money:
    again = input("\nAdd another expense? (Y/N): ").upper()

    if again == "Y":
        expense1 = input("\nWhat was the money used for? ")
        amount1 = float(input("How much was spent? P"))

        if amount1 <= 0:
            print("INVALID AMOUNT")
            print("TRY AGAIN")
            exit()

        again = input("\nAdd another expense? (Y/N): ").upper()

        if again == "Y":
            expense2 = input("\nWhat was the money used for? ")
            amount2 = float(input("How much was spent? P"))

            if amount2 <= 0:
                print("INVALID AMOUNT")
                print("TRY AGAIN")
                exit()

            again = input("\nAdd another expense? (Y/N): ").upper()

            if again == "Y":
                expense3 = input("\nWhat was the money used for? ")
                amount3 = float(input("How much was spent? P"))

                if amount3 <= 0:
                    print("INVALID AMOUNT")
                    print("TRY AGAIN")
                    exit()
else:
    print("The amount is exactly equal to your available money.")

total_spent = float(amount)

if 'amount1' in locals():
    total_spent += amount1

if 'amount2' in locals():
    total_spent += amount2

if 'amount3' in locals():
    total_spent += amount3

if total_spent > money:
    print("\nInsufficient funds.")
    print("TOTAL EXPENSES EXCEED AVAILABLE FUNDS.")
    print("TRY AGAIN")
    exit()

remaining_funds = money - total_spent

print('')
print("="*54)
print("                 TRANSPARENCY REPORT")
print("="*54)

print(f"{expense}: P{amount:.2f}")

if 'expense1' in locals():
    print(f"{expense1}: P{amount1:.2f}")

if 'expense2' in locals():
    print(f"{expense2}: P{amount2:.2f}")

if 'expense3' in locals():
    print(f"{expense3}: P{amount3:.2f}")

print("="*54)
print(f"FUNDS: P{money:.2f}")
print(f"TOTAL SPENT: P{total_spent:.2f}")
print(f"REMAINING FUNDS: P{remaining_funds:.2f}")
print("="*54)