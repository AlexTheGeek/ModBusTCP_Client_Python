# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from pymodbus.client.sync import ModbusTcpClient as ModbusClient

server_host = str(sys.argv[1])
server_port = int(sys.argv[2])

DEFAULT_STYLE = """
QProgressBar{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center;
    height: 10px;
    width: 10px;
}

QProgressBar::chunk {
    background-color: lightblue;
}
"""

COMPLETED_STYLE = """
QProgressBar{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center;
    height: 10px;
    width: 10px;
}

QProgressBar::chunk {
    background-color: red;
}
"""




class Monitoring(QWidget):
    def __init__(self):
        super().__init__()
        self.InitGUI()

    def InitGUI(self):
        self.setWindowTitle("ModBusTCP Client")
        self.resize(640,100)


        self.bt1 = QPushButton("1 to Coil Outputs 0",self)
        self.bt1.clicked.connect(self.abt1)
        self.bt1.move(0,50)

        self.bt2 = QPushButton("0 to Coil Outputs 0",self)
        self.bt2.clicked.connect(self.abt2)
        self.bt2.move(0,50)

        self.bt3 = QPushButton("toggle Coil Outputs 0",self)
        self.bt3.clicked.connect(self.abt3)
        self.bt3.move(0,50)


        self.Psatus = QProgressBar(self,maximum=32767,textVisible=False)
        self.Plabel = QLabel('Valeur HR 40001',self)

        self.Lstatus = QProgressBar(self,maximum=1,textVisible=False)
        self.Llabel = QLabel ('LIGHT',self)
        self.Lstatus.setStyleSheet(DEFAULT_STYLE)

        self.infolayout = QGridLayout(self)
        self.infolayout.addWidget(self.Plabel,0,0)
        self.infolayout.addWidget(self.Psatus,0,1)
        self.infolayout.addWidget(self.Lstatus,1,1)
        self.infolayout.addWidget(self.Llabel,1,0)
        self.infolayout.setHorizontalSpacing(40)
        self.infolayout.addWidget(self.bt1,0,3)
        self.infolayout.addWidget(self.bt2,1,3)
        self.infolayout.addWidget(self.bt3,2,3)

        self.show()


    def setPval(self,val):
        self.Psatus.setValue(val)


    def setLval(self,val):
        if val == 10000:
            self.Lstatus.setValue(1)
            self.Lstatus.setStyleSheet(COMPLETED_STYLE)
        else:
            self.Lstatus.setValue(0)



    def abt1(self):
        client.write_coil(0, 1, unit = 1)

    def abt2(self):
        client.write_coil(0, 0, unit = 1)

    def abt3(self):
        regs2 = client.read_coils(0,1,unit=1)
        if regs2.bits[0]:
            client.write_coil(0, 0, unit = 1)
        else:
            client.write_coil(0, 1, unit = 1)


def affiche():
    regs = client.read_holding_registers(0,5,unit=1)
    IHM.setPval(int(regs.registers[0]))
    IHM.setLval(int(regs.registers[0]))


if __name__ == '__main__':
    client = ModbusClient(host=server_host, port=server_port)
    client.connect()
    app = QApplication(sys.argv)
    IHM=Monitoring()
    timer=QTimer()
    timer.timeout.connect(affiche)
    timer.start(100)
    app.exec()
