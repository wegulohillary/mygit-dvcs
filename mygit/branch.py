from mygit.utils import get_current_commit

def branch(branch_name):
    if not os.path.exists('.mygit'):
        print("Not a repository. Run 'init' first.")
        return
    
    current_commit = get_current_commit()
    with open(f".mygit/refs/{branch_name}", 'w') as branch_file:
        branch_file.write(current_commit)
    print(f"Created branch '{branch_name}' at commit {current_commit}")
