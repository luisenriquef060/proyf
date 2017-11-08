from django.shortcuts import render_to_response,get_object_or_404
from django.shortcuts import render
from .forms import UploadImageForm
from .models import Producto
from .models import Vendedor
from .models import ProductoImage
from .forms import ProductoForm
from .forms import VendedorForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def nuevo(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return render(request, 'blog/base.html')
    context = {
        "form": form,
    }
    return render(request,"blog/post_form.html",context)


@login_required
def nuevoU(request):
    form = VendedorForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(reverse('lista'))
    context = {
        "form": form,
    }
    return render(request,"blog/post_form.html",context)

@login_required
def upload_image_view(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Image uploaded succesfully!"
    else:
        form = UploadImageForm()

    return render_to_response('blog/upload.html', locals(), context_instance=RequestContext(request))


def home_view(request):
    posts = Producto.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render_to_response('blog/base.html', {'posts': posts})
