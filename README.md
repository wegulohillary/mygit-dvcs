# Simplified Git-Like DVCS

## Description
This project is a simplified distributed version control system (DVCS) similar to Git. It supports essential features such as repository initialization, file staging, commits, branches, merging, remote pushing/pulling, and cloning.

The system is implemented in Python and includes both local and networked repository management.

---

## Features
1. **Initialize a repository**: Create a new `.mygit` directory to track changes.
2. **Add files to staging**: Stage files for the next commit.
3. **Commit changes**: Commit staged changes with a message.
4. **Create and switch branches**: Manage multiple branches.
5. **Merge branches**: Merge branches with conflict detection and resolution.
6. **Push and Pull**: Synchronize repositories with a remote server over HTTP.
7. **Remote Cloning**: Clone a repository from a remote server.

---

## Software Requirements
- **Python 3.8+**
- **Flask** for remote repository support
- **Requests** for HTTP-based communication

Install dependencies using:

```bash
pip install -r requirements.txt


## Installation

 Follow the following steps to set up th\
e repository

1. Clone repository
```bash
git clone <repository_url>
cd mygit-dvcs

2. Install dependencies
```bash
pip install -r requirements.txt

3. 3. Start the Server (for remote pushing/pulling):

python mygit/server.py




---

Usage

1. Initialize a Repository

To create a new repository, run:

python main.py init


---

2. Add Files to Staging

Stage one or more files for the next commit:

python main.py add <file1> <file2> ...

Example:

python main.py add file1.txt file2.txt


---

3. Commit Changes

Commit the staged files with a message:

python main.py commit "Your commit message"

Example:

python main.py commit "Initial commit"


---

4. Create and Switch Branches

Create a new branch:

python main.py branch <branch_name>

Example:

python main.py branch feature


---

5. Merge Branches

Merge a branch into the current branch:

python main.py merge <branch_name>

Example:

python main.py merge feature

If conflicts are detected, you will be prompted to resolve them interactively.


---

6. Push to a Remote Repository

Push changes to a remote server:

1. Start the remote server:

python mygit/server.py


2. Push to the server:

python main.py push http://localhost:5000




---

7. Pull from a Remote Repository

Pull changes from a remote server:

python main.py pull http://localhost:5000


---

8. Clone a Remote Repository

Clone a repository from a remote server:

python main.py clone http://localhost:5000 /path/to/destination

Example:

python main.py clone http://localhost:5000 my_remote_repo


---

Project Structure

The project is organized as follows:

mygit-dvcs/
│
├── mygit/               # Core functionalities
│   ├── __init__.py
│   ├── init.py          # Initialize a repository
│   ├── add.py           # Stage files
│   ├── commit.py        # Commit staged changes
│   ├── branch.py        # Branch management
│   ├── merge.py         # Merge branches with conflict resolution
│   ├── rebase.py        # Rebase commits
│   ├── remote.py        # Push, pull, and remote cloning
│   ├── diff.py          # File comparison/diffs
│   ├── utils.py         # Shared utility functions
│   └── server.py        # Lightweight server for remote repository
│
├── main.py              # Entry point for CLI commands
├── requirements.txt     # Python dependencies
└── README.md            # Documentation


---

Example Workflow

1. Initialize a repository:

python main.py init


2. Add files and commit:

python main.py add file1.txt
python main.py commit "Added file1"


3. Create a branch and switch:

python main.py branch feature


4. Merge branches:

python main.py merge feature


5. Push to a remote repository:

python mygit/server.py       # Start the server
python main.py push http://localhost:5000


6. Clone a remote repository:

python main.py clone http://localhost:5000 my_clone




---

Notes

The project does not support advanced Git features like rebasing or cherry-picking but focuses on core DVCS functionalities.

Conflict resolution is handled interactively during merges.



---

Author

[Your Name]
[Your Contact Information]


---

License

This project is licensed under the MIT License.


