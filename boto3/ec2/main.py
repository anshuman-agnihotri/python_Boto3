import boto3

# Function to get all available regions for EC2
def get_ec2_regions():
    ec2_client = boto3.client('ec2', region_name='ap-south-1')  # You can use any region to get the available regions
    regions = ec2_client.describe_regions()
    return [region['RegionName'] for region in regions['Regions']]

# Function to print all EC2 instances in a given region
def print_ec2_instances(region):
    ec2_client = boto3.client('ec2', region_name=region)
    response = ec2_client.describe_instances()
    
    print(f"\nInstances in region: {region}")
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance.get('InstanceId')
            instance_type = instance.get('InstanceType')
            state = instance.get('State'ec2_client, {}).get('Name')
            public_ip = instance.get('PublicIpAddress', 'N/A')
            private_ip = instance.get('PrivateIpAddress', 'N/A')
            
            print(f"Instance ID: {instance_id}")
            print(f"  Instance Type: {instance_type}")
            print(f"  State: {state}")
            print(f"  Public IP: {public_ip}")
            print(f"  Private IP: {private_ip}")
            print("-" * 40)  # Separator for readability

# Main logic to print instances in all regions
if __name__ == "__main__":
    all_regions = get_ec2_regions()
    for region in all_regions:
        print_ec2_instances(region)
