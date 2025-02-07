import sys
import json
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, 
    QListWidget, QListWidgetItem, QMessageBox, QDialog, QLabel, QMainWindow, QMenuBar, QMenu
)
from PyQt6.QtGui import QPalette, QColor

DATA_FILE = "jobs.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

class JobManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.jobs = load_data()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Jenkins Job Manager")
        self.setGeometry(100, 100, 600, 500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()

        self.job_name = QLineEdit(self)
        self.job_name.setPlaceholderText("Job Name")
        
        self.job_url = QLineEdit(self)
        self.job_url.setPlaceholderText("Jenkins Job URL")

        self.job_desc = QTextEdit(self)
        self.job_desc.setPlaceholderText("Job Description")

        self.add_button = QPushButton("➕ Add Job", self)
        self.add_button.clicked.connect(self.add_job)

        self.search_box = QLineEdit(self)
        self.search_box.setPlaceholderText("🔍 Search Jobs")
        self.search_box.textChanged.connect(self.filter_jobs)

        self.job_list = QListWidget(self)
        self.job_list.itemClicked.connect(self.view_job)

        layout.addWidget(self.job_name)
        layout.addWidget(self.job_url)
        layout.addWidget(self.job_desc)
        layout.addWidget(self.add_button)
        layout.addWidget(self.search_box)
        layout.addWidget(self.job_list)

        self.central_widget.setLayout(layout)
        self.load_jobs()
        self.apply_styles()

        # Add menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction("Exit", self.close)

        jobs_menu = menu_bar.addMenu("Jobs")
        jobs_menu.addAction("Add New Job", self.add_job)
        jobs_menu.addAction("Refresh Jobs", self.load_jobs)

    def apply_styles(self):
        """ Apply colorful styling """
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f4f4f4;
            }
            QPushButton {
                background-color: #008CBA;
                color: white;
                font-size: 14px;
                padding: 8px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0073A8;
            }
            QLineEdit, QTextEdit {
                background-color: white;
                border: 1px solid #ccc;
                padding: 5px;
                border-radius: 4px;
            }
            QListWidget {
                background-color: #eaf2f8;
                border: none;
                font-size: 14px;
            }
            QListWidgetItem {
                padding: 10px;
            }
            QMenuBar {
                background-color: #008CBA;
                color: white;
            }
            QMenuBar::item {
                background-color: #008CBA;
                color: white;
                padding: 5px 10px;
            }
            QMenuBar::item:selected {
                background-color: #0073A8;
            }
        """)

    def add_job(self):
        name = self.job_name.text().strip()
        url = self.job_url.text().strip()
        desc = self.job_desc.toPlainText().strip()

        if not name or not url:
            QMessageBox.warning(self, "Input Error", "Job Name and URL are required!")
            return

        self.jobs[name] = {"url": url, "desc": desc}
        save_data(self.jobs)

        self.job_name.clear()
        self.job_url.clear()
        self.job_desc.clear()
        self.load_jobs()

    def load_jobs(self):
        self.job_list.clear()
        for job_name in self.jobs.keys():
            item = QListWidgetItem(job_name)
            item.setBackground(QColor("#D6EAF8"))
            self.job_list.addItem(item)

    def filter_jobs(self):
        query = self.search_box.text().lower()
        self.job_list.clear()
        for job_name in self.jobs.keys():
            if query in job_name.lower():
                item = QListWidgetItem(job_name)
                item.setBackground(QColor("#AED6F1"))
                self.job_list.addItem(item)

    def view_job(self, item):
        job_name = item.text()
        job = self.jobs[job_name]

        msg = QMessageBox(self)
        msg.setWindowTitle(job_name)
        msg.setText(f"**URL:** {job['url']}\n\n**Description:** {job['desc']}")
        delete_button = msg.addButton("🗑 Delete", QMessageBox.ButtonRole.RejectRole)
        msg.addButton("Close", QMessageBox.ButtonRole.NoRole)

        msg.exec()

        if msg.clickedButton() == delete_button:
            del self.jobs[job_name]
            save_data(self.jobs)
            self.load_jobs()

# Run Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JobManager()
    window.show()
    sys.exit(app.exec())
