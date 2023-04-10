# myapp/views.py

from django.http import HttpResponse
from tasks import add
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import logging

logger = logging.getLogger(__name__)

class MyView(View):
    @method_decorator(csrf_exempt)
    def my_view(request):
        result = add.delay(2, 3)
        return HttpResponse(f'Result: {result.get()}')
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            data = request.POST.get('data')
            if not data:
                raise ValueError('Data is required')
            
            # Perform some operation with data
            result = data * 2

            return JsonResponse({'result': result})

        except Exception as e:
            logger.error(str(e))
            return JsonResponse({'error': 'An error occurred. Please try again.'}, status=500)