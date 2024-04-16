# 510_lab3

Lecture: Data storage with Python
Objective: Make an app that you can use to manage your chatGPT prompts!

Getting Started

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Some debug experiences

Connecting local git and remote githut repository everytime encounter some similar problem.
Then, trying to polish the process:
1.Create a new repository on your github with README.md
2.Git clone
3.Create app.py, new stuff on vs code, then push them to repository to check how does it wrok

---

"Keep secret" part was complex process, writting down a step memo:
SQL stored: Supabase

1.Go to Supabase project setting, find your URL and password (know it in advance)
2.Open a new terminal,
2.1 evn
2.2 export MYSUPERPASSWORD=xxxxxx
3.Back to your exsiting terminal, export DATABASE_URL=postgres:xxxxxx
4.Back to app.py, write"con = psycopg2.connect(os.getenv("DATABASE_URL"))"
5.Create a ".env" file, put your secret inside
5.On Streamlit cloud, keep your secret
