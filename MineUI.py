# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MineUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(824, 695)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/MineWechat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.groupBox_login = QtWidgets.QGroupBox(Form)
        self.groupBox_login.setGeometry(QtCore.QRect(225, 589, 581, 88))
        self.groupBox_login.setObjectName("groupBox_login")
        self.textEdit_output = QtWidgets.QTextEdit(self.groupBox_login)
        self.textEdit_output.setGeometry(QtCore.QRect(1, 18, 580, 70))
        self.textEdit_output.setObjectName("textEdit_output")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(225, 10, 581, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.chat_friend = QtWidgets.QWidget()
        self.chat_friend.setObjectName("chat_friend")
        self.groupBox_friend_record = QtWidgets.QGroupBox(self.chat_friend)
        self.groupBox_friend_record.setGeometry(QtCore.QRect(13, 8, 550, 300))
        self.groupBox_friend_record.setObjectName("groupBox_friend_record")
        self.textEdit_friend_record = QtWidgets.QTextEdit(self.groupBox_friend_record)
        self.textEdit_friend_record.setGeometry(QtCore.QRect(0, 18, 550, 282))
        self.textEdit_friend_record.setObjectName("textEdit_friend_record")
        self.groupBox_text_friend = QtWidgets.QGroupBox(self.chat_friend)
        self.groupBox_text_friend.setGeometry(QtCore.QRect(13, 340, 550, 191))
        self.groupBox_text_friend.setObjectName("groupBox_text_friend")
        self.textEdit_text_friend = QtWidgets.QTextEdit(self.groupBox_text_friend)
        self.textEdit_text_friend.setGeometry(QtCore.QRect(1, 18, 549, 80))
        self.textEdit_text_friend.setObjectName("textEdit_text_friend")
        self.pushButton_text_friend = QtWidgets.QPushButton(self.groupBox_text_friend)
        self.pushButton_text_friend.setGeometry(QtCore.QRect(280, 150, 261, 23))
        self.pushButton_text_friend.setObjectName("pushButton_text_friend")
        self.lineEdit_text_friend = QtWidgets.QLineEdit(self.groupBox_text_friend)
        self.lineEdit_text_friend.setGeometry(QtCore.QRect(90, 120, 451, 20))
        self.lineEdit_text_friend.setText("")
        self.lineEdit_text_friend.setCursorPosition(0)
        self.lineEdit_text_friend.setPlaceholderText("")
        self.lineEdit_text_friend.setObjectName("lineEdit_text_friend")
        self.pushButton_text_helper = QtWidgets.QPushButton(self.groupBox_text_friend)
        self.pushButton_text_helper.setGeometry(QtCore.QRect(10, 150, 261, 23))
        self.pushButton_text_helper.setObjectName("pushButton_text_helper")
        self.label_text_friend = QtWidgets.QLabel(self.groupBox_text_friend)
        self.label_text_friend.setGeometry(QtCore.QRect(10, 122, 71, 16))
        self.label_text_friend.setObjectName("label_text_friend")
        self.tabWidget.addTab(self.chat_friend, "")
        self.chat_chatroom = QtWidgets.QWidget()
        self.chat_chatroom.setObjectName("chat_chatroom")
        self.groupBox_text_chatroom = QtWidgets.QGroupBox(self.chat_chatroom)
        self.groupBox_text_chatroom.setGeometry(QtCore.QRect(13, 340, 550, 190))
        self.groupBox_text_chatroom.setObjectName("groupBox_text_chatroom")
        self.textEdit_text_chatroom = QtWidgets.QTextEdit(self.groupBox_text_chatroom)
        self.textEdit_text_chatroom.setGeometry(QtCore.QRect(1, 18, 549, 82))
        self.textEdit_text_chatroom.setObjectName("textEdit_text_chatroom")
        self.pushButton_text_chatroom = QtWidgets.QPushButton(self.groupBox_text_chatroom)
        self.pushButton_text_chatroom.setGeometry(QtCore.QRect(10, 150, 530, 23))
        self.pushButton_text_chatroom.setObjectName("pushButton_text_chatroom")
        self.lineEdit_text_chatroom = QtWidgets.QLineEdit(self.groupBox_text_chatroom)
        self.lineEdit_text_chatroom.setGeometry(QtCore.QRect(90, 120, 450, 20))
        self.lineEdit_text_chatroom.setObjectName("lineEdit_text_chatroom")
        self.label_text_chatroom = QtWidgets.QLabel(self.groupBox_text_chatroom)
        self.label_text_chatroom.setGeometry(QtCore.QRect(10, 122, 71, 16))
        self.label_text_chatroom.setObjectName("label_text_chatroom")
        self.groupBox_chatroom_record = QtWidgets.QGroupBox(self.chat_chatroom)
        self.groupBox_chatroom_record.setGeometry(QtCore.QRect(13, 8, 550, 300))
        self.groupBox_chatroom_record.setObjectName("groupBox_chatroom_record")
        self.textEdit_chatroom_record = QtWidgets.QTextEdit(self.groupBox_chatroom_record)
        self.textEdit_chatroom_record.setGeometry(QtCore.QRect(0, 18, 550, 282))
        self.textEdit_chatroom_record.setObjectName("textEdit_chatroom_record")
        self.tabWidget.addTab(self.chat_chatroom, "")
        self.file_send = QtWidgets.QWidget()
        self.file_send.setObjectName("file_send")
        self.groupBox_file_dir = QtWidgets.QGroupBox(self.file_send)
        self.groupBox_file_dir.setGeometry(QtCore.QRect(13, 180, 550, 111))
        self.groupBox_file_dir.setObjectName("groupBox_file_dir")
        self.lineEdit_file_dir = QtWidgets.QLineEdit(self.groupBox_file_dir)
        self.lineEdit_file_dir.setGeometry(QtCore.QRect(90, 70, 450, 20))
        self.lineEdit_file_dir.setObjectName("lineEdit_file_dir")
        self.label_file_dir = QtWidgets.QLabel(self.groupBox_file_dir)
        self.label_file_dir.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_file_dir.setObjectName("label_file_dir")
        self.pushButton_open_file = QtWidgets.QPushButton(self.groupBox_file_dir)
        self.pushButton_open_file.setGeometry(QtCore.QRect(10, 30, 530, 23))
        self.pushButton_open_file.setObjectName("pushButton_open_file")
        self.groupBox_file_send = QtWidgets.QGroupBox(self.file_send)
        self.groupBox_file_send.setGeometry(QtCore.QRect(13, 300, 550, 231))
        self.groupBox_file_send.setObjectName("groupBox_file_send")
        self.lineEdit_file_chatroom = QtWidgets.QLineEdit(self.groupBox_file_send)
        self.lineEdit_file_chatroom.setGeometry(QtCore.QRect(90, 160, 450, 20))
        self.lineEdit_file_chatroom.setObjectName("lineEdit_file_chatroom")
        self.label_file_friend = QtWidgets.QLabel(self.groupBox_file_send)
        self.label_file_friend.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.label_file_friend.setObjectName("label_file_friend")
        self.lineEdit_file_friend = QtWidgets.QLineEdit(self.groupBox_file_send)
        self.lineEdit_file_friend.setGeometry(QtCore.QRect(90, 80, 450, 20))
        self.lineEdit_file_friend.setObjectName("lineEdit_file_friend")
        self.pushButton_file_friend = QtWidgets.QPushButton(self.groupBox_file_send)
        self.pushButton_file_friend.setGeometry(QtCore.QRect(10, 110, 530, 23))
        self.pushButton_file_friend.setObjectName("pushButton_file_friend")
        self.label_file_chatroom = QtWidgets.QLabel(self.groupBox_file_send)
        self.label_file_chatroom.setGeometry(QtCore.QRect(10, 160, 71, 16))
        self.label_file_chatroom.setObjectName("label_file_chatroom")
        self.pushButton_file_chatroom = QtWidgets.QPushButton(self.groupBox_file_send)
        self.pushButton_file_chatroom.setGeometry(QtCore.QRect(10, 190, 530, 23))
        self.pushButton_file_chatroom.setObjectName("pushButton_file_chatroom")
        self.pushButton_file_helper = QtWidgets.QPushButton(self.groupBox_file_send)
        self.pushButton_file_helper.setGeometry(QtCore.QRect(10, 30, 530, 23))
        self.pushButton_file_helper.setObjectName("pushButton_file_helper")
        self.groupBox_send_record = QtWidgets.QGroupBox(self.file_send)
        self.groupBox_send_record.setGeometry(QtCore.QRect(13, 8, 551, 151))
        self.groupBox_send_record.setObjectName("groupBox_send_record")
        self.textEdit_send_record = QtWidgets.QTextEdit(self.groupBox_send_record)
        self.textEdit_send_record.setGeometry(QtCore.QRect(1, 18, 549, 133))
        self.textEdit_send_record.setObjectName("textEdit_send_record")
        self.tabWidget.addTab(self.file_send, "")
        self.remote = QtWidgets.QWidget()
        self.remote.setObjectName("remote")
        self.groupBox_remote = QtWidgets.QGroupBox(self.remote)
        self.groupBox_remote.setGeometry(QtCore.QRect(13, 8, 550, 521))
        self.groupBox_remote.setObjectName("groupBox_remote")
        self.checkBox_remote = QtWidgets.QCheckBox(self.groupBox_remote)
        self.checkBox_remote.setGeometry(QtCore.QRect(20, 25, 441, 17))
        self.checkBox_remote.setObjectName("checkBox_remote")
        self.textEdit_remote = QtWidgets.QTextEdit(self.groupBox_remote)
        self.textEdit_remote.setGeometry(QtCore.QRect(1, 50, 549, 471))
        self.textEdit_remote.setObjectName("textEdit_remote")
        self.tabWidget.addTab(self.remote, "")
        self.option = QtWidgets.QWidget()
        self.option.setObjectName("option")
        self.groupBox_option = QtWidgets.QGroupBox(self.option)
        self.groupBox_option.setGeometry(QtCore.QRect(13, 8, 550, 521))
        self.groupBox_option.setObjectName("groupBox_option")
        self.checkBox_busy = QtWidgets.QCheckBox(self.groupBox_option)
        self.checkBox_busy.setGeometry(QtCore.QRect(30, 30, 111, 17))
        self.checkBox_busy.setObjectName("checkBox_busy")
        self.checkBox_robot = QtWidgets.QCheckBox(self.groupBox_option)
        self.checkBox_robot.setGeometry(QtCore.QRect(30, 90, 101, 17))
        self.checkBox_robot.setObjectName("checkBox_robot")
        self.lineEdit_busy = QtWidgets.QLineEdit(self.groupBox_option)
        self.lineEdit_busy.setGeometry(QtCore.QRect(150, 50, 361, 20))
        self.lineEdit_busy.setObjectName("lineEdit_busy")
        self.label_busy = QtWidgets.QLabel(self.groupBox_option)
        self.label_busy.setGeometry(QtCore.QRect(30, 50, 101, 20))
        self.label_busy.setObjectName("label_busy")
        self.tabWidget.addTab(self.option, "")
        self.help = QtWidgets.QWidget()
        self.help.setObjectName("help")
        self.groupBox_help = QtWidgets.QGroupBox(self.help)
        self.groupBox_help.setGeometry(QtCore.QRect(13, 8, 550, 520))
        self.groupBox_help.setObjectName("groupBox_help")
        self.textEdit_help = QtWidgets.QTextEdit(self.groupBox_help)
        self.textEdit_help.setGeometry(QtCore.QRect(1, 18, 549, 502))
        self.textEdit_help.setObjectName("textEdit_help")
        self.tabWidget.addTab(self.help, "")
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(12, 10, 200, 570))
        self.toolBox.setObjectName("toolBox")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setGeometry(QtCore.QRect(0, 0, 200, 518))
        self.page_1.setObjectName("page_1")
        self.listView_friend = QtWidgets.QListView(self.page_1)
        self.listView_friend.setGeometry(QtCore.QRect(-1, -1, 200, 511))
        self.listView_friend.setObjectName("listView_friend")
        self.toolBox.addItem(self.page_1, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 200, 518))
        self.page_2.setObjectName("page_2")
        self.listView_chatroom = QtWidgets.QListView(self.page_2)
        self.listView_chatroom.setGeometry(QtCore.QRect(-1, -1, 200, 511))
        self.listView_chatroom.setObjectName("listView_chatroom")
        self.toolBox.addItem(self.page_2, "")
        self.pushButton_login = QtWidgets.QPushButton(Form)
        self.pushButton_login.setGeometry(QtCore.QRect(20, 610, 180, 23))
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_logout = QtWidgets.QPushButton(Form)
        self.pushButton_logout.setGeometry(QtCore.QRect(20, 650, 180, 23))
        self.pushButton_logout.setObjectName("pushButton_logout")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(5)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MineWechat"))
        self.groupBox_login.setTitle(_translate("Form", "系统信息"))
        self.groupBox_friend_record.setTitle(_translate("Form", "私聊记录"))
        self.groupBox_text_friend.setTitle(_translate("Form", "发送文字"))
        self.textEdit_text_friend.setPlaceholderText(_translate("Form", "输入消息："))
        self.pushButton_text_friend.setText(_translate("Form", "发送至好友"))
        self.pushButton_text_helper.setText(_translate("Form", "发送至文件传输助手"))
        self.label_text_friend.setText(_translate("Form", "好友昵称："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.chat_friend), _translate("Form", "微信私聊"))
        self.groupBox_text_chatroom.setTitle(_translate("Form", "发送文字"))
        self.textEdit_text_chatroom.setPlaceholderText(_translate("Form", "可以@群里的某人"))
        self.pushButton_text_chatroom.setText(_translate("Form", "发至群聊"))
        self.label_text_chatroom.setText(_translate("Form", "群聊名称："))
        self.groupBox_chatroom_record.setTitle(_translate("Form", "群聊@记录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.chat_chatroom), _translate("Form", "微信群聊"))
        self.groupBox_file_dir.setTitle(_translate("Form", "选取文件"))
        self.label_file_dir.setText(_translate("Form", "文件目录："))
        self.pushButton_open_file.setText(_translate("Form", "点击选择文件（暂不支持中文文件名）"))
        self.groupBox_file_send.setTitle(_translate("Form", "发送文件"))
        self.label_file_friend.setText(_translate("Form", "好友昵称："))
        self.pushButton_file_friend.setText(_translate("Form", "发给好友"))
        self.label_file_chatroom.setText(_translate("Form", "群聊名称："))
        self.pushButton_file_chatroom.setText(_translate("Form", "发至群聊"))
        self.pushButton_file_helper.setText(_translate("Form", "发送至文件传输助手"))
        self.groupBox_send_record.setTitle(_translate("Form", "发送记录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.file_send), _translate("Form", "发送文件"))
        self.groupBox_remote.setTitle(_translate("Form", "远程控制"))
        self.checkBox_remote.setText(_translate("Form", "手机端微信控制此电脑"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.remote), _translate("Form", "远程控制"))
        self.groupBox_option.setTitle(_translate("Form", "功能选项"))
        self.checkBox_busy.setText(_translate("Form", "忙碌回复"))
        self.checkBox_robot.setText(_translate("Form", "机器人回复"))
        self.label_busy.setText(_translate("Form", "编辑回复内容："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.option), _translate("Form", "功能选项"))
        self.groupBox_help.setTitle(_translate("Form", "帮助信息"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.help), _translate("Form", "帮助信息"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_1), _translate("Form", "好友列表"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "群聊列表"))
        self.pushButton_login.setText(_translate("Form", "扫码登录"))
        self.pushButton_logout.setText(_translate("Form", "注销退出"))

import img_rc
