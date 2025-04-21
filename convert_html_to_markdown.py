import sys
import requests
from markdownify import markdownify

def convert_url_to_markdown(url):
    try:
        # Fetch the HTML content from the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        html_content = response.text
        
        # Convert HTML to Markdown
        markdown_content = markdownify(html_content)
        
        # Print the Markdown content
        print(markdown_content)
        # Save the Markdown content to a file
        with open('./test_converted.md', 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        print(f"Markdown content saved to test_converted.md")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_html_to_markdown.py <url>")
        sys.exit(1)
    
    url = sys.argv[1]
    convert_url_to_markdown(url)
