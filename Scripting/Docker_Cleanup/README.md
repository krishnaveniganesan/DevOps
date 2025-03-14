🚀 Docker Cleanup Script

A simple and efficient shell script to clean up specific Docker containers and images by name or pattern. This script is helpful for managing and freeing up resources in your Docker environment.

✨ Features
🗑️ Remove Specific Containers: Deletes containers with names matching nginx.
🧹 Remove Specific Images: Deletes Docker images with names starting with ngi or ngin.

📜 Script Overview

The script performs two main tasks:
Container Cleanup:
🟢 Checks for containers with the name nginx and removes them forcefully if they exist.

Image Cleanup:
🔵 Identifies images with names matching patterns ngi* or ngin* and removes them.

🛠️ How to Use
✅ Prerequisites
🐳 Docker must be installed and running on your system.
🔒 You need sudo privileges or permission to execute Docker commands.

🏁 Steps to Run
Clone the Repository:
git clone <repository-url>
cd <repository-directory>

Make the Script Executable:
chmod +x cleanup.sh
Run the Script:

./cleanup.sh

⚠️ Notes
Pattern Matching:
The script uses patterns (ngi* and ngin*) to match container and image names. Modify these patterns in the script if needed to fit your use case.

Force Removal:
The -f option in docker rm and docker rmi ensures forceful deletion. Be cautious when using this script, as it will remove matching containers and images without confirmation.


📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
