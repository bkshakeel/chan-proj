import json
from django.db import models
from django.template.defaultfilters import linebreaks_filter
from django.utils.six import python_2_unicode_compatible
from channels import Group
from django.contrib.auth.models import User


# Create your models here.
@python_2_unicode_compatible
class Calculate(models.Model):
    result = models.CharField(max_length=255)
    def __str__(self):
        return self.result



@python_2_unicode_compatible
class CalcPost(models.Model):
    calculate = models.ForeignKey(Calculate, related_name="calcposts")
    body = models.TextField()
    operand1 = models.TextField( default="x")
    operand2 = models.TextField( default="y")
    symbol = models.TextField( default="+")


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "#%i: %s" % (self.id, self.body_intro())

    def body_intro(self):
        """
        Short first part of the body to show in the admin or other compressed
        views to give you some idea of what this is.
        """
        return  self.body[:50]

    def html_body(self):
        """
        Returns the rendered HTML body to show to browsers.
        You could change this method to instead render using RST/Markdown,
        or make it pass through HTML directly (but marked safe).
        """
        return linebreaks_filter(self.operand1+ self.symbol +self.operand2 + "="+self.body)

    def send_notification(self):
        """
        Sends a notification to everyone in our Liveblog's group with our
        content.
        """
        # Make the payload of the notification. We'll JSONify this, so it has
        # to be simple types, which is why we handle the datetime here.
        print("in notification")
        notification = {
            "id": self.id,
            "html": self.html_body(),
            "created": self.created.strftime("%a %d %b %Y %H:%M"),
        }
        # Encode and send that message to the whole channels Group for our
        # liveblog. Note how you can send to a channel or Group from any part
        # of Django, not just inside a consumer.
        Group("shakeel").send({
            # WebSocket text frame, with JSON content
            "text": json.dumps(notification),
        })

    def save(self, *args, **kwargs):
        """
        Hooking send_notification into the save of the object as I'm not
        the biggest fan of signals.
        """
        print("in save")
        result = super(CalcPost, self).save(*args, **kwargs)
        self.send_notification()
        return result
