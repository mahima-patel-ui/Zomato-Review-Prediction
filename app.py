import sys
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QTextEdit
)

# ✅ Load your CSV (with exact column names as in your file)
data = pd.read_csv("restaurants.csv")  # Make sure it's in same folder

class ZomatoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zomato Finder")
        self.setGeometry(100, 100, 500, 400)

        layout = QVBoxLayout()

        self.label = QLabel("🔍 Enter Restaurant or Cuisine:")
        self.input_box = QLineEdit()
        self.button = QPushButton("Search")
        self.output = QTextEdit()
        self.output.setReadOnly(True)

        layout.addWidget(self.label)
        layout.addWidget(self.input_box)
        layout.addWidget(self.button)
        layout.addWidget(self.output)

        self.setLayout(layout)
        self.button.clicked.connect(self.search)

    def search(self):
        query = self.input_box.text().lower()
        results = ""

        for index, row in data.iterrows():
            name = str(row["Name"]).lower()
            cuisine = str(row["Cuisines"]).lower()

            if query in name or query in cuisine:
                results += (
                    f"🍽️ {row['Name']}\n"
                    f"🌐 Link: {row['Links']}\n"
                    f"💰 Cost: {row['Cost']}\n"
                    f"🍱 Cuisine: {row['Cuisines']}\n"
                    f"🕒 Timings: {row['Timings']}\n\n"
                )

        if results == "":
            results = "❌ No matching restaurants found."

        self.output.setText(results)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ZomatoApp()
    window.show()
    sys.exit(app.exec_())
