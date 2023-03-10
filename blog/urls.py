from django.urls import path, include
from .views import PostListView, PostDetailView, UserDetailView, UserListView, AboutView, UserUpdateView, \
	UserPostListView, CustomLogoutView, HomePageView, UserProfileView, LoginViewForm
from blog.views import LoginViewForm, RegisterView
from blog.views import PostCreate, PostUpdate, LogoutView, LoginViewForm, CategoryListView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = "blog"

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path("about/", AboutView.as_view(), name="about"),

	# path("login/", LoginView.as_view(), name="login"),
	path('login/', LoginViewForm.as_view(), name='login'),
	path('logout/', CustomLogoutView.as_view(), name='logout'),
	# path('logout/', CustomLogoutView.as_view(), name="logout"),
	path("register/", RegisterView.as_view(), name="register"),

	path("profile/<str:username>/", UserDetailView.as_view(), name="user_profile"),
	path("profile/<slug:username>/update/", UserUpdateView.as_view(), name='user_update'),

	path("users/", UserListView.as_view(), name="user_list"),
	path('user/<str:username>/', UserDetailView.as_view(), name='user_detail'),

	path("create/", PostCreate.as_view(), name="post_create"),
	path("post/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
	path('post/<slug:slug>/update/', PostUpdate.as_view(), name='post_update'),

	path('myposts/', UserPostListView.as_view(), name='user_posts'),

	path('categories/', CategoryListView.as_view(), name='category_list'),
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
