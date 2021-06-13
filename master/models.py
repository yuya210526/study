from django.db import models


class Parent(models.Model):
    """親"""
    name = models.CharField('名称', max_length=255)

    def __str__(self):
        return self.name


class Child(models.Model):
    """子"""
    name = models.CharField('名称', max_length=255)
    parent =  models.ForeignKey(Parent, verbose_name='名称', related_name='children', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
