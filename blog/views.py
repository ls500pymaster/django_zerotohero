from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView, TemplateView, ListView, CreateView
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.views.generic.edit import FormMixin

from .forms import CommentForm

from accounts.forms import RegisterForm
from .models import Post, Category, Tag, Comments
from .models import UserProfile


def home(request):
    category_list = Category.objects.all()
    tag_list = Tag.objects.all()
    post_list = Post.objects.all()
    context = {
        "category_list": category_list,
        "tag_list": tag_list,
        "post_list": post_list,
    }
    return render(request, "blog/home.html", context)


class LoginViewForm(FormView):
    form_class = AuthenticationForm
    template_name = "blog/login.html"
    success_message = "Login successful"
    success_url = reverse_lazy("blog:home")
    error_message = "Login False!"

    def form_valid(self, form):
        # We log the user in and redirect to the home page.
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = "blog/register.html"
    success_message = "Registration successful"
    success_url = reverse_lazy("blog:home")
    error_message = "Registration False!"

    def form_valid(self, form):
        user = form.save()
        user = authenticate(self.request, username=user.username, password=form.cleaned_data.get("password1"))
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)


# class HomePageView(ListView):
#     model = Post
#     context_object_name = "home"
#     template_name = "blog/home.html"
#
#     def get_queryset(self):
#         return Post.objects.order_by('-created')

class CategoryListView(generic.ListView):
    model = Category
    context_object_name = "category_list"
    template_name = "blog/category_list.html"


class CategoryDetailView(generic.DetailView):
    model = Category
    context_object_name = "category_detail"
    template_name = "blog/category_detail.html"

    def get_object(self, queryset=None):
        name = self.kwargs.get("name")
        return get_object_or_404(Category, name=name)


class TagList(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "blog/tag_list.html"


class TagDetailView(generic.DetailView):
    model = Tag
    context_object_name = "tag_detail"
    template_name = 'blog/tag_detail.html'

    def get_object(self, queryset=None):
        name = self.kwargs.get("name")
        return get_object_or_404(Tag, name=name)


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    paginate_by = 4
    template_name = "blog/post_list.html"


class PostDetailView(generic.DetailView, FormMixin):
    form_class = CommentForm
    model = Post
    context_object_name = "post_detail"
    paginate_by = 4
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_message = "Comment added"
    template_name = "blog/post_detail.html"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.username = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_detail'] = self.get_object()
        comments = Comments.objects.filter(post=self.object, published=True).order_by("created")
        context["comments"] = comments
        return context

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"slug": self.kwargs['slug']})


class PostCreate(LoginRequiredMixin, generic.CreateView):
    model = Post
    context_object_name = "post_create"
    template_name = "blog/post_create.html"
    fields = ["title", "body", "short_description", "categories", "tags", "image", "status"]
    success_url = reverse_lazy("blog:post_detail")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        from django.urls import reverse
        return reverse("blog:post_detail", kwargs={"slug": self.object.slug})


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    context_object_name = "post_update"
    template_name = "blog/post_update.html"
    fields = ["title", "body", "tags", "image"]
    success_message = "Post updated"

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"slug": self.object.slug})


class CommentCreateView(LoginRequiredMixin, CreateView):
    pass
    # model = Comments
    # form_class = CommentForm
    # template_name = "blog/comment_form.html"
    # success_message = "Comment added"
    # slug_url_kwarg = "slug"
    #
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     form.instance.post = get_object_or_404(Post, slug=self.kwargs['slug'])
    #     return super().form_valid(form)
    #
    # def get_success_url(self):
    #     return reverse_lazy("blog:post_detail", kwargs={"slug": self.kwargs["slug"]})


class UserListView(generic.ListView):
    model = UserProfile
    context_object_name = "user_list"
    paginate_by = 5
    template_name = "blog/user_list.html"


class UserDetailView(DetailView):
    model = UserProfile
    context_object_name = "user_detail"
    template_name = "blog/user_detail.html"

    def get_object(self, queryset=None):
        username = self.kwargs.get("username")
        return get_object_or_404(UserProfile, username=username)


class UserProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'blog/user_profile.html'


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = "user_posts"
    template_name = "blog/user_posts.html"
    paginate_by = 4

    def get_queryset(self):
        username = self.request.user
        return Post.objects.filter(author=username).order_by("-created")


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UserProfile
    context_object_name = "user_update"
    template_name = "blog/user_update.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    fields = ["full_name", "email", "mobile", "address", "age", "gender", "biography", "location", "website"]
    success_message = "Profile Updated"

    def get_success_url(self):
        username = self.object.username
        return reverse_lazy("blog:user_profile", kwargs={"username": username})


class AboutView(TemplateView):
    template_name = "blog/about.html"
