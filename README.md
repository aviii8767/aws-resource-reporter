# aws-resource-reporter
> A fully serverless AWS automation project that generates and emails daily cloud infrastructure reports using AWS Lambda, Boto3, EventBridge, Amazon SES, and CloudWatch.

![AWS](https://img.shields.io/badge/AWS-Lambda%20%7C%20SES%20%7C%20EventBridge-orange)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Boto3](https://img.shields.io/badge/Boto3-AWS%20SDK-yellow)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📖 Overview

Monitoring AWS resources manually every day can be repetitive and time-consuming. This project automates the process by collecting information about AWS resources and sending a daily infrastructure report via email.

Using an event-driven, serverless architecture, the solution eliminates the need for EC2 instances, cron jobs, or manual intervention while remaining within the AWS Free Tier under normal usage.

---

## ✨ Features

- Fully serverless architecture
- Automated daily execution using Amazon EventBridge
- Collects EC2, S3, and IAM resource information
- Sends formatted email reports using Amazon SES
- Implements least-privilege IAM permissions
- CloudWatch logging for monitoring and troubleshooting
- Runs within AWS Free Tier under normal usage

---

## 🏗️ Architecture

```
               Amazon EventBridge
                       │
                       ▼
                 AWS Lambda
                       │
               Python + Boto3
          ┌────────┼─────────┐
          ▼        ▼         ▼
        EC2       S3        IAM
          │
          ▼
      Report Generator
          │
          ▼
       Amazon SES
          │
          ▼
      Email Notification

      CloudWatch Logs
          ▲
          │
      Lambda Execution
```

---

## ⚙️ Workflow

1. Amazon EventBridge triggers the Lambda function on a daily schedule.
2. Lambda uses Boto3 to retrieve AWS resource information.
3. Resource data is formatted into a readable report.
4. Amazon SES sends the report to the configured email address.
5. CloudWatch Logs capture execution details for monitoring.

---

## 🛠️ Tech Stack

| Service | Purpose |
|----------|---------|
| AWS Lambda | Serverless compute |
| Python 3.12 | Application logic |
| Boto3 | AWS SDK |
| Amazon EventBridge | Scheduled execution |
| Amazon SES | Email delivery |
| IAM | Least-privilege access control |
| CloudWatch Logs | Monitoring & logging |

---

## 🔒 Security

The solution follows the **Principle of Least Privilege**.

### AWS Managed Policies

- AmazonEC2ReadOnlyAccess
- AmazonS3ReadOnlyAccess
- IAMReadOnlyAccess
- AWSLambdaBasicExecutionRole

### Custom Inline Policy

Permissions:

- ses:SendEmail
- ses:SendRawEmail

No write, update, or delete permissions are granted for AWS resources.

---

## 📧 Sample Report

```
AWS Daily Cloud Report

EC2 INSTANCES
------------------------------------
i-0123456789 | Running | t2.micro

S3 BUCKETS
------------------------------------
my-project-bucket

IAM USERS
------------------------------------
admin-user      MFA Enabled
developer-user  MFA Disabled
```

---

## 🚀 Deployment

1. Create an IAM execution role.
2. Attach the required read-only policies.
3. Add a custom SES send-email policy.
4. Verify the email identity in Amazon SES.
5. Deploy the Lambda function.
6. Configure an EventBridge scheduled trigger.
7. Test the function and verify CloudWatch logs.

---

## 📂 Project Structure

```
automated-aws-resource-reporter/
│
├── lambda_function.py
├── requirements.txt
├── README.md
├── architecture.png
└── screenshots/
```

---

## 📸 Screenshots

Add screenshots of:

- Lambda Function
- EventBridge Scheduler
- IAM Role
- SES Verified Identity
- CloudWatch Logs
- Email Output

---

## 💰 Cost

This project operates within the **AWS Free Tier** under normal usage.

| Service | Usage |
|----------|-------|
| Lambda | ~30 executions/month |
| EventBridge | ~30 scheduled events/month |
| Amazon SES | ~30 emails/month |
| CloudWatch Logs | Minimal log storage |

Estimated monthly cost:

**≈ $0 (within Free Tier limits)**

---

## 💡 Challenges

- Designing least-privilege IAM permissions
- Configuring Amazon SES verified identities
- Scheduling Lambda using EventBridge
- Formatting multi-service AWS reports
- Monitoring execution with CloudWatch Logs

---

## 🔮 Future Improvements

- Export reports as PDF
- Store historical reports in Amazon S3
- Integrate AWS Cost Explorer
- Slack / Microsoft Teams notifications
- Multi-account AWS monitoring
- Security alerts for non-MFA IAM users

---

## 🎯 Skills Demonstrated

- AWS Lambda
- Amazon EventBridge
- Amazon SES
- IAM
- Boto3
- CloudWatch
- Serverless Architecture
- Cloud Automation
- Infrastructure Monitoring
- Least Privilege Security

---

## 📈 Key Outcomes

- 100% Serverless
- Fully Automated
- Event-Driven Architecture
- Secure by Design
- AWS Free Tier Friendly
- Production-style AWS Architecture

---

## 👨‍💻 Author

**Avishkar Purushottam Gaware**

AWS Certified Cloud Practitioner (CLF-C02)

B.E. Electronics & Telecommunication Engineering (2026)

📧 gawareavishkar2004@gmail.com

🔗 LinkedIn: https://linkedin.com/in/avishkar-gaware/
