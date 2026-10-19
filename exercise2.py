# Appendix IX - Exercise 2: Student Performance Data Analyzer
# Student: Ladica | ID: TUPM-26-1844

LAST_NAME = "Ladica"
STUDENT_ID = "TUPM-26-1844"
FAVORITE_ARTIST = "ALEC BENJAMIN"

SEED_NUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
student_ids = [f"{LAST_NAME}_{i}" for i in range(1, 6)]
artist_vals = [ord(char) % 40 + 60 for char in FAVORITE_ARTIST if char.isalpha()]

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

distinct_records = list(set(raw_performance_data))
duplicate_records = list(set([r for r in raw_performance_data if raw_performance_data.count(r) > 1]))

print("\n=== 2. DUPLICATE RECORDS REJECTED ===")
for dup in duplicate_records:
    print(dup)

print("\n=== 3. DISTINCT RECORDS ===")
for dist in distinct_records:
    print(dist)

student_profiles = {}
for student_id, subject, score in distinct_records:
    if student_id not in student_profiles:
        student_profiles[student_id] = {}
    student_profiles[student_id][subject] = score

print("\n=== 4. ORGANIZED STUDENT PROFILES ===")
for sid, profile in student_profiles.items():
    print(f"{sid}: {profile}")

all_scores = [score for _, _, score in distinct_records]
print("\n=== 5. PERFORMANCE STATISTICAL SUMMARY ===")
print(f"Total Evaluated Records: {len(all_scores)}")
print(f"Highest Score: {max(all_scores)}")
print(f"Lowest Score: {min(all_scores)}")
print(f"Class Average: {sum(all_scores) / len(all_scores):.2f}")

high_performers = [s for s in distinct_records if s[2] >= 85]
average_performers = [s for s in distinct_records if 70 <= s[2] < 85]
low_performers = [s for s in distinct_records if s[2] < 70]

print(f"\nHigh Performers (>=85): {len(high_performers)}")
print(f"Average Performers (70-84): {len(average_performers)}")
print(f"Low Performers (<70): {len(low_performers)}")

sorted_records = sorted(distinct_records, key=lambda x: (x[0], x[1]))
print("\n=== 6. ORDERED PERFORMANCE RESULTS ===")
for r in sorted_records:
    print(f"Student: {r[0]} | Subject: {r[1]} | Score: {r[2]}")