from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, Http404, HttpResponseRedirect, get_object_or_404

from analytics.signals import page_view
from comments.forms import CommentForm
from comments.models import Comment
from .models import Video, Category, TaggedItem



#@login_required
def video_detail(request, cat_slug, vid_slug):
	cat = get_object_or_404(Category, slug=cat_slug)
	video = get_object_or_404(Video, slug=vid_slug, category=cat)
	page_view.send(request.user, 
				page_path=request.get_full_path(), 
				primary_obj=video,
				secondary_obj=cat
	)
	if request.user.is_authenticated() or video.has_preview:
		try:
			is_member = request.user.is_member
		except:
			is_member = None
		if is_member or video.has_preview:
			comments = video.comment_set.all()
			comment_form = CommentForm(request.POST or None)
			context = {
				"video": video, 
				"comments":comments, 
				"comment_form": comment_form,
			}
			return render(request, "videos/video_detail.html", context)
		else:
			# upgrade account
			next_url = video.get_absolute_url()
			return HttpResponseRedirect("%s?next=%s"%(reverse('account_upgrade'), next_url))
	else:
		next_url = video.get_absolute_url()
		return HttpResponseRedirect("%s?next=%s"%(reverse('login'), next_url))

def category_list(request):
	categories = Category.objects.all()
	template='videos/category_list.html'
	context = {
		'categories': categories
	}
	return render(request, template, context)

# @login_required
def category_detail(request, cat_slug):
	category = get_object_or_404(Category, slug=cat_slug)
	videos = category.video_set.all()
	page_view.send(request.user, 
				page_path=request.get_full_path(), 
				primary_obj=category
	)
	template='videos/video_list.html'
	context = {
		'category': category,
		'videos': videos
	}
	return render(request, template, context)


# def video_edit(request):

# 	template='videos/video_single.html'
# 	context = {}
# 	return render(request, template, context)

# def video_create(request):

# 	template='videos/video_single.html'
# 	context = {}
# 	return render(request, template, context)