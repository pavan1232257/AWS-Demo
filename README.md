What is AWS S3?

Amazon Simple Storage Service (S3) is a scalable, highly durable, and secure object storage service designed for storing and retrieving any amount of data from anywhere. It is commonly used for backup, data storage, hosting static websites, and data archiving.

<img width="468" alt="image" src="https://github.com/user-attachments/assets/d052ec35-5919-45d1-9381-91b37e17f02c" />

What is AWS S3?
Amazon Simple Storage Service (S3) is a scalable, highly durable, and secure object storage service designed for storing and retrieving any amount of data from anywhere. It is commonly used for backup, data storage, hosting static websites, and data archiving.

Key Features of AWS S3
1️⃣ Scalability
Automatically scales to store unlimited data.
No upfront cost; you pay only for what you use.
2️⃣ Durability & Availability
99.999999999% (11 9’s) durability, meaning data is replicated across multiple facilities.
High availability with multiple redundancy mechanisms.
3️⃣ Security & Access Control
Supports encryption (SSE-S3, SSE-KMS, SSE-C) for data protection.
Fine-grained access control using IAM policies, ACLs, and Bucket Policies.
4️⃣ Storage Classes (Cost Optimization)
AWS S3 provides different storage classes for cost savings:

Storage Class	Use Case	Cost	Durability
S3 Standard	Frequently accessed data	High	11 9’s
S3 Intelligent-Tiering	Automatically moves data between storage classes	Medium	11 9’s
S3 Standard-IA (Infrequent Access)	Long-lived, less-accessed data	Lower	11 9’s
S3 One Zone-IA	Lower-cost, non-mission-critical data	Lower	11 9’s (Single AZ)
S3 Glacier	Archive storage, retrieval in minutes to hours	Very Low	11 9’s
S3 Glacier Deep Archive	Long-term archival (retrieval in hours)	Lowest	11 9’s
5️⃣ Versioning & Lifecycle Policies
Versioning: Keep multiple versions of an object to prevent accidental deletion.
Lifecycle Policies: Automate moving objects between storage classes or set automatic expiration.
6️⃣ S3 Object Lock & Compliance
Object Lock prevents objects from being deleted or modified for a specified period.
Useful for compliance & regulatory requirements.
How Does AWS S3 Work?
1️⃣ Create a Bucket → A container where objects are stored. Each bucket has a unique name globally.
2️⃣ Upload Objects → Store files as objects with metadata and unique keys (file names).
3️⃣ Set Permissions → Define access control using IAM policies, ACLs, or bucket policies.
4️⃣ Access Objects → Use the AWS console, CLI, SDKs, or REST APIs to retrieve data.

Common AWS S3 Use Cases
✅ Backup & Disaster Recovery – Store backups securely with versioning and cross-region replication.
✅ Big Data Analytics – Store large datasets for data processing with AWS services like Athena & Redshift.
✅ Static Website Hosting – Host HTML, CSS, and JavaScript files directly from an S3 bucket.
✅ Content Delivery (CDN Integration) – Integrate with AWS CloudFront to serve data globally with low latency.
✅ Machine Learning Data Storage – Store training datasets for ML models.
✅ IoT Data Storage – Capture and store IoT sensor data in S3 buckets.

<img width="468" alt="image" src="https://github.com/user-attachments/assets/708373d3-aad0-4104-aded-90cf2cf38dca" />

Aws upload a file using command line

brew install awscli  # macOS
Configure AWS CLI
aws configure
aws s3 cp local-file.txt s3://your-bucket-name/

<img width="468" alt="image" src="https://github.com/user-attachments/assets/bfb07e32-b59b-4aa0-a362-5cfe1d22ae66" />
Aws upload a file using command line

brew install awscli  # macOS
Configure AWS CLI
aws configure
aws s3 cp local-file.txt s3://your-bucket-name/
![image](https://github.com/user-attachments/assets/5c51f4a0-03dd-43e2-8ec1-30a11ec42089)



WHAT IS IAM
AWS Identity and Access Management (IAM) allows you to securely manage access to AWS services and resources.
It helps in controlling who can do what in your AWS account.


![image](https://github.com/user-attachments/assets/5ea7cc3e-ae92-40f8-80e0-f3a9a70ea50c)

Access keys (1)
Create access key
Use access keys to send programmatic calls to AWS from the AWS CLI, AWS Tools for PowerShell, AWS SDKs, or direct AWS API calls. You can have a maximum of two access keys (active or inactive) at a time.

<img width="1467" alt="Screenshot 2025-02-17 at 6 40 24 PM" src="https://github.com/user-attachments/assets/b796dfab-d43c-490c-9e42-1dd2b0d1779d" />

An instance profile is a container for an AWS Identity and Access Management (IAM) role that you can use to pass role information to an Amazon EC2 instance when the instance starts.

you're referring to AWS Identity and Access Management (IAM), which is a service that helps you securely control access to AWS resources. I can use IAM to:

Create and manage AWS users and groups: This allows you to control who can access AWS resources.
Grant permissions to users: By creating IAM policies, you can grant fine-grained access control to specific AWS resources.
Enable multi-factor authentication (MFA): Enhance security by requiring users to provide two forms of authentication.

Use roles: Roles allow you to delegate access to users or services without sharing long-term credentials.
If you're just getting started, some key concepts are:

Users: Entities that represent a person or application that interacts with AWS resources.
Groups: A collection of IAM users that are managed together, typically for applying common permissions.
Roles: Temporary security credentials for users or services that need to assume a role to gain access to resources.
Policies: JSON documents that define permissions. Policies can be attached to users, groups, or roles.
Access Keys: Used for programmatic access to AWS services (CLI, SDKs, etc.)









