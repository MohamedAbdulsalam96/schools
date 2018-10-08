from django.conf.urls import url, include
from profiles.views import parent_views

urlpatterns = [
    url(r'^$', parent_views.get_parent_list, name="parent-list"),
    url(r'^list$', parent_views.get_parent_list, name="parent-list"),
    url(r'^new/$', parent_views.save_update_parent, name="new-parent"),
    url(r'^(?P<id>[\d]+)/$', parent_views.get_parent_profile, name="parent-profile"),
    url(r'^(?P<id>[\d]+)/edit$', parent_views.save_update_parent, name="update-parent"),
    url(r'^(?P<id>[\d]+)/delete$', parent_views.delete_parent, name="delete-parent"),
]
