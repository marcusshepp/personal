from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from main.views import (
    Main,
    foo,
    slideshow,
    modal,
)

from blog.views import (
    blog_landing,
    PostViewSet,
    CommentViewSet,
    CategoryViewSet,
)

blog_router = DefaultRouter()
blog_router.register(r'posts', PostViewSet)
blog_router.register(r'categories', CategoryViewSet)

urlpatterns = [
    url(r'^foo/', admin.site.urls),
    url(r'^$', Main.as_view(), name="main"),
    url(r'^foobar/$', foo, name="foo"),
    url(r'^slideshow/$', slideshow, name="slideshow"),
    url(r'^modal/$', modal, name="modal"),
    
    # blog
    url(r'^blog/$', blog_landing, name="blog_landing"),
    
    # api 
    url(r'^api/', include(blog_router.urls)),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
