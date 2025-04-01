import os
import re
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class AIAgent:
    def __init__(self):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def fetch_content(self, url):
        """Fetch and clean webpage text"""
        if not self._validate_url(url):
            raise ValueError("Invalid URL format")
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove non-content elements
            for tag in ['script', 'style', 'nav', 'footer']:
                for element in soup.find_all(tag):
                    element.decompose()
                    
            return soup.get_text(separator=' ', strip=True)[:10000]
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error: {str(e)}")

    def generate_summary(self, text):
        """Generate summary using Gemini"""
        try:
            response = self.model.generate_content(f"""
                Summarize in 5 bullet points:
                - Key facts and figures
                - Main arguments/conclusions
                - Technical terms defined
                - Actionable insights
                - Limitations/missing info
                CONTENT: {text}
            """)
            return response.text
        except Exception as e:
            raise Exception(f"Summarization failed: {str(e)}")

    def _validate_url(self, url):
        """Prevent malicious URLs"""
        regex = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) is not None