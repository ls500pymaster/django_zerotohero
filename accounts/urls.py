from django.urls import path, include
from blog.views import PostListView, PostDetailView, UserDetailView
from accounts.views import LoginView, RegisterView
from blog.views import PostCreate
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path("user/", UserDetailView.as_view(), name="user_detail"),
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
