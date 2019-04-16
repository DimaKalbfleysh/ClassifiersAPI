from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from classifier.models import Classifier


class ClassifierSerializer(serializers.ModelSerializer):
    parent = RecursiveField(allow_null=True)

    class Meta:
        model = Classifier
        fields = ('name', 'parent')




