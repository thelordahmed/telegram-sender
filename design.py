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
        MainWindow.resize(782, 1055)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainwindow_frame = QFrame(self.centralwidget)
        self.mainwindow_frame.setObjectName(u"mainwindow_frame")
        self.horizontalLayout_6 = QHBoxLayout(self.mainwindow_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(1, 1, -1, -1)
        self.listWidget = QListWidget(self.mainwindow_frame)
        icon = QIcon()
        icon.addFile(u":/black-icons/Data/imgs/black icons/icons8-decision-52.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setIcon(icon);
        icon1 = QIcon()
        icon1.addFile(u":/black-icons/Data/imgs/black icons/icons8-male-user-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setIcon(icon1);
        icon2 = QIcon()
        icon2.addFile(u":/black-icons/Data/imgs/black icons/icons8-chat-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setIcon(icon2);
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QSize(160, 0))
        self.listWidget.setStyleSheet(u"QListView { /* The tab widget frame */\n"
"    background:transparent;\n"
"	font-weight:bold;\n"
"}\n"
"\n"
"QListView::item {\n"
"    background: qlineargradient(spread:pad, x1:0.44335, y1:0.482955, x2:1, y2:0, stop:0 rgba(219, 219, 219, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    min-width: 8ex;\n"
"    padding: 20px 0;\n"
"}\n"
"\n"
"QListView::item:selected, QListView::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB;\n"
"	color:black;\n"
"	border-right: 0;\n"
"}\n"
"\n"
"QListView::item:!selected {\n"
"    margin-top: 0px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.listWidget.setLineWidth(1)
        self.listWidget.setMidLineWidth(0)
        self.listWidget.setIconSize(QSize(33, 33))
        self.listWidget.setFlow(QListView.TopToBottom)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QListView.Fixed)
        self.listWidget.setLayoutMode(QListView.SinglePass)
        self.listWidget.setSpacing(0)
        self.listWidget.setViewMode(QListView.ListMode)
        self.listWidget.setModelColumn(0)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setBatchSize(100)
        self.listWidget.setWordWrap(False)
        self.listWidget.setSelectionRectVisible(False)

        self.horizontalLayout_6.addWidget(self.listWidget)

        self.container_tabwid = QTabWidget(self.mainwindow_frame)
        self.container_tabwid.setObjectName(u"container_tabwid")
        self.container_tabwid.setStyleSheet(u"")
        self.container_tabwid.setTabPosition(QTabWidget.North)
        self.container_tabwid.setElideMode(Qt.ElideRight)
        self.container_tabwid.setUsesScrollButtons(False)
        self.container_tabwid.setDocumentMode(False)
        self.container_tabwid.setTabBarAutoHide(False)
        self.anonymous = QWidget()
        self.anonymous.setObjectName(u"anonymous")
        self.verticalLayout_9 = QVBoxLayout(self.anonymous)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.tabWidget = QTabWidget(self.anonymous)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"    position: absolute;\n"
"    top: -0.5em;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 "
                        "#fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}")
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
        icon3 = QIcon()
        icon3.addFile(u":/black-icons/Data/imgs/black icons/icons8-add-administrator-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addAccount_btn.setIcon(icon3)
        self.addAccount_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_11.addWidget(self.addAccount_btn)

        self.removeAccount_btn = QPushButton(self.frame)
        self.removeAccount_btn.setObjectName(u"removeAccount_btn")
        self.removeAccount_btn.setStyleSheet(u"padding:10px 0")
        icon4 = QIcon()
        icon4.addFile(u":/black-icons/Data/imgs/black icons/icons8-remove-administrator-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.removeAccount_btn.setIcon(icon4)
        self.removeAccount_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_11.addWidget(self.removeAccount_btn)


        self.verticalLayout_16.addWidget(self.frame)

        self.tabWidget.addTab(self.accounts, icon1, "")
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.verticalLayout_7 = QVBoxLayout(self.main)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 20, -1, -1)
        self.groupBox_3 = QGroupBox(self.main)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.phone_rb.sizePolicy().hasHeightForWidth())
        self.phone_rb.setSizePolicy(sizePolicy2)
        self.phone_rb.setChecked(True)

        self.horizontalLayout_2.addWidget(self.phone_rb)

        self.username_rb = QRadioButton(self.groupBox_3)
        self.username_rb.setObjectName(u"username_rb")
        sizePolicy2.setHeightForWidth(self.username_rb.sizePolicy().hasHeightForWidth())
        self.username_rb.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.username_rb)


        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.groupBox_9 = QGroupBox(self.main)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy1.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy1)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
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
        sizePolicy2.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.messages_sb = QSpinBox(self.groupBox_10)
        self.messages_sb.setObjectName(u"messages_sb")
        sizePolicy2.setHeightForWidth(self.messages_sb.sizePolicy().hasHeightForWidth())
        self.messages_sb.setSizePolicy(sizePolicy2)
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
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
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
        self.attachments_le.setReadOnly(False)

        self.horizontalLayout_3.addWidget(self.attachments_le)

        self.attachments_btn = QToolButton(self.groupBox_4)
        self.attachments_btn.setObjectName(u"attachments_btn")

        self.horizontalLayout_3.addWidget(self.attachments_btn)


        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.horizontalLayout_3)


        self.verticalLayout_7.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.main)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy4)
        self.groupBox_5.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_5.setFont(font1)
        self.groupBox_5.setAlignment(Qt.AlignCenter)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 5, -1, 5)
        self.frame1 = QFrame(self.groupBox_5)
        self.frame1.setObjectName(u"frame1")
        sizePolicy1.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy1)
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
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.message_text.sizePolicy().hasHeightForWidth())
        self.message_text.setSizePolicy(sizePolicy5)
        self.message_text.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_6.addWidget(self.message_text)


        self.verticalLayout_7.addWidget(self.groupBox_5)

        self.verticalLayout_7.setStretch(3, 1)
        icon5 = QIcon()
        icon5.addFile(u":/black-icons/Data/imgs/black icons/icons8-home-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.main, icon5, "")
        self.report = QWidget()
        self.report.setObjectName(u"report")
        self.verticalLayout_2 = QVBoxLayout(self.report)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self.report)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        icon6 = QIcon()
        icon6.addFile(u":/black-icons/Data/imgs/black icons/icons8-contacts-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setIcon(icon6);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        icon7 = QIcon()
        icon7.addFile(u":/black-icons/Data/imgs/black icons/icons8-circled-right-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setIcon(icon7);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        icon8 = QIcon()
        icon8.addFile(u":/black-icons/Data/imgs/black icons/icons8-call-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setIcon(icon8);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        icon9 = QIcon()
        icon9.addFile(u":/black-icons/Data/imgs/black icons/icons8-info-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setIcon(icon9);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(493, 0))
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.sheet_btn = QPushButton(self.report)
        self.sheet_btn.setObjectName(u"sheet_btn")
        self.sheet_btn.setStyleSheet(u"padding:15px 0")
        icon10 = QIcon()
        icon10.addFile(u":/black-icons/Data/imgs/black icons/icons8-hospital-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sheet_btn.setIcon(icon10)
        self.sheet_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.sheet_btn)

        self.newSession_btn = QPushButton(self.report)
        self.newSession_btn.setObjectName(u"newSession_btn")
        sizePolicy2.setHeightForWidth(self.newSession_btn.sizePolicy().hasHeightForWidth())
        self.newSession_btn.setSizePolicy(sizePolicy2)
        self.newSession_btn.setStyleSheet(u"padding:10px 20px")
        icon11 = QIcon()
        icon11.addFile(u":/black-icons/Data/imgs/black icons/icons8-trash-can-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newSession_btn.setIcon(icon11)

        self.verticalLayout_2.addWidget(self.newSession_btn, 0, Qt.AlignHCenter)

        icon12 = QIcon()
        icon12.addFile(u":/black-icons/Data/imgs/black icons/icons8-combo-chart-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.report, icon12, "")
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

        icon13 = QIcon()
        icon13.addFile(u":/black-icons/Data/imgs/black icons/icons8-about-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.about, icon13, "")

        self.verticalLayout_9.addWidget(self.tabWidget)

        self.horizontalFrame = QFrame(self.anonymous)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy2.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy2)
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.start_btn = QPushButton(self.horizontalFrame)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setMaximumSize(QSize(16777215, 45))
        icon14 = QIcon()
        icon14.addFile(u":/black-icons/Data/imgs/black icons/icons8-play-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_btn.setIcon(icon14)
        self.start_btn.setIconSize(QSize(34, 48))

        self.horizontalLayout_10.addWidget(self.start_btn)

        self.stop_btn = QPushButton(self.horizontalFrame)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setMaximumSize(QSize(16777215, 45))
        icon15 = QIcon()
        icon15.addFile(u":/black-icons/Data/imgs/black icons/icons8-stop-500.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_btn.setIcon(icon15)
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
        self.tabWidget_2.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"    position: absolute;\n"
"    top: -0.5em;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 "
                        "#fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}")
        self.tabWidget_2.setIconSize(QSize(15, 15))
        self.main_2 = QWidget()
        self.main_2.setObjectName(u"main_2")
        self.verticalLayout_11 = QVBoxLayout(self.main_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 30, -1, 0)
        self.groupBox_6 = QGroupBox(self.main_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy1.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy1)
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
        sizePolicy2.setHeightForWidth(self.phone_rb_2.sizePolicy().hasHeightForWidth())
        self.phone_rb_2.setSizePolicy(sizePolicy2)
        self.phone_rb_2.setChecked(True)

        self.horizontalLayout_5.addWidget(self.phone_rb_2)

        self.username_rb_2 = QRadioButton(self.groupBox_6)
        self.username_rb_2.setObjectName(u"username_rb_2")
        sizePolicy2.setHeightForWidth(self.username_rb_2.sizePolicy().hasHeightForWidth())
        self.username_rb_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.username_rb_2)


        self.verticalLayout_11.addWidget(self.groupBox_6)

        self.groupBox_2 = QGroupBox(self.main_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy6)
        self.groupBox_2.setFont(font1)
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_11 = QGroupBox(self.groupBox_2)
        self.groupBox_11.setObjectName(u"groupBox_11")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy7)
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
        sizePolicy1.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy1)
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
        self.attachments_le_2.setReadOnly(False)

        self.horizontalLayout_8.addWidget(self.attachments_le_2)

        self.attachments_btn_2 = QToolButton(self.groupBox_7)
        self.attachments_btn_2.setObjectName(u"attachments_btn_2")

        self.horizontalLayout_8.addWidget(self.attachments_btn_2)


        self.formLayout_2.setLayout(0, QFormLayout.SpanningRole, self.horizontalLayout_8)


        self.verticalLayout_11.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.main_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy4.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy4)
        self.groupBox_8.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_8.setFont(font1)
        self.groupBox_8.setAlignment(Qt.AlignCenter)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 5, -1, 5)
        self.widget = QWidget(self.groupBox_8)
        self.widget.setObjectName(u"widget")
        sizePolicy6.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy6)
        self.horizontalLayout_9 = QHBoxLayout(self.widget)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(1, 1, -1, -1)
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_9.addWidget(self.pushButton_2)

        self.append_newmessage_2 = QPushButton(self.widget)
        self.append_newmessage_2.setObjectName(u"append_newmessage_2")

        self.horizontalLayout_9.addWidget(self.append_newmessage_2)


        self.verticalLayout_12.addWidget(self.widget)

        self.message_text_2 = QPlainTextEdit(self.groupBox_8)
        self.message_text_2.setObjectName(u"message_text_2")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.message_text_2.sizePolicy().hasHeightForWidth())
        self.message_text_2.setSizePolicy(sizePolicy8)
        self.message_text_2.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_12.addWidget(self.message_text_2)

        self.verticalLayout_12.setStretch(1, 1)

        self.verticalLayout_11.addWidget(self.groupBox_8)

        self.verticalLayout_11.setStretch(3, 2)
        self.tabWidget_2.addTab(self.main_2, icon5, "")
        self.report_2 = QWidget()
        self.report_2.setObjectName(u"report_2")
        self.verticalLayout_5 = QVBoxLayout(self.report_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableWidget_2 = QTableWidget(self.report_2)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setIcon(icon6);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        icon16 = QIcon()
        icon16.addFile(u":/black-icons/Data/imgs/black icons/icons8-phone-500.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setIcon(icon16);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setIcon(icon9);
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
        self.sheet_btn_2.setIcon(icon10)
        self.sheet_btn_2.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.sheet_btn_2)

        self.newSession_btn_2 = QPushButton(self.report_2)
        self.newSession_btn_2.setObjectName(u"newSession_btn_2")
        sizePolicy2.setHeightForWidth(self.newSession_btn_2.sizePolicy().hasHeightForWidth())
        self.newSession_btn_2.setSizePolicy(sizePolicy2)
        self.newSession_btn_2.setStyleSheet(u"padding:10px 20px")
        self.newSession_btn_2.setIcon(icon11)

        self.verticalLayout_5.addWidget(self.newSession_btn_2, 0, Qt.AlignHCenter)

        self.tabWidget_2.addTab(self.report_2, icon12, "")
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

        self.tabWidget_2.addTab(self.about_2, icon13, "")

        self.verticalLayout_15.addWidget(self.tabWidget_2)

        self.horizontalFrame_2 = QFrame(self.familiar)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        sizePolicy2.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy2)
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, 10)
        self.start_btn_2 = QPushButton(self.horizontalFrame_2)
        self.start_btn_2.setObjectName(u"start_btn_2")
        self.start_btn_2.setMaximumSize(QSize(16777215, 45))
        self.start_btn_2.setIcon(icon14)
        self.start_btn_2.setIconSize(QSize(34, 48))

        self.horizontalLayout_15.addWidget(self.start_btn_2)

        self.stop_btn_2 = QPushButton(self.horizontalFrame_2)
        self.stop_btn_2.setObjectName(u"stop_btn_2")
        self.stop_btn_2.setMaximumSize(QSize(16777215, 45))
        self.stop_btn_2.setIcon(icon15)
        self.stop_btn_2.setIconSize(QSize(38, 37))

        self.horizontalLayout_15.addWidget(self.stop_btn_2)


        self.verticalLayout_15.addWidget(self.horizontalFrame_2, 0, Qt.AlignHCenter)

        self.container_tabwid.addTab(self.familiar, "")
        self.groups = QWidget()
        self.groups.setObjectName(u"groups")
        self.verticalLayout_24 = QVBoxLayout(self.groups)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, -1, -1, 0)
        self.connect_inputs = QFrame(self.groups)
        self.connect_inputs.setObjectName(u"connect_inputs")
        sizePolicy6.setHeightForWidth(self.connect_inputs.sizePolicy().hasHeightForWidth())
        self.connect_inputs.setSizePolicy(sizePolicy6)
        self.horizontalLayout_14 = QHBoxLayout(self.connect_inputs)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_5 = QFrame(self.connect_inputs)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy9 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy9)
        self.verticalLayout_21 = QVBoxLayout(self.frame_5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_21.addWidget(self.label_5)

        self.phone_le = QLineEdit(self.frame_5)
        self.phone_le.setObjectName(u"phone_le")

        self.verticalLayout_21.addWidget(self.phone_le)


        self.horizontalLayout_14.addWidget(self.frame_5)

        self.frame_2 = QFrame(self.connect_inputs)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy9.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy9)
        self.verticalLayout_19 = QVBoxLayout(self.frame_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_19.addWidget(self.label_2)

        self.api_id_le = QLineEdit(self.frame_2)
        self.api_id_le.setObjectName(u"api_id_le")

        self.verticalLayout_19.addWidget(self.api_id_le)


        self.horizontalLayout_14.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.connect_inputs)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy6.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy6)
        self.verticalLayout_20 = QVBoxLayout(self.frame_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_20.addWidget(self.label_3)

        self.api_hash_le = QLineEdit(self.frame_3)
        self.api_hash_le.setObjectName(u"api_hash_le")

        self.verticalLayout_20.addWidget(self.api_hash_le)


        self.horizontalLayout_14.addWidget(self.frame_3)


        self.verticalLayout_18.addWidget(self.connect_inputs)

        self.label = QLabel(self.groups)
        self.label.setObjectName(u"label")

        self.verticalLayout_18.addWidget(self.label, 0, Qt.AlignHCenter)

        self.telegram_link = QCommandLinkButton(self.groups)
        self.telegram_link.setObjectName(u"telegram_link")
        font3 = QFont()
        font3.setUnderline(True)
        self.telegram_link.setFont(font3)
        self.telegram_link.setCursor(QCursor(Qt.PointingHandCursor))
        self.telegram_link.setStyleSheet(u"\n"
"background: transparent;\n"
"border:0;\n"
"font-size:12px\n"
"\n"
"")
        self.telegram_link.setIconSize(QSize(0, 0))

        self.verticalLayout_18.addWidget(self.telegram_link, 0, Qt.AlignHCenter)

        self.frame2 = QFrame(self.groups)
        self.frame2.setObjectName(u"frame2")
        sizePolicy6.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy6)
        self.verticalLayout_22 = QVBoxLayout(self.frame2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_6 = QFrame(self.frame2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy3.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy3)
        self.frame_6.setStyleSheet(u"padding:10px 20px")
        self.horizontalLayout_17 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.connect_btn = QPushButton(self.frame_6)
        self.connect_btn.setObjectName(u"connect_btn")
        sizePolicy4.setHeightForWidth(self.connect_btn.sizePolicy().hasHeightForWidth())
        self.connect_btn.setSizePolicy(sizePolicy4)
        self.connect_btn.setStyleSheet(u"")

        self.horizontalLayout_17.addWidget(self.connect_btn)


        self.verticalLayout_22.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.widget_4 = QWidget(self.frame2)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy10 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy10)
        self.horizontalLayout_12 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_12.addWidget(self.label_4)

        self.confirm_code_le = QLineEdit(self.widget_4)
        self.confirm_code_le.setObjectName(u"confirm_code_le")

        self.horizontalLayout_12.addWidget(self.confirm_code_le)

        self.confirm_code_btn = QPushButton(self.widget_4)
        self.confirm_code_btn.setObjectName(u"confirm_code_btn")

        self.horizontalLayout_12.addWidget(self.confirm_code_btn)


        self.verticalLayout_22.addWidget(self.widget_4, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.frame2)

        self.line = QFrame(self.groups)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_18.addWidget(self.line)

        self.groupBox_12 = QGroupBox(self.groups)
        self.groupBox_12.setObjectName(u"groupBox_12")
        sizePolicy4.setHeightForWidth(self.groupBox_12.sizePolicy().hasHeightForWidth())
        self.groupBox_12.setSizePolicy(sizePolicy4)
        self.verticalLayout_23 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.listWidget_2 = QListWidget(self.groupBox_12)
        self.listWidget_2.setObjectName(u"listWidget_2")
        sizePolicy5.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy5)

        self.verticalLayout_23.addWidget(self.listWidget_2)

        self.refresh_groups_btn = QPushButton(self.groupBox_12)
        self.refresh_groups_btn.setObjectName(u"refresh_groups_btn")
        sizePolicy11 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.refresh_groups_btn.sizePolicy().hasHeightForWidth())
        self.refresh_groups_btn.setSizePolicy(sizePolicy11)

        self.verticalLayout_23.addWidget(self.refresh_groups_btn, 0, Qt.AlignHCenter)

        self.horizontalWidget = QWidget(self.groupBox_12)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        sizePolicy10.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy10)
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_23.addWidget(self.horizontalWidget, 0, Qt.AlignHCenter)

        self.groupBox1 = QGroupBox(self.groupBox_12)
        self.groupBox1.setObjectName(u"groupBox1")
        self.horizontalLayout_18 = QHBoxLayout(self.groupBox1)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.output_le = QLineEdit(self.groupBox1)
        self.output_le.setObjectName(u"output_le")

        self.horizontalLayout_18.addWidget(self.output_le)

        self.output_btn = QToolButton(self.groupBox1)
        self.output_btn.setObjectName(u"output_btn")

        self.horizontalLayout_18.addWidget(self.output_btn)


        self.verticalLayout_23.addWidget(self.groupBox1)

        self.verticalLayout_23.setStretch(2, 2)

        self.verticalLayout_18.addWidget(self.groupBox_12)

        self.spinner = QLabel(self.groups)
        self.spinner.setObjectName(u"spinner")

        self.verticalLayout_18.addWidget(self.spinner, 0, Qt.AlignHCenter)

        self.verticalWidget = QWidget(self.groups)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy10.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy10)
        self.verticalWidget.setStyleSheet(u"padding:15px 30px")
        self.verticalLayout_25 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, -1, -1, 0)
        self.extract_btn = QPushButton(self.verticalWidget)
        self.extract_btn.setObjectName(u"extract_btn")
        sizePolicy9.setHeightForWidth(self.extract_btn.sizePolicy().hasHeightForWidth())
        self.extract_btn.setSizePolicy(sizePolicy9)

        self.verticalLayout_25.addWidget(self.extract_btn)


        self.verticalLayout_18.addWidget(self.verticalWidget, 0, Qt.AlignHCenter)

        self.verticalLayout_18.setStretch(4, 1)

        self.verticalLayout_24.addLayout(self.verticalLayout_18)

        self.container_tabwid.addTab(self.groups, "")

        self.horizontalLayout_6.addWidget(self.container_tabwid)


        self.verticalLayout.addWidget(self.mainwindow_frame)

        self.license_frame = QFrame(self.centralwidget)
        self.license_frame.setObjectName(u"license_frame")
        sizePolicy1.setHeightForWidth(self.license_frame.sizePolicy().hasHeightForWidth())
        self.license_frame.setSizePolicy(sizePolicy1)
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
        sizePolicy12 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.license_le.sizePolicy().hasHeightForWidth())
        self.license_le.setSizePolicy(sizePolicy12)
        self.license_le.setMinimumSize(QSize(400, 0))
        self.license_le.setStyleSheet(u"padding:7px;\n"
"font-size:14px")

        self.horizontalLayout_25.addWidget(self.license_le)

        self.license_btn = QPushButton(self.license_frame)
        self.license_btn.setObjectName(u"license_btn")
        sizePolicy2.setHeightForWidth(self.license_btn.sizePolicy().hasHeightForWidth())
        self.license_btn.setSizePolicy(sizePolicy2)
        self.license_btn.setStyleSheet(u"padding:8px;\n"
"font-weight:bold")

        self.horizontalLayout_25.addWidget(self.license_btn)


        self._2.addLayout(self.horizontalLayout_25)

        self.license_status_label = QTextBrowser(self.license_frame)
        self.license_status_label.setObjectName(u"license_status_label")
        sizePolicy4.setHeightForWidth(self.license_status_label.sizePolicy().hasHeightForWidth())
        self.license_status_label.setSizePolicy(sizePolicy4)
        self.license_status_label.setMinimumSize(QSize(0, 100))
        self.license_status_label.setMaximumSize(QSize(16777215, 100))
        self.license_status_label.setFocusPolicy(Qt.NoFocus)
        self.license_status_label.setStyleSheet(u"color:#e63c41;\n"
"font-weight:bold;\n"
"border:none;\n"
"")

        self._2.addWidget(self.license_status_label)


        self.verticalLayout.addWidget(self.license_frame)

        self.frame3 = QFrame(self.centralwidget)
        self.frame3.setObjectName(u"frame3")
        self.horizontalLayout_13 = QHBoxLayout(self.frame3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 1, -1, -1)
        self.commandLinkButton = QCommandLinkButton(self.frame3)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        sizePolicy3.setHeightForWidth(self.commandLinkButton.sizePolicy().hasHeightForWidth())
        self.commandLinkButton.setSizePolicy(sizePolicy3)
        self.commandLinkButton.setMaximumSize(QSize(16777215, 25))
        self.commandLinkButton.setFont(font2)
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"background: transparent;\n"
"border:0")
        icon17 = QIcon()
        iconThemeName = u";"
        if QIcon.hasThemeIcon(iconThemeName):
            icon17 = QIcon.fromTheme(iconThemeName)
        else:
            icon17.addFile(u"../Yellow Pages sg", QSize(), QIcon.Normal, QIcon.Off)
        
        self.commandLinkButton.setIcon(icon17)

        self.horizontalLayout_13.addWidget(self.commandLinkButton, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.listWidget.currentRowChanged.connect(self.container_tabwid.setCurrentIndex)

        self.listWidget.setCurrentRow(-1)
        self.container_tabwid.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Anonymous", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Familiar", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Groups", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.addAccount_btn.setText("")
        self.removeAccount_btn.setText("")
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
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"API ID", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"API HASH", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Get API ID & Hash from this link", None))
        self.telegram_link.setText(QCoreApplication.translate("MainWindow", u"http://my.telegram.org/", None))
        self.connect_btn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Enter The Code", None))
        self.confirm_code_btn.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Choose a Group", None))
        self.refresh_groups_btn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.groupBox1.setTitle(QCoreApplication.translate("MainWindow", u"Export Location", None))
        self.output_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.spinner.setText("")
        self.extract_btn.setText(QCoreApplication.translate("MainWindow", u"Extract Members", None))
        self.container_tabwid.setTabText(self.container_tabwid.indexOf(self.groups), QCoreApplication.translate("MainWindow", u"groups", None))
        self.license_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your License key", None))
        self.license_btn.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Copyright 2021 LorDAhmeD", None))
    # retranslateUi

