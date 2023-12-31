from django.db import models
from mdeditor.fields import MDTextField
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
	"""Topics that users learn about"""
	public=models.BooleanField(default=False)
	topic_hide = models.BooleanField(default=False)
	text=models.CharField(max_length=200)
	date_added=models.DateTimeField(auto_now_add=True)
	owner=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		"""Returns a string representation of the model"""
		return self.text

class Entry(models.Model):
	"""学到的有关某个主题的具体知识"""

	topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
	entry_hide = models.BooleanField(default=False)
	text=MDTextField()
	date_added=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural='entries'

	def __str__(self):
		"""返回模型的字符串表示"""

		return f"{self.text[:50]}..."

