from core.permissions import IsAdminOrReadOnly
from rest_framework import status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ukpostcodeutils import validation
from api.serializers import PostcodeModelSerializer


class StandardValidationView(views.APIView):
    """View for the standard validation"""
    permission_classes = (IsAdminOrReadOnly, IsAuthenticated)

    def get(self, request):
        return Response({"message": "Validate UK Postcode"}, status=status.HTTP_200_OK)


    def post(self, request):

        postcode = request.data["postcode"]
        postcode = postcode.replace(" ", "")
        response = validation.is_valid_postcode(postcode)
        if response:
            result = "Valid"
        else:
            result = "Invalid"

        return Response({"result": result}, status=status.HTTP_200_OK)



# {
# "postcode" : "SW1A1AA"
# }
#
# {
# "postcode" : "G120YN"
# }
#





