import cv2
import time
import argparse

if __name__ == '__main__':
    script_start_time = time.time()

    parser = argparse.ArgumentParser(description='Camera visualization')

    ### Positional arguments
    parser.add_argument('-i', '--cameraSource', default=0, help="Introduce number or camera path, default is 0 (default cam)")

    args = vars(parser.parse_args())

    cap = cv2.VideoCapture(args["cameraSource"]) # 0 local o primary camera
    while cap.isOpened():

        #BGR image feed from camera
        success, img = cap.read()

        if not success:
            break
        if img is None:
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img = cv2.GaussianBlur(gray, (3, 3), 0)

        sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

        cv2.imshow("Sobel X", sobelx)
        cv2.imshow("Sobel Y", sobely)

        k = cv2.waitKey(10)
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    print('Script took %f seconds.' % (time.time() - script_start_time))

