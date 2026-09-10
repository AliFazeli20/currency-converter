# Currency Converter

A simple command-line currency converter written in Python using the [Frankfurter API](https://frankfurter.dev/).

The application allows users to convert between multiple currencies, view and search conversion history, and store conversion data locally in a JSON file.

## Features

* Convert between multiple currencies
* Supports both currency numbers and currency codes
* Fetches current exchange rates from the Frankfurter API
* Displays the exchange rate date
* Saves conversion history locally
* View previous conversions
* Search conversion history by currency
* Clear conversion history
* Input validation and error handling
* Formats large numbers for better readability

## Supported Currencies

* USD — US Dollar
* EUR — Euro
* GBP — British Pound
* CAD — Canadian Dollar
* AUD — Australian Dollar
* JPY — Japanese Yen
* CHF — Swiss Franc

## Technologies

* Python
* Requests
* JSON
* Frankfurter API

## Project Structure

```text
currency-converter/
│
├── currency_converter.py
├── history.json
└── README.md
```

### `currency_converter.py`

Contains the main application logic, including:

* Currency selection
* Exchange rate retrieval
* Currency conversion
* History management
* Input validation
* Command-line interface

### `history.json`

Stores conversion history locally in JSON format.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/AliFazeli20/currency-converter.git
```

### 2. Navigate to the project directory

```bash
cd currency-converter
```

### 3. Install the required package

Install `requests` using pip:

```bash
pip install requests
```

## Usage

Run the application with:

```bash
python currency_converter.py
```

You will see the main menu:

```text
=============================
      Currency Converter
=============================
1. Convert currency
2. View history
3. Search history
4. Clear history
0. Exit
```

### Convert Currency

Select option `1`, choose the source and target currencies, and enter the amount.

The application retrieves the exchange rate from the Frankfurter API and displays the converted amount.

### View History

Select option `2` to view previously saved conversions.

### Search History

Select option `3` and enter a currency code such as `USD` or `EUR` to find conversions involving that currency.

### Clear History

Select option `4` to delete all saved conversion history.

## API

This project uses the **Frankfurter API** to retrieve exchange rates.

Frankfurter is a free and open-source API for current and historical exchange rates.

API documentation:

https://frankfurter.dev/

Example endpoint:

```text
https://api.frankfurter.dev/v2/rate/USD/EUR
```

## Error Handling

The application handles several common errors, including:

* Invalid currency selection
* Invalid numeric input
* Amounts less than or equal to zero
* Network/API connection errors
* Invalid or corrupted history data

## Data Storage

Conversion history is stored locally in:

```text
history.json
```

The file contains information such as:

* Source currency
* Target currency
* Original amount
* Exchange rate
* Converted amount
* Exchange rate date

Example:

```json
[
    {
        "from": "USD",
        "to": "EUR",
        "amount": 100,
        "rate": 0.85,
        "converted": 85,
        "rate_date": "2026-09-10"
    }
]
```

## Future Improvements

Possible improvements for future versions include:

* Add more currencies
* Add a graphical user interface
* Add automatic currency list retrieval
* Add conversion statistics
* Add date-based history filtering
* Add unit tests
* Improve project structure by separating the application into multiple modules

## Author

**Ali Fazeli**

GitHub: [AliFazeli20](https://github.com/AliFazeli20)
