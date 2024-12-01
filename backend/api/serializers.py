from rest_framework.serializers import ModelSerializer
from .models import CustomUser, Halls, Seat, ShowMovies


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'is_admin']
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    

class HallSerializer(ModelSerializer):
    class Meta:
        model = Halls
        fields = ['hall_id','name', 'location']


class SeatSerializer(ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'seat_number', 'is_booked']

class ShowMoviesSerializer(ModelSerializer):
    seats = SeatSerializer(many=True, read_only=True)

    class Meta:
        model = ShowMovies
        fields = ['id', 'movie_id', 'show_date_and_time', 'hall', 'available_seats', 'seats']
