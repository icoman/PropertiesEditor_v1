#!/usr/bin/python

"""

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

import os, sys
import traceback
import json
import wx
from PythonCard import model, dialog
from PythonCard import __version__ as ver

import edprop

class MyBackground(model.Background):

    def on_initialize(self, event):
        self.title = 'Properties Editor'
        self.components.title.text = self.title
        if getattr(sys, 'frozen', False):
            self.position = (20, 20)
        else:
            self.position = (260, 20)
        self.loadedFilename = None
        self.confirmAddProperty = False
        self.confirmSaveProperty = False
        self.confirmCancelProperty = False
        self.confirmSaveDocument = False
        self.VERSIONS = 3 #how many doc versions to keep, at lest 2
        self.cfg = self.default_cfg()
        self.cfg['data'] = {}
        self.populate_table()
        self.components.proptable.setFocus()

    def on_close(self,evt):
        result = dialog.messageDialog(self, '''Terminate program and exit?''','Exit',wx.ICON_INFORMATION | wx.YES_NO) #wx.YES_NO sau wx.OK
        if result.accepted:
            self.Destroy()
            sys.exit(0)

    def default_cfg(self):
        return dict (
                #a data structure used for webapp config
                data = {
  "10": {
    "description": "Write here whatever you need to remember about this module",
    "name": "admin notes",
    "posturl": "",
    "type": "textarea",
    "value": "This is config of module.\r\n\r\nDSN - definition of db link to SQL server\r\naccess module - list of groups who has access to this module\r\nconfig menu - display link to editor of config menu\r\nuser config - enable user config and display link to editor"
  },
  "20": {
    "description": "Data Source Name",
    "name": "DSN",
    "posturl": "",
    "type": "text",
    "value": "protocol://user:password@host/database"
  },
  "30": {
    "description": "Enable or disable module execution",
    "name": "module disabled",
    "posturl": "",
    "type": "checkbox",
    "value": ""
  },
  "40": {
    "description": "Enable acces to user json config file",
    "name": "user config",
    "posturl": "",
    "type": "checkbox",
    "value": ""
  },
  "50": {
    "description": "Show link to module config and user config",
    "name": "config menu",
    "posturl": "",
    "type": "checkbox",
    "value": "yes"
  },
  "60": {
    "description": "List of groups who has acces to module",
    "name": "access module",
    "posturl": "/auth/groups/all",
      "type": "mc",
      "value": [
        "1",
        "2"
      ]
  }
},
                fields = {
    u'10':['name',[]],
    u'20':['description',[]],
    #mc = multiple checkbox
    u'30':['type',['text','textarea','password','checkbox','select','mc']],
    u'40':['value',[]],
    #"posturl" field is ued to populate pick list for "select" and "multiple checkbox"
    u'50':['posturl',['','/auth/groups/all','/post1','/post2','/post3']]
    }
)

    def default_cfg2(self):
        return dict (
                #a data structure used for user config
                data = {
  "10": {
    "description": "test property 1",
    "name": "prop1",
    "posturl": "",
    "type": "text",
    "value": ""
  },
  "20": {
    "description": "test property 2",
    "name": "prop2",
    "posturl": "",
    "type": "checkbox",
    "value": ""
  },
  "30": {
    "description": "test property 3",
    "name": "prop3",
    "posturl": "",
    "type": "textarea",
    "value": ""
  }
},
                fields = {
    u'10':['name',[]],
    u'20':['description',[]],
    #mc = multiple checkbox
    u'30':['type',['text','textarea','password','checkbox','select','mc']],
    u'40':['value',[]],
    #"posturl" field is ued to populate pick list for "select" and "multiple checkbox"
    u'50':['posturl',['','/auth/groups/all','/post1','/post2','/post3']]
    }
)

    def rename_ix_props(self):
        '''
            Reorder data
        '''
        data = self.cfg.get('data')
        keys = [int(x) for x in data.keys()]
        keys.sort()
        L = [data[unicode(x)] for x in keys]
        new_data = {}
        for i,v in enumerate(L):
            ix = unicode(10+i*10)
            new_data[ix] = v
        self.cfg['data'] = new_data

    def rename_ix_fields(self):
        '''
            Reorder fields
        '''
        fields = self.cfg.get('fields')
        keys = [int(x) for x in fields.keys()]
        keys.sort()
        L = [fields[unicode(x)] for x in keys]
        new_fields = {}
        for i,v in enumerate(L):
            ix = unicode(10+i*10)
            new_fields[ix] = v
        self.cfg['fields'] = new_fields

    def populate_table(self):
        '''
            Populate MultiColumnList
        '''
        fields = self.cfg.get('fields')
        fields_l = [fields[k][0] for k in sorted(fields.keys())]
        columnHeadings = ['ix',] + fields_l
        self.components.proptable.columnHeadings = columnHeadings
        self.components.fieldslist.items = fields_l
        items = []
        data = self.cfg.get('data')
        keys = [int(x) for x in data.keys()]
        keys.sort()
        for ix in keys:
            initial_v = data.get(unicode(ix))
            final_v = {}
            l = ['{:03d}'.format(int(ix))]
            for i in fields_l:
                value = unicode(initial_v.get(i,u''))
                final_v.update({i:value}) #update data if structure fields changed
                l.append(value)
            data[unicode(ix)] = final_v
            items.append(l)
        self.components.proptable.items = items

    def on_datainfo_command(self, event):
        '''
            Menu: Info -> Data info
        '''
        datainfo = json.dumps(self.cfg.get('data'), sort_keys=True, indent=2, separators=(',', ': '))
        result = dialog.scrolledMessageDialog(self, datainfo, 'Data Info')

    def on_fieldsinfo_command(self, event):
        '''
            Menu: Info -> Fields info
        '''
        fieldsinfo = json.dumps(self.cfg.get('fields'), sort_keys=True, indent=2, separators=(',', ': '))
        result = dialog.scrolledMessageDialog(self, fieldsinfo, 'Fields Info')

    def on_docraw_command(self, event):
        '''
            Menu: Info -> Document raw
        '''
        docinfo = json.dumps(self.cfg, sort_keys=True, separators=(',', ': '))
        result = dialog.scrolledMessageDialog(self, docinfo, 'JSON Document Raw Format')

    def on_docpp_command(self, event):
        '''
            Menu: Info -> Document pretty print
        '''
        docinfo = json.dumps(self.cfg, sort_keys=True, indent=2, separators=(',', ': '))
        result = dialog.scrolledMessageDialog(self, docinfo, 'JSON Document Pretty Print')

    def on_new_empty_command(self, event):
        '''
            New document
        '''
        result = dialog.messageDialog(self, 'New empty document?','New',wx.ICON_INFORMATION | wx.YES_NO) #wx.YES_NO sau wx.OK
        if result.accepted:
            self.loadedFilename = None
            self.title = 'New empty document'
            self.cfg = self.default_cfg()
            self.cfg['data'] = {}
            self.populate_table()

    def on_new_command(self, event):
        '''
            New document populated for web config
        '''
        result = dialog.messageDialog(self, 'New web config document?','New',wx.ICON_INFORMATION | wx.YES_NO) #wx.YES_NO sau wx.OK
        if result.accepted:
            self.loadedFilename = None
            self.title = 'New web config document'
            self.cfg = self.default_cfg()
            self.populate_table()

    def on_new_user_command(self, event):
        '''
            New document populated for user config
        '''
        result = dialog.messageDialog(self, 'New user config document?','New',wx.ICON_INFORMATION | wx.YES_NO) #wx.YES_NO sau wx.OK
        if result.accepted:
            self.loadedFilename = None
            self.title = 'New user config document'
            self.cfg = self.default_cfg2()
            self.populate_table()

    def on_addprop_command(self, event):
        '''
            Add a property
        '''
        if self.confirmAddProperty:
            result = dialog.messageDialog(self, 'Add property?','Add',wx.ICON_INFORMATION | wx.YES_NO) #wx.YES_NO sau wx.OK
        if not self.confirmAddProperty or result.accepted:
            self.saved_data = self.cfg.get('data').copy()
            fields = self.cfg.get('fields')
            fields_l = [fields[k][0] for k in sorted(fields.keys())]
            keys = [int(x) for x in self.cfg.get('data').keys()]
            if keys:
                ix = 1 + int(max(keys))
            else:
                ix = 1
            new_key = unicode(ix)
            prop = {}
            for i in fields_l:
                prop[i] = ''
            self.cfg['data'].update({new_key:prop})
            self.rename_ix_props()
            self.populate_table()
            self.components.proptable.SetSelection(-1) #select last entry
            self.on_proptable_mouseDoubleClick(None)

    def on_deleteprop_command(self, event):
        '''
            Delete a property
        '''
        L = self.components.proptable.GetSelectedItems()
        if L:
            for i in L:
                ix = unicode(int(i[0]))
                data = self.cfg.get('data')
                prop_str = json.dumps(data.get(ix), sort_keys=True, indent=2, separators=(',', ': '))
                result = dialog.messageDialog(self, 'Confirm delete #{}\n\n{}'.format(ix, prop_str),'Delete',wx.ICON_INFORMATION | wx.YES_NO) #wx.YES_NO sau wx.OK
                if result.accepted:
                    del data[ix]
            self.populate_table()
        else:
            dialog.messageDialog(self, 'Nothing selected.', 'Error',wx.ICON_ERROR | wx.OK)

    def on_addfield_command(self, event):
        '''
            Add a field
        '''
        result = dialog.textEntryDialog(self, 
                        'Name of new field',
                        'New field', 
                        'new field')
        if result.accepted:
            field_name = result.text
            fields = self.cfg.get('fields')
            fields_l = [fields[k][0] for k in sorted(fields.keys())]
            if not field_name in fields_l:
                keys = [int(x) for x in fields.keys()]
                if keys:
                    ix = 1+max(keys)
                else:
                    ix = 1
                new_key = unicode(ix)
                if 1:
                    #a new field has empty options list
                    fields[new_key] = [field_name,[]]
                else:
                    #or a new field has a predefined list
                    fields[new_key] = [field_name,['opt 1','opt 2','opt 3']]
                self.rename_ix_fields()
                self.populate_table()
            else:
                dialog.messageDialog(self, 'Field already exists.', 'Error',wx.ICON_ERROR | wx.OK)

    def on_deletefield_command(self, event):
        '''
            Delete one or more fields
            Select fields from a dialog box
        '''
        fields = self.cfg.get('fields')
        fields_l = [fields[k][0] for k in sorted(fields.keys())]
        result = dialog.multipleChoiceDialog(self,
                        "Select fields you want to delete",
                        "Delete fields",
                        fields_l)
        if result.accepted:
            self.cfg['fields'] = {x:fields[x] for x in fields \
                    if not fields[x][0] in result.selection}
            self.populate_table()

    def on_upprop_command(self, event):
        '''
            Move up a property
        '''
        L = self.components.proptable.GetSelectedItems()
        if L:
            search_tag = L[0][1:]
            data = self.cfg.get('data')
            ix = unicode(int(L[0][0]))
            new_ix = unicode(int(ix) - 15)
            d = data.get(ix)
            del data[ix]
            data[new_ix] = d
            self.rename_ix_props()
            self.populate_table()
            for i,item in enumerate(self.components.proptable.items):
                if search_tag == item[1:]:
                    self.components.proptable.SetSelection(i)
            self.components.proptable.setFocus()

    def on_downprop_command(self, event):
        '''
            Move down a property
        '''
        L = self.components.proptable.GetSelectedItems()
        if L:
            search_tag = L[0][1:]
            data = self.cfg.get('data')
            ix = unicode(int(L[0][0]))
            new_ix = unicode(int(ix) + 15)
            d = data.get(ix)
            del data[ix]
            data[new_ix] = d
            self.rename_ix_props()
            self.populate_table()
            for i,item in enumerate(self.components.proptable.items):
                if search_tag == item[1:]:
                    self.components.proptable.SetSelection(i)
            self.components.proptable.setFocus()

    def on_upfield_command(self, event):
        '''
            Move up a field
        '''
        selix = self.components.fieldslist.selection
        fields = self.cfg.get('fields')
        fields_l = [fields[k][0] for k in sorted(fields.keys())]
        if selix > -1:
            search_tag = fields_l[selix]
            ix = [k for k in fields if fields[k][0] == search_tag][0]
            new_ix = unicode(int(ix) - 15)
            d = fields.get(ix)
            del fields[ix]
            fields[new_ix] = d
            self.rename_ix_fields()
            self.populate_table()
            fields = self.cfg.get('fields')
            fields_l = [fields[k][0] for k in sorted(fields.keys())]
            self.components.fieldslist.selection = fields_l.index(search_tag)
            self.components.fieldslist.setFocus()

    def on_downfield_command(self, event):
        '''
            Move down a field
        '''
        selix = self.components.fieldslist.selection
        fields = self.cfg.get('fields')
        fields_l = [fields[k][0] for k in sorted(fields.keys())]
        if selix > -1:
            search_tag = fields_l[selix]
            ix = [k for k in fields if fields[k][0] == search_tag][0]
            new_ix = unicode(int(ix) + 15)
            d = fields.get(ix)
            del fields[ix]
            fields[new_ix] = d
            self.rename_ix_fields()
            self.populate_table()
            fields = self.cfg.get('fields')
            fields_l = [fields[k][0] for k in sorted(fields.keys())]
            self.components.fieldslist.selection = fields_l.index(search_tag)
            self.components.fieldslist.setFocus()



    def on_fieldslist_mouseDoubleClick(self, event):
        '''
            Change pick list for a field
        '''
        ix = self.components.fieldslist.selection
        fields = self.cfg.get('fields')
        fields_l = [fields[k][0] for k in sorted(fields.keys())]
        key = sorted(fields.keys())[ix]
        fieldname, options = fields[key]
        result = dialog.textEntryDialog(self, 
            'Edit pick list for\n\n{}'.format(fieldname),
            'Edit field', 
            '{}'.format(options))
        if result.accepted:
            try:
                value = [unicode(x) for x in eval(result.text)]
                fields[key][1] = value
            except:
                dialog.messageDialog(self, 'Invalid list.', 'Error',wx.ICON_ERROR | wx.OK)

    def on_load_command(self, event):
        '''
            Load JSON document
        '''
        try:
            wildcard = "JSON files (*.json)|*.json|All Files (*.*)|*.*"
            result = dialog.openFileDialog(wildcard=wildcard)
            if result.accepted:
                filename = result.paths[0]
                with open(filename,'rb') as f:
                     self.cfg = json.loads(f.read())
                self.populate_table()
                self.loadedFilename = filename
                self.title = self.loadedFilename
        except Exception as ex:
            err = traceback.format_exc()
            dialog.messageDialog(self, err, 'Error',wx.ICON_ERROR | wx.OK)

    def _saveData(self, filename):
        '''
            Save document
            Used by Save and SaveAs
        '''
        for cnt in range(self.VERSIONS-1, 0, -1):
            oldfile = '{}.{}'.format(filename, cnt)
            newfile = '{}.{}'.format(filename, cnt-1)
            if os.path.isfile(oldfile):
                os.remove(oldfile)
            if os.path.isfile(newfile):
                os.rename(newfile, oldfile)
        newfile = '{}.{}'.format(filename, 0)
        if os.path.isfile(filename):
            os.rename(filename, newfile)
        with open(filename, 'wb') as f:
            f.write(json.dumps(self.cfg, sort_keys=True, indent=2, separators=(',', ': ')).encode('utf-8'))


    def on_save_command(self, event):
        '''
            Save
        '''
        if self.loadedFilename:
            if self.confirmSaveDocument:
                result = dialog.messageDialog(self, 'Confirm save.','Save',wx.ICON_INFORMATION | wx.YES_NO) #wx.YES_NO sau wx.OK
            if not self.confirmSaveDocument or result.accepted:
                filename = self.loadedFilename
                self._saveData(filename)
                dialog.messageDialog(self, 'Saved', 'Saved',wx.ICON_INFORMATION | wx.OK)
        else:
            self.on_saveas_command(None)

    def on_saveas_command(self, event):
        '''
            Save As
        '''
        try:
            wildcard = "JSON files (*.json)|*.json|All Files (*.*)|*.*"
            result = dialog.saveFileDialog(wildcard=wildcard)
            if result.accepted:
                filename = result.paths[0]
                self._saveData(filename)
                self.loadedFilename = filename
                dialog.messageDialog(self, 'Saved', 'Saved',wx.ICON_INFORMATION | wx.OK)
                self.title = self.loadedFilename
        except Exception as ex:
            err = traceback.format_exc()
            dialog.messageDialog(self, err, 'Error',wx.ICON_ERROR | wx.OK)

    def callback_ed(self, flag):
        '''
            callback function for "Edit properties form"
        '''
        if flag:
            fields = self.cfg.get('fields')
            fields_l = [fields[k][0] for k in sorted(fields.keys())]
            L = self.components.proptable.GetSelectedItems()
            ix = unicode(int(L[0][0]))
            data = self.cfg.get('data')
            d = {}
            for i,prop_name in enumerate(fields_l):
                name = 'fld{}'.format(i+1)
                d[prop_name] = self.ed.components[name].text
            data[unicode(ix)] = d
        else:
            self.cfg['data'] = self.saved_data
        self.saved_data = None
        self.rename_ix_props()
        self.populate_table()
        self.components.proptable.SetSelection(-1) #select last entry


    def on_proptable_mouseDoubleClick(self, event):
        '''
            Edit selected property
        '''
        L = self.components.proptable.GetSelectedItems()
        if L:
            if self.saved_data is None:
                self.saved_data = self.cfg.get('data').copy()
            ix = int(L[0][0])
            self.ed = model.childWindow(self, edprop.MyBackground)
            self.ed.position = (self.position[0]+50, self.position[1]+50)
            self.ed.title = 'Edit #{}'.format(ix)
            self.ed.components.title.text = self.ed.title 
            self.ed.callback = self.callback_ed
            self.ed.confirmSaveProperty = self.confirmSaveProperty
            self.ed.confirmCancelProperty = self.confirmCancelProperty
            #Here start populate form sequence
            x, y = 20, 50
            dx, ddx, dy = 80, 200, 20
            name = 'lab0'
            self.ed.components[name] = {'type':'StaticText','name':name,
                'text':'ix', 'size':(dx, dy), 'position':(x, y)}
            name = 'fld0'
            self.ed.components[name] = {'type':'TextField','name':name,
                'text':str(ix), 'enabled':False,
                'size':(ddx, dy), 'position':(x+dx+10, y-5)}
            y += dy+5
            d = self.cfg.get('data').get(str(ix))
            fields = self.cfg.get('fields')
            fields_l = [fields[k][0] for k in sorted(fields.keys())]
            fields_opts = [fields[k][1] for k in sorted(fields.keys())]
            for i,prop_name in enumerate(fields_l):
                name = 'lab{}'.format(i+1)
                self.ed.components[name] = {'type':'StaticText','name':name,
                    'text':prop_name,
                    'size':(dx, dy), 'position':(x, y)}
                name = 'fld{}'.format(i+1)
                value = unicode(d[prop_name])
                if not fields_opts[i]:
                    #TextField or TextArea
                    if '\n' in value:
                        self.ed.components[name] = {'type':'TextArea','name':name,
                            'text':value,
                            'size':(ddx,dy+50), 'position':(x+dx+10, y-5)}
                        y += 50
                    else:
                        self.ed.components[name] = {'type':'TextField','name':name,
                            'text':value,
                            'size':(ddx,dy), 'position':(x+dx+10, y-5)}
                else:
                    #ComboBox
                    items = fields_opts[i]
                    default = value or (items and items[0] or '')
                    self.ed.components[name] = {'type':'ComboBox','name':name,
                        'text':unicode(d[prop_name]),
                        'size':(ddx,dy), 'position':(x+dx+10, y-5),
                        'items':items,
                        'stringSelection':default}
                i += 1
                y += dy+5
            if fields:
                self.ed.components['fld1'].SetFocus()
            self.ed.MakeModal(True)


    def on_help_command(self, event):
        '''
            Menu: Help -> Help
        '''
        result = dialog.messageDialog(self, '''{}

This program is designed to generate "web config documents"
and is a tool used with a web application server.
The edit part of such documents is used on "web config editor".

The "web config documents" are stored in JSON format.

The "web config editor" is provided by an web application
server and allow admin and normal user to alter properties.

The default structure of new created documents
allow admin of webserver to configure over
web some properties of web application module
such as: groups access, SQL DSN, boolean flags, ...
and also allow normal user to customize its application.

You can change the structure of document by adding
or removing fields, but for "web config documents"
the structure must remain unchanged.
A field in this editor is viewed as an attribute of
selected data entry on "web config editor".

This editor does nothing and know nothing and the real
magic is happening on "web config editor", when the
fields "select" and "mc" (multiple checks) are dinamically
populated using AJAX POST with data provided by webserver.

'''.format(self.components.title.text), 'Help',wx.ICON_INFORMATION | wx.OK) #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL)



    def on_about_command(self, event):
        '''
            Menu: Help -> About
        '''
        result = dialog.messageDialog(self, '''{}

(C) 2019 Ioan Coman

PythonCard version: {}
wx version: {}

Python version:
{}

'''.format(self.components.title.text, ver.VERSION_STRING, wx.version(), sys.version), 'About',wx.ICON_INFORMATION | wx.OK) #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL)



def fix_frozen_apps():
    #
    #fix import for py2exe, cx_freeze, pyinstaller, ...
    #
    #import here whatever fail to import when application is frozen
    #
    #import pyodbc, pymssql, _mssql
    #from sqlalchemy.sql import default_comparator
    #from PythonCard.components import slider
    #from PythonCard.components import radiogroup
    from PythonCard.components import button
    #from PythonCard.components import list
    #from PythonCard.components import choice
    from PythonCard.components import statictext
    #from PythonCard.components import checkbox
    #from PythonCard.components import gauge
    from PythonCard.components import multicolumnlist
    #from PythonCard.components import passwordfield
    from PythonCard.components import textarea
    from PythonCard.components import combobox
    #from PythonCard.components import calendar
    from PythonCard.components import imagebutton



if __name__ == '__main__':
    app = model.Application(MyBackground)
    app.MainLoop()
