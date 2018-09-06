from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="images/")
    summary = models.TextField(max_length=500)

    def __str__(self):
        return self.title

    def body(self):
        return self.summary[:100]