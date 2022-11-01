from django.contrib import admin
from django.urls import include, re_path, path
# from django.urls import path
# from django.conf.urls import url
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]
