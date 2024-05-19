from rest_framework import serializers
from .models import Members
from section.models import Sections


class MembersSerializer(serializers.ModelSerializer):
    section = serializers.CharField(max_length=225)

    class Meta:
        model = Members
        fields = ['name', 'email', 'section']

    def validate_section_name(self, value):
        try:
            Sections.objects.get(name=value)
        except Sections.DoesNotExist:
            raise serializers.ValidationError("Invalid section name.")
        return value

    def create(self, validated_data):
        section_name = validated_data.pop('section', None)

        try:
            section = Sections.objects.get(name=section_name)
        except Sections.DoesNotExist:
            raise serializers.ValidationError("Invalid section name.")

        validated_data['section'] = section
        member = Members.objects.create(**validated_data)
        return member


class MembersActivationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.IntegerField()

    def validate(self, data):
        email = data.get('email')
        confirmation_code = data.get('confirmation_code')

        try:
            member = Members.objects.get(email=email, confirmation_code=confirmation_code)
        except Members.DoesNotExist:
            raise serializers.ValidationError("Invalid email or confirmation code.")

        data['member'] = member
        return data
