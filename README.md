# ✦ Aurora E-Commerce

A modern full-stack e-commerce web application built with Django.  
Aurora provides a premium online shopping experience with authentication, product management, cart system, wishlist, orders, reviews, REST APIs, cloud image storage, and production deployment.

🌐 Live Demo:
https://aurora-ecommerce.onrender.com


---

## ✨ Features

### 🛍️ Store Features

- Browse products
- Product categories
- Product search
- Price sorting
- Product detail pages
- Product images
- Customer reviews
- Rating system


---

### 👤 User Features

- User registration
- User login/logout
- User profile
- Shopping cart
- Wishlist
- Order history


---

### 🛒 Cart & Orders

- Add products to cart
- Remove products
- Manage quantities
- Checkout system
- Order tracking


---

### ⭐ Reviews

- Add product reviews
- Product rating system
- Average rating calculation


---

### 🛠 Admin Features

- Django admin panel
- Manage products
- Manage categories
- Manage users
- Manage orders

Custom dashboard with:

- Total products
- Total users
- Total orders
- Revenue tracking
- Top products


---

## 🔌 REST API

Aurora includes Django REST Framework APIs.

Features:

- Product API
- CRUD operations
- Token authentication
- Pagination
- Search
- Filtering
- Ordering


Example:

```
GET /api/products-new/
```


Response:

```json
{
    "count": 10,
    "results": [
        {
            "id": 1,
            "name": "iPhone 16 Pro Max",
            "price": "144900.00"
        }
    ]
}
```


---

# 🧰 Tech Stack


## Backend

- Python
- Django 6
- Django REST Framework


## Database

- PostgreSQL
- Neon Database


## Media Storage

- Cloudinary


## Deployment

- Render
- Gunicorn
- WhiteNoise


## Other Tools

- Git
- GitHub
- Environment Variables


---

# 📂 Project Structure


```
aurora-ecommerce/

│
├── accounts/
│   └── User authentication
│
├── cart/
│   └── Shopping cart logic
│
├── orders/
│   └── Order management
│
├── store/
│   ├── Products
│   ├── Categories
│   ├── Reviews
│   └── APIs
│
├── templates/
│
├── static/
│
├── ecommerce/
│   └── Settings
│
├── manage.py
│
└── requirements.txt
```


---

# 🚀 Deployment

Application deployed using:

- Render Web Service
- Neon PostgreSQL database
- Cloudinary media hosting


Production configuration:

- Environment variables
- DEBUG disabled
- External database
- Cloud image storage


---

# ⚙️ Local Installation


Clone repository:


```bash
git clone https://github.com/atishaya2020-gif/aurora-ecommerce.git
```


Move into folder:


```bash
cd aurora-ecommerce
```


Create virtual environment:


```bash
python -m venv env
```


Activate environment:


Windows:

```bash
env\Scripts\activate
```


Install dependencies:


```bash
pip install -r requirements.txt
```


Run migrations:


```bash
python manage.py migrate
```


Start server:


```bash
python manage.py runserver
```


---

# 🔐 Environment Variables

Create `.env` file:

```env
SECRET_KEY=your_secret_key

DEBUG=True

DATABASE_URL=your_database_url

CLOUD_NAME=your_cloudinary_name

API_KEY=your_cloudinary_key

API_SECRET=your_cloudinary_secret
```


---

# 📸 Screenshots

(Add screenshots)

- Homepage
- Product page
- Cart
- Admin dashboard
- API


---

# Future Improvements

- Payment integration
- Email notifications
- JWT authentication
- React frontend
- AI recommendations
- Docker support


---

# 👨‍💻 Developer

Built by **ATISHAYA**

A full-stack Django project focused on real-world backend development, APIs, databases, cloud storage, and deployment.


---

⭐ If you like this project, consider giving it a star!
