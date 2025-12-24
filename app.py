import openai

openai.api_key = "<replace this value with your open ai key or Azure OpenAI key>"

openai.api_type = 'azure'
openai.api_version = '2023-05-15'
openai.api_base = "<endpoint found in Azure Portal where your API key is>"
deployment_name = "<deployment name>"

# add your completion code
prompt1 = "Complete the following: Once upon a time there wasb a"
messages = [{"role": "user", "content": prompt}]

# make completion
completion = openai.chat.completions.create(model=deployment_name, messages=messages)

# print response
print(completion.choices[0].message.content)