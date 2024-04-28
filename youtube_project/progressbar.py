import requests
from PyQt6.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton, QVBoxLayout
from PyQt6.QtCore import QThread, pyqtSignal


class DownloadThread(QThread):
    progress = pyqtSignal(int)

    def __init__(self, url, save_path):
        super().__init__()
        self.url = url
        self.save_path = save_path

    def run(self):
        data_0 = 0
        response = requests.get(self.url, stream=True,proxies={'https': '127.0.0.1:4780'})
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        with open(self.save_path, 'wb') as f:
            for data in response.iter_content(block_size):
                f.write(data)
                data_0 += len(data)
                self.progress.emit(int(data_0 / total_size * 100))
        self.progress.emit("100")


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('File Downloader')
        self.setGeometry(100, 100, 400, 100)
        self.init_ui()

    def init_ui(self):
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setMaximum(100)
        self.download_button = QPushButton('Download')
        self.download_button.clicked.connect(self.download_file)
        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.download_button)
        self.setLayout(layout)

    def download_file(self):
        url = 'https://rr2---sn-i3b7kn6s.googlevideo.com/videoplayback?expire=1679763186&ei=ktIeZL-kJd28vcAP0uehgAE&ip=220.246.252.116&id=o-AOHwwA260lfbC5eeKplEglHBuMoyW-rSXNBoCAd1zq-D&itag=244&source=youtube&requiressl=yes&mh=lu&mm=31%2C26&mn=sn-i3b7kn6s%2Csn-p5qlsnrr&ms=au%2Conr&mv=m&mvi=2&pl=21&initcwndbps=1432500&vprv=1&mime=video%2Fwebm&gir=yes&clen=9513457&dur=502.034&lmt=1648920642713476&mt=1679741130&fvip=1&keepalive=yes&fexp=24007246&c=ANDROID&txp=5437434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAPQaXsA1WfaoMnu0l7EcMLi6Ehn5UPkul8pcnsmW6CN3AiEAzlSC7BWgBImQxLjLPfRvB2nPlcVs5v2di072z8t9TKI%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhANJcNisi4nOo-MImca5O5sdGYo2-METhWP9s2_kk4FguAiAyihKsOelWlsn2-fu317ZDnxHiA6XVDx0eyYVM8TAqGw%3D%3D'
        # url = 'https://www.diskboss.com/setups_x64/diskboss_setup_v13.5.18_x64.exe'
        save_path = 'C:/Users/dazhizhi/Downloads/file.zip'
        self.download_thread = DownloadThread(url, save_path)
        self.download_thread.progress.connect(self.update_progress)
        self.download_thread.run()

    def update_progress(self, value):
        self.progress_bar.setValue(value)


if __name__ == '__main__':
    app = QApplication([])
    window = App()
    window.show()
    app.exec()
