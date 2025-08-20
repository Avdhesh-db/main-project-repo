#!/usr/bin/env python3
"""
Main Databricks workflow file demonstrating cross-repository imports.

This file imports functions from the utils-repo and demonstrates modular 
project structure in Databricks workflows.

Instructions for Databricks:
1. Add both repositories as Git folders in your Databricks workspace
2. Ensure both repos are in the same parent directory or adjust the import path
3. Run this file as a Databricks notebook or workflow
"""

import sys
import os

# Add the utils-repo to the Python path for importing
# In Databricks, adjust this path based on where your git folders are located
# Example: If both repos are in /Workspace/Repos/your_username/
# then the path would be /Workspace/Repos/your_username/utils-repo
utils_repo_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'utils-repo')
if os.path.exists(utils_repo_path):
    sys.path.append(utils_repo_path)
    print(f"✅ Added utils-repo to Python path: {utils_repo_path}")
else:
    print(f"⚠️  Utils repo not found at: {utils_repo_path}")
    print("Please adjust the path based on your Databricks git folder structure")

try:
    # Import functions from the utils repository
    from message_utils import get_greeting_message, say_goodbye
    
    def main():
        """Main function demonstrating cross-repo imports in Databricks."""
        
        print("=== Databricks Modular Project Demo ===\n")
        
        # Using the imported function from utils-repo
        message1 = get_greeting_message()
        print(message1)
        
        # Using the imported function with a custom name
        message2 = get_greeting_message("Data Engineer")
        print(message2)
        
        # Using the second imported function
        goodbye_message = say_goodbye("Databricks User")
        print(goodbye_message)
        
        print(f"\n✅ Successfully demonstrated cross-repository imports!")
        print(f"📁 Utils repo location: {utils_repo_path}")
        print(f"📁 Main repo location: {os.path.dirname(os.path.abspath(__file__))}")
    
    if __name__ == "__main__":
        main()
        
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("\nTroubleshooting:")
    print("1. Ensure both git repositories are added to your Databricks workspace")
    print("2. Verify the path to utils-repo is correct")
    print("3. Check that message_utils.py exists in the utils-repo")
    print(f"4. Current Python path includes: {sys.path[:3]}...")
