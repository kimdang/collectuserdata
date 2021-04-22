from django.shortcuts import render

# from collect_app.forms import GetNameAge 

import logging, json
from user_agents import parse
from tallytable import add_entry


logger = logging.getLogger(__name__) ## get an instance of a logger


def getnameage (request):
    # form = GetNameAge()

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    ua_string = request.META['HTTP_USER_AGENT']
    user_agent = parse(ua_string)

    user_dict = {
        "source_IP": ip, 
        "browser": user_agent.browser.family,
        "os": 'Mac' if user_agent.os.family == 'Mac OS X' else 'Windows',
    }
    add_entry(user_dict)

    user_json = json.dumps(user_dict)
    logger.info(user_json)

    ## info dict is used for display purposes
    info = {
        # "form": form,
        "ip": ip, 
        "browser": user_agent.browser.family, 
        "os": user_agent.os.family,
    }

    return render(request, "index.html", info)


# def confirm (request):
#     info = {
#         "age": request.GET["age"], 
#         "name" : request.GET["fname"]
#         }
#     return render(request, "confirm.html", info)


"""
Note: A form to prompt user input was developed along with the application, but is omitted from the final product. In the code, the section pertaining to this form is commented out.
"""