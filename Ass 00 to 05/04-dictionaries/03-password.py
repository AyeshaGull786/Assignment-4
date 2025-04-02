# 03_powerful_passwords

# You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want
# to make a program that can match which password belongs to which website without storing the actual password!

# This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier.
# This is done using a hash function. Luckily, there are several resources that can help us with this.

import hashlib  # Import hashlib for hashing

def hash_password(password: str) -> str:
    """Hashes a given password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()

def login(email: str, password_to_check: str, stored_logins: dict) -> bool:
    """
    Check if the entered password (after hashing) matches the stored hash.

    Parameters:
    - email: User's email.
    - password_to_check: Entered password to verify.
    - stored_logins: Dictionary containing stored hashed passwords.

    Returns:
    - True if password matches, False otherwise.
    """
    if email in stored_logins:  # Check if email exists
        return stored_logins[email] == hash_password(password_to_check)  # Compare hashes
    return False  # Email not found

# ✅ Example Usage:
stored_logins = {
    "user@example.com": hash_password("securepassword123"),  # Store hashed password
    "admin@example.com": hash_password("adminpass")
}

# 🔍 Simulating login attempts
print(login("user@example.com", "securepassword123", stored_logins))  # ✅ True (Correct password)
print(login("user@example.com", "wrongpassword", stored_logins))      # ❌ False (Incorrect password)
print(login("unknown@example.com", "randompass", stored_logins))      # ❌ False (Email not found)
