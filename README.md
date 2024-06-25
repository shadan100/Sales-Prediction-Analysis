# Sales-Prediction-Analysis
The aim is to build a predictive model and find out the sales of each product at a particular store. Using this model, BigMart will try to understand the properties of products and stores which play a key role in increasing sales. So the idea is to find out the properties of a product, and store which impacts the sales of a product.

**Dataset link:-** https://www.kaggle.com

### Setup
#### Step 1: Install Python

Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/). It's recommended to use Python 3.x (e.g., Python 3.8 or Python 3.9).


#### Step 2: Create and Activate Virtual Environment

1. Navigate to your project directory in the terminal:
   ```
   cd path/to/your/project
   ```

2. Create a new virtual environment (replace `myenv` with your preferred name):
   ```
   virtualenv myenv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     myenv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source myenv/bin/activate
     ```

#### Step 3: Install requirement.txt

1. It will install all the packages that are required for this project:
   ```
   pip install -r requirements.txt
   ```

#### Step 4: Apply Migration 
1. Make initial migrations for the Django project:
   ```
   python manage.py makemigrations
   ```

2. Apply migrations to set up your database:
   ```
   python manage.py migrate
   ```

#### Step 5: Change model location 
1. The machine learning model (.sav) location inside django views.py need to be change according to your file system.
   
#### Step 6: Run Django Development Server

1. Start the Django development server:
   ```
   python manage.py runserver
   ```

2. Open your web browser and go to `http://127.0.0.1:8000/` or `http://localhost:8000/` to see your Django project running locally.

### Additional Notes

- **Project Structure**: Ensure your project files are organized appropriately for a Django project. You may need to create apps (`python manage.py startapp appname`) within your project for specific functionalities like the stroke prediction analysis.
  
- **Database Configuration**: Django uses SQLite by default. Modify `settings.py` if you want to use a different database like PostgreSQL or MySQL.
