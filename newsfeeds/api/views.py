from newsfeeds.api.serializers import NewsFeedSerializer
from newsfeeds.models import NewsFeed
from newsfeeds.services import NewsFeedService
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from utils.paginations import EndlessPagination

class NewsFeedViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = EndlessPagination

    def get_queryset(self):
        return NewsFeedService.get_cached_newsfeeds(self.request.user.id)

    def list(self, request):
        queryset = self.paginate_queryset(self.get_queryset())
        serializer = NewsFeedSerializer(
            queryset,
            context={"request": request},
            many=True,
        )
        return self.get_paginated_response(serializer.data)