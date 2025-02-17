from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.db.models import Q
from .models import ImageNew
from .forms import CommentForm

class SubmitImage(CreateView):
    template_name = "gallery/create_image.html"
    model = ImageNew
    fields = "__all__"
    success_url = "/upload"

def image_list(request):
    # Get the tags from the URL query parameter
    tag_filter = request.GET.get('tag', None)
    
    if tag_filter:
        images = ImageNew.objects.filter(Q(tags__icontains=tag_filter) & Q(user=request.user))
    else:
        images = ImageNew.objects.filter(user=request.user)

    return render(request, 'gallery/images.html', {'images': images, 'tag_filter': tag_filter})
def image_detail(request, pk):
    # Get the image
    image = get_object_or_404(ImageNew, pk=pk)
    
    # Track the viewed images in session
    viewed_images = request.session.get('viewed_images', [])
    if pk not in viewed_images:
        viewed_images.append(pk)
        request.session['viewed_images'] = viewed_images
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect('image_detail', pk=image.pk)
    else:
        form = CommentForm()

    return render(request, 'gallery/details.html', {'image': image})