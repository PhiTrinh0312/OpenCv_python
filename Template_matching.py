import cv2


# cap=cv2.VideoCapture(0) # mặc định là sài cam máy lun
# while True:
#     _,image= cap.read()#tham số 1 thì nó trả về true or false mà ta ko cần nên để _
#     cv2.imshow("video", image)  # hiển thị nhìu bức ảnh thì nó sẽ thành vid
#     if cv2.waitKey(1) == ord('q'):
#         break

path1 = r'C:\Users\ADMIN\Pictures\Aot.jpg'
s_img = cv2.imread(path1)
path2 = r'C:\Users\ADMIN\Pictures\Aot(3).jpg'
t_img = cv2.imread(path2)

method = eval('cv2.TM_CCOEFF_NORMED')
s_img_copy = s_img.copy()
res = cv2.matchTemplate(s_img_copy, t_img, method)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
if method in [cv2.TM_SQDIFF_NORMED, cv2.TM_SQDIFF]:
    top_left = min_loc  # điểm bên trái ngoài cùng bức ảnh bé
else:
    top_left = max_loc

height, width, channel = t_img.shape
bottom_right = (top_left[0] + width, top_left[1] + height)
cv2.rectangle(s_img, top_left, bottom_right, (255, 0, 0), 3)

cv2.imshow("image to find ", t_img)
cv2.imshow("the original image ", s_img_copy)
cv2.imshow("Original photo after finding it ", s_img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
