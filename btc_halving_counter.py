from datetime import datetime

# Η ημερομηνία του επόμενου Bitcoin halving (προβλεπόμενη)
next_halving_date = datetime(2024, 4, 20)  # μπορείς να ενημερώσεις αυτή την ημερομηνία αν χρειαστεί

# Σημερινή ημερομηνία
today = datetime.now()

# Υπολογισμός των ημερών που απομένουν
days_remaining = (next_halving_date - today).days

print(f"Οι ημέρες που απομένουν μέχρι το επόμενο Bitcoin halving είναι: {days_remaining}")
