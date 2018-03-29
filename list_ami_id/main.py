import json
import list_ami_id


PREFIX = 'kong'
VERSION = '0.12'
OWNERS = ['aws-marketplace']
filters = [
        {
            'Name': 'state',
            'Values': [
                'available',
            ]
        },
        {
            'Name': 'name',
            'Values': [
                PREFIX + '-' + VERSION + '*',
            ]
        },
        {
            'Name': 'architecture',
            'Values': [
                'x86_64',
            ]
        },
        {
            'Name': 'virtualization-type',
            'Values': [
                'hvm',
            ]
        },
        {
            'Name': 'root-device-type',
            'Values': [
                'ebs',
            ]
        },
        ]


def main():
    regions = list_ami_id.get_regions()
    # regions = ['ap-northeast-1', 'us-west-2']
    ami_dict = {'ami': []}
    for region in regions:
        ami_dict.get('ami').append({
            'region': region,
            'images': list_ami_id.get_ami_id(region, filters, OWNERS)
            })
        # print(ami_dict)
    print(json.dumps(ami_dict, indent=4))


if __name__ == "__main__":
    main()
