# pip install pyjwt
import jwt

from flask import Flask, request, abort

app = Flask(__name__)

# Somewhere in the config module
app.config['DEPLOYMENT_1_MASTER_KEY'] = '123'
app.config['DEPLOYMENT_1_ID'] = 'deployment_1'
app.config['DEPLOYMENT_2_MASTER_KEY'] = '321'
app.config['DEPLOYMENT_2_ID'] = 'deployment_2'

deployment_key_map = {
    app.config['DEPLOYMENT_1_ID']: app.config['DEPLOYMENT_1_MASTER_KEY'],
    app.config['DEPLOYMENT_2_ID']: app.config['DEPLOYMENT_2_MASTER_KEY'],
}


@app.route('/', methods=['GET'])
def generate_token():
    """
    Validate user access and generate a JWT token.

    Example request URL::

        https://example.com/?deployment=deployment_1
    """
    deployment_id = request.args.get('deployment') or abort(400)
    master_key = deployment_key_map.get(deployment_id) or abort(400)

    token = jwt.encode({}, master_key, algorithm='HS256')

    return {'token': token}
