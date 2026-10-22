app_code = '''import os
from google import genai
from google.colab import userdata

# Initialize the client
api_key = userdata.get('ai_powered_study_assistant.ipynb')
client = genai.Client(api_key=api_key)

def study_assistant(user_prompt):
    """
    Sends a prompt to the Gemini model and gets a response.
    """
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=user_prompt
    )
    return response.text

if __name__ == '__main__':
    user_question = "Explain Generative AI in simple terms"
    print(f"Prompt: {user_question}\n")
    result = study_assistant(user_question)
    print("Response:")
    print(result)
'''

with open('app.py', 'w') as f:
    f.write(app_code)

print("app.py has been successfully written to the local directory!")