# Lab Test Booking Assistant

## Project Overview
The Lab Test Booking Assistant is an AI-powered conversational application that helps users explore laboratory tests, check appointment availability, book appointments, view their bookings, and cancel appointments.

The system uses a Large Language Model (LLM), LangChain tools, and an SQLite database to provide interactive assistance.

## Technologies Used
- Python
- LangChain
- LangChain Groq
- Groq LLM – `openai/gpt-oss-20b`
- LangGraph
- SQLite
- Pandas
- DuckDuckGo Search (DDGS)
- Kaggle Notebook

## Key Features
1. Display available laboratory tests and prices.
2. Check available appointment slots.
3. Book laboratory test appointments with user approval.
4. View user-specific bookings.
5. Cancel appointments with user approval.
6. Search for general laboratory information online.
7. Interactive conversational interface.
8. Evaluation using eight test scenarios.

## System Workflow
1. User interacts with the assistant.
2. The LLM understands the user's query.
3. LangChain selects the appropriate tool.
4. The tool retrieves information or performs an approved database operation.
5. SQLite stores and manages booking information.
6. The assistant displays the result.

## Database
SQLite is used to store:
- Laboratory tests
- Appointment slots
- User bookings

## Evaluation
The system is evaluated using eight test cases covering test listing, slot availability, user-specific bookings, web search, booking approval, and cancellation.

## How to Run
1. Open the notebook in Kaggle or Jupyter Notebook.
2. Configure your Groq API key securely.
3. Install the required Python packages.
4. Execute the notebook cells in order.
5. Interact with the booking assistant.

## Security Note
Do not upload API keys, passwords, or other credentials to GitHub. Configure API keys through Kaggle Secrets or environment variables.

## Project Status
Implementation and evaluation completed.