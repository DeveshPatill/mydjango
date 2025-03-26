# E-Commerce Dairy Product Website (Django)

## Overview
This project is a Django-based e-commerce website that allows users to browse, purchase, and manage dairy products online. The platform includes user authentication, a product catalog, order management, and payment integration.

## Features
- **User Authentication:** Secure login, registration, and password management.
- **Product Management:** Categories include milk, curd, paneer, ghee, cheese, and ice cream.
- **Shopping Cart & Wishlist:** Users can add/remove products before checkout.
- **Secure Checkout & Payment:** Integrated with Razorpay for transactions.
- **Order Tracking:** Users can track order status.
- **Admin Dashboard:** Manage products, orders, and users.
- **Responsive UI:** Optimized for both desktop and mobile.

## Technologies Used
- **Backend:** Django, Django ORM
- **Frontend:** HTML, CSS, JavaScript,Bootstrap
- **Database:** SQLite / PostgreSQL
- **Authentication:** Django Auth System
- **Payment Gateway:** Razorpay
- **Hosting:** AWS / DigitalOcean / Heroku (if applicable)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/dairy-ecommerce.git
   cd dairy-ecommerce
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables in a `.env` file:
   ```
   DATABASE_URL=your_database_url
   SECRET_KEY=your_django_secret_key
   RAZORPAY_KEY=your_payment_api_key
   ```
5. Run database migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure
```
ecommerce-dairy/
│── app/                # Main application
│   ├── models.py       # Database models (Products, Customers, Cart, Orders, Wishlist)
│   ├── forms.py        # Django Forms for authentication and user input
│   ├── apps.py         # Django application configuration
│   ├── views.py        # Business logic and request handling (Not uploaded)
│   ├── urls.py         # URL routing (Not uploaded)
│   ├── templates/      # HTML templates for frontend (Not uploaded)
│   ├── static/         # Static files (CSS, JS, images) (Not uploaded)
│── manage.py           # Django management script
│── requirements.txt    # List of dependencies (Not uploaded)
│── db.sqlite3          # Database file (if using SQLite) (Not uploaded)
│── .env                # Environment variables (Not uploaded)
```

## Usage
- Users can register and log in to browse products.
- Add products to cart or wishlist before checkout.
- Secure payment through Razorpay.
- Track orders and manage profiles.
- Admins can manage inventory and orders via the admin panel.

## Contribution
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Added a new feature"
   ```
4. Push the changes:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License.

## Contact
For queries or support, contact [patildevesh677@gmail.com] 
![image](https://github.com/user-attachments/assets/91d84265-2f7d-424e-b2aa-456e7aaaaa14)
![image](https://github.com/user-attachments/assets/40ad839e-e636-414a-91f9-6ca745454cd5)



