from django.urls import path, include

from contact.forms import ContactForm
from .views import home, CommentCreateView
from .views import PostListView, PostDetailView, UserDetailView, UserListView, AboutView, UserUpdateView, \
	UserPostListView, CustomLogoutView, UserProfileView, LoginViewForm, home
from blog.views import LoginViewForm, RegisterView
from blog.views import PostCreate, PostUpdate, LogoutView, LoginViewForm, CategoryListView, TagList, TagDetailView, CategoryDetailView
from django.conf import settings
from contact.views import ContactViewMain, success_view

app_name = "blog"

urlpatterns = [

	path('', home, name='home'),
	path("about/", AboutView.as_view(), name="about"),

	path('login/', LoginViewForm.as_view(), name='login'),
	path('logout/', CustomLogoutView.as_view(), name='logout'),
	path("register/", RegisterView.as_view(), name="register"),

	path("profile/<str:username>/", UserDetailView.as_view(), name="user_profile"),
	path("profile/<slug:username>/update/", UserUpdateView.as_view(), name='user_update'),

	path("users/", UserListView.as_view(), name="user_list"),
	path('user/<str:username>/', UserDetailView.as_view(), name='user_detail'),

	path("create/", PostCreate.as_view(), name="post_create"),
	path("post/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
	path('post/<slug:slug>/update/', PostUpdate.as_view(), name='post_update'),

	path('post/<slug:slug>/comment/', CommentCreateView.as_view(), name='add_comment'),

	path('myposts/<str:username>/', UserPostListView.as_view(), name='user_posts'),

	path("category/", CategoryListView.as_view(), name='category_list'),
	path("category/<str:name>", CategoryDetailView.as_view(), name='category_detail'),

	path("tags/", TagList.as_view(), name='tag_list'),
	path("tags/<str:name>", TagDetailView.as_view(), name='tag_detail'),

	path('contact/', ContactViewMain.as_view(), name='contact'),
	path("success/", success_view, name="success"),
]

if settings.DEBUG:
    urlpatterns += path('__debug__/', include('debug_toolbar.urls')),

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
