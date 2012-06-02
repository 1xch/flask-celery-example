from flask import Blueprint, jsonify, request, session
from flask.views import MethodView
from celery.decorators import task

blueprint = Blueprint('myapi', __name__)

class MyAPI(MethodView):

    def get(self, resource_tag):
        #return jsonify(here="here")
        return get_resource.apply_async(resource_tag)
        #return get_document.apply_async(args = [ database.db_session,
        #                                         session.get('public_token', None),
        #                                         request.form.get('return', "raw"),
        #                                         document_tag ] )      

@task(name="get_resource")
def get_resource(resource_tag):
#def get_document(session, token, return_as, doc_tag):
    pass
    #print dir(celery)
    #print type(celery)
    #print celery.conf
    #try:
    #    d = Document.get_by_filtered(session, "part_of", token, "tag", doc_tag)
    #    return jsonify(tag = str(d.tag), document = getattr(d,return_as)() )
    #except:
    #    return jsonify(error="That document could not be returned")
