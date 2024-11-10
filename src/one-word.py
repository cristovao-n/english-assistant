from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an English vocabulary assistant. Use \"-\" to list text. Please explain me the meaning of the words I'll provide you following this template: # Word: {{provided English word}} ({{word translated to Portuguese}})  \n## Meaning(s)  \n### As a {{List the meanings according to the possibles part of speech}}  \n## Usage Examples  \n{{At least 3 usage examples}}## synonyms  \n",
        ),
        ("user", "{text}"),
    ]
)

chain = prompt_template | model | parser

word = input()

with open(f"out/result.md", "w") as f:
            output = chain.invoke({"text": word})
            f.write(f"{output}\n\n")

print("Output saved to out/result.md.")
