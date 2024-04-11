from rest_framework import serializers

from apps.models import Contact, Label


class ContactsSerializer(serializers.ModelSerializer):
    company_position = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()

    def get_company_position(self, instance):
        text = ''
        if instance.company:
            text = instance.company
        if instance.position:
            if text:
                text += f' ({instance.position})'
            else:
                text = instance.position
        return text

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


class ContactCreateSerializer(serializers.ModelSerializer):
    label = serializers.ListField()

    class Meta:
        model = Contact
        exclude = ('id',)

    def create(self, validated_data):
        labels = validated_data.pop('label') if validated_data.get('label') else None

        contact = Contact(**validated_data)
        contact.save()
        if labels:
            create_list = [
                Label(
                    contact=contact,
                    name=label,
                )
                for label in labels
            ]
            Label.objects.bulk_create(create_list, batch_size=500)
        return contact
