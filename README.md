# Coding-Challenge-Personal-Expense-Tracker-Pustikom

Testing Project:
1. Clone the repository
   git clone https://github.com/senoo12/Coding-Challenge-Personal-Expense-Tracker-Pustikom.git
   cd Coding-Challenge-Personal-Expense-Tracker-Pustikom
2. Create Virtual Env.
   python -m venv venv
   venv\Scripts\activate       # Windows
   source venv/bin/activate    # macOS / Linux
3. Install the Dependencies
   pip install -r requirements.txt
4. Create Migrations
   py manage.py makemigrations
   py manage.py migrate
5. Running the server
   python manage.py runserver
6. Web Server:
   http://127.0.0.1:8000/api/expenses/

  End Point Testing:
  GET - /api/expenses/ 
  GET ID - /api/expenses/{id}
  GET DATA BY CATEGORY - /api/expenses/?category={category}
  POST - /api/expenses/
  PUT / PATCH - /api/expenses/{id}/
  DELETE - /api/expenses/{id}/
