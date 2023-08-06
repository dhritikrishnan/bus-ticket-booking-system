places = {"Chennai": 100, "Hyderabad": 75, "Pondicherry": 50}

with open("ticket_info.txt", "w") as f:
    for place, tickets in places.items():
        f.write(f"{place},{tickets}\n")

with open("ticket_info.txt", "r") as f:
    for line in f:
        place, tickets = line.strip().split(",")
        tickets = int(tickets)
        print(f"{place}: {tickets} tickets available")
