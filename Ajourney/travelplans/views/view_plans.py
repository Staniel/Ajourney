from django.http import HttpResponse
from django.template import RequestContext, loader
from travelplans.plan_manager import PlanManager
from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth import logout
from travelplans.facebook_proxy import get_picture_url

def available_plans(request):
    try:
        user=request.user
        if not user.is_authenticated():
            return redirect('login')
        pm=PlanManager()
        available_plans=pm.get_all_available_plans(user)
        template = loader.get_template('travelplans/view_plans.html')
        context = RequestContext(request, {
            'plan_list': available_plans,
            'list_title': "All Available Plans",
        })
        return HttpResponse(template.render(context))
    except:
        logout(request)
        return render_to_response('travelplans/login.html')

def my_plans(request):
    user=request.user
    if not user.is_authenticated():
        return redirect('login')
    pm=PlanManager()
    my_plans=pm.get_plans_by_user(user)
    template = loader.get_template('travelplans/view_plans.html')
    context = RequestContext(request, {
        'plan_list': my_plans,
        'list_title': "All My Plans",
    })
    return HttpResponse(template.render(context))

def joined_plans(request):
    user=request.user
    if not user.is_authenticated():
        return redirect('login')
    pm=PlanManager()
    joined_plans=pm.get_joined_plans(user)
    template = loader.get_template('travelplans/view_plans.html')
    context = RequestContext(request, {
        'plan_list': joined_plans,
        'list_title': "All Joined Plans",
    })
    return HttpResponse(template.render(context))

def view_plan_detail(request,planid):
    try:
        user=request.user
        if not user.is_authenticated():
            return redirect('login')
        pm = PlanManager()
        plan=pm.get_plan_by_id(planid)
        if plan.holder.is_superuser:
            picture_url = ''
        else:
            holder_fb = plan.holder.social_auth.filter(provider = 'facebook').first()
            holder_fb_id = holder_fb.uid
            picture_url = get_picture_url(user, holder_fb_id)
            
        if plan and pm.viewable(user,plan):
            template = loader.get_template('travelplans/plan_detail.html')
            context = RequestContext(request, {
            'plan': plan,
            'editable':pm.editable(user,plan),
            'sharable':pm.sharable(user,plan),
            'joinable':pm.joinable(user,plan),
            'joiners':pm.get_all_joiners(plan),
            'has_joined':pm.has_joined_plan(user,plan),
            'picture_url':picture_url,
            })
            return HttpResponse(template.render(context))
        else:
            return HttpResponse("This plan is not available.")
    except Exception as e:
        print str(e)
        logout(request)
        return render_to_response('travelplans/login.html')
        '''
        user=request.user
        if not user.is_authenticated():
            return redirect('login')
        pm=PlanManager()
        plan=pm.get_plan_by_id(planid)
        if plan.holder.first_name is '':
            picture_url = 
        else:
            picture_url=get_picture_url(plan.holder)
        if plan and pm.viewable(user,plan):
            template = loader.get_template('travelplans/plan_detail.html')
            context = RequestContext(request, {
            'plan': plan,
            'editable':pm.editable(user,plan),
            'sharable':pm.sharable(user,plan),
            'joinable':pm.joinable(user,plan),
            'joiners':pm.get_all_joiners(plan),
            'has_joined':pm.has_joined_plan(user,plan),
            'picture_url':picture_url,
            })
            return HttpResponse(template.render(context))
        else:
            return HttpResponse("This plan is not available.")
        '''    
def help(request):
    template = loader.get_template('travelplans/help.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
