import json


class PasswordManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.passwords = self.load_passwords()

    def load_passwords(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_passwords(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.passwords, file, indent=4)

    def add_password(self, website, username, password):
        if website not in self.passwords:
            self.passwords[website] = {}
        self.passwords[website][username] = password
        self.save_passwords()

    def get_password(self, website, username):
        if website in self.passwords and username in self.passwords[website]:
            return self.passwords[website][username]
        return None

    def remove_password(self, website, username):
        if website in self.passwords and username in self.passwords[website]:
            del self.passwords[website][username]
            if not self.passwords[website]:
                del self.passwords[website]
            self.save_passwords()

    def list_websites(self):
        return list(self.passwords.keys())

    def list_usernames(self, website):
        if website in self.passwords:
            return list(self.passwords[website].keys())
        return []


pm = PasswordManager("./passwords.json")

pm.add_password("example.com", "user1", "password1")
pm.add_password("example.com", "user2", "password2")
pm.add_password("google.com", "user3", "password3")

print(pm.get_password("example.com", "user1"))  # Output: password1

pm.remove_password("example.com", "user2")

print(pm.list_websites())  # Output: ['example.com', 'google.com']

print(pm.list_usernames("example.com"))  # Output: ['user1']
