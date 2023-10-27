import csv
import random
from datetime import datetime, timedelta

# Utility function to generate random dates
def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())))

# Generate Schedule Location CSV
with open('Schedule Location.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Header
    writer.writerow(["partitionKey", "sortKey", "categoryId", "CategoryName", "clientDetails", 
                     "createdAt", "createdBy", "franchiseeId", "fromDate", "locationId", 
                     "maximumCapacity", "maximumWaitngListCapacity", "occurrence", "repeat",
                     "room", "scheduleType", "serviceId", "serviceName", "trainerAvailability",
                     "tarinerId", "trainerName", "trainerSlots", "updatedAt"])

    # Data
    service_names = ["Play Group", "Private Training", "Workshop"]
    repeat_values = ["Daily", "Monthly", "Weekly"]
    room_names = ["Room1", "Room2", "Room3", "Room4"]

    for _ in range(10):
        partition_key = f"#LOC{random.randint(10000, 99999)}"
        sort_key = f"#APPO#{random.randint(10000, 99999)}"
        category_id = f"#SRVCS#{random.randint(10000, 99999)}"
        category_name = random.choice(service_names)

        # Client Details Array
        client_details = {
            "payLater": bool(random.getrandbits(1)),
            "clientParentId": f"#CLI#{random.randint(10000, 99999)}",
            "clientChildID": f"#PET#{random.randint(10000, 99999)}",
            "creditAvailable": random.randint(1, 10),
            "clientParentName": f"ParentName{random.randint(1, 50)}",
            "clientChildName": f"ChildName{random.randint(1, 50)}",
            "clientChildProfile": f"Profile{random.randint(1, 50)}",
            "clientChildBirthDate": f"DOB{random.randint(1, 28)}-{random.randint(1, 12)}-{random.randint(2000, 2022)}",
            "clientEmailId": f"email{random.randint(1, 100)}@example.com"
        }

        start_date = random_date(datetime(2023, 1, 1), datetime(2023, 12, 31))
        end_date = start_date + timedelta(days=random.randint(1, 30))

        writer.writerow([partition_key, sort_key, category_id, category_name, client_details, "", "", 
                         f"FRA#{random.randint(10000, 99999)}", start_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), 
                         partition_key, random.randint(1, 12), "", 
                         {
                             "freq": random.randint(1, 30),
                             "dtstart": start_date.strftime("%Y-%m-%d"),
                             "until": end_date.strftime("%Y-%m-%d")
                         },
                         random.choice(repeat_values),
                         {
                             "name": random.choice(room_names),
                             "roomLimit": random.randint(3, 10)
                         },
                         "appointment", f"#SRVCE#{random.randint(10000, 99999)}", category_name,
                         {
                             "day": random.choice(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]),
                             "startTime": "9:00AM",
                             "endTime": "6:00PM"
                         },
                         f"#USER#{random.randint(10000, 99999)}", f"TrainerName{random.randint(1, 50)}", "", ""])
