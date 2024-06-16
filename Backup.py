import os
import shutil
import zipfile

class BackupSystem:
    '''This class handles Backup.'''
    def __init__(self):
        self.backup_folder = "Backupfolder"
      

    def create_backup(self):
        '''Create back up function.'''
        count = 1
        backup_folder_name = ""
        
        if not os.path.exists(self.backup_folder):
            os.makedirs(self.backup_folder)
        
        while True:
            backup_folder_name = f"Backup_{count}"
            backup_folder_path = os.path.join(self.backup_folder, backup_folder_name)
            if not os.path.exists(backup_folder_path) and not os.path.exists(backup_folder_path + ".zip"):
                os.makedirs(backup_folder_path)
                break
            count += 1
        
        # copy files 
        backup_files = ["Mealmembermanagement.log", "MealMemberManagement.db"]
        for file in backup_files:
            _path = os.path.join(os.getcwd(), file)
            get_backup_path = os.path.join(backup_folder_path, file)
            if os.path.isfile(_path):
                shutil.copy2(_path, get_backup_path)

        # zip backup folder
        _zip = os.path.join(self.backup_folder, backup_folder_name + ".zip")
        try:
            with zipfile.ZipFile(_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for _root, _dirs, _files in os.walk(backup_folder_path):
                    for f in _files:
                        _path_of_folder = os.path.join(_root, f)
                        zipf.write(_path_of_folder, os.path.relpath(_path_of_folder, backup_folder_path))
        except Exception as e:
            print(f"Exception: {str(e)}")

        # delete unzipped folder
        shutil.rmtree(backup_folder_path)
    
    

    def GetBackupFolders(self):
        '''Retrieve the list of backup folders in the backup folder.'''
        try:
            # Check if the backup folder exists
            if not os.path.exists(self.backup_folder):
                print(f"The backup folder '{self.backup_folder}' does not exist.")
                return []

            # Retrieve the list of .zip files in the backup folder
            backups = []
            for f in os.listdir(self.backup_folder):
                if f.endswith('.zip'):
                    backups.append(f)
            
            # Check if the backups list is empty
            if not backups:
                print("No backups available.")
            
            return backups

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return []


    def restore(self, backupname):
        '''Retrieve the list of backup files in the backup folder.'''
        # Find the latest backup zip file
        get_zipped_folder = os.path.join(self.backup_folder, backupname)

        # Check if the zip file exists
        if not os.path.exists(get_zipped_folder):
            print(f"The backup file '{get_zipped_folder}' does not exist.")
            return

        # Create a folder to extract the backup
        get_path = os.path.splitext(get_zipped_folder)[0]
        os.makedirs(get_path, exist_ok=True)

        # Unzip the folder
        try:
            with zipfile.ZipFile(get_zipped_folder, 'r') as zipf:
                zipf.extractall(get_path)
        except Exception as e:
            print(f"Exception: {str(e)}")
            return
        
        # Copy files to the original location, overwriting if they exist
        for root, _, files in os.walk(get_path):
            for file in files:
                folder_path = os.path.join(root, file)
                destination_path = os.path.join(os.getcwd(), file)
                shutil.copy2(folder_path, destination_path)

        # Delete the extracted backup folder
        shutil.rmtree(get_path)