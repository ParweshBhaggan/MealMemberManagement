from datetime import datetime
from Encryption import*
import os
import base64

security = EncryptionHandler()

def log(username, description, additional_info="", suspicious="No"):
    global security
    '''Create and Write Logs to log file.'''
    log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Mealmembermanagement.log')
    
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    log_number = next_log_number(log_file)
    
    current_datetime = datetime.now()
    date = current_datetime.strftime('%d-%m-%Y')
    time = current_datetime.strftime('%H:%M:%S')
    
    log_message = f'{log_number}'
    plain_message = f'{date} {time} "{username}" {description} {additional_info} {suspicious}'
    
    log_message = log_message + " " + plain_message + "\n"
    encrypted_log_message = security.encrypt_data(log_message)
    encoded_log_message = base64.b64encode(encrypted_log_message).decode('utf-8') + '\n'

    with open(log_file, 'a') as file:
        if log_number == 1:
            header = "No. Date, Time, Username, Description activity, Additional Information, Suspicious\n"
            encrypted_header = security.encrypt_data(header)
            encoded_header = base64.b64encode(encrypted_header).decode('utf-8') + '\n'
            file.write(encoded_header)
        file.write(encoded_log_message)

def next_log_number(log_file):
    global security
    '''Returns next open line of the log file.'''
    
    if not os.path.exists(log_file):
        return 1
    
    with open(log_file, 'r') as file:
        lines = file.readlines()
        if len(lines) <= 1:
            return 1
        for line in reversed(lines):
            try:
                decoded_line = base64.b64decode(line.strip().encode('utf-8'))
                last_line = security.decrypt_data(decoded_line)
                last_log_number = int(last_line.split()[0])
                return last_log_number + 1
            except (rsa.pkcs1.DecryptionError, ValueError):
                continue
    return 1

def logViewer():
    global security
    '''Display the log in the console.'''
    print('\nViewing log file')
    
    log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Mealmembermanagement.log')
    if not os.path.exists(log_file):
        print("Log file does not exist.")
        return
    
    with open(log_file, 'r') as file:
        logs = file.readlines()
        for log in logs:
            try:
                decoded_log = base64.b64decode(log.strip().encode('utf-8'))
                decrypted_log = security.decrypt_data(decoded_log)
                print(decrypted_log)
            except (rsa.pkcs1.DecryptionError, ValueError):
                print("Error decrypting a log entry.")
    
    input("Press enter to continue")