import multiprocessing
import requests

def downloadfile(url, name):
    response = requests.get(url)
    open(f"{name}.jpg", "wb").write(response.content)

if __name__ == "__main__":

    url = "https://picsum.photos/2000/3000"
    pros = []
    for i in range(5):
        p = multiprocessing.Process(target = downloadfile, args = [url, i])
        p.start()
        pros.append(p)
        p.join()

#so by using multiprocessing here we downloaded all 4 images immediately at once.