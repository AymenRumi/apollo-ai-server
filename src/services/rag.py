from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from src.services.openai import MODEL
from src.shared.prompt import read_prompt


def handle_request(request: str, notes: list = []):

    handle_request_prompt_template = PromptTemplate.from_template(
        read_prompt("REQUEST_PROMPT")
    )
    request_chain = (
        {"notes": RunnablePassthrough(), "question": RunnablePassthrough()}
        | handle_request_prompt_template
        | MODEL
        | StrOutputParser()
    )

    try:
        response = request_chain.invoke(
            {"notes": ", ".join(notes), "question": request}
        )
    except:
        raise

    return response
