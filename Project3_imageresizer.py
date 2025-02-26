import cv2
image = cv2.imread(r"C:\Users\arora\OneDrive - John Holland Group\Github Repos\python_new_repo\pythoon_image.jpg")

if image is None:
    print(f"Error:coould not find the image")
else:
    
    width = 300
    height = 200
    dsize = (width,height)
    resized_img = cv2.resize(image, dsize, interpolation=cv2.INTER_LINEAR)
    cv2.imshow("Original image", image)
    cv2.imshow("displayed image", resized_img)
    cv2.waitKey(0)              # Wait until a key is pressed
    cv2.destroyAllWindows()
