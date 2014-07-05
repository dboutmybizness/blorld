from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

class dblog_Author(models.Model):
	author = models.ForeignKey(User)
	display_name = models.CharField(max_length=40, blank=True)
	img_thumb = ResizedImageField(max_width=100, upload_to='authors/thumb', blank=True)
	author_url = models.CharField(max_length=254, blank=True)
	author_short = models.CharField(max_length=254)
	author_gplus = models.CharField(max_length=35,blank=True)
	author_twitter = models.CharField(max_length=35,blank=True)
	author_facebook = models.CharField(max_length=35,blank=True)

	def __unicode__(self):
		return self.display_name

class dblog_Tag(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=254)

    def __unicode__(self):
        return self.name

class dblog_Post(models.Model):
    ptypes = (
        ('HTML', 'HTML markup'),
        ('TEXT', 'text only'),
        ('IMG', 'image'),
        #('VIDEO', 'video'), may have different apis here (youtube vs our own vids we will see)

    )

    published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    post_by = models.ForeignKey(dblog_Author, blank=True)
    post_type = models.CharField(max_length=10, choices=ptypes)
    headline_text = models.CharField(max_length=100)
    headline_image = ResizedImageField(max_width=800, upload_to='authors/thumb', blank=True)
    headline_image_alt_tag = models.CharField(max_length=100, blank=True)
    headline_image_credit_label = models.CharField(max_length=35, blank=True)
    headline_image_credit_href = models.CharField(max_length=100, blank=True)
    seo_page_title = models.CharField(max_length=100, blank=True)
    short_description = models.CharField(max_length=254)
    text = models.CharField(max_length=254, blank = True)
    body = models.TextField(blank = True)
    tags = models.ManyToManyField(dblog_Tag, blank=True)
    
    display_date_published = models.DateTimeField()
    display_date_updated = models.DateTimeField()
    allow_comments = models.BooleanField()
    allow_su_comments = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add = True)
    modified_time = models.DateTimeField(auto_now = True)

    def display_text(self):
        if self.text:
            return self.text
        return self.body

    def __unicode__(self):
        return self.headline