import glob
import os
import shutil
import zipfile

def create_backup():
    '''Function that checks if there is a backup folder, if not make on
        copy files to the folder, zip the folder, delete the non zipped folder
        '''
    count = 1
    backup_folder_name = ""
    while True:
        backup_folder_name = "Backup_" + str(count) 
        if not os.path.exists(backup_folder_name) and not os.path.exists(backup_folder_name + ".zip"):
            os.makedirs(backup_folder_name)
            break
        count += 1

    # copy files 
    backup_files = ["public_key.pem", "private_key.pem", "Fitness_db.db"]
    for file in backup_files:
        _path = os.path.join(os.getcwd(), file)
        get_backup_path = os.path.join(os.getcwd(), backup_folder_name, file)
        if os.path.isfile(_path):
            shutil.copy2(_path, get_backup_path)

    # zip backup folder
    _zip = backup_folder_name + ".zip"
    try:
        with zipfile.ZipFile(_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for _root, _dirs, _files in os.walk(backup_folder_name):
                for f in _files:
                    _path_of_folder = os.path.join(_root, f)
                    zipf.write(_path_of_folder, os.path.relpath(_path_of_folder, backup_folder_name))
    except Exception as e:
        print(f"Exception: {str(e)}")

    # delete unzipped folder
    shutil.rmtree(backup_folder_name)


def restore():
    '''This function will search for the latest backup folder
        create a folder
        extract the backup folder and save in created folder
        delete empty backup folder'''
    
    zipped_folders = sorted(glob.glob("Backup_*.zip"))
    if len(zipped_folders) == 0:
        print("There are no backup folders")
        return
    get_zipped_folder = zipped_folders[-1]

    # create folder
    get_path = os.path.splitext(get_zipped_folder)[0]
    os.makedirs(get_path, exist_ok=True)

    # unzip folder
    try:
        with zipfile.ZipFile(get_zipped_folder, 'r') as zipf:
            zipf.extractall(get_path)
    except Exception as e:
        print(f"Exception: {str(e)}")
     
    # copy files to created folder
    for root, file, files in os.walk(get_path):
        for file in files:
            folder_path = os.path.join(root, file)
            destination_path = os.path.join(os.getcwd(), file)
            shutil.copy2(folder_path, destination_path)

    # delete empty folder
    shutil.rmtree(get_path)