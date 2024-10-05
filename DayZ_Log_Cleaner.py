import os
import traceback

def log_info(message):
    with open("DayZCleaner.log", "a") as log_file:
        log_file.write(f"INFO: {message}\n")
    print(message)

def log_error(message):
    with open("DayZCleaner.log", "a") as log_file:
        log_file.write(f"ERROR: {message}\n")
    print(message)

def clean_dayz_logs():
    try:
        # Log the start of the process
        log_info("DayZCleaner.exe started.")
        
        # Get the LOCALAPPDATA environment variable
        local_appdata = os.getenv('LOCALAPPDATA')
        if not local_appdata:
            log_error("Error: LOCALAPPDATA environment variable is not set.")
            return

        # Define the DayZ log folder path
        dir_path = os.path.join(local_appdata, 'DayZ')
        log_info(f"Looking for files in: {dir_path}")
        
        # Check if the directory exists
        if not os.path.exists(dir_path):
            log_error(f"Directory {dir_path} does not exist.")
            return
        
        # Define file extensions to delete
        extensions = ['.log', '.adm', '.rpt', '.mdmp']
        
        # Initialize total size of removed files
        total_size_removed = 0
        
        # Delete files and calculate total size removed
        for file in os.listdir(dir_path):
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(dir_path, file)
                try:
                    file_size = os.path.getsize(file_path)
                    os.remove(file_path)
                    total_size_removed += file_size
                    log_info(f"Deleted {file}")
                except Exception as e:
                    log_error(f"Error deleting file {file}: {e}")
        
        # Convert the total size to GB and log the result
        size_in_gb = round(total_size_removed / (1024 * 1024 * 1024), 2)
        log_info(f"DayZ cleanup complete! Removed {size_in_gb} GB of log data.")
        
    except Exception as e:
        log_error(f"Unexpected error: {traceback.format_exc()}")

if __name__ == "__main__":
    clean_dayz_logs()
