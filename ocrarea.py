#!/usr/bin/env python

""" Lector: ocrarea.py

    Copyright (C) 2008 Davide Setti

    This program is released under the GNU GPLv2
""" 

import sys
import Image
import os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication as qa


class OcrArea(QtGui.QGraphicsRectItem):
    
    ## static data
    resizeborder = .0
    
    def __init__(self, pos, size, type, parent = None, scene = None, areaBorder = 2, index = 0, textSize = 50):
        QtGui.QGraphicsRectItem.__init__(self, 0, 0, size.width(), size.height(), parent, scene)
        self.setPos(pos)
        
        #self.setAcceptedMouseButtons(QtCore.Qt.NoButton)
        self.setFlags(QtGui.QGraphicsItem.ItemIsMovable |
            QtGui.QGraphicsItem.ItemIsFocusable |
            QtGui.QGraphicsItem.ItemIsSelectable)
        
        ## set index label
        self.text = QtGui.QGraphicsTextItem("%d" % index, self)
        self.setTextSize(textSize)

        ## TODO: come creare delle costanti per il tipo? (come le costanti nelle Qt) (enum?)
        self.type = type

        pen = QtGui.QPen(self.color, areaBorder, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin)
        self.setPen(pen)
        self.setAcceptsHoverEvents(True)

        # self.text.setFlag(QtGui.QGraphicsItem.ItemIgnoresTransformations)


    def setIndex(self, idx):
        self.text.setPlainText("%d" % idx)


    def setTextSize(self, size):
        font = QtGui.QFont()
        font.setPointSizeF(size)
        self.text.setFont(font)


    def contextMenuEvent(self, event):
        menu = QtGui.QMenu()
        removeAction = menu.addAction(qa.translate('QOcrWidget', "Remove"))
        #Action = menu.addAction(self.scene().tr("Remove"))
        menu.addSeparator()
        textAction = menu.addAction(qa.translate('QOcrWidget', "Text"))
        graphicsAction = menu.addAction(qa.translate('QOcrWidget', "Graphics"))
        selectedAction = menu.exec_(event.screenPos())

        if selectedAction == removeAction:
            self.scene().removeArea(self)
        elif selectedAction == textAction:
            self.type = 1
        elif selectedAction == graphicsAction:
            self.type = 2


    ## type property
    def _setType(self, type):
        self.__type = type
        
        if self.__type == 1:
            self.color = QtCore.Qt.darkGreen
        else: ## TODO: else -> elif ... + else raise exception
            self.color = QtCore.Qt.blue
        
        self.text.setDefaultTextColor(self.color)

        pen = self.pen()
        pen.setColor(self.color)
        self.setPen(pen)

    def _type(self):
        return self.__type

    type = property(fget=_type, fset=_setType)


