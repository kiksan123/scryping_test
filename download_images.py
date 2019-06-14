import urllib.request
import sys
import time

def download():

    start_num = int(sys.argv[1])
    end_num = start_num + 100000
    

    for val in range(start_num,end_num):
        url = "https://im.uniqlo.com/images/jp/pc/goods/" + str(val) + "/sub/" +str(val) + "_sub7_popup.jpg"
        title = str(val) + ".jpg"
        try:
            urllib.request.urlretrieve(url,"{0}".format(title))
            # for server fuka
            time.sleep(1)
        except:
            pass

if __name__ == "__main__":
    download()
