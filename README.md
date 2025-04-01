# AI Agent URL Summary

## Installation
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Features
- URL content retrieval
- Summarization of web content

## Usage
To run the application, execute the following command:
```bash
streamlit run src/app.py  
```
### Example Workflow
1. Input a URL in the provided text box.
2. Click the "Summarize" button.
3. View the summary displayed on the page.

## Technologies Used
- Streamlit
- Google Generative AI
- Beautiful Soup
- Requests
- Python Dotenv

## Folder Structure
```
/AI_AGENT_URL_SUMMARY
│
├── app.py
├── requirements.txt
└── venv/
```

## Limitations
- *Static Content Only*: Cannot render JavaScript-heavy pages (e.g., React/Angular apps).
- *API Dependency*: Requires a valid Gemini API key (free tier has usage limits).
- *Summary Quality*: May vary for complex or poorly structured web content.

## requirements.txt
```
streamlit==1.32.0
google-generativeai==0.5.2
beautifulsoup4==4.12.3
requests==2.31.0
python-dotenv==1.0.1
```
