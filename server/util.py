# Updated code to use data from the JSON file
import json
import numpy as np

# __locations = None
__data_columns = None

# Load the data from the JSON file
with open('../model/data.json', 'r') as json_file:  # Correct path to your file
    cocktails_data = json.load(json_file)

# List of available cocktails (data columns)
__data_columns = list(cocktails_data.keys())

# Function to get data columns (cocktail names)
def get_data_columns():
    return __data_columns

# Function to search for top 3 bars based on the cocktail
# def search_cocktail(cocktail_name):
#     cocktail_name = cocktail_name.title()  # Ensure proper case
#     if cocktail_name in __data_columns:
#         print(f"\n{'*' * 40}")
#         print(f"{cocktail_name.upper()} - Top 3 Bars\n")
#         for idx, bar in enumerate(cocktails_data[cocktail_name], 1):
#             print(f" {idx}. {bar}")
#         print(f"{'*' * 40}\n")
#     else:
#         print(f"\n{'=' * 40}")
#         print(f"Sorry, no information available for '{cocktail_name}'.")
#         print(f"{'=' * 40}\n")

def search_cocktail(cocktail_name):
    cocktail_name = cocktail_name.title()  # Ensure proper case

    if cocktail_name in cocktails_data:
        # Construct the result string
        result = f"<br>{'*' * 40}<br>{cocktail_name.upper()} - Top 3 Bars<br>"
        for idx, bar in enumerate(cocktails_data[cocktail_name], 1):
            result += f" {idx}. {bar}<br>"
        result += f"{'*' * 40}<br>"

        return result  # Return the formatted result string
    else:
        return f"Sorry, no information available for '{cocktail_name}'.\n"  # Return not found message


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns1

    with open("./artifacts/columns.json", "r") as f:
        __data_columns1 = json.load(f)['data_columns']

    print("loading saved artifacts...done")


# Example of using the search engine
if __name__ == "__main__":
    load_saved_artifacts()
    user_input = input("🍸 Enter the name of the cocktail you're searching for: ")
    res = search_cocktail(user_input)
    print(res)
