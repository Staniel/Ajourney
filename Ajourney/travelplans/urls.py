from django.conf.urls import patterns, url

from travelplans.views import view_plans,manipulate_plans,join_plan,share_plan, views


urlpatterns = patterns('',
    url(r'^$', view_plans.view_plans, name='view_plans'),
    url(r'^my_plans$', view_plans.my_plans, name='view_my_plans'),
    url(r'^available_plans$', view_plans.available_plans, name='view_available_plans'),
    url(r'^joined_plans$', view_plans.joined_plans, name='view_joined_plans'),
    url(r'^view_plan_detail$', view_plans.view_plan_detail, name='view_plan_detail'),

    # url(r'^create_plan$', manipulate_plans.create_plan, name='create_plan'),
    # url(r'^edit_plan$', manipulate_plans.edit_plan, name='edit_plan'),
    # url(r'^delete_plan$', manipulate_plans.delete_plan, name='delete_plan'),

    # url(r'^join_plan$', join_plan.join_plan, name='join_plan'),
    # url(r'^share_plan$', share_plan.share_plan, name='share_plan'),
    url(r'^index$', views.index, name='index'),
)
