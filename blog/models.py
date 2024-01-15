from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.TextField()
    blog = models.ForeignKey(to=Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.text}'

class Like(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.Model)
    status = models.BooleanField(default=True)
    comment = models.ForeignKey(to=Comment, on_delete=models.CASCADE, null=True, blank=True)
    blog = models.ForeignKey(to=Blog, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.author)


