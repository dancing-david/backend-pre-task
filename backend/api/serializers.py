from rest_framework import serializers

from apps.models import Contact


class ContactsSearchSerializer(serializers.Serializer):
    page = serializers.IntegerField(help_text='페이지 번호', required=False, default=1)
    page_size = serializers.IntegerField(help_text='한 페이지 당 갯수', required=False, default=10)
    order = serializers.ChoiceField(choices=('name', 'email', 'phone'), help_text='정렬', required=False, default='id')


class ContactCreateSerializer(serializers.Serializer):
    page = serializers.IntegerField(help_text='페이지 번호', required=False, default=1)
    page_size = serializers.IntegerField(help_text='한 페이지 당 갯수', required=False, default=10)
    order = serializers.ChoiceField(choices=('name', 'email', 'phone'), help_text='정렬', required=False, default='id')


class ContactsSerializer(serializers.ModelSerializer):
    company_position = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()

    def get_company_position(self, instance):
        return f'{instance.company} ({instance.position})'

    def get_label(self, instance):
        return instance.label.all().values_list('name', flat=True)

    class Meta:
        model = Contact
        fields = ('id', 'profile_image', 'name', 'email', 'phone', 'company_position', 'label')


class ContactSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()

    def get_label(self, instance):
        return instance.label.all().values_list('name', flat=True)

    class Meta:
        model = Contact
        fields = ('id', 'profile_image', 'name', 'email', 'phone', 'company', 'position', 'memo', 'label', 'address', 'birthday',
                  'website')
