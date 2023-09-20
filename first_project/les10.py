# guests = ["Alice", "Bob", "Charlie", "Eve", "Trudy", "Mallory", "Oliver", "Emily"]
#
# guests_with_e = [name for name in guests if "e" in name.lower()]
# print(guests_with_e)

guests = {
    "John Smith",
    "Jane Smith",
    "Alex Johnson",
    "Alice Johnson",
    "Jane Doe",
    "John Doe",
    "Jenny Doe",
}

party_guests = {
"Alice": 1,
"Bob": 2,
"Charlie": 3,
"David": 1,
"Eva": 2,
"Fiona": 1
}

# last_names = {guest.split()[1] for guest in guests}
# duplicate_last_names = [last_name for last_name in last_names
#                         if sum(1 for guest in guests if guest.endswith(last_name)) > 1]
# print(duplicate_last_names)

inverted_guests = {}
for guest, number in party_guests.items():
    if number not in inverted_guests:
        inverted_guests[number] = [guest]
    else:
        inverted_guests[number].append(guest)

print(inverted_guests)
