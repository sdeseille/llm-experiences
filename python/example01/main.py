from ollama import chat

print('Start chat')

messages = [
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
]

for part in chat('phi', messages=messages, stream=True):
  print(part['message']['content'], end='', flush=True)

# end with a newline
print()
print('End chat')