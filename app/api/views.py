from core.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, views, filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ukpostcodeutils import validation
from core.models import PostcodeModel
from api.serializers import PostcodeModelSerializer
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict


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

class AdvancedValidationView(views.APIView):
    """View for the advanced validation"""
    permission_classes = (IsAdminOrReadOnly, IsAuthenticated)

    def get(self, request):
        return Response({"message": "Validate UK Postcode"}, status=status.HTTP_200_OK)


    def post(self, request):

        postcode = request.data["postcode"]
        postcode = postcode.replace(" ", "")

        uk_postcode = PostcodeModel.objects.filter(postcode=postcode).first()

        if uk_postcode:
            uk_postcode = model_to_dict(uk_postcode)
            return Response({"result": uk_postcode}, status=status.HTTP_200_OK)
        else:
            return Response({"result": "Invalid"}, status=status.HTTP_200_OK)




class PostcodeModelViewSet(viewsets.ModelViewSet):
    """Viewset for Postcode Model"""
    permission_classes = (IsAuthenticated,)
    serializer_class = PostcodeModelSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filterset_fields = ["postcode",]
    search_fields = ("postcode",)
    ordering_fields = "__all__"
    queryset = PostcodeModel.objects.all().order_by("postcode")

    def get_queryset(self):
        queryset = self.queryset
        return queryset






# {
# "postcode" : "BD177JW"
# }
#
# {
# "postcode" : "G120YN"
# }
#





