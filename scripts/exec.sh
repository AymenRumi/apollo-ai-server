
#!/bin/bash
if [ $# -eq 0 ]; then
    echo "Please provide project name"
    exit 1
fi

PROJECT_NAME="$1"

pyinstaller --name $PROJECT_NAME --onefile server.py
pyinstaller "$PROJECT_NAME.spec"
