from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page,name='post-home'),
    path('user_posts/<int:user_id>/', views.user_posts, name='user-posts'),
    path('timeline/', views.timeline_page,name='post-timeline'),
    path('about/',views.about_page,name='post-about'),
    path('account/',views.account_page,name='post-account'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)