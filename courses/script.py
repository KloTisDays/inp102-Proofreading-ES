#!/usr/bin/env python3
import os
import re

def find_and_fix_missing_explanations(root_dir):
    """
    Recursively searches through all .yml files in the directory structure and
    adds 'explanation: |' if it's missing.
    """
    fixed_files = 0
    scanned_files = 0
    skipped_files = 0
    
    # Walk through the directory structure
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Filter for yml files
        for filename in [f for f in filenames if f.endswith('.yml')]:
            # Skip files named "question.yml"
            if filename == "question.yml":
                skipped_files += 1
                print(f"Skipping question.yml file: {os.path.join(dirpath, filename)}")
                continue
                
            file_path = os.path.join(dirpath, filename)
            scanned_files += 1
            
            # Read the file content
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Skip if any kind of explanation field is already present
            # This regex matches "explanation:" followed by any character until the end of line
            if re.search(r'explanation:.*$', content, re.MULTILINE):
                skipped_files += 1
                print(f"Skipping file with existing explanation: {file_path}")
                continue
            
            # Check if explanation is missing
            # At this point we know there's no "explanation:" in the file
            # Check if there's a "reviewed: false" line
            if "reviewed: false" in content:
                # Replace "reviewed: false" with "explanation: |\n\nreviewed: false"
                new_content = content.replace("reviewed: false", "explanation: |\n\nreviewed: false")
                
                # Write the updated content back to the file
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                
                fixed_files += 1
                print(f"Fixed file: {file_path}")
            elif "wrong_answers:" in content:
                # If there's a "wrong_answers:" section but no "reviewed: false",
                # look for the end of the wrong_answers section and add explanation after it
                lines = content.split('\n')
                new_lines = []
                wrong_answers_found = False
                
                for i, line in enumerate(lines):
                    new_lines.append(line)
                    
                    if line.strip() == "wrong_answers:":
                        wrong_answers_found = True
                    elif wrong_answers_found and line.strip().startswith("- "):
                        # Still in wrong_answers section
                        continue
                    elif wrong_answers_found and not line.strip().startswith("- "):
                        # First line after wrong_answers section
                        wrong_answers_found = False
                        if i < len(lines) - 1:
                            new_lines.append("explanation: |")
                            fixed_files += 1
                            print(f"Fixed file by adding after wrong_answers: {file_path}")
                
                # Write the updated content back to the file
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write('\n'.join(new_lines))
    
    return scanned_files, fixed_files, skipped_files

if __name__ == "__main__":
    # Current directory as the root
    root_directory = os.getcwd()
    
    print(f"Starting to scan for .yml files in: {root_directory}")
    print("Looking for files missing 'explanation:'")
    
    scanned, fixed, skipped = find_and_fix_missing_explanations(root_directory)
    
    print(f"\nSummary:")
    print(f"Files scanned: {scanned}")
    print(f"Files fixed: {fixed}")
    print(f"Files skipped: {skipped}")
    if fixed == 0:
        print("No files needed fixing!")
    else:
        print("All missing 'explanation: |' lines have been added!")