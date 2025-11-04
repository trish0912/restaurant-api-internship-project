# 🍽️ RestaurantHub

**RestaurantHub** is a Django + Django REST Framework project designed to manage restaurants, menus, orders, and customer interactions.  
It provides both a **web frontend** (Django templates) and a **RESTful API backend** (DRF + JWT authentication).  

This project was created as part of an internship assignment to demonstrate full-stack Django development, REST API design, authentication, and database management using PostgreSQL.

---

## 🚀 Features

### 🏪 Restaurant Management
- Create and manage restaurant profiles
- Add logos and business details
- Slug-based restaurant URLs

### 🍴 Menu Management
- Each restaurant can have multiple menu items
- Menu items include images, price, and availability
- Search and filter options
- API endpoints for CRUD operations

### 🧾 Order Management
- Customer model linked to Orders
- Orders with multiple MenuItems via OrderItem relation
- Order status tracking: Pending → Confirmed → Delivered → Cancelled
- JWT-secured API endpoints for Orders

### 💬 Contact App
- Simple contact form with database save
- About page for static content

### 🔐 Authentication (JWT)
- Users can register/login using Django’s default authentication system
- JWT tokens used to secure API endpoints
- Anonymous users have read-only access (`IsAuthenticatedOrReadOnly`)

### 💾 Database
- **PostgreSQL** used as the primary database
- Fixtures provided to load dummy data with logos and menu images

### 🖼️ Media & Static Files
- Restaurants have logo images
- Menu items have food images
- Media files served via `/media/` during development

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-------------|
| Backend | Django 5 + Django REST Framework |
| Authentication | Simple JWT |
| Database | PostgreSQL |
| Frontend | Django Templates (HTML, CSS) |
| Media Handling | Django `ImageField`, `MEDIA_ROOT`, `MEDIA_URL` |
| API Testing | Postman / DRF Browsable API |

---

## 📂 Project Structure
```
RestaurantHub/
│
├── apps/
│ ├── restaurants/
│ ├── menu/
│ ├── orders/
│ └── contact/
│
├── media/
│ ├── restaurants/logos/
│ └── menu/images/
│
├── fixtures/
│ └── sample_data.json
│
├── restauranthub/
│ └── settings.py
│
├── manage.py
└── README.md

```
---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/trish0912/restaurant-api-internship-project.git
cd RestaurantHub
```
## Create and activate virtual environment
```
python -m venv .venv
on Windows use: .venv\Scripts\activate
```
## Install dependencies
```
pip install -r requirements.txt
```
## Configure PostgreSQL
Create a database and update your .env or settings.py:
```
DATABASE_NAME=restaurantdb
DATABASE_USER=postgres
DATABASE_PASSWORD=yourpassword
DATABASE_HOST=localhost
DATABASE_PORT=5432
```
## Run migrations
```
python manage.py makemigrations
python manage.py migrate
```
## Load dummy data
```
python manage.py loaddata fixtures/sample_data.json
```
## Create a superuser
```
python manage.py createsuperuser
```
## Run the server
```
python manage.py runserver
```
## API Endpoints
```
| Feature       | Endpoint              | Method                 | Auth |
| ------------- | --------------------- | ---------------------- | ---- |
| Restaurants   | `/api/restaurants/`   | GET, POST              | JWT  |
| Menu Items    | `/api/menu/`          | GET, POST              | JWT  |
| Orders        | `/api/orders/`        | GET, POST, PUT, DELETE | JWT  |
| Token Obtain  | `/api/token/`         | POST                   | -    |
| Token Refresh | `/api/token/refresh/` | POST                   | -    |
```
## Authentication Example (Postman)
## Obtain token
```
POST /api/token/
{
    "username": "admin",
    "password": "admin123"
}
```
## Use token in headers
```
Authorization: Bearer <access_token>
```
## Access protected endpoints like:
```
GET /api/orders/
POST /api/menu/
```
## Internship Outcome

This project demonstrates:

Full Django project structure & app modularization

REST API creation with DRF ViewSets

Integration of JWT Authentication

PostgreSQL database handling

Admin customization with image previews

Static & Media file management

Testing APIs via Postman

## License

This project is open-sourced under the MIT License.

## Author

**Trishna Roy**  
Django Intern @ Perpex  
📧 [trishnaroy@example.com](mailto:trish0991@yahoo.in)  
🔗 [GitHub](https://github.com/trish0912) | [LinkedIn](https://www.linkedin.com/in/trishna-r-06026914a/)

















