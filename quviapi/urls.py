from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path('project/editor/', views.editor, name="editor"),
    path('editor/generate_index', views.generate_index, name="generate_index"),
    path("project/editor/background_cleaner",views.background_cleaner, name="background_cleaner"),
    path("editor/generate_item",views.generate_item, name="generate_item"),
    path("editor/generate_canvas",views.generate_canvas, name="generate_canvas"),
    path("project/", views.projectChoose, name="project"),
    path("userInfo/", views.userInfo, name="userInfo"),
    path("project/editor/save_canvas_data", views.save_canvas_data, name="save_canvas_data"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
