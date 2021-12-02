import boto3
import uuid
from chalice import Chalice, NotFoundError

app = Chalice('chalice_crud')


def get_app_db():
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table('records')
    return table


@app.route('/create', methods=['POST'])
def create():
    body = app.current_request.json_body
    item_id = str(uuid.uuid4())
    get_app_db().put_item(
        Item={
            'id': item_id,
            'score':  body['score'],
            'player': body['player'],
        }
    )
    return {
        'message': 'CREATED',
        'id': item_id,
    }


@app.route('/list', methods=['GET'])
def list():
    data = get_app_db().scan()
    return data['Items']


@app.route('/get/{entry_id}', methods=['GET'])
def get(entry_id):
    data = get_app_db().get_item(
        Key={
            'id': entry_id,
        }
    )
    if item := data.get('Item'):
        return item
    raise NotFoundError


@app.route('/delete/{entry_id}', methods=['POST'])
def delete(entry_id):
    get_app_db().delete_item(
        Key={
            'id':entry_id,
        }
    )
    return {
        'message': 'DELETED',
        'entry_id': entry_id,
    }