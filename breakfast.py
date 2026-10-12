from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Read the .env file so OPENAI_API_KEY becomes an environment variable
load_dotenv()

# Create the model object (LangChain finds the key automatically)
llm = ChatOpenAI(model="gpt-4o-mini")

# The prompt: be specific about COUNT and FORMAT
prompt = (
    "Give me exactly 5 healthy breakfast ideas.\n"
    "Format rules:\n"
    "- Use a numbered list from 1 to 5.\n"
    "- Write each idea on a single line (a short name, at most a few words).\n"
    "- Do not add any introduction or closing sentence.\n"
    "- Do not use bold or any other markdown formatting.\n"
    "Output only the list."
)


# Send the prompt to the model and store what comes back
response = llm.invoke(prompt)

# .content pulls out ONLY the text of the reply
print(response.content)