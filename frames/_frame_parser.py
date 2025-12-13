import glob
import os

from PIL import Image
import cv2

W = 64
H = 36
if __name__ == '__main__':
    cap = cv2.VideoCapture('_badapple.mp4')
    if True:
        print("Video > Images")
        if not os.path.isdir("frames"):
            os.mkdir("frames")
        i = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if frame is None:
                print("done")
                break
            if i % 2 == 0:
                i += 1
                continue
            frame = cv2.resize(frame, (W, H), fx=0, fy=0, interpolation=cv2.INTER_AREA)
            cv2.imwrite(f"frames/{str(i).zfill(5)}.png", frame)
            i += 1
            # define q as the exit button
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # release the video capture object
        cap.release()
        # Closes all the windows currently opened.
        cv2.destroyAllWindows()

    print("Images > Array")
    frames = []
    for path in sorted(glob.glob("frames/*.png")):
        img = Image.open(path)
        pixels = list(img.getdata(0))
        frame = [13 if p > 128 else 69 for p in pixels]
        frames.append(frame)

    print("Array > Python")
    with open("../badapple_frames.py", "w") as f:
        f.write("FRAMES = ")
        f.write(repr(frames))

    print(f"Parsed {len(frames)} frames")
