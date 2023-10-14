## Running the Boi-Ghor Application

### Prerequisites

1. **Python:** Ensure you have Python (version 3.x) installed. You can check this by running:
    ```bash
    python3 --version
    ```

2. **pip:** Make sure you have pip installed:
    ```bash
    pip3 --version
    ```

3. **Virtual Environment (Optional but Recommended):** It's often a good practice to run Python projects within a virtual environment to manage dependencies. Install `virtualenv` if you haven't:
    ```bash
    pip3 install virtualenv
    ```

### Setup & Activation

1. **Clone the Repository:**
    ```bash
    git clone git@github.com:emoncse/Boi-Ghor.git
    cd Boi-Ghor
    ```

2. **Set up a Virtual Environment (Optional):**
    ```bash
    virtualenv venv
    ```

   - **Activate the Virtual Environment:**
     - On macOS and Linux:
       ```bash
       source venv/bin/activate
       ```
     - On Windows:
       ```bash
       .\venv\Scripts\activate
       ```

3. **Install Dependencies:**
    ```bash
    pip3 install -r requirements.txt
    ```

### Database Migrations

Before running the server, ensure you apply the migrations to set up your database schema:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Run the server

```bash
python3 manage.py runserver
```


### To add books, author, category

```bash
Username: admin
Password: Somikoron
Admin URL: http://127.0.0.1:8000/admin/
```


#### Thanks
