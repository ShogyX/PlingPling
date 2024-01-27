import random
import requests

def generate_company_names(num_names):
    # Use a public API for random company names
    api_url = "https://api.company.name/v1/company?count={}".format(num_names)
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        company_names = response.json()
        return company_names
    else:
        print("Error fetching company names. Using default names.")
        # Default names in case of an error
        default_names = [
            "Acme Corporation",
            "Tech Innovators",
            "Global Solutions Ltd.",
            "Pinnacle Enterprises",
            "Dynamic Ventures",
            # Add more default names as needed
        ]
        return default_names[:num_names]

# Generate 5000 company names
num_company_names = 5000
company_names = generate_company_names(num_company_names)

# Save the list to a text file
with open("company_names.txt", "w") as file:
    file.write("\n".join(company_names))
