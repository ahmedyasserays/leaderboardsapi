from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import scoreSerializer, boardSerializer
from renderer.models import leaderBoard

# Create your views here.

@api_view(["GET"])
def api_overview(request):
    urls = {
        '/api/create_board/': 'POST: creates new board from "name" and "password"',
        '/api/save_score/': 'POST: save new score to a board with it\'s "name" and "password", score need name and "score" and a "name"', 
        '/api/get_scores/<string:board name>/': 'GET: gets all scores in a board given it\'s "name"', 
        '/api/update_password/': 'POST: update password given "name" , "old_password", "password"', 
    }
    return Response(urls)


@api_view(["POST"])
def create_board(request):
    print(request.data)
    serializer = boardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'board created successfully'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': f'invalid data: make sure the data you\'ve entered is vaild\nerrors: {serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def save_score(request):
    board_name = request.data.get("board")
    try:
        board = leaderBoard.objects.get(name=board_name)
    except ObjectDoesNotExist:
        return Response({'message': 'leader board Not found: coudln\'t find the leader board you tried to reach please check your spelling'}, status=status.HTTP_404_NOT_FOUND)
    if not request.data.get("password") == board.password:
        return Response({'message': 'Wrong password: make sure you\'ve entered the right paswword'}, status=status.HTTP_403_FORBIDDEN)
    data = {
        "score": request.data.get("score"),
        "name": request.data.get("name"),
        "leader_board": board.id
    }
    serializer = scoreSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'score saved successfully'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': f'invalid data: make sure the data you\'ve entered is vaild\nerrors: {serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def get_scores(request, board_name):
    try:
        board = leaderBoard.objects.get(name=board_name)
    except ObjectDoesNotExist:
        return Response({'message': 'leader board Not found: coudln\'t find the leader board you tried to reach please check your spelling'}, status=status.HTTP_404_NOT_FOUND)
    scores = board.score_set.all().order_by("-score")
    serializer = scoreSerializer(scores, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def update_pass(request):
    board_name = request.data.get("name")
    try:
        board = leaderBoard.objects.get(name=board_name)
    except ObjectDoesNotExist:
        return Response({'message': 'leader board Not found: coudln\'t find the leader board you tried to reach please check your spelling'}, status=status.HTTP_404_NOT_FOUND)
    if not request.data.get("old_password") == board.password:
        return Response({'message': 'Wrong password: make sure you\'ve entered the right paswword'}, status=status.HTTP_403_FORBIDDEN)
    serializer = boardSerializer(instance=board, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "your password was updated successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"message":  f'invalid data: make sure the data you\'ve entered is vaild\nerrors: {serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)


