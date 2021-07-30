def lambda_handler(event, context):
    import boto3
    from botocore.exceptions import ClientError
    client = boto3.client('elbv2')
    response = response = client.modify_listener(
        ListenerArn='<copy Listener ARN from loadbalancer>',
        Protocol='HTTPS',
        DefaultActions=[
            {
            'Type': 'forward',
            'ForwardConfig': {
                'TargetGroups': [
                    {
                    'TargetGroupArn': '<copy Target group ARN from target groups of live webapplication>' 
                    }
                ]
            }

            }
            ]
    )
        
