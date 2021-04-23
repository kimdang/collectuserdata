### without this, matplotlib would give assertion warning message
import matplotlib
matplotlib.use('Agg')
##

import matplotlib.pyplot as plt 
import base64 
from io import BytesIO

def pie (tally):
    os_labels = ['Windows', 'Mac']
    os_sizes = [tally['Windows'], tally['Mac']]

    fig = plt.figure(figsize=(10,7))
    plt.pie(os_sizes, labels=os_labels)
    fig.savefig('test.png')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    return image_png
