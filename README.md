# 510_lab3

## Lecture: Data Storage with Python

### Objective

Create an app to manage your ChatGPT prompts.

### Changes Made

- Corrected a small typo mentioned by the TA and refreshed the app page.

## Getting Started

1. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Debug Experiences

### GitHub Repository Connection

Connecting a local Git repository to a remote GitHub repository often encounters similar problems. Here’s an improved process:

1. Create a new repository on GitHub with a `README.md`.
2. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
3. Create `app.py` and other files in VS Code, then push them to the repository to check how it works:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

### Keeping Secrets Secure

Managing secrets securely can be complex. Here’s a step-by-step memo:

1. **SQL Stored: Supabase**
   - Go to Supabase project settings, find your URL and password.
2. **Setting Up Environment Variables**

   - Open a new terminal:
     ```bash
     # Create a new environment variable
     export MYSUPERPASSWORD=xxxxxx
     ```
   - Go back to your existing terminal:
     ```bash
     export DATABASE_URL=postgres://username:password@hostname:port/databasename
     ```

3. **Updating `app.py`**

   - Update your database connection:

     ```python
     import os
     import psycopg2

     con = psycopg2.connect(os.getenv("DATABASE_URL"))
     ```

4. **Creating a `.env` File**

   - Create a `.env` file and put your secrets inside:
     ```
     DATABASE_URL=postgres://username:password@hostname:port/databasename
     ```

5. **Streamlit Cloud**
   - On Streamlit cloud, keep your secrets secure by setting them in the environment settings.

## How to Run This Project

1. Install required packages:

   ```bash
   pip install streamlit psycopg2 python-dotenv plotly
   ```

2. Set up your database URL:

   ```bash
   export DATABASE_URL=postgresql://username:password@hostname:port/databasename
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

Feel free to make any additional adjustments based on your specific requirements or additional information.
