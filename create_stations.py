from screen_app.models import Station
from django.contrib.auth.models import User

# Fetch some existing users to assign as managers
users = User.objects.all()

if not users.exists():
    print("Please ensure you have some users in your database.")
else:
    # Select a user to assign as the manager
    selected_manager = users.first()

    # Create stations with names station2 to station19
    for i in range(2, 20):  # Creating stations from station2 to station19
        station_name = f"station{i}"
        Station.objects.create(
            name=station_name,
            manager=selected_manager  # Assign a manager
        )
        print(f"Created: {station_name}")
