
# DevOps Repository

This repository contains DevOps utilities and tools, including AWS Lambda functions to manage EC2 instances based on tags.

## Contents
- `lambda-functions/`: Contains Lambda function code and dependencies.
  - `start_instance/`: Lambda function to start EC2 instances with specific tags.
  - `stop_instance/`: Lambda function to stop EC2 instances with specific tags.
- `docs/`: Documentation, including setup instructions and permissions.

## Getting Started

### Prerequisites
- AWS account with EC2 permissions.
- Python 3.x installed locally for testing.

### Deploying Lambda Functions
1. Navigate to the respective Lambda folder (e.g., `lambda-functions/start_instance/`).
2. Follow the instructions in the function's `README.md` file.


## License
This repository is licensed under the MIT License.
