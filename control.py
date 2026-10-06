from interfaz import Application
from imutils.video import VideoStream
import tkinter as tk
import time

def main():
    print("[INFO] warming up camera...")
    vs = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)

    root = tk.Tk()
    app = Application(root, vs)
    app.mainloop()


if __name__ == "__main__":
    main()
