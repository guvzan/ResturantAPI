<h1>Setup</h1>
1. Download repository.<br>
2. Install packages from requirements.txt to your virtual environment with "-r requirements.txt" command.<br>
3. Create .env file in root directory with Django SECRET_KEY and Database configuration:<br>
<ul>
  <li>SECRET_KEY=some_secret_key</li>
  <li>DB_NAME=postgres</li>
  <li>DB_USER=postgres</li>
  <li>DB_PASSWORD=your_password</li>
  <li>DB_HOST=localhost</li>
  <li>DB_PORT=5432</li>
</ul>

4. Make migrations to populate your Database with tables by running this commands: "python manage.py makemigrations" and then "python manage.py migrate"<br>
