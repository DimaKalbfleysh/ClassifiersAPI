import re
import coreapi
import coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.views import APIView
from classifier.models import Classifier
from classifier.serializers import ClassifierSerializer


def verify_validity(name, children):
    if name == ' ':
        return 'Name cannot be empty'
    name = re.sub(" +", " ", name)
    for child in children:
        if child.name == name:
            return 'A classifier with this name already exists'
    unreadable_characters = '@#%^&*()-+=/;:|<>~№_'
    for char in name:
        if char in unreadable_characters:
            return 'Name cannot contain invalid characters'
    return False


class CreateRoot(APIView):
    """get: Creating a root"""
    schema = ManualSchema(
        description='Creating a root',
        fields=[
            coreapi.Field(
                "name",
                required=True,
                location="query",
                schema=coreschema.String(),
                description="The name of the root"
            ),
        ])

    def get(self, request):
        name = request.GET['name']
        error = verify_validity(name, [])
        if not error:
            classifier = Classifier.objects.create(name=name)
            serializer = ClassifierSerializer([classifier, ], many=True)
            return Response(serializer.data)
        else:
            return Response(error)


class Create(APIView):
    """get: Create new a classifier"""
    schema = ManualSchema(
        description='Create new a classifier',
        fields=[
            coreapi.Field(
                "name",
                required=True,
                location="query",
                schema=coreschema.String(),
                description="The name of the classifier"
            ),
            coreapi.Field(
                "parent",
                required=True,
                location="query",
                schema=coreschema.String(),
                description="The name of the parent in which you create the classifier"
            ),
        ])

    def get(self, request):
        try:
            parent = Classifier.objects.select_related().get(name=request.GET['parent'])
        except:
            return Response("Required argument 'parent'")
        name = request.GET['name']
        error = verify_validity(name, parent.children_classifiers.all())
        if not error:
            classifier = Classifier.objects.create(name=name, parent=parent)
            serializer = ClassifierSerializer([classifier, ], many=True)
            return Response(serializer.data)
        else:
            return Response(error)


class Branch(APIView):
    """get: All children of the specified parent"""
    schema = ManualSchema(
        description='All children of the specified parent',
        fields=[
            coreapi.Field(
                "parent",
                required=True,
                location="query",
                schema=coreschema.String(),
                description="The name of the parent"
            ),
        ])

    def get(self, request):
        try:
            parent = Classifier.objects.select_related().get(name=request.GET['parent'])
        except:
            return Response("Required argument 'parent'")
        children = parent.get_children()
        serializer = ClassifierSerializer(children, many=True)
        return Response(serializer.data)


class UpdatePath(APIView):
    """get: Changes the path of the classifier"""
    schema = ManualSchema(
        description='Changes the path of the classifier',
        fields=[
            coreapi.Field(
                "name",
                required=True,
                location="query",
                schema=coreschema.String(),
                description="The name of the classifier"
            ),
            coreapi.Field(
                "parent",
                required=True,
                location="query",
                schema=coreschema.String(),
                description="The name of the parent in which the classifier is changed"
            ),
            coreapi.Field(
                "new_parent",
                required=True,
                location="query",
                schema=coreschema.String(),
                description="The name new parent of the classifier"
            ),
        ])

    def get(self, request):
        try:
            parent = Classifier.objects.select_related().get(name=request.GET['parent'])
        except:
            return Response("Required argument 'parent'")
        classifier = parent.children_classifiers.get(name=request.GET['name'])
        new_parent = Classifier.objects.get(name=request.GET['new_parent'])
        classifier.parent = new_parent
        classifier.save()
        return Response('Successfully changed path')


class UpdateName(APIView):
    """ get: Changes the name of the classifier """
    schema = ManualSchema(
        description='Changes the name of the classifier',
        fields=[
            coreapi.Field(
                "name",
                required=True,
                location="query",
                schema=coreschema.String(),
                description="The name of the classifier"
            ),
            coreapi.Field(
                "parent",
                required=True,
                location="query",
                schema=coreschema.String(),
                description="The name of the parent in which the classifier is changed"
            ),
            coreapi.Field(
                "new_name",
                required=True,
                location="query",
                schema=coreschema.String(),
                description="The new name of the classifier"
            ),
        ])

    def get(self, request):
        try:
            parent = Classifier.objects.select_related().get(name=request.GET['parent'])
        except:
            return Response("Required argument 'parent'")
        classifier = parent.children_classifiers.get(name=request.GET['name'])
        new_name = request.GET['new_name']
        classifier.name = new_name
        classifier.save()
        return Response('Successfully changed name')


class Delete(APIView):
    """ get: Delete a classifier """
    schema = ManualSchema(
        description='Delete a classifier',
        fields=[
            coreapi.Field(
                "name",
                required=True,
                location="query",
                schema=coreschema.String(),
                description="The name of the classifier"
            ),
            coreapi.Field(
                "parent",
                required=True,
                location="query",
                schema=coreschema.String(),
                description="The name of the parent in which you delete the classifier"
            ),
        ])

    def get(self, request):
        try:
            parent = Classifier.objects.select_related().get(name=request.GET['parent'])
        except:
            return Response("Required argument 'parent'")
        classifier = parent.children_classifiers.get(name=request.GET['name'])
        classifier.delete()
        return Response('Successfully removed')
