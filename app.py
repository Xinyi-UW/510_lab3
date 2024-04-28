import os
import datetime
from dataclasses import dataclass
import psycopg2
import streamlit as st
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

@dataclass
class Prompt:
    """Dataclass to hold prompt details."""
    title: str
    prompt: str
    is_favorite: bool
    created_at: datetime.datetime = None
    updated_at: datetime.datetime = None

def setup_database():
    """Setup database connection and initialize prompts table."""
    con = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS prompts (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            prompt TEXT NOT NULL,
            is_favorite BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    con.commit()
    return con, cur

def prompt_form(prompt=None):
    """Create form to submit new prompts or edit existing ones."""
    default = Prompt("", "", False) if prompt is None else prompt
    with st.form(key="prompt_form", clear_on_submit=True):
        title = st.text_input("Title", value=default.title)
        prompt_content = st.text_area("Prompt", height=200, value=default.prompt)
        is_favorite = st.checkbox("Favorite", value=default.is_favorite)
        submitted = st.form_submit_button("Submit")
        if submitted and title and prompt_content:
            return Prompt(title, prompt_content, is_favorite)
        elif submitted:
            st.error('Please fill in both the title and prompt fields.')

def display_prompts(cur, con):
    """Display, search, and manage prompts."""
    search_query = st.text_input("Search prompts")
    sort_order = st.selectbox("Sort by", options=[
        "Created date (newest first)", "Created date (oldest first)",
        "Updated date (newest first)", "Updated date (oldest first)"
    ])
    order_query = {
        "Created date (newest first)": "ORDER BY created_at DESC",
        "Created date (oldest first)": "ORDER BY created_at ASC",
        "Updated date (newest first)": "ORDER BY updated_at DESC",
        "Updated date (oldest first)": "ORDER BY updated_at ASC"
    }[sort_order]
    cur.execute(f"SELECT * FROM prompts WHERE title LIKE %s {order_query}", ('%' + search_query + '%',))
    prompts = cur.fetchall()
    for p in prompts:
        with st.expander(f"{p[1]} (created at: {p[4]})"):
            title = st.text_input("Title", value=p[1], key=f"title{p[0]}")
            content = st.text_area("Content", value=p[2], height=200, key=f"content{p[0]}")
            is_favorite = st.checkbox("Favorite", value=p[3], key=f"fav{p[0]}")
            if st.button("Save Changes", key=f"save{p[0]}"):
                cur.execute("UPDATE prompts SET title = %s, prompt = %s, is_favorite = %s, updated_at = CURRENT_TIMESTAMP WHERE id = %s", 
                            (title, content, is_favorite, p[0]))
                con.commit()
                st.success("Updated successfully!")
            if st.button("Delete", key=f"delete{p[0]}"):
                cur.execute("DELETE FROM prompts WHERE id = %s", (p[0],))
                con.commit()
                st.experimental_rerun()

if __name__ == "__main__":
    st.title("PromptsLand")
    st.subheader("An App to store and retrieve prompts")

    con, cur = setup_database()

    new_prompt = prompt_form()
    if new_prompt:
        try:
            cur.execute("INSERT INTO prompts (title, prompt, is_favorite) VALUES (%s, %s, %s)",
                        (new_prompt.title, new_prompt.prompt, new_prompt.is_favorite))
            con.commit()
            st.success("Prompt added successfully!")
        except psycopg2.Error as e:
            st.error(f"Database error: {e}")

    display_prompts(cur, con)
    con.close()
