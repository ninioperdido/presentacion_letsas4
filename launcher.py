import os,webbrowser

from fsevents import Observer, Stream
from subprocess import call

def callback(file_event):
    if file_event.name == os.getcwd()+"/slides.md":# the path of the modified file
        call(["/usr/bin/keydown", "slides", "slides.md"])
        url="file:///"+os.getcwd()+"/slides.html"
        webbrowser.open_new_tab(url)

    else:
        print file_event.name
def main():
    observer = Observer()
    observe_path = os.getcwd() # just for this example
    stream = Stream(callback, observe_path, file_events=True)
    observer.start()
    observer.schedule(stream)


if __name__ == '__main__':
    main()
