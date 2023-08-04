import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
    # initialize pyQT
    app = QApplication( sys.argv )
    widget = QWidget()

    # create a label, set it's text and position in the window
    textLabel = QLabel(widget)
    textLabel.setText( "Hello World" )
    textLabel.move( 110, 85 )

    # set window startin position and window size
    widget.setGeometry( 50, 50, 320, 200 )
    # set window title
    widget.setWindowTitle( "PyQt5 Hello World App" )
    # display window
    widget.show()
    sys.exit( app.exec_() )

if __name__ == '__main__':
    window()