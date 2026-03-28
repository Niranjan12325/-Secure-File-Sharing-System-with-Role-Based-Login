#  Secure File Sharing System with Role-Based Access

##  Overview

This project is a **secure file sharing web application** that allows users to upload, store, and access files with **encryption and role-based access control (RBAC)**.

The system ensures that only authorized users can access specific files, making it suitable for real-world organizational use cases.

---

##  Features

*  **AES Encryption**

  * Files are encrypted before storage
  * Ensures data confidentiality

*  **Role-Based Access Control (RBAC)**

  * Admin: Upload & access all files
  * Employee: Access only assigned files

*  **File Assignment System**

  * Admin assigns files to specific users
  * Unauthorized access is restricted

*  **Authentication System**

  * Login with username & password
  * Role-based authorization

*  **Simple Web Interface**

  * Login page
  * Dashboard for upload/download

---

##  How It Works

1. User logs into the system
2. Admin uploads file
3. File is encrypted using AES algorithm
4. File is assigned to a specific user
5. User downloads file → backend decrypts → original file is received

---

##  Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, JavaScript
* **Encryption:** AES (CBC Mode) using PyCryptodome
* **Concepts Used:**

  * Role-Based Access Control (RBAC)
  * Authentication & Authorization
  * File Handling
  * Cryptography

---

##  Project Structure


secure-file-sharing/
│
├── backend/
│   ├── app.py
│   ├── files/
│
├── frontend/
│   ├── index.html
│   ├── dashboard.html
│
└── README.md




##  Installation & Setup

### 1. Clone the Repository


git clone https://github.com/Niranjan12325/-Secure-File-Sharing-System-with-Role-Based-Login.git
cd -Secure-File-Sharing-System-with-Role-Based-Login


### 2. Install Dependencies

pip install flask flask-cors pycryptodome


---

### 3. Run Backend

```
cd backend
python app.py
```

---

### 4. Open Frontend

* Open `frontend/index.html` in your browser

---

##  Default Users

| Username | Password | Role     |
| -------- | -------- | -------- |
| admin    | 123      | Admin    |
| emp      | 123      | Employee |

---

##  Usage

* Login as **Admin**

  * Upload file
  * Assign file to user

* Login as **Employee**

  * Download assigned files only

---

##  Security Features

* AES encryption ensures secure file storage
* Role-based access prevents unauthorized usage
* Files are decrypted only during authorized download

---

##  Future Improvements

* Add database (SQLite / MongoDB)
* Implement JWT authentication
* File preview system
* Deploy on cloud (AWS / Render)
* Improve UI with React

---

##  Conclusion

This project demonstrates how **security, access control, and full-stack development** can be combined to build a real-world application.

---

##  Author

**Niranjan E**
