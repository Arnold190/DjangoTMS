# checkpoint/callbacks.py

def permission_callback(request):
    return request.user.has_perm("checkpoint.change_model")

def environment_callback(request):
    """
    Callback has to return a list of two values represeting text value and the color
    type of the label displayed in top right corner.
    """
    return ["Production", "danger"] # info, danger, warning, success


def badge_callback(request):
    return 3