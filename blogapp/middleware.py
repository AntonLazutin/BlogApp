class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Hello from middleware")
        response = self.get_response(request)
        print("Bye")

        return response


class Second:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Hello from second middleware")
        response = self.get_response(request)
        print("Bye x2")

        return response