def http_error(exc):
    status = exc.resp.status

    if status == 400:
        print(f"\n\u001b[31mError {status}: Bad Request. There is some issues with Google requests.\u001b[0m")

    elif status == 403:
        print(f"\n\u001b[31mError {status}: Forbidden. Probably, you exceeded your YouTube API quota.\u001b[0m")

    elif status == 404:
        print(f"\n\u001b[31mError {status}: Not Found. Probably, the non-existent video was found.\u001b[0m")

    else:
        print(f"\n\u001b[31mUnexpected HTTP error: {status}\u001b[0m")
    
    input("\nPress Enter to return...")