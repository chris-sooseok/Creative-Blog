import uuid
from django.db import models
from django.db.models.fields import CharField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Category(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=60)

    class Meta:
        ordering = ['category']

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return str(self.category)

class Topic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="topics", blank=True, null=True)
    topic = models.CharField(max_length=60)

    def __str__(self):
        return str(self.topic)

    class Meta:
        ordering = ['topic']

class Note(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    order = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,related_name="notes",)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200, blank=True)
    date = models.DateField(auto_now=True)
    # content media file path is set in setting to uploads
    content = RichTextUploadingField(blank=True, null=True, config_name="notes")

    def __str__(self):
        return str(self.order) + '. ' + str(self.title)
    
    class Meta:
        ordering = ['order']
