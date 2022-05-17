from PyQt5.QtWidgets import QApplication,QMainWindow,QTextEdit
import sys


class Main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,900,700)

        self.main_input=QTextEdit(self)
        self.main_input.setGeometry(0,0,self.width(),self.height())
        
        




if __name__=="__main__":
    app=QApplication(sys.argv)

    main_window=Main_window()
    main_window.show()

    sys.exit(app.exec_())
    