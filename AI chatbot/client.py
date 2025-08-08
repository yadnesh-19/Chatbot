import openai

openai.api_key = openai.openAI(api_key=" ")

response = openai.ChatCompletion.create(
  model="gemini-2.5-flash",
  messages=[
        {"role": "user", "content":"You are a person name harry who speaks hindi as  well as"
         "English and is a coder" "Hello!",}
    ]
)

print(response)

