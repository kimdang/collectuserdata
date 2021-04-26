### without this, matplotlib would flag assertion warning message
import matplotlib
matplotlib.use('Agg')
##

import matplotlib.pyplot as plt 
import base64 
from io import BytesIO



def pie_os (tally):
    os_labels = ['Windows', 'Mac', 'Other']
    os_sizes = [tally['Windows'], tally['Mac'], tally['Other_OS']]
    colors = ['cyan', 'lightgreen', 'magenta']

    fig = plt.figure(figsize=(7,7))
    plt.pie(os_sizes, labels=os_labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    return image_png



def pie_browser (tally):
    browser_labels = ['Chrome', 'Safari', 'Firefox', 'Other']
    browser_sizes = [tally['Chrome'], tally['Safari'], tally['Firefox'], tally['Other_browser']]
    colors = ['gold', 'salmon', 'royalblue', 'peru']

    fig = plt.figure(figsize=(7,7))
    plt.pie(browser_sizes, labels=browser_labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    return image_png