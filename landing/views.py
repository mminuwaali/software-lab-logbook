from django.shortcuts import render, redirect


def index_view(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            return redirect("/admin")
        elif user.groups.filter(name="student").exists():
            return redirect("student:index-view")
        elif user.groups.filter(name="staff").exists():
            return redirect("staff:index-view")
    return render(request, "landing/index.html")


def about_view(request):
    return render(request, "landing/about.html")
