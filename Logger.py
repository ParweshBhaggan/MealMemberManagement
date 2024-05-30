from datetime import datetime
import os


def log(message):
    log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Log\Mealmembermanagement.log')
    if not os.path.exists(log_file):
        with open(log_file, 'w') as file:
            file.write('Log file created\n')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a') as file:
        file.write(f'{timestamp} - {message}\n')

def logViewer():
        print('\nViewing log file')
        log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Log\Mealmembermanagement.log')
        with open(log_file, 'r') as f:
            logs = f.read()
            print(logs)