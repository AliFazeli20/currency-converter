import requests
import json
import os


currencies = {
    1: ("USD", "US Dollar"),
    2: ("EUR", "Euro"),
    3: ("GBP", "British Pound"),
    4: ("CAD", "Canadian Dollar"),
    5: ("AUD", "Australian Dollar"),
    6: ("JPY", "Japanese Yen"),
    7: ("CHF", "Swiss Franc")
}


HISTORY_FILE = "history.json"


def show_currencies():
    print("\nAvailable currencies:")

    for number, (code, name) in currencies.items():
        print(f"{number}. {code} - {name}")

    print("0. Exit")


def choose_currency(message):
    while True:
        choice = input(message).strip()

        if choice == "0":
            return None

        if choice.isdigit():
            choice = int(choice)

            if choice in currencies:
                return currencies[choice][0]

            print("Invalid currency number.")

        else:
            code = choice.upper()

            valid_codes = [currency[0] for currency in currencies.values()]

            if code in valid_codes:
                return code

            print("Invalid currency code.")


def get_exchange_rate(from_currency, to_currency):
    if from_currency == to_currency:
        return 1, None

    url = f"https://api.frankfurter.dev/v2/rate/{from_currency}/{to_currency}"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    rate = data["rate"]
    rate_date = data["date"]

    return rate, rate_date


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_history(history):
    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def add_to_history(
    from_currency,
    to_currency,
    amount,
    rate,
    converted,
    rate_date
):
    history = load_history()

    conversion = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "rate": rate,
        "converted": converted,
        "rate_date": rate_date
    }

    history.append(conversion)

    save_history(history)


def format_number(number):
    return f"{number:,.2f}"


def show_history(history=None):
    if history is None:
        history = load_history()

    if not history:
        print("\nNo conversion history found.")
        return

    print("\n=============================")
    print("       Conversion History")
    print("=============================")

    for number, conversion in enumerate(history, start=1):
        amount = conversion["amount"]
        converted = conversion["converted"]
        rate = conversion["rate"]

        print(f"\n{number}.")
        print(
            f"{format_number(amount)} "
            f"{conversion['from']} -> "
            f"{format_number(converted)} "
            f"{conversion['to']}"
        )

        print(
            f"Rate: 1 {conversion['from']} = "
            f"{rate:g} {conversion['to']}"
        )

        if conversion["rate_date"]:
            print(f"Rate date: {conversion['rate_date']}")

    print("\n=============================")
    print(f"Total records: {len(history)}")


def clear_history():
    history = load_history()

    if not history:
        print("\nHistory is already empty.")
        return

    print(f"\nYou have {len(history)} conversion(s) in history.")

    confirmation = input(
        "Are you sure you want to delete all history? (y/n): "
    ).strip().lower()

    if confirmation == "y":
        save_history([])
        print("\nHistory cleared successfully.")

    else:
        print("\nHistory was not deleted.")


def search_history():
    history = load_history()

    if not history:
        print("\nNo conversion history found.")
        return

    search = input(
        "\nEnter currency code to search: "
    ).strip().upper()

    valid_codes = [currency[0] for currency in currencies.values()]

    if search not in valid_codes:
        print("\nInvalid currency code.")
        return

    results = []

    for conversion in history:
        if (
            conversion["from"] == search
            or conversion["to"] == search
        ):
            results.append(conversion)

    if not results:
        print(f"\nNo conversions found for {search}.")
        return

    print(f"\nResults for {search}:")

    show_history(results)


def convert_currency():
    show_currencies()

    from_currency = choose_currency(
        "Select source currency: "
    )

    if from_currency is None:
        return False

    to_currency = choose_currency(
        "Select target currency: "
    )

    if to_currency is None:
        return False

    while True:
        try:
            amount = float(input("Amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    try:
        rate, rate_date = get_exchange_rate(
            from_currency,
            to_currency
        )

        converted = amount * rate

        print("\n-----------------------------")
        print("Conversion Result")
        print("-----------------------------")

        print(
            f"Amount: "
            f"{format_number(amount)} "
            f"{from_currency}"
        )

        print(
            f"Rate: 1 {from_currency} = "
            f"{rate:g} {to_currency}"
        )

        print(
            f"Result: "
            f"{format_number(converted)} "
            f"{to_currency}"
        )

        if rate_date:
            print(f"Rate date: {rate_date}")

        print("-----------------------------")

        add_to_history(
            from_currency,
            to_currency,
            amount,
            rate,
            converted,
            rate_date
        )

        print("Conversion saved to history.")

    except requests.RequestException:
        print("\nCould not connect to the currency API.")

    return True


def main():
    while True:
        print("\n=============================")
        print("      Currency Converter")
        print("=============================")
        print("1. Convert currency")
        print("2. View history")
        print("3. Search history")
        print("4. Clear history")
        print("0. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            convert_currency()

        elif choice == "2":
            show_history()

        elif choice == "3":
            search_history()

        elif choice == "4":
            clear_history()

        elif choice == "0":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option.")


main()