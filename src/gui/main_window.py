import sys
from qfluentwidgets import NavigationWidget, NavigationItemPosition, setTheme, Theme
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QLineEdit, QCheckBox, QPushButton, QSpinBox, QHBoxLayout, QProgressBar, QFileDialog

class DownloadPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("批量下载"))
        self.textLinks = QTextEdit()
        self.textLinks.setPlaceholderText("每行一个抖音链接")
        layout.addWidget(self.textLinks)
        # Cookie配置
        cookieLayout = QHBoxLayout()
        self.editMsToken = QLineEdit(); self.editMsToken.setPlaceholderText("msToken")
        self.editTtwid = QLineEdit(); self.editTtwid.setPlaceholderText("ttwid")
        self.editOdin = QLineEdit(); self.editOdin.setPlaceholderText("odin_tt")
        self.editPassport = QLineEdit(); self.editPassport.setPlaceholderText("passport_csrf_token")
        self.editSid = QLineEdit(); self.editSid.setPlaceholderText("sid_guard")
        for w in [self.editMsToken, self.editTtwid, self.editOdin, self.editPassport, self.editSid]:
            cookieLayout.addWidget(w)
        layout.addLayout(cookieLayout)
        # 下载选项
        optionsLayout = QHBoxLayout()
        self.chkVideo = QCheckBox("视频"); self.chkImage = QCheckBox("图片")
        self.chkMusic = QCheckBox("音乐"); self.chkCover = QCheckBox("封面")
        self.chkAvatar = QCheckBox("头像"); self.chkJson = QCheckBox("JSON")
        for w in [self.chkVideo, self.chkImage, self.chkMusic, self.chkCover, self.chkAvatar, self.chkJson]:
            optionsLayout.addWidget(w)
        layout.addLayout(optionsLayout)
        # 下载模式
        modeLayout = QHBoxLayout()
        self.chkPost = QCheckBox("作品"); self.chkLike = QCheckBox("喜欢")
        self.chkMix = QCheckBox("合集"); self.chkMusicMix = QCheckBox("音乐合集")
        for w in [self.chkPost, self.chkLike, self.chkMix, self.chkMusicMix]:
            modeLayout.addWidget(w)
        layout.addLayout(modeLayout)
        # 数量与线程
        numThreadLayout = QHBoxLayout()
        numThreadLayout.addWidget(QLabel("数量限制"))
        self.spinNumber = QSpinBox(); self.spinNumber.setRange(0, 9999)
        numThreadLayout.addWidget(self.spinNumber)
        numThreadLayout.addWidget(QLabel("线程数"))
        self.spinThread = QSpinBox(); self.spinThread.setRange(1, 32); self.spinThread.setValue(5)
        numThreadLayout.addWidget(self.spinThread)
        layout.addLayout(numThreadLayout)
        # 保存路径
        pathLayout = QHBoxLayout()
        pathLayout.addWidget(QLabel("保存路径"))
        self.editPath = QLineEdit(); self.editPath.setPlaceholderText("选择文件夹")
        pathLayout.addWidget(self.editPath)
        self.btnChoosePath = QPushButton("选择")
        self.btnChoosePath.clicked.connect(self.choose_path)
        pathLayout.addWidget(self.btnChoosePath)
        layout.addLayout(pathLayout)
        # 开始下载
        self.btnStart = QPushButton("开始下载")
        layout.addWidget(self.btnStart)
        # 进度条
        self.progressBar = QProgressBar(); self.progressBar.setRange(0, 100)
        layout.addWidget(self.progressBar)
        # 日志输出
        self.textLog = QTextEdit(); self.textLog.setReadOnly(True); self.textLog.setPlaceholderText("日志输出...")
        layout.addWidget(self.textLog)
    def choose_path(self):
        path = QFileDialog.getExistingDirectory(self, "选择保存路径")
        if path:
            self.editPath.setText(path)

class ConfigPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("配置管理页"))

class LogPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("日志/进度页"))

class AboutPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("关于页"))

class MainWindow(NavigationWidget):
    def __init__(self):
        super().__init__()
        setTheme(Theme.LIGHT)
        # 添加页面
        self.addNavigationItem(
            routeKey="download",
            icon=None,
            text="批量下载",
            onClick=lambda: self.switchTo("download"),
            position=NavigationItemPosition.TOP
        )
        self.addWidget("download", DownloadPage())
        # 依次添加其他页面...
        self.setWindowTitle("Douyin Downloader")
        self.resize(1000, 700)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
