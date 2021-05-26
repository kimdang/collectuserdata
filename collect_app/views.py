from django.shortcuts import render
import logging, json, base64
from user_agents import parse
from utils.tallytable import add_entry
from utils import graph

from django.http import HttpResponse

logger = logging.getLogger(__name__) ## get an instance of a logger



def getuserinfo (request):

    ## user_agent 
    x_forwarded_for = request.META.get('HTTP_ORIGINAL_X_FORWARDED_FOR')

    if not x_forwarded_for:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    ua_string = request.META['HTTP_USER_AGENT']
    user_agent = parse(ua_string)


    ## categorize operating system (e.g. Mac, Windows, Linux, Other)
    os_list = ['Mac', 'Windows', 'Linux']
    for o in os_list:
        if o in user_agent.os.family:
            operating_system = o
            break
        else:
            operating_system = 'Other_OS'


    ## categorize browsers (e.g. Safari, Chrome, Firefox, Other)
    browser_list = ['Chrome', 'Safari', 'Firefox']
    for b in browser_list:
        if b in user_agent.browser.family:
            browser = b
            break
        else:
            browser = 'Other_Browsers'



    ## create user_dict
    user_dict = {
        "source_IP": ip,
        "browser": browser,
        "os": operating_system, }

    ## add to dynamoDB
    tally = add_entry(user_dict)


    ## create pie charts
    image_os = graph.pie_os(tally)
    chart_os = base64.b64encode(image_os)
    chart_os = chart_os.decode('utf-8')

    image_browser = graph.pie_browser(tally)
    chart_browser = base64.b64encode(image_browser)
    chart_browser = chart_browser.decode('utf-8')


    ## log user_dict 
    user_json = json.dumps(user_dict)
    logger.info(user_json)



    ## info is used for display purposes
    info = {
        "chart_os": chart_os,
        "chart_browser": chart_browser,
        "ip": ip, 
        "browser": user_agent.browser.family, 
        "os": user_agent.os.family,
    }

    return render(request, "index.html", info)

