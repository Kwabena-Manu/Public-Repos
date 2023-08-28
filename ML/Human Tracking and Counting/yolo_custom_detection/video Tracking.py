import cv2


cap = cv2.VideoCapture("./video with people.mp4")

#Object Detection From Stable Camera Or Background 
object_detector = cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=20)
while True:
    ret, frame = cap.read()
    height,weight,_ = frame.shape
    # print(height,weight)
    
    # Extract Region of Interest
    # roi = 
    
    # Object Detection
    mask = object_detector.apply(frame)
    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        #Calculate area and remove small elements 
        
        area = cv2.contourArea(cnt)
        if area > 400:
            # cv2.drawContours(frame,[cnt],-1,(0,255,0),2)
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    
    
    cv2.imshow("Frame",frame)   
    cv2.imshow("Mask",mask)
    key = cv2.waitKey(30)
    
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()