#!/bin/bash

# Directory containing the request JSON files
REQUEST_DIR="./requests"

# Array of filenames
FILES=("create.json" "update.json" "delete.json")

# Loop through each file and send its contents
for FILE in "${FILES[@]}"; do
    echo "Processing $FILE..."

    # Read the content of the JSON file
    JSON=$(cat "${REQUEST_DIR}/${FILE}")

    # Extract hostname and port from URL inside the JSON (you'll need to adjust this part)
    # HOST=$(echo "$JSON" | grep -oP '(?<="url":\s?"https://)[^/]+')
    HOST=$(echo "$JSON" | jq -r '.url' | grep -oP 'https?://\K[^/]+')
    PORT=80  # Standard HTTP port

    # Send the JSON object
    echo "$JSON" | socat - TCP:$HOST:$PORT

    echo -e "\n$FILE processed.\n"
done
