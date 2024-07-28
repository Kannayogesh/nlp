# data_preparation.py

def load_transactions():
    # Sample transaction descriptions
    return [
        "Payment to ABC Corp for office supplies",
        "Received payment from XYZ Inc.",
        "Transfer to DEF LLC for consulting services",
        "Payment for coffee",
        "Received dividend from GHI Industries"
    ]

def load_organizations():
    # List of known organizations
    return ["ABC Corp", "XYZ Inc.", "DEF LLC", "GHI Industries"]

def clean_data(data):
    # This function can be extended to perform actual data cleaning
    return [item.strip() for item in data]
# pattern_matching.py

def identify_organization(transaction, organizations):
    for org in organizations:
        if org.lower() in transaction.lower():
            return org
    return "Unknown"

def match_transactions_with_organizations(transactions, organizations):
    results = []
    for transaction in transactions:
        org = identify_organization(transaction, organizations)
        results.append((transaction, org))
    return results
# output.py

def display_results(results):
    for transaction, org in results:
        print(f"Transaction: '{transaction}' - Identified Organization: '{org}'")

def save_results_to_file(results, filename="results.txt"):
    with open(filename, 'w') as file:
        for transaction, org in results:
            file.write(f"Transaction: '{transaction}' - Identified Organization: '{org}'\n")
# main.py

from data_preparation import load_transactions, load_organizations, clean_data # type: ignore
from pattern_matching import match_transactions_with_organizations # type: ignore
from output import display_results, save_results_to_file # type: ignore

def main():
    # Load and clean data
    transactions = clean_data(load_transactions())
    organizations = clean_data(load_organizations())
    
    # Match transactions with organizations
    results = match_transactions_with_organizations(transactions, organizations)
    
    # Display or save results
    display_results(results)
    save_results_to_file(results)

if __name__ == "__main__":
    main()
