async def app(scope, receive, send):
    assert scope["type"] == "http"

    path = scope.get("path", "/")

    if path == "/":
        body = b"Welcome to the homepage!"
        status = 200
    elif path == "/hello":
        body = b"Hello, World!"
        status = 200
    else:
        body = b"Page not found."
        status = 404

    # Start the response
    await send(
        {
            "type": "http.response.start",
            "status": status,
            "headers": [[b"content-type", b"text/plain"]],
        }
    )

    # Send the body
    await send(
        {
            "type": "http.response.body",
            "body": body,
        }
    )
