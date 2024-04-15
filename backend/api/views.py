from django.conf import settings
from django.core.paginator import Paginator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ContactsSerializer, ContactSerializer, ContactCreateSerializer
from .swagger_serializers import ContactsSearchSerializer, ContactCreatableSerializer
from apps.models import Contact


# Create your views here.


class ContactsAPIView(APIView):
    @swagger_auto_schema(tags=['연락처 검색'], query_serializer=ContactsSearchSerializer)
    def get(self, request):
        params = request.GET.dict()
        order = params.get('order', 'id')
        page = int(params.get('page', 1))
        page_size = int(params.get('pagesize', 10))

        if order != 'id':
            if settings.PREVIOUS_ORDER != order:
                settings.PREVIOUS_ORDER = order
                settings.ORDER_DESC = ''
            else:
                if settings.ORDER_DESC is None:
                    settings.ORDER_DESC = ''
                elif settings.ORDER_DESC == '':
                    settings.ORDER_DESC = '-'
                else:
                    settings.ORDER_DESC = None
                    order = 'id'

        order_by = f'{settings.ORDER_DESC}{order}' if settings.ORDER_DESC else order
        contacts = Contact.objects.all().order_by(order_by)
        if contacts.exists():
            paginator = Paginator(contacts, page_size)
            contacts = paginator.get_page(page)

            serializers = ContactsSerializer(contacts, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(tags=['연락처 생성'], request_body=ContactCreatableSerializer)
    def post(self, request):
        if 'name' not in request.data:
            return Response('이름을 입력하세요', status=status.HTTP_400_BAD_REQUEST)

        serializer = ContactCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('연락처가 저장되었습니다.', status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class ContactAPIView(APIView):
    contact_id = openapi.Parameter('contact_id', openapi.IN_PATH, description='Contact Id', required=True, type=openapi.TYPE_NUMBER)

    @swagger_auto_schema(tags=['연락처 상세정보'], manual_parameters=[contact_id])
    def get(self, request, contact_id):
        contacts = Contact.objects.filter(id=contact_id)
        if contacts.exists():
            contact = contacts.first()
            serializers = ContactSerializer(contact)
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
