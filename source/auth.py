from flask import Blueprint, Flask, request
#from source.models import data_register
from flask_restful import marshal_with, fields
#from source import db
import boto3
from boto3.dynamodb.conditions import Attr
from source import name, aws_region

registerfield = {
    'id':fields.Integer,
    'name':fields.String,
    'especialidad':fields.String,
    'correo':fields.String 
}

dynamodb = boto3.resource('dynamodb',region_name=aws_region)
                    #aws_access_key_id = key_id,
                    #aws_secret_access_key = access_key)


register = Blueprint("register", __name__, url_prefix="/api/v1/auth")

table = dynamodb.Table(name)

@register.route('/', methods=['POST','GET'])
#@auth.post('/register')
@marshal_with(registerfield)
def get_register():

    if request.method == 'POST':
        data = request.json

        #new_table = table(name=data['name'], especialidad=data['especialidad'], correo=data['correo'])

        response = table.put_item(
            Item={
                'id': data['id'],    
                'name': data['name'],
                'especialidad': data['especialidad'],
                'correo': data['correo']
            }
        )
        #print(data)
        return data

    else: 
        #actual = data_register.query.all()
        response = table.scan()
        #print(response)
        return response['Items']

#@auth.get('/me')
@register.get("/<int:pk>")
@marshal_with(registerfield)
def get_register_pk(pk):
    #tablepk = table.scan(FilterExpression=Attr('id').eq('pk'))
    response = table.scan(
        FilterExpression = Attr("id").eq(pk)
    )

    return response['Items']

@register.delete("/<int:pk>")
@marshal_with(registerfield)
def delete_register(pk):

    response = table.delete_item(
        Key={
        'id' : pk
        }
    )

    #print(response)

    return table
        
@register.put("/<int:pk>")
@marshal_with(registerfield)
def put_register(pk):
    data = request.json

    response = table.update_item(
        Key={
            'id': pk
        },
        UpdateExpression=" set #nm=:newname, especialidad=:e, correo=:c ",
        ExpressionAttributeValues={
                    ':newname': data['name'], ':e': data['especialidad'], ':c': data['correo']},
        ExpressionAttributeNames={
            "#nm": "name"
        },
        ReturnValues="UPDATED_NEW"
    )

    #print(response)


    return response['Attributes']
