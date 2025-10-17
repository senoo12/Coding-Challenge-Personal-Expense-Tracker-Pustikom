# Coding-Challenge-Personal-Expense-Tracker-Pustikom

## Testing Project:
1. Clone the repository.<br>
   git clone https://github.com/senoo12/Coding-Challenge-Personal-Expense-Tracker-Pustikom.git<br>
   cd Coding-Challenge-Personal-Expense-Tracker-Pustikom <br>
   cd pustikom
2. Create Virtual Env.<br>
   python -m venv venv<br>
   venv\Scripts\activate       # Windows <br>
   source venv/bin/activate    # macOS / Linux
3. Install the Dependencies<br>
   pip install -r requirements.txt
4. Import Database on Local Server.<br>
   name of database: db_pustikom
6. Create Migrations<br>
   py manage.py makemigrations<br>
   py manage.py migrate
7. Running the server<br>
   python manage.py runserver
8. Web Server:<br>
   http://127.0.0.1:8000/api/expenses/
9. Add Data: <br>
   Fill the form and submiy the button.
11. Get Data with Filtering:<br>
    Use button filtering and choose the category.
12. Edit Data: <br>
    Go to the specific url, with example: /api/expenses/{id} <br>
    Change the data with the form.
13. Delete Data: <br>
    Go to the specific url, with example: /api/expenses/{id} <br>
    Touch the button 'delete'. 

    

  ## End Point Testing:<br>
  GET - /api/expenses/ <br>
  GET ID - /api/expenses/{id} <br>
  GET DATA BY CATEGORY - /api/expenses/?category={category} <br>
  POST - /api/expenses/ <br>
  PUT / PATCH - /api/expenses/{id}/ <br>
  DELETE - /api/expenses/{id}/ <br>
