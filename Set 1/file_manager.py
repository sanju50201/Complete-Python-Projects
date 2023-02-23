class FileManager:
    def __init__(self):
        self.files = {}

    def create_file(self, filename, contents):
        self.files[filename] = contents
        print(f"File '{filename}' created successfully.")

    def read_file(self, filename):
        if filename in self.files:
            print(f"Contents of '{filename}':")
            print(self.files[filename])
        else:
            print(f"File '{filename}' does not exist.")

    def delete_file(self, filename):
        if filename in self.files:
            del self.files[filename]
            print(f"File '{filename}' deleted successfully.")
        else:
            print(f"File '{filename}' does not exist.")

    def search_file(self, keyword):
        results = []
        for filename, contents in self.files.items():
            if keyword in contents:
                results.append(filename)
        if results:
            print(f"Files containing the keyword '{keyword}':")
            for filename in results:
                print(filename)
        else:
            print(f"No files were found containing the keyword '{keyword}'.")

    def show_files(self):
        if self.files:
            print("List of files:")
            for filename in self.files:
                print(filename)
        else:
            print("No files found.")


manager = FileManager()

while True:
    print("1. Create file")
    print("2. Read file")
    print("3. Delete file")
    print("4. Search file")
    print("5. Show all files")
    print("6. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        filename = input("Enter filename: ")
        contents = input("Enter file contents: ")
        manager.create_file(filename, contents)
    elif choice == 2:
        filename = input("Enter filename: ")
        manager.read_file(filename)
    elif choice == 3:
        filename = input("Enter filename: ")
        manager.delete_file(filename)
    elif choice == 4:
        keyword = input("Enter keyword to search: ")
        manager.search_file(keyword)
    elif choice == 5:
        manager.show_files()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Try again.")
