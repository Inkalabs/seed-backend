from django.shortcuts import redirect


def not_found_url_middleware(get_response):
    """
    Redirect to the base path if the page is not found.
    """

    def middleware(request):
        response = get_response(request)
        if response.status_code == 404:
            return redirect('/')

        return response

    return middleware
