import os
from dotenv import load_dotenv
from groq import Groq

from website_reader import search_website

# ==========================
# LOAD API KEY
# ==========================

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ==========================
# SYSTEM PROMPT
# ==========================

SYSTEM_PROMPT = """
You are UNIUYO AI.

You assist only students of the University of Uyo,
particularly those in the Faculty of Computing and
Department of Data Science.

Rules:

1. Always answer using the website information if available.

2. If the website does not contain the answer,
answer using reliable information about
University of Uyo.

3. Never invent information.

4. If the question is unrelated to University of Uyo,
politely explain that you are designed only for
UNIUYO students.
"""

# ==========================
# AI RESPONSE
# ==========================

def get_ai_response(question):

    website = search_website(question)

    if website:

        prompt = f"""
Website Information:

{website["content"]}

Student Question:

{question}

Answer ONLY using the website information.
If the website doesn't contain enough information,
say so politely.
"""

    else:

        prompt = f"""
The website contains no answer.

Question:

{question}

Answer ONLY if it relates to the University of Uyo,
Faculty of Computing, or the Department of Data Science.

If it is unrelated, politely explain that this AI
is only for UNIUYO students.
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[

            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },

            {
                "role":"user",
                "content":prompt
            }

        ],

        temperature=0.3

    )

    return response.choices[0].message.content