import os
import sys
import subprocess
from threading import Thread

# Update the system path to include your project
sys.path.insert(0, os.path.dirname(__file__))

# Function to start Streamlit
def run_streamlit():
    streamlit_path = os.path.join(os.path.dirname(__file__), 'Main.py')
    streamlit_path = '/home/prathmes/test.cse-aiml.live/"00_🔒_Login.py"'
    subprocess.run(['streamlit', 'run', streamlit_path, '--server.port=8501'])

# Start Streamlit in a separate thread
thread = Thread(target=run_streamlit)
thread.start()

# Dummy WSGI application to keep the process running
def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    return [b"Streamlit is running."]
