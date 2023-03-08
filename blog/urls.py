from django.urls import path, include
from .views import PostListView, PostDetailView, UserDetailView, UserListView, AboutView, UserUpdateView, \
	UserPostListView, CustomLogoutView, HomePageView
from blog.views import LoginView, RegisterView
from blog.views import PostCreate, PostUpdate, LogoutView
from django.conf import settings
from django.conf.urls.static import static

app_name = "blog"

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	# path("user/<int:pk>/", UserDetailView.as_view(), name="user_profile"),
	path("about/", AboutView.as_view(), name="about"),

	path("login/", LoginView.as_view(), name="login"),
	path('logout/', CustomLogoutView.as_view(), name="logout"),
	path("register/", RegisterView.as_view(), name="register"),

	path("users/", UserListView.as_view(), name="user_list"),
	path('user/<str:username>/', UserDetailView.as_view(), name='user_detail'),
	path('user/<slug:username>/update/', UserUpdateView.as_view(), name='user_update'),

	path("create/", PostCreate.as_view(), name="post_create"),
	path("post/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
	path('post/<slug:slug>/update/', PostUpdate.as_view(), name='post_update'),

	path('myposts/', UserPostListView.as_view(), name='user_posts'),
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
