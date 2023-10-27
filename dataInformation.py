import csv
from faker import Faker
import random

fake = Faker()

# Total number of clients
num_clients = 15

# Generate unique client names dynamically
def generate_client_name(used_names):
    name = fake.unique.first_name() + ' ' + fake.unique.last_name()
    while name in used_names:
        name = fake.unique.first_name() + ' ' + fake.unique.last_name()
    used_names.add(name)
    return name

# Generate unique client places dynamically
def generate_client_place(used_places):
    place = fake.unique.country()
    while place in used_places:
        place = fake.unique.country()
    used_places.add(place)
    return place

# Generate client details and write to CSV
used_names = set()
used_places = set()

with open('client_details.csv', 'w', newline='') as file1, open('client_details2.csv', 'w', newline='') as file2:
    writer1 = csv.writer(file1)
    writer2 = csv.writer(file2)

    # Write headers
    writer1.writerow(["client_id", "client_name"])
    writer2.writerow(["client_id", "client_place"])

    for i in range(num_clients):
        client_id = i + 101  # Starting ID from 101
        client_name = generate_client_name(used_names)
        client_place = generate_client_place(used_places)

        writer1.writerow([client_id, client_name])
        writer2.writerow([client_id, client_place])

print("CSV files generated!")
