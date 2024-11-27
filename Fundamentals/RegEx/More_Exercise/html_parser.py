import re

def extract_html_info(html):
    # Extract the title from between <title> and </title> tags
    title = re.search(r'<title>(.*?)</title>', html)
    title = title.group(1) if title else "No title found"
    
    # Extract the content from between <body> and </body> tags
    body = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
    body_content = body.group(1) if body else "No content found"
    
    # Remove any HTML tags from the content using a regular expression
    body_content = re.sub(r'<[^>]*>', '', body_content)
    
    # Print the results
    print(f"Title: {title}")
    print(f"Content: {body_content.strip()}")

# Read the input
html_input = input()

# Call the function to extract the title and content
extract_html_info(html_input)
