### without this, matplotlib would flag assertion warning message
import matplotlib
matplotlib.use('Agg')
##

import matplotlib.pyplot as plt 
import base64 
from io import BytesIO
import random

os = ['Mac', 'Windows', 'Other_OS'] ## all possible browsers
browsers = ['Chrome', 'Safari', 'Firefox', 'Other_Browsers'] ## all possible operating systems


def pie_os (tally):
    labels = []
    sizes = []
    for item in tally.keys():
        if item in os:
            labels.append(item)
            sizes.append(tally[item])

    colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(len(labels))]
            

    fig = plt.figure(figsize=(5,5))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90, normalize=True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    return image_png



def pie_browser (tally):
    labels = []
    sizes = []
    for item in tally.keys():
        if item in browsers:
            labels.append(item)
            sizes.append(tally[item])

    colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(len(labels))]

    fig = plt.figure(figsize=(5,5))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, normalize=True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    return image_png