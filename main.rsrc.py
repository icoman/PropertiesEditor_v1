{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'Standard Template with File->Exit menu',
          'size':(1094, 702),
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileNewdocument',
                   'label':u'New Empty Document',
                   'command':'new_empty',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileNewDocument',
                   'label':u'New Web Config Document',
                   'command':'new',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileNewUserConfigDocument',
                   'label':u'New User Config Document',
                   'command':'new_user',
                  },
                  {'type':'MenuItem',
                   'name':'menuFile-',
                   'label':u'-',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileLoaddocument',
                   'label':u'Open...',
                   'command':'load',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileSavedocument',
                   'label':u'Save',
                   'command':'save',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileSaveAsdocument',
                   'label':u'Save As...',
                   'command':'saveas',
                  },
                  {'type':'MenuItem',
                   'name':'menuFile-',
                   'label':u'-',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':u'Exit',
                   'command':'exit',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuProperty',
             'label':u'Properties',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuPropertyAdd',
                   'label':u'Add',
                   'command':'addprop',
                  },
                  {'type':'MenuItem',
                   'name':'menuPropertyDelete',
                   'label':u'Delete',
                   'command':'deleteprop',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuFields',
             'label':u'Fields',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFieldsAdd',
                   'label':u'Add',
                   'command':'addfield',
                  },
                  {'type':'MenuItem',
                   'name':'menuFieldsDelete',
                   'label':u'Delete',
                   'command':'deletefield',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuInfo',
             'label':u'Info',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuInfoDatainfo',
                   'label':u'Data info',
                   'command':'datainfo',
                  },
                  {'type':'MenuItem',
                   'name':'menuInfoFieldsinfo',
                   'label':u'Fields info',
                   'command':'fieldsinfo',
                  },
                  {'type':'MenuItem',
                   'name':'menuInfo-',
                   'label':u'-',
                  },
                  {'type':'MenuItem',
                   'name':'menuInfoDocumentraw',
                   'label':u'Document raw',
                   'command':'docraw',
                  },
                  {'type':'MenuItem',
                   'name':'menuInfoDocument',
                   'label':u'Document pretty print',
                   'command':'docpp',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuHelp',
             'label':u'Help',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuHelpHelp',
                   'label':u'Help',
                   'command':'help',
                  },
                  {'type':'MenuItem',
                   'name':'menuHelpAbout',
                   'label':u'About',
                   'command':'about',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'StaticText', 
    'name':'Fields', 
    'position':(870, 250), 
    'size':(141, 37), 
    'alignment':'center', 
    'font':{'faceName': u'Segoe UI', 'family': 'sansSerif', 'size': 18}, 
    'text':'Fields', 
    },

{'type':'ImageButton', 
    'name':'ImageButton14', 
    'position':(940, 290), 
    'size':(48, 48), 
    'border':'transparent', 
    'command':'deletefield', 
    'file':'icons/delete.png', 
    'toolTip':'Delete fields', 
    },

{'type':'ImageButton', 
    'name':'ImageButton13', 
    'position':(880, 290), 
    'size':(48, 48), 
    'border':'transparent', 
    'command':'addfield', 
    'file':'icons/add.png', 
    'toolTip':'Add field', 
    },

{'type':'ImageButton', 
    'name':'ImageButton12', 
    'position':(1020, 450), 
    'size':(48, 48), 
    'border':'transparent', 
    'command':'downfield', 
    'file':'icons/down.png', 
    'toolTip':'Move down selected field', 
    },

{'type':'ImageButton', 
    'name':'ImageButton11', 
    'position':(1020, 380), 
    'size':(48, 48), 
    'border':'transparent', 
    'command':'upfield', 
    'file':'icons/up.png', 
    'toolTip':'Move up selected field', 
    },

{'type':'ImageButton', 
    'name':'ImageButton7', 
    'position':(360, 10), 
    'size':(48, 48), 
    'border':'transparent', 
    'command':'deleteprop', 
    'file':'icons/delete.png', 
    'toolTip':'Delete selected properties', 
    },

{'type':'ImageButton', 
    'name':'ImageButton6', 
    'position':(860, 170), 
    'size':(48, 48), 
    'border':'transparent', 
    'command':'downprop', 
    'file':'icons/down.png', 
    'toolTip':'Move down selected property', 
    },

{'type':'ImageButton', 
    'name':'ImageButton5', 
    'position':(860, 90), 
    'size':(48, 48), 
    'border':'transparent', 
    'command':'upprop', 
    'file':'icons/up.png', 
    'toolTip':'Move up selected property', 
    },

{'type':'ImageButton', 
    'name':'ImageButton4', 
    'position':(300, 10), 
    'size':(48, 48), 
    'border':'transparent', 
    'command':'addprop', 
    'file':'icons/add.png', 
    'toolTip':'Add property', 
    },

{'type':'List', 
    'name':'fieldslist', 
    'position':(870, 350), 
    'size':(144, 281), 
    'font':{'faceName': u'Segoe UI', 'family': 'sansSerif', 'size': 12}, 
    'items':[], 
    },

{'type':'MultiColumnList', 
    'name':'proptable', 
    'position':(22, 72), 
    'size':(830, 560), 
    'backgroundColor':(255, 255, 255, 255), 
    'columnHeadings':[], 
    'font':{'faceName': u'Segoe UI', 'family': 'sansSerif', 'size': 10}, 
    'items':[], 
    'maxColumns':20, 
    'rules':1, 
    },

{'type':'StaticText', 
    'name':'title', 
    'position':(20, 10), 
    'font':{'faceName': u'Segoe UI', 'family': 'sansSerif', 'size': 18}, 
    'text':'title', 
    },

] # end components
} # end background
] # end backgrounds
} }
