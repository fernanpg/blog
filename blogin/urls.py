from django.conf.urls import url
from .views import index, add_post, view_post, delete_comment, update_post, login

urlpatterns = [
    url(r'^$', login, name='login'),
    url(r'^index$', index, name='index'),
    url(r'^add_post$', add_post, name='add-post'),
    url(r'^view_post/(?P<post_id>\d+)$', view_post, name='view-post'),
    url(r'^delete_comment/(?P<comment_id>\d+)$', delete_comment, name='delete-comment'),
    url(r'^update_post/(?P<post_id>\d+)$', update_post, name='update-post'),
]
