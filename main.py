#!/usr/bin/env python

from PyQt5 import QtWidgets, QtCore, QtGui
from window import Ui_MainWindow
import page_templates as templates

import requests
import pyperclip as pc
import webbrowser
import qtmodern.styles

_, paste = pc.determine_clipboard()


def get_meanings_block(term):
    url = f'https://jisho.org/api/v1/search/words?keyword={term}'
    r = requests.get(url)
    return r.json()['data']


class myWindow(QtWidgets.QMainWindow):
    def __init__(self, app):
        self.app = app
        qtmodern.styles.dark(self.app)
        super(myWindow, self).__init__()
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.webEngineView.setHtml(templates.get_intro_html())
        self.connect_functions()
        self.primary = True
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
        self.ui.actionGithub.triggered.connect(self.visit_github)
        self.ui.actionSearchInJishoWeb.triggered.connect(self.search_web)
        self.ui.actionPrimarySelection.triggered.connect(self._clipboard)
        self.ui.actionExit.triggered.connect(self.exit)
        # keys
        self.ui.toolSync.setShortcut(
            QtGui.QKeySequence.Refresh
        )
        self.ui.actionExit.setShortcut(
            QtGui.QKeySequence("Q")
        )
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

    def exit(self):
        self.app.exit(0)

    def _clipboard(self):
        self.primary = self.ui.actionPrimarySelection.isChecked()

    def get_clipboard(self):
        if not self.primary:
            return paste()
        
        # to avoid asking the primary selection for itself and being
        # unable to get it from X since it is busy waiting inside this
        # function. checking if there is selected text on itself will
        # avoid it having ask through X.
        if self.ui.webEngineView.hasSelection():
            return self.ui.webEngineView.selectedText()
        else:
            try:
                return paste(primary=True)
            except TypeError:
                # In  case there is no primary clipboard
                return paste()


    def auto_mode(self):
        term = self.get_clipboard()
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
            self.ui.webEngineView.setHtml(
                templates.get_error_html('Connection Error',str(e)))
        except requests.exceptions.ConnectTimeout as e:
            self.ui.webEngineView.setHtml(
                templates.get_error_html('Connection Timeout',str(e)))

    def search_web(self):
        webbrowser.open(f'jisho.org/{self.term}')

    def visit_github(self):
        webbrowser.open('https://github.com/Atreyagaurav/jisho-chibi')

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
        if len(self.meanings) == 0:
            self.ui.webEngineView.setHtml(templates.get_error_html(
                'Zero Results',
                f'We couldn\'t find any words matching <u>{self.term}</u>, please try ' +
                'to prune out the extra particles at the begining/end of the word and try again.'))
            self.statusBar().showMessage(f'Zero results for {self.term}.')
        else:
            wrd = self.meanings[self.position]
            self.statusBar().showMessage(f'{self.position+1} of {len(self.meanings)} search result(s)')
            self.ui.webEngineView.setHtml(templates.get_meanings_html(wrd))
            # with open("/tmp/t.html", "w") as w:
            #     w.write(templates.get_meanings_html(wrd))


def main():
    app = QtWidgets.QApplication([])
    win = myWindow(app)
    win.show()
    app.exec_()

        
if __name__ == "__main__":
    main()
