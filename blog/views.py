from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from .models import Post, Card, Checkbox, CardType, Project, ProjectCard, CardLink, ProjectResource , ProjectResult, ProjectStep
from .forms import PostForm
from django.http import JsonResponse

# list of mobile User Agents
mobile_uas = [
	'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
	'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
	'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
	'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
	'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
	'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
	'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
	'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
	'wapr','webc','winw','winw','xda','xda-'
	]
 
mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone' , 'Android']

def mobileBrowser(request):
    ''' Super simple device detection, returns True for mobile devices '''
    mobile_browser = False
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]
    if (ua in mobile_uas):
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True
    return mobile_browser

def post_list(request):
    if mobileBrowser(request):
        base_template = 'blog/m_base.html'
    else:
        base_template = 'blog/base.html'
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'base_template': base_template})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def howstr_home(request):
    projectresources = Project.objects.filter(title='Cold Brew Coffee').first().projectresource_set.select_related('resource_card').all()
    projectsteps = Project.objects.filter(title='Cold Brew Coffee').first().projectstep_set.select_related('step_card').all()
    projectresults = Project.objects.filter(title='Cold Brew Coffee').first().projectresult_set.select_related('result_card').all()
    return render(request, 'blog/howstr_home.html', {'projectresources':projectresources, 'projectsteps':projectsteps, 'projectresults':projectresults})

def howstr_checkbox(request,flag,card_id):
    card = Card.objects.filter(id=card_id).first()
    if card is None:
        return JsonResponse({'card': None, 'checkbox': None})
    else:
        checkbox_query = Checkbox.objects.filter(card=card).filter(created_by=request.user)
        checkbox = checkbox_query.exists()
        result = None
        if flag=='yes':
            if checkbox:
                result = 'doing nothing because value already exists'
            else:
                result = Checkbox(title=card.title, card=card, created_by=request.user).save()
        elif flag=='no':
            if checkbox:
                result = checkbox_query.delete()
            else:
                result = 'doing nothing because value already empty'
        else:
            result = 'returning value in checkbox parameter'
        return JsonResponse({'card': card.title, 'checkbox': checkbox, 'result':result})



