from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Classifier(MPTTModel):
    name = models.CharField(max_length=150, blank=False, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children_classifiers')

    class MPTTMeta:
        order_insertion_by = ['name']