import json

from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from .models import Photo
from .utils import static_fallback_open

class PhotoListView(ListView):
    model = Photo
    template_name = "photo_list.html"

def index(request):
    asset_manifest = {}
    with static_fallback_open("reactjs/asset-manifest.json") as json_file:
        asset_manifest = json.load(json_file)

    react_css_bundle = asset_manifest["files"]["main.css"]
    react_js_bundle = asset_manifest["files"]["main.js"]

    context = {"react_css_bundle": react_css_bundle, "react_js_bundle": react_js_bundle}
    return render(request, "index.html", context=context)

@login_required
def index_authenticated(request):
    """
    our default view for showing React app content
    leverages the Django authentication system.
    """
    return index(request)