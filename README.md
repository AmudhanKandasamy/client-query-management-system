# Client Query Management System

A role-based web application built using **Python, Streamlit, and MySQL** that allows:
- **Clients** to submit support queries
- **Support users** to view, track, and close queries

This project demonstrates real-world concepts such as authentication, database operations, and role-based access.

---

## 🚀 Features

### Client
- Secure login
- Submit support queries
- Queries are stored with timestamps

### Support
- Secure login
- View all client queries
- Mark queries as *Closed*
- Track open vs closed queries

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (UI)
- **MySQL** (Database)
- **PyMySQL**
- **Pandas**
- **Git & GitHub**

---

## 📂 Project Structure

client-query-management-system/
│
├── application.py # Streamlit application
├── database_operations.py # Database logic
├── user_db.py # Script to seed users
├── config_example.py # Sample DB config (no secrets)
├── .gitignore # Ignored files
│
├── sql/
│ └── database_schema.sql # Database & table creation
│
└── README.md


---

## ⚙️ Setup Instructions

1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/client-query-management-system.git
cd client-query-management-system

2️⃣ Install dependencies

pip install streamlit pymysql pandas

3️⃣ Database Setup

Open MySQL

Run the SQL script:

sql/database_schema.sql

This will create the database and required tables

4️⃣ Configure Database Connection

Copy:

config_example.py → config.py


Update your MySQL credentials inside config.py

⚠️ config.py is ignored by Git for security.

5️⃣ (Optional) Seed Sample Users

python user_db.py

6️⃣ Run the Application

streamlit run application.py

🔐 Security Practices

Database credentials are not stored in the repository

.gitignore prevents sensitive files from being committed

config_example.py is provided for safe setup

📌 Author

Amudhan K
Senior Business Analyst
Straive, India


