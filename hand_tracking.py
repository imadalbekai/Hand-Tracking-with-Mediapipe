import mediapipe as mp
import cv2


cap = cv2.VideoCapture(0)

mp_hand = mp.solutions.hands
hands=mp_hand.Hands()
mp_draw=mp.solutions.drawing_utils


ret = True
while ret:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_RGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hands.process(frame_RGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
             for id,lm in enumerate(handlms.landmark):
                  #print(id,lm)
                  h, w, c= frame.shape
                  cx, cy =int(lm.x*w),int(lm.y*h)
                  print(id,cx,cy)
                  if id==0:
                      cv2.circle(frame,(cx,cy),15,(255,0,255),cv2.FILLED)
                     
             mp_draw.draw_landmarks(frame,handlms,mp_hand.HAND_CONNECTIONS)
             

    if not ret:
        break
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()