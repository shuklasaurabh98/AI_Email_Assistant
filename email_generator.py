import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_email(subject, purpose, tone, recipient, key_points, sender):
    
    prompt = f"""
    You are an expert email writer.

    Write a {tone} email using the details below.

    IMPORTANT:
    - DO NOT include "Subject:" inside the email body
    - Only write the email content (greeting + body + closing)

    Details:
    Subject: {subject}
    Purpose: {purpose}
    Recipient: {recipient}

    Key Points: {key_points}

    Sender Name: {sender}

    Structure:
    - Proper greeting
    - Clear and professional body
    - Polite closing with sender name
    """

    response = model.generate_content(prompt)

    return response.text.strip()


# if __name__ == "__main__":
#     email = generate_email(
#         subject="Leave Request",
#         purpose="Request leave for 2 days",
#         tone="Formal",
#         recipient="Manager",
#         key_points="Not feeling well, will complete pending work after return",
#         sender="Saurabh"
#     )

#     print(email)