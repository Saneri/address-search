import csv
import json

# This script processes a CSV file containing address data and converts it into bulk JSON files suitable for OpenSearch.
# It reads the CSV file, removes duplicate addresses, replaces municipality codes with their corresponding names,
# and writes the data into multiple JSON files in chunks. Each JSON file contains index metadata and document data
# formatted for bulk indexing into an OpenSearch index.

INDEX_NAME = 'addresses'
INPUT_FILE = './finland_addresses/Finland_addresses_2024-02-13.csv'
OUTPUT_FILE = './finland_address_bulks/finland_addresses'

def csv_to_opensearch_bulk(csv_file_path, output_file_path, chunk_size=100000):
    # Load the municipality codes and names
    with open('./municipalities.json', 'r') as f:
        municipalities = json.load(f)
        # Flatten the list of dictionaries into a single dictionary
        municipality_dict = {k: v for d in municipalities for k, v in d.items()}

    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        output_file = None
        seen_addresses = set()
        for i, row in enumerate(reader):
            # Determine the output file for this row
            if i % chunk_size == 0:
                if output_file is not None:
                    output_file.close()
                chunk_file_path = f"{output_file_path}_{i // chunk_size}.json"
                output_file = open(chunk_file_path, 'w')

            # Create a tuple representing the address
            address = (row['municipality'], row['street'], row['house_number'], row['postal_code'])

            # If we've seen this address before, skip it
            if address in seen_addresses:
                continue

            # Otherwise, add it to the set of seen addresses
            seen_addresses.add(address)

            # Write the index metadata line
            index_metadata = {"index": {"_index": INDEX_NAME, "_id": i}}
            output_file.write(json.dumps(index_metadata) + "\n")

            # Replace the municipality code with the name
            municipality_name = municipality_dict.get(row['municipality'], row['municipality'])

            # Write the document data line
            document_data = {"municipality": municipality_name, "street": row['street'], "house_number": row['house_number'], "postal_code": row['postal_code']}
            output_file.write(json.dumps(document_data) + "\n")

        if output_file is not None:
            output_file.close()

csv_to_opensearch_bulk('./finland_addresses/Finland_addresses_2024-02-13.csv', './finland_address_bulks/finland_addresses')