# pip install pyjwt
import jwt

from flask import Flask, request, abort

app = Flask(__name__)

# Somewhere in the config module
app.config['DEPLOYMENT_1_MASTER_KEY'] = 'key_XREeuYWSOkfG1UcYY4TqOs52US3fSlEj97Zldoc' \
                                        'MQUbRZXUiOxXxj7IXR8RvPRr2ACqsiaX2xIaDaVu22l' \
                                        'dXYfDpvLvUoBNaWKZxUAtkXbJ3nxh2jKihuJJE9Gsample'
app.config['DEPLOYMENT_1_ID'] = 'deployment_cQPneKKawjVsample'

app.config['DEPLOYMENT_2_MASTER_KEY'] = 'key_c2C1OPimUlnhAgZq4PSWhYmKe77DfdhnHMv8WII' \
                                        'VXdHNBOXvyKwRgZQyLa8n8ppf7ddguJpu6Wlbk6a7y1' \
                                        'xGPaeSAeDDxLPcJuTiZ73gOVtC5tcyQbT2oHePL6sample'
app.config['DEPLOYMENT_2_ID'] = 'deployment_F2fHsQkpBoPsample'

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
