from django.db import models
from time import time
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

#def generate_filename(instance, filename):

    #takes user filename and splits out the extensions
    #It converst the current time to an integer to eliminate
    #any decimals points, then converts the integer in a string
    #so it can be used in the file name. The function returns a
    #concatenation of the imagedump/ path, the current time and
    #the file name - a system generated filename
    #         courtesy of 'code.techandstartup.com'  

#    ext = filename.split('.')[-1]
#    return 'imagedump/' + str(int(time())) + '.' + ext

class posts(models.Model):
    author      = models.CharField(max_length = 30)
    title       = models.CharField(max_length = 100)
    #image       = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    bodytext    = models.TextField()
    timestamp   = models.DateTimeField()
    
#posts.objects.order_by('timestamp')
    
#    def __unicode__(self):
#        return self.title
    
#    class Meta:
#        ordering = ['title']
    
    

#@receiver(post_delete, sender=posts)
#def stuff_post_delete_handler(sender, **kwargs):
#    posts = kwargs['instance']
#    storage, path = posts.image1.storage, posts.image1.path
#    storage.delete(path)
    
    
    