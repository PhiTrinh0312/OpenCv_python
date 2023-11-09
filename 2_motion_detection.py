import cv2

cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
#set camera có kích thước cố định
_, frame = cap.read()
frame=cv2.resize(frame,(640,480))
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
last_frame= gray
#Lấy một khung hình từ máy ảnh và chuyển đổi nó thành hình ảnh xám.
#So sánh hình ảnh xám hiện tại với hình ảnh xám trước đó (lưu trong biến last_frame)
# bằng cách sử dụng hàm cv2.absdiff() để tính toán sự khác biệt tuyệt đối
# (giá trị tuyệt đối của hiệu) giữa hai hình ảnh.
# Điều này sẽ tạo ra một hình ảnh mới biểu thị
# các sự thay đổi trong hình ảnh giữa hai khung hình liên tiếp.
#Hình ảnh kết quả của sự khác biệt được lưu trong biến abs_img.


while True:
    _, frame= cap.read()

    #xu li frame
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    abs_img=cv2.absdiff(last_frame,gray)
    #muốn phát hiện chuyển động ta lấy cái
    # dùng hàm abs để tính ra số dương nếu ra âm sẽ bị nhiễu
    last_frame=gray
    _,img_mask=cv2.threshold(abs_img,30,255,cv2.THRESH_BINARY)
    #tạo ra 1 ngưỡng  nếu nó vượt quá 30 thì nó sẽ thành màu trắng dưới 30 thì sẽ là 0 màu đen
    contours, _=cv2.findContours(img_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #hàm contours để vẽ ra được những hình màu trắng
    for contour in contours:
        if cv2.contourArea(contour)<900:# nếu kich thước nhỏ hơn 900 thì bỏ qua nó
            continue

        x,y,w,h=cv2.boundingRect(contour) #dhàm boundingRect được dùng đ tính toán hình chữ nhật
        #bao quanh 1 đường viền
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow("video",frame)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

