from django.db import models


class TrackTimes(models.Model):
    class Meta:
        abstract = True
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def display_date_created(self):
        return "{}".format(self.created.strftime("%a %-I:%M %p"))


class Post(TrackTimes):
    class Meta:
        ordering = ("-id",)
        unique_together = ("title", "category",)
    title = models.CharField(max_length=25, unique=True)
    body = models.TextField()
    placeholder_image = models.FileField(upload_to="blog/placeholder_images/")
    category = models.ForeignKey("Category")

    def __unicode__(self):
        return "{0}".format(self.title)
        
    def get_category_name(self):
        return "{}".format(self.category.name)
        

class Comment(TrackTimes):
    class Meta:
        ordering = ("-created",)
    body = models.TextField()
    email = models.EmailField(max_length=254)
    post = models.ForeignKey("Post")
    comments = models.ManyToManyField("self")

    def __unicode__(self):
        return "{0} -- {1}".format(self.email[:5], self.post.title)


class Category(TrackTimes):
    class Meta:
        ordering = ("-name",)
    name = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return "{}".format(self.name)
