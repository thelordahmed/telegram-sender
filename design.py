# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(634, 966)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.container_tabwid = QTabWidget(self.centralwidget)
        self.container_tabwid.setObjectName(u"container_tabwid")
        self.container_tabwid.setTabPosition(QTabWidget.West)
        self.anonymous = QWidget()
        self.anonymous.setObjectName(u"anonymous")
        self.verticalLayout_9 = QVBoxLayout(self.anonymous)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.tabWidget = QTabWidget(self.anonymous)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabBar::tab{\n"
"	padding:10px 15px;\n"
"	font-weight:bold\n"
"}\n"
"\n"
"")
        self.tabWidget.setIconSize(QSize(15, 15))
        self.accounts = QWidget()
        self.accounts.setObjectName(u"accounts")
        self.verticalLayout_16 = QVBoxLayout(self.accounts)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.accounts_listwidget = QListWidget(self.accounts)
        self.accounts_listwidget.setObjectName(u"accounts_listwidget")

        self.verticalLayout_16.addWidget(self.accounts_listwidget)

        self.frame = QFrame(self.accounts)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout_11 = QHBoxLayout(self.frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.addAccount_btn = QPushButton(self.frame)
        self.addAccount_btn.setObjectName(u"addAccount_btn")
        self.addAccount_btn.setStyleSheet(u"padding:10px 0")

        self.horizontalLayout_11.addWidget(self.addAccount_btn)

        self.removeAccount_btn = QPushButton(self.frame)
        self.removeAccount_btn.setObjectName(u"removeAccount_btn")
        self.removeAccount_btn.setStyleSheet(u"padding:10px 0")

        self.horizontalLayout_11.addWidget(self.removeAccount_btn)


        self.verticalLayout_16.addWidget(self.frame)

        icon = QIcon()
        icon.addFile(u":/black-icons/Data/imgs/black icons/icons8-male-user-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.accounts, icon, "")
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.verticalLayout_7 = QVBoxLayout(self.main)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_3 = QGroupBox(self.main)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamily(u"arial")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(u"QGroupBox{\n"
"background:transparent;\n"
"}")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.groupBox_3.setFlat(False)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 20, -1, 20)
        self.phone_rb = QRadioButton(self.groupBox_3)
        self.phone_rb.setObjectName(u"phone_rb")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.phone_rb.sizePolicy().hasHeightForWidth())
        self.phone_rb.setSizePolicy(sizePolicy1)
        self.phone_rb.setChecked(True)

        self.horizontalLayout_2.addWidget(self.phone_rb)

        self.username_rb = QRadioButton(self.groupBox_3)
        self.username_rb.setObjectName(u"username_rb")
        sizePolicy1.setHeightForWidth(self.username_rb.sizePolicy().hasHeightForWidth())
        self.username_rb.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.username_rb)


        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.groupBox_9 = QGroupBox(self.main)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.groupBox_9.setFont(font1)
        self.groupBox_9.setAlignment(Qt.AlignCenter)
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 0, -1, 10)
        self.groupBox = QGroupBox(self.groupBox_9)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textFirst_rb = QRadioButton(self.groupBox)
        self.textFirst_rb.setObjectName(u"textFirst_rb")
        self.textFirst_rb.setChecked(True)

        self.verticalLayout_3.addWidget(self.textFirst_rb)

        self.attachFirst_rb = QRadioButton(self.groupBox)
        self.attachFirst_rb.setObjectName(u"attachFirst_rb")

        self.verticalLayout_3.addWidget(self.attachFirst_rb)


        self.horizontalLayout_16.addWidget(self.groupBox)

        self.groupBox_10 = QGroupBox(self.groupBox_9)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy1.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.messages_sb = QSpinBox(self.groupBox_10)
        self.messages_sb.setObjectName(u"messages_sb")
        sizePolicy1.setHeightForWidth(self.messages_sb.sizePolicy().hasHeightForWidth())
        self.messages_sb.setSizePolicy(sizePolicy1)
        self.messages_sb.setMinimumSize(QSize(0, 0))
        self.messages_sb.setMaximumSize(QSize(60, 16777215))
        self.messages_sb.setStyleSheet(u"")
        self.messages_sb.setValue(30)

        self.horizontalLayout.addWidget(self.messages_sb)


        self.horizontalLayout_16.addWidget(self.groupBox_10)


        self.verticalLayout_17.addLayout(self.horizontalLayout_16)


        self.verticalLayout_7.addWidget(self.groupBox_9)

        self.groupBox_4 = QGroupBox(self.main)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_4.setFont(font1)
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.groupBox_4.setFlat(False)
        self.formLayout = QFormLayout(self.groupBox_4)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.attachments_le = QLineEdit(self.groupBox_4)
        self.attachments_le.setObjectName(u"attachments_le")
        self.attachments_le.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.attachments_le)

        self.attachments_btn = QToolButton(self.groupBox_4)
        self.attachments_btn.setObjectName(u"attachments_btn")

        self.horizontalLayout_3.addWidget(self.attachments_btn)


        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.horizontalLayout_3)


        self.verticalLayout_7.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.main)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy3)
        self.groupBox_5.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_5.setFont(font1)
        self.groupBox_5.setAlignment(Qt.AlignCenter)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 5, -1, 5)
        self.frame1 = QFrame(self.groupBox_5)
        self.frame1.setObjectName(u"frame1")
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.horizontalLayout_7 = QHBoxLayout(self.frame1)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(1, 1, -1, -1)
        self.pushButton = QPushButton(self.frame1)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_7.addWidget(self.pushButton)

        self.append_newmessage = QPushButton(self.frame1)
        self.append_newmessage.setObjectName(u"append_newmessage")

        self.horizontalLayout_7.addWidget(self.append_newmessage)


        self.verticalLayout_6.addWidget(self.frame1)

        self.message_text = QPlainTextEdit(self.groupBox_5)
        self.message_text.setObjectName(u"message_text")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.message_text.sizePolicy().hasHeightForWidth())
        self.message_text.setSizePolicy(sizePolicy4)
        self.message_text.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_6.addWidget(self.message_text)


        self.verticalLayout_7.addWidget(self.groupBox_5)

        self.verticalLayout_7.setStretch(3, 1)
        icon1 = QIcon()
        icon1.addFile(u":/black-icons/Data/imgs/black icons/icons8-home-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.main, icon1, "")
        self.report = QWidget()
        self.report.setObjectName(u"report")
        self.verticalLayout_2 = QVBoxLayout(self.report)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self.report)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        icon2 = QIcon()
        icon2.addFile(u":/black-icons/Data/imgs/black icons/icons8-contacts-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setIcon(icon2);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        icon3 = QIcon()
        icon3.addFile(u":/black-icons/Data/imgs/black icons/icons8-circled-right-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setIcon(icon3);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        icon4 = QIcon()
        icon4.addFile(u":/black-icons/Data/imgs/black icons/icons8-call-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setIcon(icon4);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        icon5 = QIcon()
        icon5.addFile(u":/black-icons/Data/imgs/black icons/icons8-info-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setIcon(icon5);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(493, 0))
        self.tableWidget.setMaximumSize(QSize(493, 16777215))
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.sheet_btn = QPushButton(self.report)
        self.sheet_btn.setObjectName(u"sheet_btn")
        self.sheet_btn.setStyleSheet(u"padding:15px 0")
        icon6 = QIcon()
        icon6.addFile(u":/black-icons/Data/imgs/black icons/icons8-hospital-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sheet_btn.setIcon(icon6)
        self.sheet_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.sheet_btn)

        self.newSession_btn = QPushButton(self.report)
        self.newSession_btn.setObjectName(u"newSession_btn")
        sizePolicy1.setHeightForWidth(self.newSession_btn.sizePolicy().hasHeightForWidth())
        self.newSession_btn.setSizePolicy(sizePolicy1)
        self.newSession_btn.setStyleSheet(u"padding:10px 20px")
        icon7 = QIcon()
        icon7.addFile(u":/black-icons/Data/imgs/black icons/icons8-trash-can-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newSession_btn.setIcon(icon7)

        self.verticalLayout_2.addWidget(self.newSession_btn, 0, Qt.AlignHCenter)

        icon8 = QIcon()
        icon8.addFile(u":/black-icons/Data/imgs/black icons/icons8-combo-chart-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.report, icon8, "")
        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.verticalLayout_8 = QVBoxLayout(self.about)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 50, -1, -1)
        self.textEdit_2 = QTextEdit(self.about)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 140))
        self.textEdit_2.setStyleSheet(u"background:transparent;\n"
"\n"
"\n"
"")
        self.textEdit_2.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_10.addWidget(self.textEdit_2)

        self.textBrowser_4 = QTextBrowser(self.about)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        font2 = QFont()
        font2.setFamily(u"arial")
        self.textBrowser_4.setFont(font2)
        self.textBrowser_4.setStyleSheet(u"background:transparent;\n"
"border:transparent\n"
"\n"
"")
        self.textBrowser_4.setOpenExternalLinks(True)

        self.verticalLayout_10.addWidget(self.textBrowser_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_10)

        icon9 = QIcon()
        icon9.addFile(u":/black-icons/Data/imgs/black icons/icons8-about-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.about, icon9, "")

        self.verticalLayout_9.addWidget(self.tabWidget)

        self.horizontalFrame = QFrame(self.anonymous)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy1.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy1)
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.start_btn = QPushButton(self.horizontalFrame)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setMaximumSize(QSize(16777215, 45))
        icon10 = QIcon()
        icon10.addFile(u":/black-icons/Data/imgs/black icons/icons8-play-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_btn.setIcon(icon10)
        self.start_btn.setIconSize(QSize(34, 48))

        self.horizontalLayout_10.addWidget(self.start_btn)

        self.stop_btn = QPushButton(self.horizontalFrame)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setMaximumSize(QSize(16777215, 45))
        icon11 = QIcon()
        icon11.addFile(u":/black-icons/Data/imgs/black icons/icons8-stop-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_btn.setIcon(icon11)
        self.stop_btn.setIconSize(QSize(38, 37))

        self.horizontalLayout_10.addWidget(self.stop_btn)


        self.verticalLayout_9.addWidget(self.horizontalFrame, 0, Qt.AlignHCenter)

        self.container_tabwid.addTab(self.anonymous, "")
        self.familiar = QWidget()
        self.familiar.setObjectName(u"familiar")
        self.verticalLayout_15 = QVBoxLayout(self.familiar)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, -1, -1, 0)
        self.tabWidget_2 = QTabWidget(self.familiar)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setStyleSheet(u"QTabBar::tab{\n"
"	padding:10px 15px;\n"
"	font-weight:bold\n"
"}\n"
"\n"
"")
        self.tabWidget_2.setIconSize(QSize(15, 15))
        self.main_2 = QWidget()
        self.main_2.setObjectName(u"main_2")
        self.verticalLayout_11 = QVBoxLayout(self.main_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 12, -1, 0)
        self.groupBox_6 = QGroupBox(self.main_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet(u"QGroupBox{\n"
"background:transparent;\n"
"}")
        self.groupBox_6.setAlignment(Qt.AlignCenter)
        self.groupBox_6.setFlat(False)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 20, -1, 20)
        self.phone_rb_2 = QRadioButton(self.groupBox_6)
        self.phone_rb_2.setObjectName(u"phone_rb_2")
        sizePolicy1.setHeightForWidth(self.phone_rb_2.sizePolicy().hasHeightForWidth())
        self.phone_rb_2.setSizePolicy(sizePolicy1)
        self.phone_rb_2.setChecked(True)

        self.horizontalLayout_5.addWidget(self.phone_rb_2)

        self.username_rb_2 = QRadioButton(self.groupBox_6)
        self.username_rb_2.setObjectName(u"username_rb_2")
        sizePolicy1.setHeightForWidth(self.username_rb_2.sizePolicy().hasHeightForWidth())
        self.username_rb_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.username_rb_2)


        self.verticalLayout_11.addWidget(self.groupBox_6)

        self.groupBox_2 = QGroupBox(self.main_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font1)
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_11 = QGroupBox(self.groupBox_2)
        self.groupBox_11.setObjectName(u"groupBox_11")
        sizePolicy2.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy2)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.textFirst_rb_2 = QRadioButton(self.groupBox_11)
        self.textFirst_rb_2.setObjectName(u"textFirst_rb_2")
        self.textFirst_rb_2.setChecked(True)

        self.verticalLayout_4.addWidget(self.textFirst_rb_2)

        self.attachFirst_rb_2 = QRadioButton(self.groupBox_11)
        self.attachFirst_rb_2.setObjectName(u"attachFirst_rb_2")

        self.verticalLayout_4.addWidget(self.attachFirst_rb_2)


        self.horizontalLayout_4.addWidget(self.groupBox_11)


        self.verticalLayout_11.addWidget(self.groupBox_2)

        self.groupBox_7 = QGroupBox(self.main_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_7.setFont(font1)
        self.groupBox_7.setAlignment(Qt.AlignCenter)
        self.groupBox_7.setFlat(False)
        self.formLayout_2 = QFormLayout(self.groupBox_7)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(5)
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.attachments_le_2 = QLineEdit(self.groupBox_7)
        self.attachments_le_2.setObjectName(u"attachments_le_2")
        self.attachments_le_2.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.attachments_le_2)

        self.attachments_btn_2 = QToolButton(self.groupBox_7)
        self.attachments_btn_2.setObjectName(u"attachments_btn_2")

        self.horizontalLayout_8.addWidget(self.attachments_btn_2)


        self.formLayout_2.setLayout(0, QFormLayout.SpanningRole, self.horizontalLayout_8)


        self.verticalLayout_11.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.main_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy)
        self.groupBox_8.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_8.setFont(font1)
        self.groupBox_8.setAlignment(Qt.AlignCenter)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, -1, -1)
        self.pushButton_2 = QPushButton(self.groupBox_8)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_9.addWidget(self.pushButton_2)

        self.append_newmessage_2 = QPushButton(self.groupBox_8)
        self.append_newmessage_2.setObjectName(u"append_newmessage_2")

        self.horizontalLayout_9.addWidget(self.append_newmessage_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_9)

        self.message_text_2 = QPlainTextEdit(self.groupBox_8)
        self.message_text_2.setObjectName(u"message_text_2")
        self.message_text_2.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_12.addWidget(self.message_text_2)


        self.verticalLayout_11.addWidget(self.groupBox_8)

        self.verticalLayout_11.setStretch(3, 1)
        self.tabWidget_2.addTab(self.main_2, icon1, "")
        self.report_2 = QWidget()
        self.report_2.setObjectName(u"report_2")
        self.verticalLayout_5 = QVBoxLayout(self.report_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableWidget_2 = QTableWidget(self.report_2)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setIcon(icon2);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        icon12 = QIcon()
        icon12.addFile(u":/black-icons/Data/imgs/black icons/icons8-phone-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setIcon(icon12);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setIcon(icon5);
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(125)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)

        self.verticalLayout_5.addWidget(self.tableWidget_2)

        self.sheet_btn_2 = QPushButton(self.report_2)
        self.sheet_btn_2.setObjectName(u"sheet_btn_2")
        self.sheet_btn_2.setStyleSheet(u"padding:15px 0")
        self.sheet_btn_2.setIcon(icon6)
        self.sheet_btn_2.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.sheet_btn_2)

        self.newSession_btn_2 = QPushButton(self.report_2)
        self.newSession_btn_2.setObjectName(u"newSession_btn_2")
        sizePolicy1.setHeightForWidth(self.newSession_btn_2.sizePolicy().hasHeightForWidth())
        self.newSession_btn_2.setSizePolicy(sizePolicy1)
        self.newSession_btn_2.setStyleSheet(u"padding:10px 20px")
        self.newSession_btn_2.setIcon(icon7)

        self.verticalLayout_5.addWidget(self.newSession_btn_2, 0, Qt.AlignHCenter)

        self.tabWidget_2.addTab(self.report_2, icon8, "")
        self.about_2 = QWidget()
        self.about_2.setObjectName(u"about_2")
        self.verticalLayout_13 = QVBoxLayout(self.about_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 50, -1, -1)
        self.textEdit_3 = QTextEdit(self.about_2)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMaximumSize(QSize(16777215, 140))
        self.textEdit_3.setStyleSheet(u"background:transparent;\n"
"\n"
"\n"
"")
        self.textEdit_3.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_14.addWidget(self.textEdit_3)

        self.textBrowser_5 = QTextBrowser(self.about_2)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setFont(font2)
        self.textBrowser_5.setStyleSheet(u"background:transparent;\n"
"border:transparent\n"
"\n"
"")
        self.textBrowser_5.setOpenExternalLinks(True)

        self.verticalLayout_14.addWidget(self.textBrowser_5)


        self.verticalLayout_13.addLayout(self.verticalLayout_14)

        self.tabWidget_2.addTab(self.about_2, icon9, "")

        self.verticalLayout_15.addWidget(self.tabWidget_2)

        self.horizontalFrame_2 = QFrame(self.familiar)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        sizePolicy1.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, 10)
        self.start_btn_2 = QPushButton(self.horizontalFrame_2)
        self.start_btn_2.setObjectName(u"start_btn_2")
        self.start_btn_2.setMaximumSize(QSize(16777215, 45))
        self.start_btn_2.setIcon(icon10)
        self.start_btn_2.setIconSize(QSize(34, 48))

        self.horizontalLayout_15.addWidget(self.start_btn_2)

        self.stop_btn_2 = QPushButton(self.horizontalFrame_2)
        self.stop_btn_2.setObjectName(u"stop_btn_2")
        self.stop_btn_2.setMaximumSize(QSize(16777215, 45))
        self.stop_btn_2.setIcon(icon11)
        self.stop_btn_2.setIconSize(QSize(38, 37))

        self.horizontalLayout_15.addWidget(self.stop_btn_2)


        self.verticalLayout_15.addWidget(self.horizontalFrame_2, 0, Qt.AlignHCenter)

        self.container_tabwid.addTab(self.familiar, "")

        self.verticalLayout.addWidget(self.container_tabwid)

        self.license_frame = QFrame(self.centralwidget)
        self.license_frame.setObjectName(u"license_frame")
        sizePolicy.setHeightForWidth(self.license_frame.sizePolicy().hasHeightForWidth())
        self.license_frame.setSizePolicy(sizePolicy)
        self.license_frame.setStyleSheet(u"QFrame{\n"
"	background:transparent\n"
"}")
        self._2 = QVBoxLayout(self.license_frame)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(100, 100, 100, 0)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, 0, -1, -1)
        self.license_le = QLineEdit(self.license_frame)
        self.license_le.setObjectName(u"license_le")
        self.license_le.setStyleSheet(u"padding:7px;\n"
"font-size:14px")

        self.horizontalLayout_25.addWidget(self.license_le)

        self.license_btn = QPushButton(self.license_frame)
        self.license_btn.setObjectName(u"license_btn")
        self.license_btn.setStyleSheet(u"padding:8px;\n"
"font-weight:bold")

        self.horizontalLayout_25.addWidget(self.license_btn)


        self._2.addLayout(self.horizontalLayout_25)

        self.license_status_label = QTextBrowser(self.license_frame)
        self.license_status_label.setObjectName(u"license_status_label")
        sizePolicy3.setHeightForWidth(self.license_status_label.sizePolicy().hasHeightForWidth())
        self.license_status_label.setSizePolicy(sizePolicy3)
        self.license_status_label.setMinimumSize(QSize(0, 100))
        self.license_status_label.setMaximumSize(QSize(16777215, 100))
        self.license_status_label.setStyleSheet(u"color:#e63c41;\n"
"font-weight:bold;\n"
"border:none;\n"
"")

        self._2.addWidget(self.license_status_label)


        self.verticalLayout.addWidget(self.license_frame)

        self.frame2 = QFrame(self.centralwidget)
        self.frame2.setObjectName(u"frame2")
        self.horizontalLayout_13 = QHBoxLayout(self.frame2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 1, -1, -1)
        self.commandLinkButton = QCommandLinkButton(self.frame2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        sizePolicy2.setHeightForWidth(self.commandLinkButton.sizePolicy().hasHeightForWidth())
        self.commandLinkButton.setSizePolicy(sizePolicy2)
        self.commandLinkButton.setMaximumSize(QSize(16777215, 25))
        self.commandLinkButton.setFont(font2)
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"background: transparent;\n"
"border:0")
        icon13 = QIcon()
        iconThemeName = u";"
        if QIcon.hasThemeIcon(iconThemeName):
            icon13 = QIcon.fromTheme(iconThemeName)
        else:
            icon13.addFile(u"../Yellow Pages sg", QSize(), QIcon.Normal, QIcon.Off)
        
        self.commandLinkButton.setIcon(icon13)

        self.horizontalLayout_13.addWidget(self.commandLinkButton, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.container_tabwid.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.addAccount_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeAccount_btn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.accounts), QCoreApplication.translate("MainWindow", u"Accounts", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Sending Mode", None))
        self.phone_rb.setText(QCoreApplication.translate("MainWindow", u"Send By Phone Number", None))
        self.username_rb.setText(QCoreApplication.translate("MainWindow", u"Send By Username", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sending Order", None))
        self.textFirst_rb.setText(QCoreApplication.translate("MainWindow", u"Text First", None))
        self.attachFirst_rb.setText(QCoreApplication.translate("MainWindow", u"Attachment First", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Messages per account", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Attachments", None))
        self.attachments_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Images, videos, documents", None))
        self.attachments_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Text Message", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Append {name}", None))
        self.append_newmessage.setText(QCoreApplication.translate("MainWindow", u"new message", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), QCoreApplication.translate("MainWindow", u"Main", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Sender", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Phone or ID  ", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.sheet_btn.setText(QCoreApplication.translate("MainWindow", u"Import Contacts", None))
        self.newSession_btn.setText(QCoreApplication.translate("MainWindow", u"Start New Session", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.report), QCoreApplication.translate("MainWindow", u"Report", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.SF NS Text'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:22pt; font-weight:600;\">If you face any problem or requiring a custom functionality, just contact me anytime</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:22pt; font-weight:600;\"><br />Thank You &lt;3</span></p></body></html>", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'arial'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" styl"
                        "e=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:18pt; font-weight:600;\">- Contact Me -</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:16pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600; color:#107d41;\">Whatsapp</span><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600;\"> : </span><a href=\"https://web.whatsapp.com/send?phone=201120641378\"><span style=\" font-family:'Helvetica'; font-size:12pt; text-decoration: underline; color:#0000ff;\">+201120641378</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:"
                        "empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600; color:#445bb8;\">Facebook</span><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600;\"> : </span><a href=\"https://www.facebook.com/lord.ahmed110\"><span style=\" font-family:'Helvetica'; font-size:12pt; text-decoration: underline; color:#0000ff;\">fb.com/lord.ahmed110</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;"
                        " margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600; color:#db9409;\">Fiverr</span><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600;\"> : </span><a href=\"https://www.fiverr.com/lordahmed\"><span style=\" font-family:'Helvetica'; font-size:12pt; text-decoration: underline; color:#0000ff;\">Fiverr.com/lordahmed</span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), QCoreApplication.translate("MainWindow", u"About", None))
        self.start_btn.setText("")
        self.stop_btn.setText("")
        self.container_tabwid.setTabText(self.container_tabwid.indexOf(self.anonymous), QCoreApplication.translate("MainWindow", u"Anonymous", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Sending Mode", None))
        self.phone_rb_2.setText(QCoreApplication.translate("MainWindow", u"Send By Phone Number", None))
        self.username_rb_2.setText(QCoreApplication.translate("MainWindow", u"Send By Username", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Sending Order", None))
        self.textFirst_rb_2.setText(QCoreApplication.translate("MainWindow", u"Text First", None))
        self.attachFirst_rb_2.setText(QCoreApplication.translate("MainWindow", u"Attachment First", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Attachments", None))
        self.attachments_le_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Images, videos, documents", None))
        self.attachments_btn_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Text Message", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Append {name}", None))
        self.append_newmessage_2.setText(QCoreApplication.translate("MainWindow", u"new message", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.main_2), QCoreApplication.translate("MainWindow", u"Main", None))
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Phone or ID", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.sheet_btn_2.setText(QCoreApplication.translate("MainWindow", u"Import Contacts", None))
        self.newSession_btn_2.setText(QCoreApplication.translate("MainWindow", u"Start New Session", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.report_2), QCoreApplication.translate("MainWindow", u"Report", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.SF NS Text'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:22pt; font-weight:600;\">If you face any problem or requiring a custom functionality, just contact me anytime</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:22pt; font-weight:600;\"><br />Thank You &lt;3</span></p></body></html>", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'arial'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" styl"
                        "e=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:18pt; font-weight:600;\">- Contact Me -</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:16pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600; color:#107d41;\">Whatsapp</span><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600;\"> : </span><a href=\"https://web.whatsapp.com/send?phone=201120641378\"><span style=\" font-family:'Helvetica'; font-size:12pt; text-decoration: underline; color:#0000ff;\">+201120641378</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:"
                        "empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600; color:#445bb8;\">Facebook</span><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600;\"> : </span><a href=\"https://www.facebook.com/lord.ahmed110\"><span style=\" font-family:'Helvetica'; font-size:12pt; text-decoration: underline; color:#0000ff;\">fb.com/lord.ahmed110</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Helvetica'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;"
                        " margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600; color:#db9409;\">Fiverr</span><span style=\" font-family:'Helvetica'; font-size:12pt; font-weight:600;\"> : </span><a href=\"https://www.fiverr.com/lordahmed\"><span style=\" font-family:'Helvetica'; font-size:12pt; text-decoration: underline; color:#0000ff;\">Fiverr.com/lordahmed</span></a></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.about_2), QCoreApplication.translate("MainWindow", u"About", None))
        self.start_btn_2.setText("")
        self.stop_btn_2.setText("")
        self.container_tabwid.setTabText(self.container_tabwid.indexOf(self.familiar), QCoreApplication.translate("MainWindow", u"Familiar", None))
        self.license_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your License key", None))
        self.license_btn.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Copyright 2020 LorDAhmeD", None))
    # retranslateUi

