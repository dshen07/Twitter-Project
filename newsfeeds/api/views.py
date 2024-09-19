from newsfeeds.api.serializers import NewsFeedSerializer
from newsfeeds.models import NewsFeed
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
        return NewsFeed.objects.filter(user=self.request.user)
    def list(self, request):
        cached_newsfeeds = NewsFeedService.get_cached_newsfeeds(request.user.id)
        page = self.paginator.paginate_cached_list(cached_newsfeeds, request)
        # if page is None, cache data does not fill a page
        # there may be data in the queryset
        if page is None:
            queryset = NewsFeed.objects.filter(user=request.user)
            page = self.paginate_queryset(queryset)
        serializer = NewsFeedSerializer(
            page,
            context={'request': request},
            many=True,
        )
        return self.get_paginated_response(serializer.data)