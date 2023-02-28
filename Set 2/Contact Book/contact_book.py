from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, QWidget
import sys
import sqlite3


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class ContactBook:
    def __init__(self):
        self.conn = sqlite3.connect('./contacts.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts(
                name TEXT,
                email TEXT,
                phone TEXT
            )
        ''')
        self.conn.commit()

    def add_contact(self, contact):
        self.cursor.execute('INSERT INTO contacts VALUES (?, ?, ?)',
                            (contact.name, contact.email, contact.phone))
        self.conn.commit()

    def get_contacts(self):
        self.cursor.execute('SELECT * FROM contacts')
        rows = self.cursor.fetchall()
        contacts = []
        for row in rows:
            contact = Contact(row[0], row[1], row[2])
            contacts.append(contact)
        return contacts


class AddContactForm(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Contact")
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        self.phone_label = QLabel("Phone:")
        self.phone_input = QLineEdit()
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_contact)

        form_layout = QVBoxLayout()
        form_layout.addWidget(self.name_label)
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.email_label)
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(self.phone_label)
        form_layout.addWidget(self.phone_input)
        form_layout.addWidget(self.save_button)

        self.setLayout(form_layout)

    def save_contact(self):
        name = self.name_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()
        contact = Contact(name, email, phone)
        self.contact_book = ContactBook()
        self.contact_book.add_contact(contact)
        self.accept()


class ViewContactsForm(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("View Contacts")
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Name', 'Email', 'Phone'])
        self.load_contacts()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table)
        self.setLayout(main_layout)

    def load_contacts(self):
        self.contact_book = ContactBook()
        contacts = self.contact_book.get_contacts()
        self.table.setRowCount(len(contacts))
        for i, contact in enumerate(contacts):
            self.table.setItem(i, 0, QTableWidgetItem(contact.name))
            self.table.setItem(i, 1, QTableWidgetItem(contact.email))
            self.table.setItem(i, 2, QTableWidgetItem(contact.phone))


class ContactBookWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contact Book")
        self.setGeometry(100, 100, 500, 500)

        # Create the central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Create the "Add Contact" button and connect it to the slot method
        add_button = QPushButton("Add Contact")
        main_layout.addWidget(add_button)
        add_button.clicked


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    contact_book = ContactBook()
    contact_book.show()
    sys.exit(app.exec_())
