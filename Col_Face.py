import cv2


name=input("Please Enter your Name")
enroll_no=input("Enter your Enrollment NUmber")
print("Your Face recognition process will be starting...")
file=open('Attendence.txt','a')
cap = cv2.VideoCapture(0)
# cap=cv2.imread('C:\\Users\\modip\\Desktop\\Project\\000028_0.jpg',cv2.IMREAD_COLOR)

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("C:\\Users\\modip\\Desktop\\New folder\\classifier\\cascade.xml")

# while(True):
	# Capture frame-by-frame
ret, frame = cap.read()

# Our operations on the frame come here
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
	gray,
	scaleFactor=1.1,
	minNeighbors=5,
	minSize=(30, 30)
	#flags = cv2.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
	cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	no=enroll_no[-1:-3]
	file.write(f"Name= {name}\n")
	file.write(f"Enrollment NO= {str(enroll_no)}\n")
	file.write('\n--------------------------------------------------------------------\n')
	print("Your Track recorded successfully!!")


# Display the resulting frame
cv2.imshow('frame', frame)
# if cv2.waitKey(1) & 0xFF == ord('q'):
# 	# break

# When everything done, release the capture
file.close()
cap.release()
cv2.destroyAllWindows()

