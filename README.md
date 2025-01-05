

# 🏠 Real Estate Application

Welcome to the **Real Estate Application**, built with **Django REST Framework**. This project serves as the backend API for a real estate platform where users can search, list, and manage properties.

---

## 📜 Features
- **User Authentication** (Registration, Login, and Dashboard)
- **Property Listings** (CRUD functionality)
- **Search and Filter** (Search by address, country, and tag-based filtering)
- **User Dashboard** (View user details and properties they own)
- **Category Filtering** (e.g., Rent vs. Sale)
- **Commenting System** (Leave comments on properties)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- A database (default is SQLite, but you can use PostgreSQL or MySQL)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/raufnizam/real-estate-DRF-react.git
   cd real-estate-DRF-react
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the server:
   ```bash
   python manage.py runserver
   ```

7. Access the API at `http://127.0.0.1:8000/api/`

---

## 🛠️ API Endpoints

### Authentication
- **POST** `/api/register/` - Register a new user
- **POST** `/api/login/` - Login to get a token

### Properties
- **GET** `/api/properties/` - List all properties
- **POST** `/api/properties/` - Create a new property (Authenticated users only)
- **GET** `/api/properties/{id}/` - View property details
- **PATCH** `/api/properties/{id}/` - Update a property (Owner only)
- **DELETE** `/api/properties/{id}/` - Delete a property (Owner only)

### Comments
- **GET** `/api/comments/` - List all comments
- **POST** `/api/comments/` - Add a comment (Authenticated users only)

### Search
- **GET** `/api/properties/?search=<query>` - Search properties by country or address
- **GET** `/api/properties/?tag=<tag>` - Filter properties by tag

---

