from datetime import datetime
import os

def log(username, description, additional_info="", suspicious="No"):
    log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Mealmembermanagement.log')
    
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    log_number = next_log_number(log_file)
    
    current_datetime = datetime.now()
    date = current_datetime.strftime('%d-%m-%Y')
    time = current_datetime.strftime('%H:%M:%S')
    
    log_message = f'{log_number} {date} {time} {username} {description} {additional_info} {suspicious}\n'
    
    with open(log_file, 'a') as file:
        if log_number == 1:
            header = "No. Date, Time, Username, Description activity, Additional Information, Suspicious\n"
            file.write(header)
        file.write(log_message)


def next_log_number(log_file):
    if not os.path.exists(log_file):
        return 1
    with open(log_file, 'r') as file:
        lines = file.readlines()
        if len(lines) <= 1:
            return 1
        last_line = lines[-1]
        last_log_number = int(last_line.split()[0])
        return last_log_number + 1

def logViewer():
        print('\nViewing log file')
        log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Mealmembermanagement.log')
        with open(log_file, 'r') as f:
            logs = f.read()
            print(logs)
        input("Press enter to continue")