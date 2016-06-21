import json
from channels import Group
from .models import Calculate


def connect_blog(message):
    print("in connectblog")
    Group("shakeel").add(message.reply_channel)


def disconnect_blog(message):
    Group("shakeel").discard(message.reply_channel)
