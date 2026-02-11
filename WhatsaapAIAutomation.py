import pywhatkit
from langchain_community.llms import Ollama
llm = Ollama(model="phi3:mini")
task = "send a polite follow-up message to HR regarding interview schedule udates and express continued interest"
# task = input()
prompt = f"""
write  short , polite and professional whatsapp message
keep it formal and concise.PermissionError
task: {task}
"""
message = llm(prompt)
pywhatkit.sendwhatmsg_instantly(
    phone_no = "+91XXXXXXXXXX", #input()
    message = message,
    wait_time = 20,
    tab_close = True
)

print("whatsap message sent sucessfully")
