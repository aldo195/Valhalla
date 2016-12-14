from flask import render_template, Blueprint, json, request, Response

from . import config, generate_powershell

app_views = Blueprint('app_views', __name__,
                      template_folder=config.TEMPLATE_FOLDER)


@app_views.route('/<path:path>')
@app_views.route('/')
def hello_world(path=None):
    return render_template('index.html', config=config)


@app_views.route('/api/search', methods=['POST'])
def search():
    data = json.loads(request.data)
    term = data['q']

    raid_db = [
        {
            'id': '101',
            'param': 'Target Location'
        },
        {
            'id': '102',
            'param': 'Target Location'
        },
        {
            'id': '103',
            'param': 'Target IP Address'
        }
    ]

    if term != '':
        for raid in raid_db:
            if raid['id'] == term:
                result = raid

    return json.dumps(result)


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

    # until database added, this just returns success

    result = 'Successfully created raid of type '+data['type']+' with parameter: '+data['path']

    return json.dumps(result)


@app_views.route('/api/run', methods=['GET'])
def run():
    result = {
        'id': '1337',
        'path': r'C:\Users\Omer\Documents\Valhalla'
    }

    return json.dumps(result)


@app_views.route('/download_raid', methods=['GET'])
def download_raid():
    # Create raid powershell script with ID built in
    raid_contents = generate_powershell.ps_downloader('777', r'%appdata%')

    # Send raid script for user to download
    return Response(raid_contents, mimetype="text/plain",
                    headers={"Content-Disposition": "attachment;filename=raid.ps1"})
