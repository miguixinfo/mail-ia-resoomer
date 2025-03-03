import os
import asyncio
from dotenv import load_dotenv

from authenticate_gmail import get_gmail_service
from read_emails import get_recent_emails

from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

from telegram_bot import send_message

load_dotenv()

template = ("""You are the user's secretary. Your task is to read their emails and summarize them in a clear and concise manner.  

Each email will be provided in the format:  
"Email 1: Subject \n\n Content"  

Your response **must strictly follow the same format**, summarizing each email concisely under its respective header (e.g., "Email 1: Summary"). The summary should be **short and to the point**, capturing the key details to help the user quickly understand the topic.  

⚠ **Do not include any greetings, farewells, or additional information.**  
⚠ **Only return the summaries in the requested format.**  
  
Here is the email content:  
{email_content}""")

async def main():
    """
    Main function to retrieve recent emails, summarize their content using a language model, 
    and send the summary to a Telegram chat.
    Steps:
    1. Retrieve recent emails using the Gmail service.
    2. Summarize the content of each email using a language model.
    3. Combine all summaries into a single summary.
    4. Send the combined summary to a Telegram chat.
    Raises:
        Exception: If no recent emails are found.
    """
    service = get_gmail_service()
    
    emails = get_recent_emails(service, max_results=5)
    if not emails:
        raise Exception("No recent emails found.")
        
    llm = OllamaLLM(model="llama3")
    prompt = PromptTemplate(template=template)
    chain = prompt | llm
    
    summaries = []
    for email in emails:
        summary = chain.invoke({"email_content": email})
        summaries.append(summary)
        
    full_summary = "\n\n".join(summaries)
    print("Resumen generado: \n\n", full_summary)
    
    await send_message(full_summary)
    print("Mensaje enviado a Telegram")
    
if __name__ == "__main__":
    asyncio.run(main())
    
    