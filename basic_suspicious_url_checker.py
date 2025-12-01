url = input("Enter URL or filename: ").lower()

bad_ext = [".exe", ".bat", ".scr", ".js"]
bad_words = ["free", "login", "verify", "update"]

if any(url.endswith(e) for e in bad_ext): print("⚠️ Suspicious file extension!")
elif any(w in url for w in bad_words): print("⚠️ Possible phishing pattern!")
else: print("✔️ Looks safe (no basic red flags).")
