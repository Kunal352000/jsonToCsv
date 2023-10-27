import csv
import random
from datetime import datetime, timedelta

# Utility function to generate random dates
def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())))

# Generate Schedule Client CSV
with open('Schedule Client.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Header
    writer.writerow(["partitionKey", "sortKey", "appointmentId", "clientChildBirthDate", 
                     "clientChildId", "clientChildName", "clientChildProfile", "clientParentId", 
                     "clientParentName", "createdAt", "purchaseId", "franchiseeId", "locationId", 
                     "occurrenceClientId", "occurrenceDate", "occurrenceId", "payLater", "status"])

    # Data
    status_values = ["Booked", "Late cancel"]
    for _ in range(10):
        appointment_id = f"#APPO#{random.randint(10000, 99999)}"
        client_child_birth_date = f"{random.randint(1, 28)}-{random.randint(1, 12)}-{random.randint(2000, 2022)}"
        client_child_id = f"#PET#{random.randint(10000, 99999)}"
        client_child_name = f"DogName{random.randint(1, 50)}"
        client_child_profile = f"Profile{random.randint(1, 50)}"
        client_parent_id = f"#CLI#{random.randint(10000, 99999)}"
        client_parent_name = f"ParentName{random.randint(1, 50)}"
        created_at = random_date(datetime(2023, 1, 1), datetime(2023, 12, 31)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        franchisee_id = f"FRA#{random.randint(10000, 99999)}"
        location_id = f"#LOC{random.randint(10000, 99999)}"
        occurrence_date = random_date(datetime(2023, 1, 1), datetime(2023, 12, 31)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        occurrence_id = appointment_id
        pay_later = bool(random.getrandbits(1))
        status = random.choice(status_values)

        writer.writerow([appointment_id, "", appointment_id, client_child_birth_date, client_child_id,
                         client_child_name, client_child_profile, client_parent_id, client_parent_name,
                         created_at, "", franchisee_id, location_id, "", occurrence_date, occurrence_id,
                         pay_later, status])
