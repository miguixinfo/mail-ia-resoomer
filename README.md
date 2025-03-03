# Mail AI Resoomer

This project is an application that uses the Gmail API to read recent emails, summarize their content using a language model, and send the summary to a Telegram chat.

## Project Structure

- [`main.py`](main.py): Main file that orchestrates email reading, summary generation, and Telegram messaging.
- [`authenticate_gmail.py`](authenticate_gmail.py): Module for authenticating with the Gmail API.
- [`read_emails.py`](read_emails.py): Module for reading recent emails.
- [`telegram_bot.py`](telegram_bot.py): Module for sending messages to a Telegram chat.
- [`.env`](.env): Configuration file with Telegram bot credentials.
- [`requirements.txt`](requirements.txt): File with project dependencies.

## Installation

1. Clone the repository:

   ```sh
   git clone <REPOSITORY_URL>
   cd mail-ia-resoomer
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv env
   source env/Scripts/activate  # On Windows
   source env/bin/activate      # On Unix or MacOS
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Create a Telegram Bot:

   - Open Telegram and search for "@BotFather"
   - Start a chat and send "/newbot"
   - Follow the instructions to create your bot
   - Save the bot token provided by BotFather
   - Start a chat with your bot and send a message
   - Get your chat ID by accessing: https://api.telegram.org/bot<YourBOTToken>/getUpdates

5. Configure credentials:
   - Create a [credentials.json](http://_vscodecontentref_/0) file with your Gmail API credentials.
   - Create a [.env](http://_vscodecontentref_/1) file with the following variables:
     ```
     TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
     TELEGRAM_CHAT_ID=YOUR_TELEGRAM_CHAT_ID
     ```

## Usage

1. Authenticate with the Gmail API:

   ```sh
   python authenticate_gmail.py
   ```

2. Run the main script:
   ```sh
   python main.py
   ```

The application will:

1. Fetch recent unread emails from your Gmail account
2. Use the Ollama LLM to summarize each email
3. Send the summarized content to your configured Telegram chat

## Requirements

This project uses several libraries including:

- Google API client for Gmail access
- python-telegram-bot for Telegram integration
- LangChain with Ollama for email summarization
- python-dotenv for environment variable management

## Contributing

Contributions are welcome. Please open an issue or a pull request to discuss any changes you wish to make.
