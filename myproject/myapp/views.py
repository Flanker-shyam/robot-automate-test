from .robot_test import run_test
from .parse import handle_output
from .constants import RESULT_FILE

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def get_data_for_test(request):
    if request.content_type!='application/json':
        return Response({"error": "Content-Type must be application/json"}, status=400)
    
    data = request.data.get("tests", [])
    error = run_test(data)
    if error:
        return Response({"error": error}, status=500)
    
    result = handle_output(RESULT_FILE)
    if result is None:
        return Response({"error": "Failed to generate result summary."}, status=500)
    
    return Response(result, status=200)