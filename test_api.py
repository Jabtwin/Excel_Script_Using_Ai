import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("No API key found in .env")
else:
    genai.configure(api_key=api_key)
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content("Xin chào, bạn có hoạt động không?")
        print("Success! Response from gemini-2.5-flash:", response.text)
    except Exception as e:
        print("Error with gemini-2.5-flash:", e)
        
        # Try gemini-pro-latest just in case
        try:
            model2 = genai.GenerativeModel('gemini-pro-latest')
            response2 = model2.generate_content("Xin chào, bạn có hoạt động không?")
            print("Success! Response from gemini-pro-latest:", response2.text)
        except Exception as e2:
            print("Error with gemini-pro-latest:", e2)
