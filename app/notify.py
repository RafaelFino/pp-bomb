import sys
from win10toast import ToastNotifier

toaster = ToastNotifier()

qty = int(sys.argv[1])

for x in range(qty)    
    toaster.show_toast("Notificacao do PP","Notificação " + str(x) + "/" + str(qty))