import json
import subprocess
import time
import pytube
import sys
import requests
import os
import scrapetube

from PySide6.QtWidgets import QApplication
from mutagen import mp4
from download_api import download


from subprocess import call
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import QSettings
from youtubedlUI import Ui_MainWindow

setting = QSettings('setting.ini', QSettings.Format.IniFormat)
ip_port_text = ''
IDMPath = "C:/Program Files (x86)/Internet Download Manager/"
os.chdir(IDMPath)
IDM = "IDMan.exe"


class DownloadForm(QtWidgets.QMainWindow, Ui_MainWindow):
    file_name = ''
    yt = None
    data = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 初始化所有控件

        # column_width_list = [50, 30, 50, 60, 70, 90, 90,90]
        #
        # for i in range(self.tableWidget.columnCount() - 1):
        #     self.tableWidget.setColumnWidth(i, column_width_list[i])

        self.parse_button.clicked.connect(self.parse_link)
        self.tableWidget.cellClicked.connect(self.cell_clicked)
        self.browse_button.clicked.connect(self.update_save_path)
        self.playlist_button.clicked.connect(self.download_playlist)
        self.ip_text.textChanged.connect(self.change_ip)
        self.merge_button.clicked.connect(self.merge_metadata)
        self.path_text.setText(setting.value('path'))
        self.ip_text.setText(setting.value('ip'))

    def status_update(self, info):
        self.status_text.showMessage(info, 0)
        app.processEvents()

    def change_ip(self):
        global ip_port_text
        ip_port_text = self.ip_text.text()

    def update_save_path(self):
        prev_path = self.path_text.text()
        save_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder', prev_path) + '/'
        if save_path == '/':
            save_path = prev_path
        self.path_text.setText(save_path)

    def add_text(self, row, column, text,remark = None):
        if text is None:
            return
        table = self.tableWidget
        item = QtWidgets.QTableWidgetItem(str(text))  # widget序号
        if remark:
            item.setToolTip(remark)
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        table.setItem(row, column, item)
        table.resizeColumnToContents(column)

    def parse_link(self):
        table = self.tableWidget
        self.status_update('Parsing video...')
        table.setRowCount(0)
        link = self.link_text.text()

        data = download(link)
        self.data = data
        formats = data['formats']

        source_count = len(formats)
        table.setRowCount(source_count)
        self.status_update('Parsing complete.')
        for i in range(source_count):
            stream = formats[i]
            self.add_text(i, 0, stream['ext'])
            self.add_text(i, 1, stream['res'])
            self.add_text(i, 2, stream['fps'])
            self.add_text(i, 3, stream['bitrate'])
            self.add_text(i, 4, stream['size'])
            self.add_text(i, 5, stream['codec'])
            self.add_text(i, 6, 'copy link',stream['url'])
            self.add_text(i, 7, 'IDM download',stream['url'])

    def cell_clicked(self, row, column):
        url = self.data['formats'][row]['url']
        title = self.data['title']
        ext = self.data['formats'][row]['ext']
        filename = f"{title}.{ext}"
        if column == 6:
            self.copy_link(url)
        if column == 7:
            self.idm_download(url,filename)

    def copy_link(self, url):
        self.clipboard = QApplication.clipboard()
        self.clipboard.setText(url)

        self.status_update('Link copied to clipboard.')

    def idm_download(self, url,file_name):
        self.status_update('Sending to IDM...')
        file_path = self.path_text.text()
        file_name = file_name.replace('.webm', '.weba')
        call([IDM, "/d", url, "/p", file_path, "/f", file_name, '/n'])
        self.status_update('IDM received.')


    def download_playlist(self):
        # 获取列表
        link = self.link2_text.text()
        if "list" in link:
            self.status_update('Retrieving playlist...')
            playlist: pytube.Playlist = pytube.Playlist(link, proxies={'https': ip_port_text})
            video_url_list = list(playlist.video_urls)
            self.status_update('Playlist retrieved.')
        if "@" in link:
            self.status_update('Retrieving channel...')

            list_path = os.path.dirname(__file__) + '/list.txt'
            if os.path.exists(list_path):
                f = open(list_path, 'r')
                video_url_list = [line.strip() for line in f.readlines()]
                f.close()
            else:
                video_url_list = []
                channel_name = link.split("/@")[1]
                videos = scrapetube.get_channel(channel_username=channel_name, content_type='streams',
                                                proxies={'https': ip_port_text})
                f = open(os.path.dirname(__file__) + '/list.txt', 'w')
                for video in videos:
                    title = video['title']['accessibility']['accessibilityData']['label']
                    if any(x in title for x in PLAYLIST_KEYWORDS):
                        video_id = video['videoId']
                        video_link = f'https://www.youtube.com/watch?v={video_id}'
                        f.write(video_link + '\n')
                        video_url_list.append(video_link)
                f.close()

            self.status_update('Channel retrieved.')

        total_n = len(video_url_list)

        for i, video_url in enumerate(video_url_list):
            # 解析视频流
            yt = pytube.YouTube(video_url, proxies={'https': ip_port_text})
            self.status_update(f'Video {i}/{total_n} object retrieved.')

            # 获取标题
            title = yt.title
            invalid = '<>:"/\|?* '
            for char in invalid:
                title = title.replace(char, '')
            self.status_update(f'Video {i}/{total_n} title retrieved.')

            # 创建目录
            file_path = self.path_text.text() + title + "/"
            if not os.path.exists(file_path):
                os.makedirs(file_path)
                self.status_update(f'Video {i}/{total_n} folder created.')
            else:
                self.status_update(f'Video {i}/{total_n} folder existed.')

            # 写入原始播放地址
            link_path = file_path + "link.txt"
            if not os.path.exists(link_path):
                open(link_path, "w").write(video_url)

            # 写入缩略图
            thumb_path = file_path + "thumbnail.jpg"
            if not os.path.exists(thumb_path):
                response = requests.get(yt.thumbnail_url, proxies={'https': ip_port_text})
                open(thumb_path, "wb").write(response.content)

            # 将视频发送给IDM下载
            file_name = title + '.weba'
            video_path = file_path + file_name

            if not os.path.exists(video_path):
                self.status_update(f'Parsing video {i}/{total_n}...')
                try:
                    url = yt.fmt_streams[-1].url
                except:
                    f = open(os.path.dirname(__file__) + '/others.txt', 'a')
                    f.write(video_url + '\n')
                    f.close()
                    self.status_update(f'Video {i}/{total_n} restricted.')
                    time.sleep(1)
                    continue

                self.status_update(f'Sending video {i}/{total_n} to IDM...')
                url_args = [IDM, "/d", url, "/p", file_path, "/f", file_name, '/n']
                call(url_args, shell=False)
                self.status_update(f'Video {i}/{total_n} sent to IDM.')
                time.sleep(5)
            else:
                self.status_update(f'Video {i}/{total_n} exists.')

    def merge_metadata(self):

        parent_path = self.path_text.text()
        mp4_path = parent_path + 'mp4/'
        mp4_list = os.listdir(mp4_path)

        for title in os.listdir(parent_path):
            if title == 'mp4' or title in mp4_list:
                continue
            child_path = parent_path + title + '/'
            audio_path = child_path + title + '.mp4'
            link_path = child_path + 'link.txt'
            thumb_path = child_path + 'thumbnail.jpg'
            if os.path.exists(audio_path) and os.path.exists(link_path) and os.path.exists(thumb_path):
                audio: mp4.MP4 = mp4.MP4(audio_path)

                link = open(link_path, "r").readline()
                audio['©ART'] = link

                picture_data = open(thumb_path, "rb").read()
                audio["covr"] = [mp4.MP4Cover(picture_data, imageformat=mp4.MP4Cover.FORMAT_JPEG)]

                audio.save(audio_path)

                self.status_update(f'Audio modified.')

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        setting.setValue('path', self.path_text.text())
        setting.setValue('ip', self.ip_text.text())
        a0.accept()

    def update_progress(self, value):
        self.status_text.showMessage(f'{value}%', 0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = DownloadForm()
    my_pyqt_form.show()
    app.exec()
