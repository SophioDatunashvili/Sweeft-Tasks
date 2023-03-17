from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import URL
from .serializers import URLSerializer


class ShortURLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer

    @action(detail=False, methods=['post'])
    def create_short_url(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            short_name = serializer.validated_data.get('short_name', None)
            is_premium_client = bool(short_name)
            short_url_obj = URL(
                url=serializer.validated_data['url'],
                short_name=short_name,
                is_premium_client=is_premium_client
            )
            short_url_obj.save()
            # Build the full short URL
            short_url = request.build_absolute_uri(f'/url/{short_url_obj.short_name}/')
            # Include the full_short_url in the response data
            response_data = self.get_serializer(short_url_obj).data
            response_data['short_url'] = short_url
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], url_path='access')
    def access_short_url(self, request, pk=None, *args, **kwargs):
        short_url = get_object_or_404(URL, short_name=pk)
        short_url.access_count += 1
        short_url.save()
        return redirect(short_url.url)


class AccessShortURLView(APIView):
    def get(self, request, short_name, format=None):
        short_url = get_object_or_404(URL, short_name=short_name)
        short_url.access_count += 1
        short_url.last_accessed = timezone.now()
        short_url.save()
        return redirect(short_url.url)
