from django.db import models
from django.contrib.auth.models import User
import hashlib

class Link(models.Model):
    key = models.CharField(max_length=16)
    link = models.URLField()
    user = models.ForeignKey(User)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def save(self, *args, **kwargs):
        
        self.key = str(hashlib.sha1(str(self.link)).hexdigest())
        # FIXME: Temporarily using same user for testing
        self.user = User.objects.get(id=1)
        return super(Link,self).save(*args, **kwargs)
