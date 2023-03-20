from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import UserActivity

@login_required
def track_activity(request):
    # Get the current user and the current time
    user = request.user
    current_time = datetime.now()

    # Check if the user has an existing UserActivity object
    try:
        activity = UserActivity.objects.get(user=user, logout_time=None)
        activity.logout_time = current_time
    except UserActivity.DoesNotExist:
        activity = UserActivity(user=user, login_time=current_time)

    # Save the UserActivity object
    activity.save()
