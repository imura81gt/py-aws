import boto3


def get_regions():
    regions = []
    ec2 = boto3.client('ec2')
    describe_regions = ec2.describe_regions()

    for region in describe_regions.get('Regions'):
        regions.append(region.get('RegionName'))

    return regions


def get_ami_id(region, filters, owners):
    ec2 = boto3.client('ec2', region)
    images = ec2.describe_images(Filters=filters, Owners=owners)
    images = images.get('Images')
    ret = {}
    for image in images:
        name = image.get('Name')
        ret[name] = image.get('ImageId')
        # ret.append(image.get('ImageId'))
    return ret
