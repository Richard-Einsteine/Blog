from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

    
class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    
    
class Posts(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    category = models.ManyToManyField(Category)
    featured = models.BooleanField()
    
    class Meta:
        verbose_name_plural = 'Posts'
        
    def get_trailer(self):
        trailer = self.overview[:100]
        return trailer
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post', kwargs={'id': self.pk})

    def __str__(self):
        return self.title
    