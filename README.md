# 📌 TextUtils - A Django-Based Text Processing App

## 📖 Overview
TextUtils is a Django-based web application that allows users to analyze and modify text. It provides functionalities like:
- Removing punctuation
- Converting text to uppercase
- Removing new lines
- Removing extra spaces

## 🚀 Features
✅ Enter any text into the form
✅ Select operations (Remove Punctuation, UPPERCASE, etc.)
✅ Submit and get the processed text as output
✅ User-friendly UI with Bootstrap
✅ Secure with CSRF protection

---

## 🛠️ Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/textutils.git
cd textutils
```

### **2️⃣ Create & Activate Virtual Environment**
```bash
python -m venv venv
# Activate Virtual Environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5️⃣ Start Django Server**
```bash
python manage.py runserver
```
Then open your browser and go to:
```
http://127.0.0.1:8000/
```

---

## 📂 Project Structure
```
textutils/
│── textutils/  # Django project settings folder
│   ├── settings.py  # Project settings
│   ├── urls.py  # URL routing
│   ├── wsgi.py  # WSGI for deployment
│── myapp/  # Django app folder
│   ├── templates/  # HTML files
│   │   ├── index.html  # Homepage with text form
│   │   ├── analyze.html  # Results page
│   ├── views.py  # Backend logic
│   ├── urls.py  # App-specific URLs
│   ├── models.py  # Database models (if any)
│── db.sqlite3  # Default SQLite database
│── manage.py  # Django CLI manager
```

---

## 🔗 URLs & Views
| URL Path       | View Function | Description |
|---------------|--------------|-------------|
| `/`           | `index`       | Homepage with text input form |
| `/analyze/`   | `analyze`     | Processes text and displays results |

---

## ✨ Features Breakdown
- **index.html** → Displays the form to enter text and select options.
- **analyze.html** → Shows the processed text after analysis.
- **views.py** → Contains Python functions to handle text processing.
- **urls.py** → Manages URL routing.

---

## ❓ Troubleshooting
### **Common Issues & Fixes**
- **Error: `ModuleNotFoundError: No module named 'django'`**  
  🔹 Run `pip install django` inside your virtual environment.

- **Error: `RuntimeError at /analyze/`**  
  🔹 Ensure that your form in `index.html` has `method='POST'` and `{% csrf_token %}` is included.
  🔹 Ensure your `analyze` function in `views.py` correctly processes POST requests.

---

## 🛠 Future Improvements
- Add more text processing options (word count, sentence count, etc.)
- Implement user authentication
- Save text history for users
- Deploy the project online

---

## 📜 License
This project is licensed under the MIT License.

🚀 **Happy Coding!**

