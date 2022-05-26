Stopping EC2 Instances Nightly

Lambda Function
Change the Lambda function timeout high enough (i.e. 1 minute) so that it can iterate through every instance in every region.

CloudWatch Event Rule
Cron expression: 0 23 ? * MON-FRI *

The lambda function will trigger at 11:00 am UTC Mon to Fri

6:00pm EST (UTC-5) == 11:00pm (23:00) UTC