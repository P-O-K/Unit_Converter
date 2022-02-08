
from tkinter import Tk, Text, Label, Button, Entry, OptionMenu, StringVar, W, E, END



class Conversion_Structure( object ):
    """Struct for conversion data"""
    
    # { TYPE_OF_UNITS{ FROM_UNIT{ TO_UNIT_VALUE } } }
    CONVERSION_STRUCTURE  = {
            'Length':{ 
                    'MM':{ 'CM':0.1,   'MT':0.001, 'KM':1e-6,   'IN':0.0393701 },
                    'CM':{ 'MM':10,    'MT':0.01,  'KM':1e-5,   'IN':0.393701 },
                    'MT':{ 'MM':1000,  'CM':100,   'KM':0.001,  'IN':39.3701 },
                    'KM':{ 'MM':1e+6,  'CM':1e+5,  'MT':1000,   'IN':0.00100000054 },
                    'IN':{ 'MM':25.4,  'CM':2.54,  'MT':0.0254, 'KM':2.54e-5, },
                    'FT':{ 'MM':304.8, 'CM':30.48, 'MT':0.3048, 'KM':0.0003048, 'IN':12 }
            },
            'Time':{
                    'SEC':{ 'MIN':0.0166667, 'HR ':0.000277778, 'DAY':1.1574e-5 },
                    'MIN':{ 'SEC':60,        'HR ':0.0166667,   'DAY':0.00069444583333 },
                    'HR ':{ 'SEC':3600,      'MIN':60,          'DAY':0.0416667 },
                    'DAY':{ 'SEC':86400,     'MIN':1440,        'HR ':24 }
            },
            'Area':{
                    'SQ IN':{ 'SQ FT':0.00694444, 'SQ YD ':0.000771605, 'SQ ML':2.491e-10, 'SQ MT':0.00064516, 'SQ KM':6.4516e-10 },
                    'SQ FT':{ 'SQ IN':144,        'SQ YD ':0.111111,    'SQ ML':3.587e-8,  'SQ MT':0.092903,   'SQ KM':9.2903e-8 },
                    'SQ YD':{ 'SQ IN':1296,       'SQ FT ':9,           'SQ ML':3.2283e-7, 'SQ MT':0.836127,   'SQ KM':8.3613e-7 },
                    'SQ ML':{ 'SQ IN':4.014e+9,   'SQ FT ':2.788e+7,    'SQ YD':3.098e+6,  'SQ MT':2.59e+6,    'SQ KM':2.58999 },
                    'SQ MT':{ 'SQ IN':1550,       'SQ FT ':10.7639,     'SQ YD':1.19599,   'SQ ML':3.861e-7,   'SQ KM':1e-6 },
                    'SQ KM':{ 'SQ IN':1.55e+9,    'SQ FT ':1.076e+7,    'SQ YD':1.196e+6,  'SQ ML':0.386102,   'SQ MT':1e+6 },
            },
            'Other':{                                   # EXAMPLE / TESTING - LAYOUT & VALUES
                    'X':{ 'xa':0, 'xb':1, 'xc':2 },
                    'Y':{ 'ya':3, 'yb':4, 'yc':5, 'yd':6 },
                    'Z':{ 'za':7, 'zb':8, 'zc':9, 'zd':10, 'ze':11 }
            }
        }




class Converter( Conversion_Structure ):

    MASTER = Tk( )
    MASTER.title( 'Multi- Converter' )
    userEnteredAmount = 0.0
    convertedTotal  = 0.0


    def __init__( self ):
        self.set_TypeMenu( )
        self.set_FromMenu( )
        self.set_ToMenu( )
        self.set_EQ_label( )
        self.assignValidationMethod( )
        self.set_ReplyField( )
        self.asignmentLayout( )
        self.masterLoop( )




    def set_TypeMenu( self ) -> None:
        self.TypeMenuItems = { item for item,_ in self.CONVERSION_STRUCTURE.items( ) }
        self.TypeMenuText = StringVar( )
        self.TypeMenuText.set( list( self.TypeMenuItems )[ 0 ] )
        self.TypeMenuText.trace( 'w',  self.ChangeInTypeMenu )
        self.TypeMenu = OptionMenu( self.MASTER, self.TypeMenuText, *self.TypeMenuItems )

    # Change in the 'TYPE-MENU' will  causes a change in the 'FROM-MENU' 
    def ChangeInTypeMenu( self, *args:None ) -> None:
        self.FromMenu[ 'menu' ].delete( 0, END )
        self.FromMenuText.set( list( self.CONVERSION_STRUCTURE[ self.TypeMenuText.get( ) ] )[ 0 ] )
        for i,_ in self.CONVERSION_STRUCTURE[ self.TypeMenuText.get( ) ].items( ):
            self.FromMenu[ 'menu' ].add_command( label=i, command=lambda value=i: self.FromMenuText.set( value ) )





    def set_FromMenu( self ) -> None:
        self.FromMenuItems = { item for item,_ in self.CONVERSION_STRUCTURE[ self.TypeMenuText.get( ) ].items( ) }
        self.FromMenuText = StringVar( )
        self.FromMenuText.set( list( self.FromMenuItems )[ 0 ] )
        self.FromMenuText.trace( 'w', self.ChangeInFromMenu )
        self.FromMenu = OptionMenu( self.MASTER, self.FromMenuText, *self.FromMenuItems )

    # Change in the 'FROM-MENU' will causes a change in the 'TO-MENU'
    def ChangeInFromMenu( self, *args:None ) -> None:
        self.ToMenu[ 'menu' ].delete( 0, END )
        self.ToMenuText.set( list( self.CONVERSION_STRUCTURE[ self.TypeMenuText.get( ) ][ self.FromMenuText.get( ) ] )[ 0 ] )
        for i,_ in self.CONVERSION_STRUCTURE[ self.TypeMenuText.get( ) ][ self.FromMenuText.get( ) ].items( ):
            self.ToMenu[ 'menu' ].add_command( label=i, command=lambda value=i: self.ToMenuText.set( value ) )





    def set_ToMenu( self ) -> None:
        self.ToMenuItems = { item for item,_ in self.CONVERSION_STRUCTURE[ self.TypeMenuText.get( ) ][ self.FromMenuText.get( ) ].items( ) }
        self.ToMenuText = StringVar( )
        self.ToMenuText.set( list( self.ToMenuItems )[ 0 ] )
        self.ToMenuText.trace( 'w', self.ChangeInToMenu )
        self.ToMenu = OptionMenu( self.MASTER, self.ToMenuText, *self.ToMenuItems )

    # Change in the 'TO-MENU' will causes a change in the 'REPLY-FIELD'
    def ChangeInToMenu( self, *args:None ) -> None:
        self.updateReplyField( )





    def set_ReplyField( self ) -> None:
        self.ReplyTextFieldMessage = '0.0'
        self.ReplyTextField = Text( self.MASTER, height=1, width=20 )
        self.ReplyTextField.insert( END, self.ReplyTextFieldMessage )

    # Updates the output field based on user input
    def updateReplyField( self ) -> None:
        if self.userEnteredAmount == 0:
            self.ReplyTextFieldMessage = '0.0'
        else:
            self.convertedTotal = self.userEnteredAmount *self.CONVERSION_STRUCTURE[ self.TypeMenuText.get( ) ][ self.FromMenuText.get( ) ][ self.ToMenuText.get( ) ]
            self.ReplyTextFieldMessage = f'{ self.convertedTotal }'
        self.ReplyTextField.delete( '1.0', END )
        self.ReplyTextField.insert( END, self.ReplyTextFieldMessage )





    # Assign function for validating user input 
    def assignValidationMethod( self ) -> None:
        vcmd = self.MASTER.register( self.validate )
        self.entryField = Entry( self.MASTER, validate='key', validatecommand=( vcmd, '%P' ) )

    # Validate function for user input
    def validate( self, textEntry:str ) -> None:
        if not textEntry:
            self.userEnteredAmount = 0.0
            return True
        try:
            if float( textEntry ):
                self.userEnteredAmount = float( textEntry )
                self.updateReplyField( )
                return True
        except ValueError:
            return False





    def set_EQ_label( self ) -> None:
        self.EqualSignMessage = '    =    '
        self.EqualSignText = StringVar( )
        self.EqualSignText.set( self.EqualSignMessage )
        self.EqualSignLabel = Label( self.MASTER, textvariable=( self.EqualSignText ) )



    # Place all elements on a grid structure on the master( WINDOW )
    def asignmentLayout( self ) -> None:
        self.TypeMenu.grid(       row=0, column=0, columnspan=5, sticky=W+E )
        self.FromMenu.grid(       row=1, column=0, columnspan=2, sticky=W+E )
        self.entryField.grid(     row=2, column=0, columnspan=2             )
        self.EqualSignLabel.grid( row=1, column=2,               sticky=W+E )
        self.ToMenu.grid(         row=1, column=3, columnspan=2, sticky=W+E )
        self.ReplyTextField.grid( row=2, column=3, columnspan=2, sticky=W+E )



    # Loop Conversion Windo tiss user exits
    def masterLoop( self ) -> None:
        self.MASTER.mainloop( )
        return



if __name__ == '__main__':
    Converter( )
    raise SystemExit
