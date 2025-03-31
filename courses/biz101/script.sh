#!/bin/bash

# Define the folder path and the strings to search and replace
FOLDER_PATH="./"  # Change this to your folder path
OLD_STRING="https://planb.network/en/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7"
NEW_STRING="https://planb.network/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7"

# Find and replace the string in all .md files
find "$FOLDER_PATH" -type f -name "*.md" -exec sed -i "s|$OLD_STRING|$NEW_STRING|g" {} +

echo "Replacement complete."
