from rest_framework.views import APIView
from rest_framework.response import Response


class CurrentUserView(APIView):
    """Checking for logged-in user"""

    def get(self, request, *args, **kwargs):
        if str(request.user) != "AnonymousUser":
            return Response({"email": request.user.email, "admin": request.user.is_superuser, "username": str(request.user)})
        else:
            return Response({"error": "Anonymous"})
