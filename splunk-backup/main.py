'''
USAGE - The script is a backup utility for Splunk that provides the user 
        with a choice of backing up either configuration files, indexed 
        data, or both. It defines default source and destination directories 
        for each type of backup. The script uses shutil and tqdm libraries 
        to copy and display the progress of copying the source directories 
        to the destination directories. The user is prompted to input the 
        source and destination directories if the default directories are 
        not used. Finally, the script runs an infinite loop until the user 
        enters a valid input for the backup type.
        
AUTHOR - https://github.com/Ahendrix9624
'''

import os
import shutil
from tqdm import tqdm

# Set constants for default directories
DEFAULT_CONFIG_SRC_DIR = '/opt/splunk/etc'
DEFAULT_CONFIG_DEST_DIR = '/opt/splunk_backup/configs'
DEFAULT_INDEX_SRC_DIR = '/opt/splunk/var/lib/splunk/defaultdb/db'
DEFAULT_INDEX_DEST_DIR = '/opt/splunk_backup/indexed_data'

def backup_configs(src_dir=DEFAULT_CONFIG_SRC_DIR, dest_dir=DEFAULT_CONFIG_DEST_DIR):
    # Use default directories if input is empty
    config_src_dir = input(f'Enter configuration files source directory [{DEFAULT_CONFIG_SRC_DIR}]: ')
    config_dest_dir = input(f'Enter configuration files destination directory [{DEFAULT_CONFIG_DEST_DIR}]: ')
    src_dir = src_dir or DEFAULT_CONFIG_SRC_DIR
    dest_dir = dest_dir or DEFAULT_CONFIG_DEST_DIR

    shutil.rmtree(dest_dir, ignore_errors=True)
    shutil.copytree(src_dir, dest_dir)
    print(f'\nConfiguration files backed up successfully to {dest_dir}.\n')

def backup_indexed_data(src_dir=DEFAULT_INDEX_SRC_DIR, dest_dir=DEFAULT_INDEX_DEST_DIR):
    # Use default directories if input is empty
    index_src_dir = input(f'Enter indexed data source directory [{DEFAULT_INDEX_SRC_DIR}]: ')
    index_dest_dir = input(f'Enter indexed data destination directory [{DEFAULT_INDEX_DEST_DIR}]: ')

    src_dir = src_dir or DEFAULT_INDEX_SRC_DIR
    dest_dir = dest_dir or DEFAULT_INDEX_DEST_DIR

    shutil.rmtree(dest_dir, ignore_errors=True)
    shutil.copytree(src_dir, dest_dir)
    print(f'\nIndexed data backed up successfully to {dest_dir}.\n')

while True:
    print('Choose backup type:')
    print('1. Configuration files')
    print('2. Indexed data')
    print('3. Both')
    choice = input('Enter choice (1/2/3): ')
    if choice in ['1', '2', '3']:
        break
    print('Invalid input, please try again.')

if choice == '1':
    backup_configs()
elif choice == '2':
    backup_indexed_data()
elif choice =='3':
    backup_configs()
    backup_indexed_data()
