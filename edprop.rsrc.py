{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'Standard Template with no menus',
          'size':(438, 540),

         'components': [

{'type':'ImageButton', 
    'name':'ImageButton2', 
    'position':(360, 110), 
    'size':(48, 48), 
    'border':'transparent', 
    'command':'cancel', 
    'file':'icons/cancel.png', 
    },

{'type':'ImageButton', 
    'name':'ImageButton1', 
    'position':(360, 30), 
    'size':(48, 48), 
    'border':'transparent', 
    'command':'ok', 
    'file':'icons/ok.png', 
    },

{'type':'StaticText', 
    'name':'title', 
    'position':(70, 10), 
    'font':{'faceName': u'Segoe UI', 'family': 'sansSerif', 'size': 14}, 
    'text':'title', 
    },

] # end components
} # end background
] # end backgrounds
} }
