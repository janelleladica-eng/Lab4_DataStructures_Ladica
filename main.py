# PHASE 2: FUNCTIONAL ENCAPSULATION & SCOPE
# Task 4: Identity-Based Computational Seed

# Student Identity
LAST_NAME = "Ladica"
STUDENT_ID = "TUPM-26-1844"

# Derive computational parameters
seed_digit = int(STUDENT_ID[-1])
id_checksum = sum(int(d) for d in STUDENT_ID if d.isdigit())
vector_dim = len(LAST_NAME)

# Encapsulate state into a Dictionary (Associative Map)
sys_config = {
    "operator": LAST_NAME,
    "auth_id": STUDENT_ID,
    "base_seed": seed_digit,
    "checksum": id_checksum,
    "vector_dim": vector_dim,
    "status": "INITIALIZED"
}

# Display system state
print("=== SYSTEM CONFIGURATION ===")
for key, value in sys_config.items():
    print(f"{key.upper()}: {value}")


# PHASE 3: MUTABLE SEQUENCES (LISTS)
# Task 5: Dynamic List Operations

# Initialize a list using the system configuration
base_val = sys_config["base_seed"]
number_sequence = [base_val, base_val + 15, sys_config["checksum"]]

print(f"\nInitial Sequence: {number_sequence}")

# Append a new value to the sequence
number_sequence.append(base_val + 20)
print(f"After Append: {number_sequence}")
# Task 6: Sequential Operations
new_numbers = [base_val + 5, sys_config["vector_dim"], base_val]
number_sequence.extend(new_numbers)
print(f"\nAfter Extend: {number_sequence}")

base_count = number_sequence.count(base_val)
print(f"Occurrences of {base_val}: {base_count}")

number_sequence.sort()
print(f"Sorted Sequence: {number_sequence}")


# PHASE 4: IMMUTABLE RECORDS & ASSOCIATIVE MAPPING
# Task 7: Immutable Sequences (Tuples)
fixed_coordinates = (sys_config["vector_dim"], sys_config["base_seed"], 0)
print(f"\nFixed Coordinates: {fixed_coordinates}")

x_val, y_val, z_val = fixed_coordinates
print(f"Unpacked Values -> X: {x_val}, Y: {y_val}, Z: {z_val}")

print("\nAttempting modification...")
try:
    fixed_coordinates[0] = 99
except TypeError as error_msg:
    print(f"Modification Error: {error_msg}")


# Task 8: Key-Value Mappings (Dictionaries)
data_payload = {
    "identifier": sys_config["auth_id"],
    "dimension": sys_config["vector_dim"],
    "status": "active"
}

print("\n--- Payload Data ---")
for key, value in data_payload.items():
    print(f"{key.capitalize()}: {value}")

data_payload["efficiency_rating"] = 98.5
print(f"\nUpdated Payload: {data_payload}")
# PHASE 5: UNIQUE COLLECTIONS (SETS)
# Task 9: Data De-duplication

# Initialize a list with deliberate duplicate values
raw_data = [base_val, base_val + 5, base_val, sys_config["vector_dim"], base_val + 5]
print(f"\nRaw List (with duplicates): {raw_data}")

# Convert the list to a Set to remove duplicates
unique_data = set(raw_data)
print(f"Unique Set: {unique_data}")


# Task 10: Mathematical Set Operations

# Define a secondary reference set for comparison
reference_set = {base_val, base_val + 10, base_val + 20}
print(f"\nReference Set: {reference_set}")

# Perform mathematical intersections and unions
common_elements = unique_data.intersection(reference_set)
combined_elements = unique_data.union(reference_set)

print(f"Intersection (Common): {common_elements}")
print(f"Union (Combined): {combined_elements}")
# PHASE 6: ADVANCED ITERATIONS
import array

# Task 11: Homogeneous Arrays
number_array = array.array('i', [sys_config["base_seed"], sys_config["vector_dim"], 100])
print(f"\nInteger Array: {number_array}")

print("\nAttempting to append a string...")
try:
    number_array.append("invalid")
except TypeError as error_msg:
    print(f"Type Error: {error_msg}")


# Task 12: List Comprehensions
base_val = sys_config["base_seed"]
generated_list = [x * base_val for x in range(1, 6)]
print(f"\nGenerated Comprehension: {generated_list}")

filtered_list = [x for x in generated_list if x > 15]
print(f"Filtered Comprehension (Values > 15): {filtered_list}")


# PHASE 7: SPECIALIZED COLLECTIONS
from collections import deque, defaultdict

# Task 13: Double-Ended Queues (Deque)
data_queue = deque([sys_config["base_seed"], sys_config["vector_dim"]])
print(f"\nInitial Deque: {data_queue}")

data_queue.append(100)
data_queue.appendleft(200)
print(f"After Appends: {data_queue}")

data_queue.popleft()
print(f"Final Deque (After Popleft): {data_queue}")


# Task 14: Fault-Tolerant Key Mappings (Defaultdict)
default_data = defaultdict(int)
default_data['active_key'] = sys_config["vector_dim"]

print(f"\nExisting Key Value: {default_data['active_key']}")
print(f"Missing Key Value (Auto-generated): {default_data['unknown_key_1']}")
# Appendix IX - Exercise 2: Student Performance Data Analyzer
# Student: Ladica | ID: TUPM-26-1844

# Student parameters
LAST_NAME = "Ladica"
STUDENT_ID = "TUPM-26-1844"
FAVORITE_ARTIST = "ALEC BENJAMIN"

# Calculate SEED_NUM from student ID digit sum
SEED_NUM = sum(int(d) for d in STUDENT_ID if d.isdigit())

# 1. Generate 5 student IDs using LAST_NAME with digits 1..5
student_ids = [f"{LAST_NAME}_{i}" for i in range(1, 6)]

# 2. Derive raw scores using character codes of FAVORITE_ARTIST
artist_vals = [ord(char) % 40 + 60 for char in FAVORITE_ARTIST if char.isalpha()]

# 3. Create raw performance dataset (including 1 duplicate and multi-subject records)
raw_performance_data = [
    (student_ids[0], "MATH", artist_vals[0]),
    (student_ids[1], "SCIENCE", artist_vals[1]),
    (student_ids[2], "ENGLISH", artist_vals[2]),
    (student_ids[3], "HISTORY", artist_vals[3]),
    (student_ids[4], "PROGRAMMING", artist_vals[4]),
    (student_ids[0], "MATH", artist_vals[0]),       # Repeated record
    (student_ids[0], "SCIENCE", artist_vals[5]),    # Multiple subject 1
    (student_ids[1], "ENGLISH", artist_vals[6])     # Multiple subject 2
]

print("=== 1. RAW PERFORMANCE DATA ===")
for record in raw_performance_data:
    print(record)

# 4. Filter and De-duplicate Data using Sets
distinct_records = list(set(raw_performance_data))
duplicate_records = list(set([r for r in raw_performance_data if raw_performance_data.count(r) > 1]))

print("\n=== 2. DUPLICATE RECORDS REJECTED ===")
for dup in duplicate_records:
    print(dup)

print("\n=== 3. DISTINCT RECORDS ===")
for dist in distinct_records:
    print(dist)

# 5. Organize into Student Profiles via Dictionaries
student_profiles = {}
for student_id, subject, score in distinct_records:
    if student_id not in student_profiles:
        student_profiles[student_id] = {}
    student_profiles[student_id][subject] = score

print("\n=== 4. ORGANIZED STUDENT PROFILES ===")
for sid, profile in student_profiles.items():
    print(f"{sid}: {profile}")

# 6. Statistical Analysis
all_scores = [score for _, _, score in distinct_records]
print("\n=== 5. PERFORMANCE STATISTICAL SUMMARY ===")
print(f"Total Evaluated Records: {len(all_scores)}")
print(f"Highest Score: {max(all_scores)}")
print(f"Lowest Score: {min(all_scores)}")
print(f"Class Average: {sum(all_scores) / len(all_scores):.2f}")

# Categorize performance into High/Average/Low
high_performers = [s for s in distinct_records if s[2] >= 85]
average_performers = [s for s in distinct_records if 70 <= s[2] < 85]
low_performers = [s for s in distinct_records if s[2] < 70]

print(f"\nHigh Performers (>=85): {len(high_performers)}")
print(f"Average Performers (70-84): {len(average_performers)}")
print(f"Low Performers (<70): {len(low_performers)}")

# 7. Ordered Results
sorted_records = sorted(distinct_records, key=lambda x: (x[0], x[1]))
print("\n=== 6. ORDERED PERFORMANCE RESULTS ===")
for r in sorted_records:
    print(f"Student: {r[0]} | Subject: {r[1]} | Score: {r[2]}")
    # Appendix IX - Exercise 3: Transaction History Analyzer
# Student: Ladica | ID: TUPM-26-1844

LAST_NAME = "Ladica"
STUDENT_ID = "TUPM-26-1844"
FAVORITE_ARTIST = "ALEC BENJAMIN"

# Calculate SEED_NUM from student ID digit sum
SEED_NUM = sum(int(d) for d in STUDENT_ID if d.isdigit())

# 1. Generate 5 customer IDs using LAST_NAME with C1..C5
customer_ids = [f"{LAST_NAME}_C{i}" for i in range(1, 6)]

# 2. Common product categories
categories = ["ELECTRONICS", "BOOKS", "CLOTHING", "HOME", "BEAUTY"]

# 3. Derive transaction values using character codes of FAVORITE_ARTIST
artist_vals = [ord(char) * 2 + SEED_NUM for char in FAVORITE_ARTIST if char.isalpha()]

# 4. Create raw transaction history (including 1 repeated record & multi-purchases)
raw_transactions = [
    (customer_ids[0], categories[0], artist_vals[0]),
    (customer_ids[1], categories[1], artist_vals[1]),
    (customer_ids[2], categories[2], artist_vals[2]),
    (customer_ids[3], categories[3], artist_vals[3]),
    (customer_ids[4], categories[4], artist_vals[4]),
    (customer_ids[0], categories[0], artist_vals[0]),   # Repeated transaction
    (customer_ids[0], categories[1], artist_vals[5]),   # Multiple purchase 1
    (customer_ids[1], categories[0], artist_vals[6])    # Multiple purchase 2
]

print("=== 1. RAW TRANSACTION HISTORY ===")
for t in raw_transactions:
    print(t)

# 5. Filter and De-duplicate Data using Sets
distinct_transactions = list(set(raw_transactions))
duplicate_transactions = list(set([t for t in raw_transactions if raw_transactions.count(t) > 1]))

print("\n=== 2. REJECTED DUPLICATE TRANSACTIONS ===")
for dup in duplicate_transactions:
    print(dup)

print("\n=== 3. DISTINCT TRANSACTIONS ===")
for dist in distinct_transactions:
    print(dist)

# 6. Organize Transactions by Customer Profiles via Dictionaries
customer_profiles = {}
for cid, cat, amount in distinct_transactions:
    if cid not in customer_profiles:
        customer_profiles[cid] = {}
    if cat not in customer_profiles[cid]:
        customer_profiles[cid][cat] = []
    customer_profiles[cid][cat].append(amount)

print("\n=== 4. ORGANIZED CUSTOMER PROFILES ===")
for cid, profile in customer_profiles.items():
    print(f"{cid}: {profile}")

# 7. Financial & Category Summaries
all_amounts = [amount for _, _, amount in distinct_transactions]
print("\n=== 5. TRANSACTION FINANCIAL SUMMARY ===")
print(f"Total Transactions Processed: {len(all_amounts)}")
print(f"Total Revenue: ${sum(all_amounts):.2f}")
print(f"Minimum Transaction: ${min(all_amounts):.2f}")
print(f"Maximum Transaction: ${max(all_amounts):.2f}")
print(f"Average Transaction: ${sum(all_amounts) / len(all_amounts):.2f}")

# 8. Ordered Transaction Logs
sorted_transactions = sorted(distinct_transactions, key=lambda x: (x[0], x[1]))
print("\n=== 6. ORDERED TRANSACTION LOGS ===")
for st in sorted_transactions:
    print(f"Customer: {st[0]} | Category: {st[1]} | Amount: ${st[2]:.2f}")