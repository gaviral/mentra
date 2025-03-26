def format_output(text):
    """Format the LLM output for better display"""
    # Clean up any artifacts from the LLM response
    text = text.strip()
    
    # Convert markdown-style headers to HTML
    lines = text.split('\n')
    formatted_lines = []
    
    for line in lines:
        if line.startswith('##'):
            line = f"<h3>{line.replace('##', '').strip()}</h3>"
        elif line.startswith('#'):
            line = f"<h2>{line.replace('#', '').strip()}</h2>"
        formatted_lines.append(line)
    
    return '\n'.join(formatted_lines)

def extract_text(content):
    """Basic text cleaning for inputs"""
    return content.strip()

def handle_errors(func):
    """Decorator for error handling"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Error: {str(e)}"
    return wrapper 