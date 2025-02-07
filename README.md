

# Jenkins Job Manager (PyQt6)  

A simple and **colorful desktop application** to manage Jenkins job details using **PyQt6**.  
Features include:  
✅ Add, edit, delete, and search Jenkins job details  
✅ Beautiful UI with styled job cards and buttons  
✅ Persistent storage using JSON  
✅ Menu bar with quick actions  

---

## **🛠 Installation**  

### **1️⃣ Install Python (if not installed)**  
Ensure you have Python **3.8+** installed.  

Check version:  
```bash
python --version

2️⃣ Install Dependencies

Clone this repository and install required packages:

git clone https://github.com/your-repo/jenkins-job-manager.git
cd jenkins-job-manager
pip install -r requirements.txt

🚀 Running the Application

python job_manager.py

🖥 Features

1️⃣ Add a New Job
	•	Enter the Job Name, Jenkins URL, and Description
	•	Click “➕ Add Job”

2️⃣ Search Jobs
	•	Use the search bar to find jobs

3️⃣ Edit or Delete Jobs
	•	Click on a job to view details
	•	Click 🗑 Delete to remove

📦 Building an Executable

For Windows (.exe)

pip install pyinstaller
pyinstaller --onefile --windowed job_manager.py

The .exe will be in the dist/ folder.

For macOS (.app)

pip install pyinstaller
pyinstaller --onefile --windowed job_manager.py

The .app file will be inside dist/.

📌 Next Steps

🚀 Future Enhancements:
✅ Dark mode toggle
✅ Drag-and-drop job reordering
✅ Cloud storage integration

📜 License

This project is open-source. Feel free to modify and improve it!

---