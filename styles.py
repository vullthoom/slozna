from PyQt5.QtGui import QFont
BACKGROUND_COLOR = 'background-color: #08457e;'
TITLE_FONT = QFont('Eurofurence', 23, QFont.Weight.Bold)
SUBTITLE_FONT = QFont('Eurofurence', 15, QFont.Weight.Normal)


class StyleButton:
    def baseButton():
        return '''
        QPushButton {
            background-color: #08457e;
            font-size: 25px;
            font-family: 'Eurofurence', sans-serif;
            color: #499EEC;
            border: 1px solid #499EEC;
            border-radius: 5px;
        }
        QPushButton:hover:pressed {
            background-color: #499EEC;
            color: #08457e;
            border: 1px solid #08457e;
        }
        '''

    def enterButton():
        return '''
        QPushButton {
            background-color: #499EEC;
            font-weight: 500;
            font-size: 40px;
            padding-top: 80px;
            color: #08457e;
            border: 1px solid #499EEC;
            border-radius: 5px;
        }
        QPushButton:hover:pressed {
            background-color: #08457e;
            color: #499EEC;
            border: 1px solid #499EEC;
        }
        '''

    def deleteButton():
        return '''
        QPushButton {
            background-color: #2B2B2B;
            font-size: 25px;
            padding-top: 5px;
            color: #499EEC;
            border: 1px solid #499EEC;
            border-radius: 5px;
        }
        QPushButton:hover:pressed {
            background-color: #499EEC;
            color: #2B2B2B;
            border: 1px solid #499EEC;
        }
        '''
    # background-color: rgba(200, 200, 200, .25);
    # 
    def settings():
        return '''
        QPushButton { 
            background-color: rgba(200, 200, 200, .0);
            padding-top: 3px;
        }
        '''
    
    def apply_back():
        return '''
        QPushButton { 
            background-color: rgba(200, 200, 200, .0);
        }
        '''