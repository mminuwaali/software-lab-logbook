from . import models, forms
from django.http import HttpResponse
from django.contrib import messages
from django.utils.timezone import now
from django.shortcuts import render, redirect


def index_view(request):
    total = models.Record.objects.filter(user=request.user)

    others = total.exclude(created_at__date=now().date())
    current = total.filter(user=request.user, created_at__date=now().date())

    notifications = models.Notification.objects.filter(user=request.user)

    context = {"current": current, "others": others, "total": total, "notifications": notifications}
    return render(request, "student/index.html", context)


def create_view(request):
    if request.method == "POST":
        form = forms.RecordForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            form.save()  # Don't save the form yet

            messages.success(request, "Log Added Successfully!")
            return redirect("student:index-view")

        messages.error(request, "Failed to save record")
        return redirect("student:create-view")
    else:
        form = forms.RecordForm()  # If the request method is not POST, create a new form instance
    return render(request, "student/create.html", {"form": form})


def download_file(request, record_id):
    record = models.Record.objects.get(id=record_id)
    if record.file_upload:
        # Assuming file_upload is a FileField
        response = HttpResponse(record.file_upload, content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename="{record.file_upload.name}"'
        return response
    else:
        return HttpResponse("File not found", status=404)

def create_viewOld(request):
    if request.method == "POST":
        form = forms.RecordForm(request.POST)
        if form.is_valid():
            instance = form.save(False)

            instance.user = request.user
            instance.save()
            
            return redirect("student:index-view")

        messages.error(request, "Failed to save record")
        return redirect("student:create-view")
    return render(request, "student/create.html")
