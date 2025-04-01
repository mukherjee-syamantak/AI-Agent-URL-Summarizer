import sys
from pathlib import Path

# Adding the project root to the Python path
sys.path.append(str(Path(__file__).parent.parent))

import streamlit as st
from src.agent import AIAgent

# Initialize agent
agent = AIAgent()

# UI configuration
st.set_page_config(page_title="AI Web Summarizer", layout="wide")
st.title("AI-Powered Web Content Analyzer")

# URL input
url = st.text_input("Enter URL", placeholder="https://example.com")

if url:
    try:
        # Fetch content
        with st.spinner("Analyzing content..."):
            content = agent.fetch_content(url)
        
        # Display preview
        st.subheader("Content Preview")
        st.code(content[:500] + "...", language=None)
        
        # Generate summary
        if st.button("Generate Summary"):
            with st.spinner("Creating summary..."):
                summary = agent.generate_summary(content)
            
            st.success("Summary ready!")
            st.subheader("Key Insights")
            st.markdown(summary)
            
            # Download option
            st.download_button(
                "Download Summary",
                summary,
                file_name="summary.txt"
            )
    except Exception as e:
        st.error(str(e))