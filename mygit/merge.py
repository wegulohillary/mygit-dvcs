from mygit.utils import three_way_merge_with_resolution

def merge(branch_name):
    target_branch_path = f".mygit/refs/{branch_name}"
    if not os.path.exists(target_branch_path):
        print(f"Branch '{branch_name}' does not exist.")
        return
    
    with open(target_branch_path, 'r') as f:
        target_commit = f.read().strip()

    print(f"Merging branch '{branch_name}'...")
    # Assume merge conflicts are handled interactively
    three_way_merge_with_resolution(target_commit)
