🚀 AWS Lambda Automation

Automating AWS resource management with Lambda functions written in Python. This repository demonstrates how to manage EC2 and RDS instances efficiently, optimize costs, and send notifications using Amazon SES.

🛠 Key Features
Start EC2 Instances: Automatically starts EC2 instances tagged with Environment=dev that are in the stopped state.
Stop EC2 Instances: Automatically stops EC2 instances tagged with Environment=dev that are in the running state.
AWS Resource Alerts: Monitors running EC2 and available RDS instances, sending email alerts via Amazon SES.

⚙️ Lambda Functions
1. Start EC2 Instances
📍 Location: lambda-functions/start_instance.py
Automatically starts all stopped EC2 instances tagged with Environment=dev.

2. Stop EC2 Instances
📍 Location: lambda-functions/stop_instance.py
Automatically stops all running EC2 instances tagged with Environment=dev.

3. AWS Resource Alerts
📍 Location: lambda-functions/alert_resources.py
Monitors running EC2 instances and available RDS instances across all AWS regions and sends a detailed email alert.

📋 How to Use

1. IAM Role Setup
Create an IAM role with the following permissions:

AmazonEC2ReadOnlyAccess
AmazonRDSReadOnlyAccess
AmazonSESFullAccess
AWSLambdaBasicExecutionRole


2. Deploy Lambda Functions
Go to the AWS Management Console.
Create a Lambda function for each script.
Upload the respective .py file and attach the IAM role.

4. Automate Execution
Use CloudWatch to schedule automated Lambda function execution:

Go to CloudWatch > Rules > Create Rule.
Set the event source to a recurring schedule (cron expression).
Set the target to the respective Lambda function.

📊 Examples
1. EC2 Instance Management
   
Start Function Output:
Started instances: ['i-1234567890abcdef']

Stop Function Output:
Stopped instances: ['i-0987654321fedcba']


3. AWS Resource Alerts
Sample Email Sent:

Subject: AWS Resources

Dear Team,

Below is a list of the current instances and RDS available in various regions. 
If any of these instances are not actively in use, please proceed to turn them off. 
This action will contribute to cost savings and help maintain an efficient AWS environment.

Running EC2 Instances:
Region: us-east-1, Instance ID: i-1234567890abcdef

Available RDS Instances:
Region: us-west-2, Instance ID: rds-instance-1, Status: available

Sincerely, 
Cloud Team

🔗 Useful Links
AWS Lambda Documentation: AWS Lambda Docs
Amazon SES Setup: Amazon SES Docs

📜 License
This project is licensed under the MIT License.

📧 Contact
If you have any questions or would like to connect, feel free to reach out:

Email: krishnaveniganesan22@gmail.com
LinkedIn: https://www.linkedin.com/in/krishnaveni-ganesan-710640207/
