# import csv

# # Sample data
# add_name = str(input("Add name: "))
# add_num = str(input("Add Number: "))
# add_mail = str(input("Add Mail: "))

# data = [
#     ["John Doe", "123456", "john@example.com"],
#     ["Jane Smith", "789012", "jane@example.com"],
#     ["Bob Johnson", "345678", "bob@example.com"],
#     []
# ]

# # Open the CSV file in write mode
# with open('output.csv', 'w', newline='') as file:
#     writer = csv.writer(file)

#     # Write each row of data to the CSV file
#     for row in data:
#         writer.writerow(row)

# print("CSV file has been written successfully!")









import csv

def read_csv(filename):
    """Read data from a CSV file."""
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def write_csv(filename, data):
    """Write data to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def add_data_to_csv(filename):
    """Add data to an existing CSV file."""
    existing_data = read_csv(filename)

    # Collect input from the user
    new_data = input("Enter new data (comma-separated): ").split(',')

    # Add the new data to the existing data
    existing_data.append(new_data)

    # Write the updated data back to the CSV file
    write_csv(filename, existing_data)

# Example usage:
add_data_to_csv('output.csv')

