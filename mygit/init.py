import os
import json

def init():
    if os.path.exists('.mygit'):
        print("Repository already initialized.")
        return
    
    os.makedirs('.mygit/objects')  # To store file snapshots and commits
    os.makedirs('.mygit/refs')     # To store branch references
    with open('.mygit/HEAD', 'w') as head_file:
        head_file.write('refs/heads/master')  # Default branch
    
    with open('.mygit/index', 'w') as index_file:
        json.dump({}, index_file)  # Initialize staging area
    
    print("Initialized empty repository in .mygit/")
