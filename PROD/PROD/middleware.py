from django.utils.timezone import now, make_aware, is_naive
from django.utils.dateparse import parse_datetime
from django.contrib.auth import logout
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from datetime import timedelta
from Checkpoint.models import Attendance


# Middleware for auto-logout based on inactivity
class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            if last_activity:
                # Use parse_datetime to handle timezone-aware datetime strings
                last_activity_time = parse_datetime(last_activity)
                
                if last_activity_time:
                    # Only make aware if it's a naive datetime
                    if is_naive(last_activity_time):
                        last_activity_time = make_aware(last_activity_time)
                    
                    # Compare using aware datetime object
                    if now() - last_activity_time > timedelta(minutes=settings.SESSION_IDLE_TIMEOUT):
                        logout(request)
            request.session['last_activity'] = str(now())  # Update the session

        response = self.get_response(request)
        return response
    

# Middleware for clock-in and clock-out functionality
class ClockInOutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Skip this logic for unauthenticated users
        if request.user.is_authenticated:
            # Clock in the user if logged in and no attendance record exists
            work_date = now().date()
            attendance, created = Attendance.objects.get_or_create(user=request.user, work_date=work_date)
            
            if created or attendance.clock_in_time is None:
                attendance.clock_in_time = now()
                attendance.save()

            # Auto-logout based on inactivity timeout
            last_activity = request.session.get('last_activity')
            if last_activity:
                # Parse last activity time to handle timezone awareness
                last_activity_time = parse_datetime(last_activity)
                
                if last_activity_time:
                    # Only make aware if it's a naive datetime
                    if is_naive(last_activity_time):
                        last_activity_time = make_aware(last_activity_time)

                    # Define inactivity timeout (e.g., 120 minutes)
                    if now() - last_activity_time > timedelta(minutes=settings.SESSION_IDLE_TIMEOUT):
                        self.clock_out_user(request)
                        logout(request)  # Log out user after inactivity timeout

            # Update last activity time on every request
            request.session['last_activity'] = str(now())

    def process_response(self, request, response):
        # Ensure clock out when the user logs out
        if request.user.is_authenticated and not request.user.is_active:
            self.clock_out_user(request)
        return response

    def clock_out_user(self, request):
        # Clock-out logic
        work_date = now().date()
        try:
            attendance = Attendance.objects.get(user=request.user, work_date=work_date, clock_out_time__isnull=True)
            attendance.clock_out_time = now()
            attendance.save()
        except Attendance.DoesNotExist:
            pass



# Signal for clock-in when user logs in
#@receiver(user_logged_in)
#def clock_in(sender, request, user, **kwargs):
    # Create an Attendance record for clock-in
#    Attendance.objects.create(user=user, clock_in_time=now())
 #   request.session['last_activity'] = str(now())  # Set session activity timestamp


# Signal for clock-out when user logs out
#@receiver(user_logged_out)
#def clock_out(sender, request, user, **kwargs):
    # Update the last clock-in record with clock-out time
 #   last_attendance = Attendance.objects.filter(user=user, clock_out_time__isnull=True).last()
  #  if last_attendance:
   #     last_attendance.clock_out_time = now()
    #    last_attendance.save()
