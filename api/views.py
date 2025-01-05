from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter
from .models import Tag, Property, Comments
from .serializers import TagSerializer, PropertySerializer, CommentsSerializer, UserSerializer
from django.contrib.auth.models import User


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['country', 'address']  

    def get_queryset(self):
        """
        Filter properties based on availability and tag.
        """
        queryset = Property.objects.all()
        
        # Filter by availability
        availability = self.request.query_params.get('availability')
        if availability:
            queryset = queryset.filter(availability__iexact=availability)  

        # Filter by tag
        tag = self.request.query_params.get('tag')
        if tag:
            queryset = queryset.filter(title_tag__title__icontains=tag) 

        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
