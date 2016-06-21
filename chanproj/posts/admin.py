from django.contrib import admin
from .models import Calculate, CalcPost


admin.site.register(
    Calculate,
    list_display=["result"],
    list_display_links=[ "result"],
    ordering=["result"],
)


admin.site.register(
    CalcPost,
    list_display=[  "created", "body_intro"],
    ordering=["-id"],
)
