#!/usr/bin/env python

from PyQt5 import QtWidgets, QtCore, QtGui
from window import Ui_MainWindow

import requests
import pyperclip as pc

_, paste = pc.determine_clipboard()


def get_meanings_block(term):
    url = f'https://jisho.org/api/v1/search/words?keyword={term}'
    r = requests.get(url)
    return r.json()['data']


class myWindow(QtWidgets.QMainWindow):
    def __init__(self, app):
        self.app = app
        super(myWindow, self).__init__()
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.webEngineView.setHtml('<small><p>Jisho Chibi GUI for jisho API.</p>' +
                                      'Visit <a href="https://jisho.org/">jisho page</a> for full dictionary use. <br \>'
                                      'For more info on this app visit <a href="https://github.com/atreyagaurav/jisho-chibi">github</a>.</small>')
        self.connect_functions()
        self.term = ''
        self.meanings = []
        self.position = -1
        self.history = []
        self.termHistory = []
        self.historyIndex = -1

    def connect_functions(self):
        # input textbox
        self.ui.txtClip.returnPressed.connect(self.search)
        # would be nice to press ESC to lose focus, but it works if I press TAB to shift focus.
        # self.ui.txtClip.inputRejected.connect(self.ui.txtClip.clearFocus)
        # buttons
        self.ui.btnSearch.clicked.connect(self.search)
        self.ui.btnNext.clicked.connect(self.next)
        self.ui.btnPrev.clicked.connect(self.prev)
        self.ui.toolSync.clicked.connect(self.auto_mode)
        # menubar
        self.ui.actionNextResult.triggered.connect(self.next)
        self.ui.actionPreviousResult.triggered.connect(self.prev)
        self.ui.actionNextSearch.triggered.connect(self.next_history)
        self.ui.actionPreviousSearch.triggered.connect(self.prev_history)
        self.ui.actionClearSearchHistory.triggered.connect(self.clear_history)
        # keys
        self.ui.actionNextResult.setShortcuts([
            QtGui.QKeySequence("n"),
            QtGui.QKeySequence.MoveToNextChar])
        self.ui.actionPreviousResult.setShortcuts([
            QtGui.QKeySequence("p"),
            QtGui.QKeySequence.MoveToPreviousChar])
        self.ui.actionNextSearch.setShortcuts([
            QtGui.QKeySequence.MoveToNextPage])
        self.ui.actionPreviousSearch.setShortcuts([
            QtGui.QKeySequence.MoveToPreviousPage])
        self.ui.actionClearSearchHistory.setShortcut(QtGui.QKeySequence("Del"))

    def auto_mode(self):
        # to avoid asking the primary selection for itself and being
        # unable to get it from X since it is busy waiting inside this
        # function. checking if there is selected text on itself will
        # avoid it having ask through X.
        sel = self.ui.webEngineView.selectedText()
        if sel:
            term = sel
        else:
            try:
                term = paste(primary=True)
            except TypeError:
                # In  case there is no primary clipboard
                term = paste()
        print(f'searching: {term}')
        self.ui.txtClip.setText(term)
        self.search()

    def search(self):
        self.term = self.ui.txtClip.text()
        self.statusBar().showMessage(f'Searching: {self.term}')
        self.app.processEvents()
        try:
            self.meanings = get_meanings_block(self.term)
            self.position = 0
            self.history.append(self.meanings)
            self.termHistory.append(self.term)
            self.historyIndex = -1
            self.update_word()
        except requests.exceptions.ConnectionError as e:
            self.ui.webEngineView.setHtml(f'Connection Error: {e}')
        except requests.exceptions.ConnectTimeout as e:
            self.ui.webEngineView.setHtml(f'Connection Timeout: {e}')

    def next(self):
        if len(self.meanings) < 2:
            self.statusBar().showMessage('No next results.')
            return
        self.position = (self.position + 1) % len(self.meanings)
        self.update_word()
        
    def prev(self):
        if len(self.meanings) < 2:
            self.statusBar().showMessage('No previous results.')
            return
        self.position = (self.position - 1) % len(self.meanings)
        self.update_word()

    def clear_history(self):
        # removes all but the current term from history
        self.history = [self.meanings]
        self.termHistory = [self.term]
        self.historyIndex = -1

    def next_history(self):
        if self.historyIndex < -1:
            self.historyIndex += 1
            self.meanings = self.history[self.historyIndex]
            self.term = self.termHistory[self.historyIndex]
            self.ui.txtClip.setText(self.term)
            self.position = 0
            self.update_word()
        else:
            self.statusBar().showMessage('No further search.')

    def prev_history(self):
        if self.historyIndex > -len(self.history):
            self.historyIndex -= 1
            self.meanings = self.history[self.historyIndex]
            self.term = self.termHistory[self.historyIndex]
            self.ui.txtClip.setText(self.term)
            self.position = 0
            self.update_word()
        else:
            self.statusBar().showMessage('No previous search.')

    def update_word(self):
        if not self.term:
            return
        try:
            wrd = self.meanings[self.position]["japanese"][0]
            self.statusBar().showMessage(f'{self.position+1} of {len(self.meanings)} search result(s)')
            html = f'<p>{wrd.get("word")} ({wrd.get("reading")})</p>'
            senses = self.meanings[self.position]["senses"]
            meanings = ["; ".join(sen["english_definitions"]) for sen in senses]
            html += '<small><ol>'
            for m in meanings:
                html += f'<li>{m}</li>'
            html += '</ol></small>'
            self.ui.webEngineView.setHtml(html)
        except (KeyError, IndexError) as e:
            self.ui.webEngineView.setHtml(f'API error: {e}')


def main():
    app = QtWidgets.QApplication([])
    win = myWindow(app)
    win.show()
    app.exec_()

        
if __name__ == "__main__":
    main()
