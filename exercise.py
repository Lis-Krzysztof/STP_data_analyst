import pandas as pd
import requests

INPUT_FILE_PATH = "sales_report_input.csv"
OUTPUT_FILE_PATH = "sales_report_output.csv"
API_ADDRESS = "https://open.er-api.com/v6/latest/"
CURRENCY = "EUR"

def main():
    url = API_ADDRESS + CURRENCY
    current_rates = requests.get(url).json()["rates"]

    sales_report_input = pd.read_csv(INPUT_FILE_PATH)

    sales_report_input["budget_local_currency"] = sales_report_input[
        "budget_EUR"
    ] * sales_report_input["local_currency"].map(current_rates)

    sales_report_input.to_csv(OUTPUT_FILE_PATH)


if __name__ == "__main__":
    main()
