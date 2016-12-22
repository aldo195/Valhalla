from flask import render_template, Blueprint, json, request, Response

from . import config, generate_powershell

import boto3, uuid

app_views = Blueprint('app_views', __name__,
                      template_folder=config.TEMPLATE_FOLDER)


@app_views.route('/<path:path>')
@app_views.route('/')
def hello_world(path=None):
    return render_template('index.html', config=config)


@app_views.route('/api/generate', methods=['POST'])
def generate():
    data = json.loads(request.data)

    # Process for generating a new raid at the server:
    # Pick a random raid ID
    # Connect to database
    # Create a new object with:
    # 1. raid-id
    # 2. raid-type-id
    # 3. list of parameter name-value pairs

    raid_id = str(uuid.uuid4())

    dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="https://dynamodb.us-west-2.amazonaws.com")
    table = dynamodb.Table('raids_dev')
    response = table.put_item(
        Item={
            'raidID': raid_id,
            'raidType': data['type'],
            'path': data['path']
        }
    )

    # TODO: Handle bad response

    return raid_id


@app_views.route('/api/run', methods=['GET'])
def run():
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="https://dynamodb.us-west-2.amazonaws.com")
    table = dynamodb.Table('raids_dev')
    response = table.get_item(
        Key={
            'raidID': request.args.get('raidid')
        }
    )

    path = response['Item']['path']
    print(path)

    result = {
        'path': path
    }

    return json.dumps(result)


# Download Raid creates a powershell script containing the ID of the raid to run
@app_views.route('/download_raid', methods=['GET'])
def download_raid():

    print('download raid')

    raid_type = request.args.get('type')
    raid_id = request.args.get('id')


    # Create raid powershell script based on the type
    raid_contents = generate_powershell.ps_downloader(raid_type, raid_id)

    # Send raid script for user to download
    return Response(raid_contents, mimetype="text/plain",
                    headers={"Content-Disposition": "attachment;filename=raid.ps1"})
