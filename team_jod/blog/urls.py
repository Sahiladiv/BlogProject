from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Blogs"),
    path('write', views.write_blog, name="Write Blog"),
    path('blog_post', views.show_blog, name="Show Blog"),
    path('paraphrase', views.paraphrase,name="Paraphrase"),
    path('publish',views.publish,name="Publish" ),
    path('comment', views.comment, name="Comments"),
    path('summary/<data_sent>', views.summarization,name="Summary"),

    path('demo', views.demo, name="DEMO"),

    path('<q>', views.people_blog, name="Blogs of the category"),

]