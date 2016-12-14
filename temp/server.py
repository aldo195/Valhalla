MOCK_RAID_ID = 1337
RAID_FILE_LOCATION = r'C:\Users\Omer\Documents\Valhalla\raid.ps1'
EICAR_SOURCE = 'http://ec2-35-165-51-220.us-west-2.compute.amazonaws.com/eicar.com'

from flask import Flask, jsonify, abort

from valhalla.generate_powershell import ps_downloader

app = Flask(__name__)

raids = [
    {
        'id': 33,
        'type': 3
    }
]


@app.route('/')
def hello_world():
    return 'Hello, World!!!'


@app.route('/raids/<int:raid_id>', methods=['GET'])
def get_raid(raid_id):
    print('TESTING: ', raids)
    raid = [raid for raid in raids if raid['id'] == raid_id]
    if len(raid) == 0:
        abort(404)
    return jsonify({'raid': raid[0]})


if __name__ == "__main__":

    # Have the user choose a raid type
    response = 1
    while response < 1:
        print('CREATE A NEW RAID')
        print('How Long Until My Security Team Notices:')
        print('1. An antivirus detecting malware on a server')
        print('2. More to come...')
        response = int(input('Select Raid: '))

    # Prepare the raid file based on the user's selection
    if response == 1:
        raid_type = 1

        print('You want to measure how long until your security team notices that antivirus on a server detected malware.')
        target_dir = input('Choose target directory for dummy malware: ')


        # TODO: validate and create new raid in DB along with values
        raid_id = MOCK_RAID_ID

        raids.append({'id': raid_id,
                      'type': raid_type,
                      'target_dir': target_dir})
        print('New raid prepared successfully!')
        print('Raid ID: ', raid_id)

        raid_ps = ps_downloader(raid_id, EICAR_SOURCE)

        raid_file = open(RAID_FILE_LOCATION, 'w')
        raid_file.write(raid_ps)
        raid_file.close()
    else:
        print('Selected raid is not supported.')

    print(raids)
    app.run()