from authenticate_gmail import get_gmail_service

def get_recent_emails(service, max_results=5):
    results = service.users().messages().list(userId="me", maxResults=max_results).execute()
    messages = results.get("messages", [])

    for msg in messages:
        msg_data = service.users().messages().get(userId="me", id=msg["id"]).execute()
        headers = msg_data["payload"]["headers"]
        subject = next((h["value"] for h in headers if h["name"] == "Subject"), "Sin asunto")
        print(f"Asunto: {subject}")

# Ejecutar
if __name__ == "__main__":
    service = get_gmail_service()
    get_recent_emails(service)
