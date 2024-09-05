from rest_framework import serializers
from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):


    # user1 liked your post
    # actor: user 1
    # verb: 'liked your post'
    # recipient: you
    # we don't show recipient because whenever serializer is used
    # it would be used on list of one user's notifications
    class Meta:
        model = Notification
        fields = (
            'id',
            'actor_content_type',
            'actor_object_id',
            'verb',
            'action_object_content_type',
            'action_object_object_id',
            'target_content_type',
            'target_object_id',
            'timestamp',
            'unread',
        )

class NotificationSerializerForUpdate(serializers.ModelSerializer):
    unread = serializers.BooleanField()

    class Meta:
        model = Notification
        fields = ('unread',)

    def update(self, instance, validated_data):
        instance.unread = validated_data['unread']
        instance.save()
        return instance