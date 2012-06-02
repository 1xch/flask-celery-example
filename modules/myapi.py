from flask import Blueprint, jsonify, request, session
from flask.views import MethodView
from celery.decorators import task

blueprint = Blueprint('myapi', __name__)

class MyAPI(MethodView):

    def get(self, resource_tag):
        #return jsonify(here="here")
        return get_resource.apply_async(resource_tag)  

@task(name="get_resource")
def get_resource(resource_tag):
    pass
