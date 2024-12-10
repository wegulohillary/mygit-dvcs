import hashlib
import os
import json

def hash_file_content(content):
    return hashlib.sha1(content.encode()).hexdigest()

def add(files):
    if not os.path.exists('.mygit'):
        print("Not a repository. Run 'init' first.")
        return

    index_path = '.mygit/index'
    with open(index_path, 'r') as index_file:
        index = json.load(index_file)

    for file in files:
        if not os.path.isfile(file):
            print(f"File not found: {file}")
            continue
        
        with open(file, 'r') as f:
            content = f.read()
            blob_hash = hash_file_content(content)
            blob_path = f".mygit/objects/{blob_hash}"
            if not os.path.exists(blob_path):
                with open(blob_path, 'w') as b:
                    b.write(content)
            index[file] = blob_hash
    
    with open(index_path, 'w') as index_file:
        json.dump(index, index_file)
    print(f"Staged files: {', '.join(files)}")
