# Run: "mypyc rsv"
# Then run benchmark
# Remove all binaries to revert back.
# Don't check binaries into git.

from io import BytesIO, StringIO
import timeit
import json
from rsv import rsv
import csv
from faker import Faker

import random

# Initialize the data structure
other_data = [["2D"]]


# Function to generate a "Pts" row
def generate_pts_row():
    return ["Pts"] + [str(random.choice([1, -1])) for _ in range(8)]


# Function to generate a "Tris" row
def generate_tris_row():
    indices = random.sample(range(0, 4), 4)
    return ["Tris"] + [str(indices[0]), str(indices[1]), str(indices[2]), str(indices[2]), str(indices[3]),
                       str(indices[0])]


print("Generate 75,000 rows")
for _ in range(500):  # Each block of "Pts" and "Tris" counts as 2 rows
    other_data.append(generate_pts_row())
    other_data.append(generate_tris_row())

# Initialize Faker
faker = Faker()

print("Generate 100,000 rows of data")
people_data = [["FirstName", "LastName", "Age", "PlaceOfBirth"]]

for _ in range(500):
    first_name = faker.first_name()
    last_name = faker.last_name()
    age = str(random.randint(1, 100)) if random.random() > 0.1 else None  # 10% chance of no age
    place_of_birth = faker.city()

    people_data.append([first_name, last_name, age, place_of_birth])

sample_data = [
    ['Name', 'ID', 'Description', 'Data'],
    ['Romanin', '0', '', None, None]
]

more_data = [
    ["FirstName", "LastName", "Age", "PlaceOfBirth"],
    ["William", "Smith", "30", "Boston"],
    ["Olivia", "Jones", "27", "San Francisco"],
    ["Lucas", "Brown", None, "Chicago"]
]

emoji_data = [
    ["Hello", "🌎"]
]


def csv_workload():
    for data in [people_data, sample_data, other_data, more_data, emoji_data]:
        buffer = StringIO()
        writer = csv.writer(buffer)
        writer.writerows(data)
        buffer.seek(0)

        reader = csv.reader(buffer)
        rows = list(reader)

        buffer = StringIO()
        writer = csv.writer(buffer)
        writer.writerows(data)
        buffer.seek(0)

        reader = csv.reader(buffer)
        rows = list(reader)


def workload():
    for data in [people_data, sample_data, other_data, more_data, emoji_data]:
        # Change this to StringIO
        buffer = BytesIO()
        rsv.dump(data, buffer)
        buffer.seek(0)

        rows = rsv.load(buffer)

        buffer = BytesIO()
        rsv.dump(data, buffer)
        buffer.seek(0)

        rows = rsv.load_split(buffer)


def json_workload():
    for data in [people_data, sample_data, other_data, more_data, emoji_data]:
        buffer = StringIO()
        json.dump(data, buffer)
        buffer.seek(0)

        rows = json.load(buffer)

        buffer = StringIO()
        json.dump(data, buffer)
        buffer.seek(0)

        rows = json.load(buffer)


print("Starting test...")
time_json_workload = timeit.timeit(json_workload, number=1000)
print(f"json workload: {time_json_workload}")

time_workload = timeit.timeit(workload, number=1000)
print(f"workload: {time_workload}")

time_csv_workload = timeit.timeit(csv_workload, number=1000)
print(f"csv workload: {time_csv_workload}")

ratio = time_json_workload / time_workload
print(f"jason/rsv ratio: {ratio}")

# Best comparison against csv, since rsv is a csv-like format
# json workload: 5.238934499910101
# rsv workload: 5.0847148001194 # mypyc speedups
# rsv workload: 8.26404339983128  # pure python
# csv workload: 2.414228399982676

