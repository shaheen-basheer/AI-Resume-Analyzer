import google.generativeai as genai

with open("gemini_key.txt", "r") as file:
    api_key = file.read().strip()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content("Say hello in one sentence.")

print(response.text)