from django.urls import path, include
from .views import PostListView, PostDetailView, UserDetailView, UserListView
from accounts.views import LoginView, RegisterView
from blog.views import PostCreate
from django.conf import settings
from django.conf.urls.static import static

app_name = "blog"

urlpatterns = [
	# path("admin/", admin.site.urls),
	path('martor/', include('martor.urls')),
	path("", PostListView.as_view(), name="post_list"),
	# path("user/<int:pk>/", UserDetailView.as_view(), name="user_profile"),
	path("create/", PostCreate.as_view(), name="post_create"),
	path("post/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
