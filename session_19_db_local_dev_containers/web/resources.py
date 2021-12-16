from falcon_autocrud.resource import CollectionResource

from model.user import User


class UserCollectionResource(CollectionResource):
    model = User
    methods = ['GET']
