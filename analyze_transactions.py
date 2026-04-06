#!/usr/bin/env python3
"""Analyze TransactionTracker.numbers — items per category and spend per person."""

from collections import defaultdict
from numbers_parser import Document

FILE = "TransactionTracker.numbers"

doc = Document(FILE)
table = doc.sheets[0].tables[0]

category_counts = defaultdict(int)
person_spend = defaultdict(float)

for row in range(1, table.num_rows):
    person = table.cell(row, 1).value
    category = table.cell(row, 2).value
    price = table.cell(row, 3).value

    if person is None:
        continue

    category_counts[category] += 1
    person_spend[person] += price

print(f"=== Number of different customers: {len(person_spend)} ===")
print()
print("=== Items bought per category ===")
for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
    print(f"  {cat:10s}  {count} items")
print(f"  {'TOTAL':10s}  {sum(category_counts.values())} items")

print()
print("=== Money paid per person ===")
for person, total in sorted(person_spend.items(), key=lambda x: -x[1]):
    print(f"  {person:15s}  {total:.0f} kr")
print(f"  {'TOTAL':15s}  {sum(person_spend.values()):.0f} kr")
