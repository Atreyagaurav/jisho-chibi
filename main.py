#!/usr/bin/env python

from mainWindow import Ui_MainWindow

import requests
import pyperclip as pc

_, paste = pc.determine_clipboard()

def get_meanings_block(term):
    url = f'https://jisho.org/api/v1/search/words?keyword={term}'
    r = requests.get(url)
    return r.json()['data']


from PyQt5 import QtWidgets, QtCore, QtGui


class myWindow(QtWidgets.QMainWindow):
    def __init__(self, app):
        self.app = app
        super(myWindow, self).__init__()
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_functions()
        self.term = ''

    def connect_functions(self):
        self.ui.btnSearch.clicked.connect(self.search)
        self.ui.btnNext.clicked.connect(self.next)
        self.ui.btnPrev.clicked.connect(self.prev)
        self.ui.toolSync.clicked.connect(self.auto_mode)

    def auto_mode(self):
        term = paste(primary=True)
        print(f'searching: {term}')
        self.ui.txtClip.setText(term)
        self.search()

    def search(self):
        self.term = self.ui.txtClip.text()
        self.statusBar().showMessage(f'Searching: {self.term}')
        self.update()
        self.meanings = get_meanings_block(self.term)
        self.position = 0
        self.update_word()

    def next(self):
        self.position = (self.position + 1) % len(self.meanings)
        self.update_word()
        
    def prev(self):
        self.position = (self.position - 1) % len(self.meanings)
        self.update_word()

    def update_word(self):
        if not self.term:
            return
        try:
            wrd = self.meanings[self.position]["japanese"][0]
            self.statusBar().showMessage(f'{self.position+1} of {len(self.meanings)} meaning(s)')
            html = f'<p>{wrd.get("word")} ({wrd.get("reading")})</p>'
            senses = self.meanings[self.position]["senses"]
            meanings = ["; ".join(sen["english_definitions"]) for sen in senses]
            html += '<small><ol>'
            for m in meanings:
                html += f'<li>{m}</li>'
            html += '</ol></small>'
            self.ui.webEngineView.setHtml(html)
        except KeyError:
            self.ui.webEngineView.setHtml('Error')


def main():
    app = QtWidgets.QApplication([])
    win = myWindow(app)
    win.show()
    app.exec_()

        
if __name__ == "__main__":
    main()
