from sub import gamesystem 
import sys
import PySide6.QtCore as Qc
import PySide6.QtWidgets as Qw



class MainWindow(Qw.QMainWindow):

  def __init__(self):
    
    super().__init__() 
    self.setWindowTitle('夢ノ中') 
    self.setGeometry(1000, 100, 400, 300) 

    self.btn_start = Qw.QPushButton('1',self)
    self.btn_start.setGeometry(10,20,100,30)
    self.btn_start.clicked.connect(self.btn_start_clicked)

    self.btn_2 = Qw.QPushButton('2',self)
    self.btn_2.setGeometry(120,20,100,30)
    self.btn_2.clicked.connect(self.btn_2_clicked)

    central_widget = Qw.QWidget(self)
    self.setCentralWidget(central_widget)
    main_layout = Qw.QVBoxLayout(central_widget) # 垂直レイアウト

    self.lb_yume = Qw.QLabel(self)
    self.lb_yume.setGeometry(10,60,380,50)
    self.lb_yume.setText(f'{game.sceneNow.lines}')
    self.lb_yume.setStyleSheet('background-color: #000000; color: #FFFFFF')
    main_layout.addWidget(self.lb_yume)

    self.tb_log = Qw.QTextEdit('',self)
    self.tb_log.setGeometry(10,120,380,140)
    self.tb_log.setReadOnly(True)
    main_layout.addWidget(self.tb_log)

    self.tb_talk = Qw.QLineEdit('',self)
    self.tb_talk.setGeometry(10,260,340,30)
    self.tb_talk.setPlaceholderText('入力')
    # self.tb_talk.textEdited.connect(self.tb_talk_textedited)
    main_layout.addWidget(self.tb_talk)

    self.btn_talk = Qw.QPushButton('話す',self)
    self.btn_talk.setGeometry(355,260,35,30)
    self.btn_talk.clicked.connect(self.btn_talk_clicked)
    # self.btn_talk.setEnabled(False)
    main_layout.addWidget(self.btn_talk)

  def btn_start_clicked(self):
    pass

  def btn_2_clicked(self):
    pass
    
  # def tb_talk_textedited(self):
  #   self.btn_talk.setEnabled(True)
  def btn_talk_clicked(self):
    text = self.tb_talk.text()
    textcheck = game.text_checker(text,game.sceneNow)
    if textcheck == 0:
      game.sceneNow = game.scene[game.sceneNow.Os]
    elif textcheck == 1:
      game.sceneNow = game.scene[game.sceneNow.Ts]
    elif textcheck == 2:
      game.sceneNow = game.scene[game.sceneNow.Fs]
    log = self.tb_log.toPlainText()
    log = self.lb_yume.text() + '\n\n' + log
    if text != '':
      log = text + '\n' + '\n' +log
    self.tb_log.setPlainText(log)
    self.tb_talk.setText('')
    self.lb_yume.setText(f'{game.sceneNow.lines}')


# 本体
if __name__ == '__main__':
  game = gamesystem()
  app = Qw.QApplication(sys.argv)
  main_window = MainWindow()
  main_window.show()
  sys.exit(app.exec())