from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
# webinars/models.py

class Webinar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='webinars', blank=True, null=True)
    date = models.DateTimeField()
    link = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    webinar = models.ForeignKey(Webinar, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.webinar.title}"

class Payment(models.Model):
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.registration.user.username} - {self.amount}"
    
class Blog(models.Model):
    title = models.CharField(max_length=200)  # Optimized for shorter text
    description = models.TextField()  # For summaries or brief descriptions
    content = RichTextUploadingField()  # For rich content editing
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)  # Track when the blog is created
    updated_at = models.DateTimeField(auto_now=True)  # Track the last update
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  # Allow multiple comments per user
    content = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')  # Consistent related_name (pluralized)
    created_at = models.DateTimeField(auto_now_add=True)  # Track when the comment is created

    def __str__(self):
        return f"Comment by {self.user.username} on {self.blog.title}"

