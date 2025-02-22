from flask import Flask, redirect, url_for
import os
import time
import subprocess

app = Flask(__name__)

# Redirect root URL to /htop
@app.route('/')
def home():
    return redirect(url_for('htop'))

@app.route('/htop')
def htop():
    # Get system details
    name = "Your Full Name"
    username = os.environ.get("USER", "default_user")
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    
    # Get top output
    try:
        top_output = subprocess.getoutput("top -b -n 1")
    except Exception as e:
        top_output = f"Error fetching 'top' output: {e}"
    
    # Format output as HTML
    html_content = f"""
    <html>
        <body>
            <h1>System Information</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
