import sys
from mygit.init import init
from mygit.add import add
from mygit.commit import commit
from mygit.branch import branch
from mygit.merge import merge

if len(sys.argv) < 2:
    print("Usage: python main.py <command> [args]")
    sys.exit(1)

command = sys.argv[1]
if command == "init":
    init()
elif command == "add":
    add(sys.argv[2:])
elif command == "commit":
    commit(sys.argv[2])
elif command == "branch":
    branch(sys.argv[2])
elif command == "merge":
    merge(sys.argv[2])
else:
    print(f"Unknown command: {command}")
