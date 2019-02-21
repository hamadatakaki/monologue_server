from rest_framework import serializers

from accounts.models import Account
from monologue_api.serializers import SaidSerialiser, ActionSerializer, EmotionSerializer


class AccountSerializer(serializers.ModelSerializer):
    action = ActionSerializer()
    emotion = EmotionSerializer()
    saids = SaidSerialiser(many=True)

    class Meta:
        model = Account
        fields = (
            'uuid',
            'screen_name',
            'username',
            'email',
            'bio',
            'saids',
            'action',
            'emotion',
            'following_accounts',
            'followers',
        )
