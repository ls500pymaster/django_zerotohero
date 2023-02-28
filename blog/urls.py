from django.urls import path, include
from .views import PostListView, PostListDetail
from accounts.views import LoginView, RegisterView
from blog.views import PostCreate

urlpatterns = [
	# path("admin/", admin.site.urls),
	path("", PostListView.as_view(), name="post_list"),
	path("login/", LoginView.as_view(), name="login"),
	path("register/", RegisterView.as_view(), name="register"),
	path('martor/', include('martor.urls')),
	path("create/", PostCreate.as_view(), name="post_create"),
]

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
