
---

````markdown
# 🌍 BookMyWay – Travel Booking Web App

BookMyWay is a full-stack Django-based travel booking platform that allows users to register, log in, browse various travel options (flights, trains, buses), and make bookings with ease.

## 🚀 Features

- User registration and login/logout
- FAQ section for answering doubts
- View all travel options with filtering
- Book tickets by selecting a travel option
- View, manage, and cancel bookings
- Admin interface to add/edit travel entries

---

## 🛠️ Local Development Setup

Follow these steps to set up the project on your local machine.

### 1. 📦 Clone the Repository

```bash
git clone https://github.com/your-username/bookmyway.git
cd bookmyway
````

### 2. 🐍 Set Up Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. 📥 Install Requirements

```bash
pip install -r requirements.txt
```

Make sure you’re using **Python 3.11 or 3.10** for best compatibility.

### 4. ⚙️ Configure Environment

Create a `.env` file (optional) or configure these settings directly in `settings.py` if not using environment variables.

### 5. 🛠️ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. 👤 Create Superuser (for Admin Panel)

```bash
python manage.py createsuperuser
```

### 7. 🚦 Run the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📝 Available Routes

| Path                     | Description                      |
| ------------------------ | -------------------------------- |
| `/`                      | Home Page                        |
| `/about`                 | About Us                         |
| `/contact`               | Contact Page                     |
|`/destinations`           | Destination Page                     |
| `/register`              | User Registration                |
| `/login/`                 | Login Page                       |
| `/logout/`                | Logout                           |
| `/profile/`               | User Profile                     |
| `/list-travel-options/`  | View & Filter Travel Options     |
| `/book/<int:travel_id>/` | Book a Travel Option             |
| `/bookings/`             | View Bookings                    |
| `/bookings/cancel/<id>/` | Cancel Booking                   |
| `/admin/`                | Admin Dashboard (Superuser only) |

---


## 👩‍💻 Author

Developed by **\[Anwishta Ghosh]**
Feel free to contribute or raise issues!

---

## 📄 License

This project is licensed under the MIT License.

