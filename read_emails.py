import re
from authenticate_gmail import get_gmail_service
import base64

def get_email_body(msg_data):
    """
    Extracts and decodes the body text from an email message.
    Args:
        msg_data (dict): The email message data containing the payload.
    Returns:
        str: The decoded body text of the email. If the body text cannot be decoded, 
             an empty string is returned.
    """
    payload = msg_data.get("payload", {})
    body_text = ""

    if "data" in payload.get("body", {}):
        data = payload["body"]["data"]
        try:
            body_text = base64.urlsafe_b64decode(data).decode('utf-8')
        except Exception as e:
            body_text = ""
    else:
        parts = payload.get("parts", [])
        for part in parts:
            if part.get("mimeType") == "text/plain" and "data" in part.get("body", {}):
                try:
                    data = part["body"]["data"]
                    text = base64.urlsafe_b64decode(data).decode('utf-8')
                    body_text += text + "\n"
                except Exception as e:
                    continue
    
    return body_text

def get_recent_emails(service, max_results=5):
    """
    Fetches recent unread emails from the primary category of the user's Gmail account.
    Args:
        service: Authorized Gmail API service instance.
        max_results (int, optional): Maximum number of emails to fetch. Defaults to 5.
    Returns:
        list: A list of strings, each containing the subject and body of an email.
    """
    emails = []
    results = service.users().messages().list(
        userId="me",
        q="category:primary is:unread",  
        maxResults=max_results
    ).execute()
    messages = results.get("messages", [])

    for i, msg in enumerate(messages):
        msg_data = service.users().messages().get(userId="me", id=msg["id"]).execute()
        headers = msg_data["payload"]["headers"]
        subject = next((h["value"] for h in headers if h["name"] == "Subject"), "Sin asunto")
        body = get_email_body(msg_data)
        email_text = f"-Email {i + 1}: Asunto: {subject}\nContenido:\n{body}"
        emails.append(email_text)
        print(email_text)
        
    return emails

if __name__ == "__main__":
    service = get_gmail_service()
    get_recent_emails(service)
