from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args, **kwargs)
    return wrapper_function
