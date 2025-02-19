import os
import asyncio
from dotenv import load_dotenv

from authenticate_gmail import get_gmail_service
from read_emails import get_recent_emails

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from telegram_bot import send_message

load_dotenv()

async def main():
    # Gmail Authentication
    service = get_gmail_service()
    
    # Read emails (str list)
    emails = get_recent_emails(service, max_results=5)
    if not emails:
        print("No se han encontrado correos")
        
    # Ollama Language Model
    llm = OllamaLLM(model="llama3")
    prompt_template = "Resume de forma concisa el siguiente email: \n\n{email_content}"
    prompt = ChatPromptTemplate(prompt_template)
    chain = prompt | llm
    
    summaries = []
    for email in emails:
        summary = chain.invoke({"email_content": email})
        summaries.append(summary)
        
    # Join summaries
    full_summary = "\n\n".join(summaries)
    print("Resumen generado: \n\n", full_summary)
    
    # Send summary to Telegram
    await send_message(full_summary)
    print("Mensaje enviado a Telegram")
    
if __name__ == "__main__":
    asyncio.run(main())
    
    