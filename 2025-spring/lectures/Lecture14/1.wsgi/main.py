def app(environ, start_response):
    path = environ.get("PATH_INFO", "/")

    if path == "/":
        response_body = b"Welcome to the homepage!"
    elif path == "/hello":
        response_body = b"Hello, World!"
    else:
        response_body = b"Page not found."
        start_response("404 Not Found", [("Content-Type", "text/plain")])
        return [response_body]

    start_response("200 OK", [("Content-Type", "text/plain")])
    return [response_body]
