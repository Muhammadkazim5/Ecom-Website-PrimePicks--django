from django.shortcuts import redirect

def RedireactMiddleware(get_response):
    def middleware(request):
        return_url = request.META['PATH_INFO']
        if not request.session.get('customer') and 'checkout' in return_url:
            return redirect(f'/login?return_url={return_url}')
        response = get_response(request)
        return response
    return middleware
