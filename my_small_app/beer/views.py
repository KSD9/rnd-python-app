from django.shortcuts import render
from rest_framework import status, views
from rest_framework.response import Response

from beer.models import BeerModel, WhiskeyModel
from beer.serializers import BeerModelSerializer, WhiskeyModelSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics


class BeerView(views.APIView):
    serializer_class = BeerModelSerializer

    def get(self, request, pk=None):
        """
            Method:             GET
            Url:                /api/beer/pk/
            Request headers:
                                {
                                    "Content-Type": "application/json",
                                    "Accept": "application/json",
                                }
            Request body:       None
            Response:
                                {
                                    beer.object.dict
                                }
        """
        try:
            beer = get_object_or_404(BeerModel, id=pk)
            beer_serializer = self.serializer_class(beer)

            return Response(
                beer_serializer.data,
                status=status.HTTP_200_OK)

        except Exception as ex:

            return Response(
                {'message': str(ex)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        """
            Method:             POST
            Url:                /api/beer/
            Request headers:
                            {
                                "Content-Type": "application/json",
                                "Accept": "application/json",
                            }
            Request body:       {
                                    'name': '{beer_name}',
                                    'beer_type': {beer_type},
                                    'description' : {beer_description}
                                }
            Response:
                            {
                                201_CREATED with the newly created beer object
                            }
        """
        serializer = BeerModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WhiskeyView(generics.ListCreateAPIView):
    """ Generic django rest view which serves both GET and POST requests

        Method:             GET
        Url:                /api/whiskey/
        Request headers:
                        {
                            "Content-Type": "application/json",
                            "Accept": "application/json",
                        }
        Request body:       None
        Response:
                        {
                            whiskey objects dictionary
                        }

        ====================================================================
        Method:             POST
        Url:                /api/whiskey/
        Request headers:
                    {
                        "Content-Type": "application/json",
                        "Accept": "application/json",
                    }
        Request body:       {
                            'brand': '{whiskey_brand}',
                            'age': {whiskey_age},
                            'description' : {whiskey_description}
                        }
        Response:
                    {
                        201_CREATED with the newly created whiskey object
                    }
    """
    serializer_class = WhiskeyModelSerializer
    model = WhiskeyModel
    queryset = WhiskeyModel.objects.all()
