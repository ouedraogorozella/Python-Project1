from PyQt5.QtWidgets import QMainWindow
from gui import *
import csv
import random

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.current_record = None

        self.button_name.clicked.connect(lambda: self.submit())
        self.button_name2.clicked.connect(lambda: self.save())
        self.button_name3.clicked.connect(lambda: self.clear())

        self.input_name2.textChanged.connect(self.show_score_boxes)

        self.hide_all_scores()
        self.input_name.setFocus()

    def hide_all_scores(self) -> None:
        """Hide all score labels and score boxes."""
        self.label_name4.hide()
        self.input_name3.hide()

        self.label_name5.hide()
        self.input_name4.hide()

        self.label_name6.hide()
        self.input_name5.hide()

        self.label_name7.hide()
        self.input_name6.hide()


    def show_score_boxes(self) -> None:
        """Show score boxes based on number of attempts."""
        attempts = self.input_name2.text().strip()

        self.hide_all_scores()

        if attempts == "1":
            self.label_name4.show()
            self.input_name3.show()

        elif attempts == "2":
            self.label_name4.show()
            self.input_name3.show()
            self.label_name5.show()
            self.input_name4.show()

        elif attempts == "3":
            self.label_name4.show()
            self.input_name3.show()
            self.label_name5.show()
            self.input_name4.show()
            self.label_name6.show()
            self.input_name5.show()

        elif attempts == "4":
            self.label_name4.show()
            self.input_name3.show()
            self.label_name5.show()
            self.input_name4.show()
            self.label_name6.show()
            self.input_name5.show()
            self.label_name7.show()
            self.input_name6.show()


    """Ai was used for this part"""
    def show_error(self, message: str):
        self.label_name9.setStyleSheet("color: red;")
        self.label_name9.setText(message)
    

    def submit(self) -> None:
        """Generate scores and calculate final score."""
        name = self.input_name.text().strip()
        attempts_text = self.input_name2.text().strip()

        if name == "":
            self.show_error("Enter student name")
            return

        try:
            attempts = int(attempts_text)

            if attempts < 1 or attempts > 4:
                self.show_error("Attempts must be 1 to 4")
                return

            self.show_score_boxes()

            scores = []

            for i in range(attempts):
                score = random.randint(0, 100)
                scores.append(score)

            self.input_name3.setText("")
            self.input_name4.setText("")
            self.input_name5.setText("")
            self.input_name6.setText("")

            if attempts >= 1:
                self.input_name3.setText(str(scores[0]))

            if attempts >= 2:
                self.input_name4.setText(str(scores[1]))

            if attempts >= 3:
                self.input_name5.setText(str(scores[2]))

            if attempts == 4:
                self.input_name6.setText(str(scores[3]))

            final_score = max(scores)
            self.input_name7.setText(str(final_score))

            while len(scores) < 4:
                scores.append(0)

            self.current_record = [
                name,
                scores[0],
                scores[1],
                scores[2],
                scores[3],
                final_score
            ]

            self.label_name9.setText("Scores generated")

        except ValueError:
            self.show_error("Attempts must be an integer")

    """Ai was used for this part"""
    def save(self) -> None:
        """Save the current record to a CSV file."""
        if self.current_record is None:
            self.label_name9.setText("Submit first")
            return

        try:
            with open("data.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(self.current_record)

            self.label_name9.setText("Saved")

        except OSError:
            self.show_error("Could not save file")

    def clear(self) -> None:
        """Clear the form."""
        self.input_name.setText("")
        self.input_name2.setText("")
        self.input_name3.setText("")
        self.input_name4.setText("")
        self.input_name5.setText("")
        self.input_name6.setText("")
        self.input_name7.setText("")
        self.label_name9.setText("")
        self.current_record = None
        self.input_name.setFocus()
