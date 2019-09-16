#!/usr/bin/python

"""
    Edit properties form

MIT License

Copyright (c) 2019 Ioan Coman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import wx
from PythonCard import model, dialog

class MyBackground(model.Background):

    def on_close(self, event):
        self.MakeModal(False)
        self.Destroy()

    def on_ok_command(self, event):
        if self.confirmSaveProperty:
            result = dialog.messageDialog(self, 'Confirm save?','Save',wx.ICON_INFORMATION | wx.YES_NO) #wx.YES_NO sau wx.OK
        if not self.confirmSaveProperty or result.accepted:
            self.close()
            self.callback(True)

    def on_cancel_command(self, event):
        if self.confirmCancelProperty:
            result = dialog.messageDialog(self, 'Confirm cancel?','Cancel',wx.ICON_INFORMATION | wx.YES_NO) #wx.YES_NO sau wx.OK
        if not self.confirmCancelProperty or result.accepted:
            self.close()
            self.callback(False)


