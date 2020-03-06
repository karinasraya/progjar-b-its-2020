import logging
import requests
import threading
from datetime import datetime
import os

def download(url=None,nama=None):

    if (url is None):
        return False

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    ff = requests.get(url)

    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = nama
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi},Waktu Download = {current_time} ")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False

if __name__=='__main__':

    threads = []

    t = threading.Thread(target=download, args=('https://timlo.net/wp-content/uploads/2019/05/sonic_the_hedgehog_movie.jpg','Gambar 1',))
    threads.append(t)
    t = threading.Thread(target=download, args=('https://i.gadgets360cdn.com/large/sonic-trailer_1573562530781.jpg?output-quality=80&output-format=webp','Gambar 2',))
    threads.append(t)
    t = threading.Thread(target=download, args=('https://thedigitalwise.com/wp-content/uploads/2019/12/maxresdefault-1-11-696x392.jpg','Gambar 3',))
    threads.append(t)

    for thr in threads:
        thr.start()