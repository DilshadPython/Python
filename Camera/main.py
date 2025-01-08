import cv2


# import the sound as alert
from pygame import mixer

mixer.init()

mixer.music.load("beep.wav")

# create an object named camera to open or catch the camera zero stand for one
# camera on the machine I am using now
camera = cv2.VideoCapture(0)

# create a loop to tell the camera open
while camera.isOpened():
    # we are interested the frame send the frame to the camera
    r, frame = camera.read()
    # create new frame to check the picture between first and second camera
    # has been captured
    r, new_frame = camera.read()

    # now compare both pictures abdsdiff stand for absolute difference
    difference = cv2.absdiff(frame, new_frame)

    # if something change show white colour if not stay black
    gray = cv2.cvtColor(difference, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # we will make the image sharper
    _, threshold = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # next we will make the white part much more significan
    dilate = cv2.dilate(threshold, None, iterations=3)

    contours, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # use a method to find contours
    cv2.drawContours(frame, contours, -1, (255, 0, 0), 2)
    
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        # Here will display a rectangle of the area in the video moving
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        mixer.music.play()

    # the if statement tell the camera is working
    if cv2.waitKey(10) == ord('q'):
        break

    cv2.imshow("Personal Security Camera", frame) # threshold, blur, gray, difference, frame
