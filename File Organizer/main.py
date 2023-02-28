import os
import shutil
import time


class FileOrganizer:
    def __init__(self, directory):
        self.directory = directory

    # method to organize files by type
    def organize_by_type(self):
        for filename in os.listdir(self.directory):
            if os.path.isfile(os.path.join(self.directory, filename)):
                file_extension = os.path.splitext(filename)[1]
                folder_name = file_extension.strip(".")
                folder_path = os.path.join(self.directory, folder_name)
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)
                shutil.move(
                    os.path.join(self.directory, filename),
                    os.path.join(folder_path, filename)
                )

    # method to organize files by size
    def organize_by_size(self):
        files = []
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if os.path.isfile(file_path):
                size = os.stat(file_path).st_size
                files.append((size, file_path))
        files.sort(key=lambda x: x[1])

        for filename, _ in files:
            file_path = os.path.join(self.directory, filename)
            file_size = os.stat(file_path).st_size
            for i in range(1, 101):
                folder_name = f"{i*10}MB"
                folder_path = os.path.join(self.directory, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                if file_size <= i * 10 * 1024 * 1024:
                    shutil.move(
                        file_path,
                        os.path.join(folder_path, filename)
                    )
                    break
    # method to organize files by date

    def organize_by_date(self):
        files = []
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if os.path.isfile(file_path):
                modified_date = os.path.getmtime(file_path)
                files.append((filename, modified_date))
        files.sort(key=lambda x: x[1])
        for filename, _ in files:
            file_path = os.path.join(self.directory, filename)
            modified_date = os.path.getmtime(file_path)
            year = str(time.gmtime(modified_date).tm_year)
            month = str(time.gmtime(modified_date).tm_mon).zfill(2)
            folder_name = f'{year}-{month}'
            folder_path = os.path.join(self.directory, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(
                file_path,
                os.path.join(folder_path, filename)
            )


organizer = FileOrganizer("E:\Complete-Python-Projects\Set 1")
organizer.organize_by_size()
