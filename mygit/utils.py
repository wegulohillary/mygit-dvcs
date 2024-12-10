def get_current_commit():
    with open('.mygit/HEAD', 'r') as head:
        ref = head.read().strip()
    ref_path = f".mygit/{ref}"
    if os.path.exists(ref_path):
        with open(ref_path, 'r') as commit_file:
            return commit_file.read().strip()
    return None

def set_current_commit(commit_hash):
    with open('.mygit/HEAD', 'w') as head:
        head.write(commit_hash)
