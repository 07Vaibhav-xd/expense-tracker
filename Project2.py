
import os
from google import genai
from dotenv import load_dotenv
load_dotenv()
Prompt = "take this information and give me 3 professional email subject lines: "  
INPUT_text=input("enter the email details on which you want the AI Assistant- ")
a=f"{INPUT_text} {Prompt} "
print(f"Final Result {a}")
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
contents = a
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=a
    )
print("\n___ AI Response___")
print(response.text)




