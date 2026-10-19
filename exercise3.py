# Appendix IX - Exercise 3: Transaction History Analyzer
# Student: Ladica | ID: TUPM-26-1844

LAST_NAME = "Ladica"
STUDENT_ID = "TUPM-26-1844"
FAVORITE_ARTIST = "ALEC BENJAMIN"

SEED_NUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
customer_ids = [f"{LAST_NAME}_C{i}" for i in range(1, 6)]
categories = ["ELECTRONICS", "BOOKS", "CLOTHING", "HOME", "BEAUTY"]
artist_vals = [ord(char) * 2 + SEED_NUM for char in FAVORITE_ARTIST if char.isalpha()]

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

distinct_transactions = list(set(raw_transactions))
duplicate_transactions = list(set([t for t in raw_transactions if raw_transactions.count(t) > 1]))

print("\n=== 2. REJECTED DUPLICATE TRANSACTIONS ===")
for dup in duplicate_transactions:
    print(dup)

print("\n=== 3. DISTINCT TRANSACTIONS ===")
for dist in distinct_transactions:
    print(dist)

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

all_amounts = [amount for _, _, amount in distinct_transactions]
print("\n=== 5. TRANSACTION FINANCIAL SUMMARY ===")
print(f"Total Transactions Processed: {len(all_amounts)}")
print(f"Total Revenue: ${sum(all_amounts):.2f}")
print(f"Minimum Transaction: ${min(all_amounts):.2f}")
print(f"Maximum Transaction: ${max(all_amounts):.2f}")
print(f"Average Transaction: ${sum(all_amounts) / len(all_amounts):.2f}")

sorted_transactions = sorted(distinct_transactions, key=lambda x: (x[0], x[1]))
print("\n=== 6. ORDERED TRANSACTION LOGS ===")
for st in sorted_transactions:
    print(f"Customer: {st[0]} | Category: {st[1]} | Amount: ${st[2]:.2f}")