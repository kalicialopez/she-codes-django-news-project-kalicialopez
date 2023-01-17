from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE   
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.URLField(blank=True)

    def get_absolute_url(self):
        return reverse('news:story', kwargs={'pk': self.pk})
   

class Comment(models.Model):
    story = models.ForeignKey(NewsStory, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), related_name="comments" ,on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.story.title, self.author)


