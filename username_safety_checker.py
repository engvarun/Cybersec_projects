username = input("Enter username: ").lower()

weak_names = ["admin", "user", "test"]

if len(username) < 5:
    print("⚠️ Username too short!")
elif username in weak_names:
    print("⚠️ Common or risky username!")
elif not username.isalnum():
    print("⚠️ Username contains special characters!")
elif username.isdigit():
    print("⚠️ Username cannot be numbers only!")
else:
    print("✔️ Username looks acceptable.")
