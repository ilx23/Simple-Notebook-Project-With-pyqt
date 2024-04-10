from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, \
    QMessageBox, QListWidget, QDialog, QLineEdit
import sys


class NoteDialog(QDialog):
    """
    Dialog window to add or edit note titles.
    """
    def __init__(self, parent=None):
        super(NoteDialog, self).__init__(parent)
        self.setWindowTitle('Add Title')  # Setting the window title
        self.note_line_edit = QLineEdit()  # Line edit widget for entering note titles
        self.ok_button = QPushButton('OK')  # Button to confirm the action
        self.cancel_button = QPushButton('Cancel')  # Button to cancel the action

        layout = QVBoxLayout()  # Vertical layout for the dialog window
        layout.addWidget(self.note_line_edit)

        button_layout = QHBoxLayout()  # Horizontal layout for buttons
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        self.ok_button.clicked.connect(self.accept)  # Connecting OK button click event to accept action
        self.cancel_button.clicked.connect(self.reject)  # Connecting Cancel button click event to reject action

        self.setLayout(layout)


class NoteText(QDialog):
    """
    Dialog window to add or edit note content.
    """
    def __init__(self, parent=None):
        super(NoteText, self).__init__(parent)
        self.setWindowTitle('Add Your Note')  # Setting the window title
        self.note_line = QTextEdit()  # Text edit widget for entering note content
        self.ok_button = QPushButton('OK')  # Button to confirm the action
        self.cancel_button = QPushButton('Cancel')  # Button to cancel the action

        layout = QVBoxLayout()  # Vertical layout for the dialog window
        layout.addWidget(self.note_line)

        button_layout = QHBoxLayout()  # Horizontal layout for buttons
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        self.ok_button.clicked.connect(self.accept)  # Connecting OK button click event to accept action
        self.cancel_button.clicked.connect(self.reject)  # Connecting Cancel button click event to reject action

        self.setLayout(layout)


class NotebookApp(QWidget):
    """
    Main application window for the Notebook Application.
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Notebook Application")  # Setting the window title
        self.notes_list = QListWidget()  # List widget to display note titles
        self.text_edit = QTextEdit()  # Text edit widget to display note content
        self.add_button = QPushButton('Add')  # Button to add a new note
        self.edit_button = QPushButton('Edit')  # Button to edit an existing note
        self.delete_button = QPushButton('Delete')  # Button to delete a note

        layout = QVBoxLayout()  # Vertical layout for the main window
        button_layout = QHBoxLayout()  # Horizontal layout for buttons
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.delete_button)
        layout.addLayout(button_layout)
        layout.addWidget(self.notes_list)  # Adding the notes list widget
        layout.addWidget(self.text_edit)  # Adding the text edit widget

        self.add_button.clicked.connect(self.add_note)  # Connecting add button click event to add_note function
        self.edit_button.clicked.connect(self.edit_note)  # Connecting edit button click event to edit_note function
        self.delete_button.clicked.connect(self.delete_note)  # Connecting delete button click event to delete_note function
        self.notes_list.itemClicked.connect(self.display_note)  # Connecting list item click event to display_note function

        self.setLayout(layout)

    def add_note(self):
        """
        Function to add a new note.
        """
        dialog = NoteDialog(self)  # Creating an instance of NoteDialog
        if dialog.exec_():
            note_title = dialog.note_line_edit.text()
            if note_title:
                self.notes_list.addItem(note_title)  # Adding the note title to the list
                self.text_edit.clear()  # Clearing the text edit widget

    def edit_note(self):
        """
        Function to edit an existing note.
        """
        if self.notes_list.currentItem() is None:
            QMessageBox.warning(self, "Error", "You haven't selected any note")
            return
        selected_item = self.notes_list.currentItem()
        if selected_item:
            dialog = NoteDialog(self)  # Creating an instance of NoteDialog
            dialog.note_line_edit.setText(selected_item.text())  # Setting the text of line edit with selected note title
            if dialog.exec_():
                edited_text = dialog.note_line_edit.text()
                if edited_text:
                    selected_item.setText(edited_text)  # Updating the note title in the list
                    self.text_edit.clear()  # Clearing the text edit widget

    def delete_note(self):
        """
        Function to delete a note.
        """
        selected_item = self.notes_list.currentItem()
        if selected_item:
            confirm = QMessageBox.question(self, "Delete Note", "Are you sure you want to Delete this Note?",
                                           QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                self.notes_list.takeItem(self.notes_list.row(selected_item))  # Removing the selected note from the list
                self.text_edit.clear()  # Clearing the text edit widget
        else:
            QMessageBox.warning(self, "Error", "You haven't selected any Note")

    def display_note(self, item):
        """
        Function to display the content of the selected note.
        """
        self.text_edit.setPlainText(item.text())  # Setting the text edit widget with the content of the selected note


def main():
    app = QApplication(sys.argv)
    notebook = NotebookApp()
    notebook.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
