### CSV Call Record CMS

This is a guide for setting up a Python-based CSV call record CMS (Content Management System) with the specified requirements.

#### Requirements:
- Python 3.10 or later
- PostgreSQL
- .env file setup
- Python environment setup
- Django app setup
- Frontend with DataTable for viewing and interacting with data
- API endpoints for dumping and reading CSV files

#### Installation Steps:

1. **Install Python 3.10**:
   - Ensure Python 3.10 or later is installed on your system.

2. **Install PostgreSQL**:
   - Install PostgreSQL on your system.
   - Create a user named 'postgres'.

3. **Create a Database**:
   - Create a database with any desired name.

4. **Setup .env File**:
   - Create a file named `.env`.
   - Copy values from the example env to `.env`.

5. **Python Environment Setup**:
   ```bash
   python -m venv env
   source env/bin/activate
   ```

6. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

7. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

8. **Check Setup**:
   ```bash
   python manage.py check
   ```

9. **Run Server**:
   ```bash
   python manage.py runserver
   ```

#### API Endpoints:

- **POST /api/dump_csv**:
  - Data:
    ```json
    {
      "csv_file": file
    }
    ```
  - Description: Endpoint to dump CSV files.

- **GET /api/read_csv?key="value"**:
  - Parameters:
    - key: Value to search for in the CSV data.
  - Description: Endpoint to read CSV data based on a provided key.

#### Frontend - DataTable:

- **app/data_table**:
  - Contains functionality for viewing and interacting with data in a DataTable.
  - Features:
    - Custom search by keys provided in the DataTable.
    - DataTable sorting and searching.
    - Pagination.

#### Additional Notes:
- Ensure PostgreSQL is running before starting the Django server.
- Customize frontend as per your design requirements.
- Secure the system properly before deploying to production.
