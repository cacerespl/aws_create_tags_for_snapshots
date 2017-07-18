import boto3
from boto.ec2 import connect_to_region

#Variables passed as arguments
account_id = sys.argv[1]
department1 = sys.argv[2]
region1 = sys.argv[3]


def create_tags(department, region):
    
    """
    
    This function create tags for snapshots already created, the description of the snapshot should 
    include the name of the Department and the retention policy (Daily or Monthly).
    If the description of the snapshot include word Montly will create a tag with Retention = Monthly
    If the description of the snapshot include word Daily will create a tag with Retention = Daily
    Arguments: Department and AWS Region 
    """

    ec2 = boto3.resource('ec2', region_name=region)
    snapshot = ec2.Snapshot('id')
    conn = connect_to_region(region)
    describe = ['Monthly-', 'Daily-']
    for i in describe:
        desc = i + department
        if i == 'Monthly-':
            filters = { 'description':'*'+desc+'*'}
            monthly_snapshots = conn.get_all_snapshots(owner=account_id,filters=filters )
            num_mothly_snapshots = len(monthly_snapshots)
            print 'There are '+str(num_monthly_snaphots)+' Monthly Backups for '+department+' in Region '+region
            for i in range(num_monthly_snapshots):
                snap = z[i].id
                ec2.create_tags(Resources=[snap,], Tags=[ {'Key': 'Department', 'Value': department},])
                ec2.create_tags(Resources=[snap,], Tags=[ {'Key': 'Retention', 'Value': 'Monthly'},])
        elif i == 'Daily-':
            filters = { 'description':'*'+desc+'*'}
            daily_snapshots = conn.get_all_snapshots(owner=account_id,filters=filters )
            num_daily_snapshots = len(daily_snapshots)
            print 'There are '+str(num_saily_snapshots)+' Daily Backups for '+description+' in Region '+region
            for i in range(num_daily_snapshots):
                snap = daily_snaphots[i].id
                ec2.create_tags(Resources=[snap,], Tags=[ {'Key': 'Department', 'Value': department},])
                ec2.create_tags(Resources=[snap,], Tags=[ {'Key': 'Retention', 'Value': 'Daily'},])
 

create_tags(department1, region1)

