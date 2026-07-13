import boto3
from datetime import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    s3 = boto3.client('s3')
    iam = boto3.client('iam')
    ses = boto3.client('ses')

    report_lines = []
    report_lines.append(f"AWS Daily Cloud Report - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report_lines.append("=" * 50)

    # ---- EC2 ----
    report_lines.append("\nEC2 INSTANCES")
    report_lines.append("-" * 30)
    instances = ec2.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            itype = instance['InstanceType']
            launch_time = instance['LaunchTime'].strftime('%Y-%m-%d %H:%M')
            report_lines.append(f"ID: {instance_id} | State: {state} | Type: {itype} | Launched: {launch_time}")

    if not instances['Reservations']:
        report_lines.append("No EC2 instances found.")

    # ---- S3 ----
    report_lines.append("\nS3 BUCKETS")
    report_lines.append("-" * 30)
    buckets = s3.list_buckets()
    for bucket in buckets['Buckets']:
        name = bucket['Name']
        created = bucket['CreationDate'].strftime('%Y-%m-%d')
        report_lines.append(f"Name: {name} | Created: {created}")

    if not buckets['Buckets']:
        report_lines.append("No S3 buckets found.")

    # ---- IAM ----
    report_lines.append("\nIAM USERS - MFA STATUS")
    report_lines.append("-" * 30)
    users = iam.list_users()
    for user in users['Users']:
        username = user['UserName']
        mfa_devices = iam.list_mfa_devices(UserName=username)
        mfa_status = "Enabled" if mfa_devices['MFADevices'] else "DISABLED"
        report_lines.append(f"User: {username} | MFA: {mfa_status}")

    if not users['Users']:
        report_lines.append("No IAM users found.")

    report_body = "\n".join(report_lines)

    # ---- Send via SES ----
    sender = "gawareavishkar2004@gmail.com"
    recipient = "gawareavishkar2004@gmail.com"

    ses.send_email(
        Source=sender,
        Destination={'ToAddresses': [recipient]},
        Message={
            'Subject': {'Data': f"AWS Daily Cloud Report - {datetime.now().strftime('%Y-%m-%d')}"},
            'Body': {'Text': {'Data': report_body}}
        }
    )

    return {
        'statusCode': 200,
        'body': 'Report sent successfully'
    }
