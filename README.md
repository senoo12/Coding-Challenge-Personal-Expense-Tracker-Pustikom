# Coding-Challenge-Personal-Expense-Tracker-Pustikom

Testing Project:
1. Clone the repository.<br>
   git clone https://github.com/senoo12/Coding-Challenge-Personal-Expense-Tracker-Pustikom.git<br>
   cd Coding-Challenge-Personal-Expense-Tracker-Pustikom
2. Create Virtual Env.<br>
   python -m venv venv<br>
   venv\Scripts\activate<br>       # Windows
   source venv/bin/activate    # macOS / Linux
3. Install the Dependencies<br>
   pip install -r requirements.txt
4. Create Migrations<br>
   py manage.py makemigrations<br>
   py manage.py migrate
5. Running the server<br>
   python manage.py runserver
6. Web Server:<br>
   http://127.0.0.1:8000/api/expenses/

  End Point Testing:<br>
  GET - /api/expenses/ <br>
  GET ID - /api/expenses/{id} <br>
  GET DATA BY CATEGORY - /api/expenses/?category={category} <br>
  POST - /api/expenses/ <br>
  PUT / PATCH - /api/expenses/{id}/ <br>
  DELETE - /api/expenses/{id}/ <br>
