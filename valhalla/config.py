import os

# Debug settings.
DEBUG = True
IS_SSL = False
# Important folders.
PROJECT_FOLDER = os.path.dirname(__file__)
STATIC_FOLDER = os.path.join(PROJECT_FOLDER, 'client')
TEMPLATE_FOLDER = os.path.join(STATIC_FOLDER, 'build')
TEMP_FOLDER = r'C:\Temp\Valhalla' if os.name == 'nt' else '/tmp'
# Server details.
IP = '127.0.0.1'
if IS_SSL:
    # If True, special localhost certificates will be used for SSL (instead of using Nginx).
    PORT = 443
else:
    # Let Nginx (or Tornado) handle all HTTPS communication.
    PORT = 8000
# DB credentials.
DB_HOST = 'localhost'
DB_USERNAME = 'AKIAJ5AD5MHDSY2NWAQA'
DB_PASSWORD = 'nGEnZ461s6x2/cFafLBfU6xBJanjHFIA/u4b/RVa' if DEBUG else 'Password1'
