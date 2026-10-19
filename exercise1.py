# Appendix IX - Exercise 1: Engineering Test Data Organizer
# Student: Ladica | ID: TUPM-26-1844

LAST_NAME = "Ladica"
STUDENT_ID = "TUPM-26-1844"
FAVORITE_ARTIST = "ALEC BENJAMIN"

SEED_NUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
artist_vals = [ord(char) % 50 + 50 for char in FAVORITE_ARTIST if char.isalpha()]

raw_test_data = [
    (f"{LAST_NAME}_TEST_1", "PASS", artist_vals[0]),
    (f"{LAST_NAME}_TEST_2", "FAIL", artist_vals[1]),
    (f"{LAST_NAME}_TEST_3", "PASS", artist_vals[2]),
    (f"{LAST_NAME}_TEST_4", "FAIL", artist_vals[3]),
    (f"{LAST_NAME}_TEST_5", "PASS", artist_vals[4]),
    (f"{LAST_NAME}_TEST_1", "PASS", artist_vals[0]),  # Duplicate entry
    (f"{LAST_NAME}_TEST_6", "PASS", artist_vals[5]),
    (f"{LAST_NAME}_TEST_7", "FAIL", artist_vals[6])
]

print("=== 1. RAW TEST DATA ===")
for entry in raw_test_data:
    print(entry)

distinct_tests = list(set(raw_test_data))
duplicate_tests = list(set([t for t in raw_test_data if raw_test_data.count(t) > 1]))

print("\n=== 2. REJECTED DUPLICATES ===")
for dup in duplicate_tests:
    print(dup)

print("\n=== 3. DISTINCT TEST RECORDS ===")
for dist in distinct_tests:
    print(dist)

test_summary = {}
for test_id, status, score in distinct_tests:
    test_summary[test_id] = {"status": status, "score": score}

print("\n=== 4. ORGANIZED TEST SUMMARY ===")
for tid, details in test_summary.items():
    print(f"{tid}: {details}")

all_scores = [s for _, _, s in distinct_tests]
print("\n=== 5. STATISTICAL SUMMARY ===")
print(f"Total Unique Tests: {len(all_scores)}")
print(f"Highest Score: {max(all_scores)}")
print(f"Lowest Score: {min(all_scores)}")
print(f"Average Score: {sum(all_scores)/len(all_scores):.2f}")