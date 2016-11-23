from django.http import Http404
from django.shortcuts import render

# Create your views here.
from main.models import News, NewsImage, Event, EventImage, Photo, SliderImage


def index_view(request):
    news = News.objects.all().order_by('-timestamp')
    events = Event.objects.all().order_by('-timestamp')
    photos = Photo.objects.all().order_by('-timestamp')
    sliderImage = SliderImage.objects.all().order_by('-timestamp')
    context = {"news": news, "events": events, "photos": photos, "sliderImage": sliderImage}

    template = 'main/index.html'

    return render(request, template, context)


def singleNews(request, id):
    try:
        news = News.objects.get(id=id)

        images = NewsImage.objects.filter(news=news)

        context = {"news": news, "images": images}
        template = 'single_post.html'

        return render(request, template, context)

    except News.DoesNotExist:
        raise Http404
    except NewsImage.DoesNotExist:
        raise Http404


def singleEvents(request, id):
    try:
        events = Event.objects.get(id=id)

        images = EventImage.objects.filter(event=events)

        context = {"events": events, "images": images}
        template = 'single_event.html'

        return render(request, template, context)

    except Event.DoesNotExist:
        raise Http404
    except EventImage.DoesNotExist:
        raise Http404
