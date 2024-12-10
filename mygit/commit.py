import json
import time
from mygit.utils import get_current_commit, set_current_commit

def commit(message):
    if not os.path.exists('.mygit'):
        print("Not a repository. Run 'init' first.")
        return
    
    index_path = '.mygit/index'
    if not os.path.exists(index_path) or os.stat(index_path).st_size == 0:
        print("No files staged for commit.")
        return

    with open(index_path, 'r') as index_file:
        index = json.load(index_file)

    commit_data = {
        'parent': get_current_commit(),
        'timestamp': int(time.time()),
        'message': message,
        'files': index
    }
    commit_hash = hashlib.sha1(json.dumps(commit_data).encode()).hexdigest()
    
    with open(f".mygit/objects/{commit_hash}", 'w') as commit_file:
        json.dump(commit_data, commit_file)
    
    set_current_commit(commit_hash)
    with open(index_path, 'w') as index_file:
        json.dump({}, index_file)  # Clear staging area
    
    print(f"Committed changes: {commit_hash}")
