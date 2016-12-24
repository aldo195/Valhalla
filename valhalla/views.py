from flask import render_template, Blueprint, json, request, Response

from . import config, generate_powershell
from random import randint
import boto3, uuid, time

app_views = Blueprint('app_views', __name__,
                      template_folder=config.TEMPLATE_FOLDER)


@app_views.route('/<path:path>')
@app_views.route('/')
def hello_world(path=None):
    return render_template('index.html', config=config)


@app_views.route('/api/generate', methods=['POST'])
def generate():
    data = json.loads(request.data)

    raid_type = data['type']

    # Generate unique Raid identifier
    raid_id = str(uuid.uuid4())

    # Generate the Raid's trophy code
    trophy = str(randint(100000, 999999))

    # Record raid start time
    start_time = str(time.time())

    dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="https://dynamodb.us-west-2.amazonaws.com")
    table = dynamodb.Table('raids_dev')
    response = table.put_item(
        Item={
            'raidID': raid_id,
            'startTime': start_time,
            'endTime': '0',
            'elapsedTime': 0,
            'trophy': trophy,
            'raidType': raid_type
        }
    )

    # TODO: Handle bad response

    result = {
            'raid_id': raid_id,
            'raid_type': raid_type,
            'trophy': trophy
    }

    return json.dumps(result)



@app_views.route('/api/finish', methods=['POST'])
def finish():
    data = json.loads(request.data)

    # Get parameter values from POST request
    raid_id = data['raidId']
    posted_trophy = data['trophy']


    # Get raid values from database
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="https://dynamodb.us-west-2.amazonaws.com")
    table = dynamodb.Table('raids_dev')
    response = table.get_item(
        Key={
            'raidID': raid_id
        }
    )
    start_time = str(response['Item']['startTime'])
    elapsed_time = str(response['Item']['elapsedTime'])
    raid_trophy = str(response['Item']['trophy'])

    if elapsed_time != '0':
        return str(elapsed_time)
    elif posted_trophy != raid_trophy:
        # The user did not provide the right trophy value, do not end the raid
        return '0'
    else:
        # Calculate how long the raid lasted
        end_time = str(time.time())
        elapsed_time = str(int(float(end_time) - float(start_time)))

        response = table.update_item(
            Key={
                'raidID': raid_id
            },
            UpdateExpression="set endTime = :t, elapsedTime = :e",
            ExpressionAttributeValues={
                ':t': end_time,
                ':e': elapsed_time
            }
        )
        # TODO: Handle bad response

        return elapsed_time


@app_views.route('/api/run', methods=['GET'])
def run():
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="https://dynamodb.us-west-2.amazonaws.com")
    table = dynamodb.Table('raids_dev')
    response = table.get_item(
        Key={
            'raidID': request.args.get('raidid')
        }
    )

    print(response)

    trophy = response['Item']['trophy']

    result = {
        "trophy": trophy
    }

    return json.dumps(result)


# Download Raid creates a powershell script containing the ID of the raid to run
@app_views.route('/download_raid', methods=['GET'])
def download_raid():

    raid_type = request.args.get('type')
    raid_id = request.args.get('id')
    trophy = request.args.get('trophy')

    # Create raid powershell script based on the type
    raid_contents = generate_powershell.ps_downloader(raid_type, raid_id, trophy)

    # Send raid script for user to download
    return Response(raid_contents, mimetype="text/plain",
                    headers={"Content-Disposition": "attachment;filename=raid.ps1"})
