import time
from plyer import notification

if __name__=="__main__":
	n_title = input("title of notification here:")
	n_message = input("description here:") 
	while True:
		notification.notify(
			title = n_title,
			message= n_message,
			timeout=5
		)
		time.sleep(5)
		break;