# -*- coding: utf-8 -*-
"""
This module contains the GUI
"""

import logging
import random

from PyQt4 import QtGui, QtCore
from util.utili18n import le2mtrans
import questFinPestuseParams as pms
from questFinPestuseTexts import trans_QFP
import questFinPestuseTexts as texts_QFP
from client.cltgui.cltguidialogs import GuiHistorique
from client.cltgui.cltguiwidgets import WPeriod, WExplication, WSpinbox
from questFinPestuseGuiSrc import questFinPestuse_Gui

logger = logging.getLogger("le2m")


class GuiDecision(QtGui.QDialog):
    def __init__(self, defered, automatique, parent, period, historique):
        super(GuiDecision, self).__init__(parent)

        # variables
        self._defered = defered
        self._automatique = automatique
        self._historique = GuiHistorique(self, historique)

        #gui
        self.ui = questFinPestuse_Gui.Ui_Dialog()
        self.ui.setupUi(self)        

        self.setWindowTitle(trans_QFP(u"Décision"))
        self.adjustSize()
        self.setFixedSize(self.size())
        
        self.ui.comboBox_nationalite.addItems(pms.NATIONALITES)
        self.ui.comboBox_discipline.addItems(pms.ETUDES_DISCIPLINES)
        self.ui.comboBox_niveau.addItems(pms.ETUDES_ANNEES)         

        if self._automatique:
            # Tirage au sort du choix coche question 1 maximum courbe bleue profit produit Y
            self.cbleuY = random.randint(1, 3)
            if self.cbleuY == 1:
                self.ui.radioButton_cbleuY_oui.setChecked(True)
            elif self.cbleuY == 2:
                self.ui.radioButton_cbleuY_non.setChecked(True)
            else:
                self.ui.radioButton_cbleuYaut.setChecked(True)
            # Tirage au sort du choix coche question 2 choisir nombre ateliers produit Y
            self.cnbatelY = random.randint(1, 3)
            if self.cnbatelY == 1:
                self.ui.radioButton_nbatelY1.setChecked(True)
            elif self.cnbatelY == 2:
                self.ui.radioButton_nbatelY2.setChecked(True)
            else:
                self.ui.radioButton_nbatelYaut.setChecked(True)
            # Choix pour le produit Z
            self.crougeZ = random.randint(1, 2)
            if self.crougeZ == 1:
                self.ui.radioButton_crougeZ_oui.setChecked(True)
            else:
                self.ui.radioButton_crougeZ_non.setChecked(True)
            self.cbleuZ = random.randint(1, 2)
            if self.cbleuZ == 1:
                self.ui.radioButton_cbleuZ_oui.setChecked(True)
            else:
                self.ui.radioButton_cbleuZ_non.setChecked(True)
            self.cvertZ = random.randint(1, 2)
            if self.cvertZ == 1:
                self.ui.radioButton_cvertZ_oui.setChecked(True)
            else:
                self.ui.radioButton_cvertZ_non.setChecked(True)
            self.c3courbesZ = random.randint(1, 2)
            if self.c3courbesZ == 1:
                self.ui.radioButton_c3courbesZ_oui.setChecked(True)
            else:
                self.ui.radioButton_c3courbesZ_non.setChecked(True)
            # Tirage au sort du choix coche question 2 choisir nombre ateliers produit Z
            self.cnbatelZ = random.randint(1, 3)
            if self.cnbatelZ == 1:
                self.ui.radioButton_cnbatelZ1.setChecked(True)
            elif self.cnbatelZ == 2:
                self.ui.radioButton_cnbatelZ2.setChecked(True)
            else:
                self.ui.radioButton_cnbatelZaut.setChecked(True)
            # Tirage au sort du choix coche question 3 produit Z
            self.cpqZ = random.randint(1, 3)
            if self.cpqZ == 1:
                self.ui.radioButton_cpqZ1.setChecked(True)
            elif self.cpqZ == 2:
                self.ui.radioButton_cpqZ2.setChecked(True)
            else:
                self.ui.radioButton_cpqZaut.setChecked(True)
                
            # Tirage au sort des donnees obligatoires
            # age
            tirage_age = random.randint(7, 77)
            self.ui.lineEdit_age.setText(str(tirage_age))
            # Sexe
            tirage_sexe = random.randint(1, 2)
            if tirage_sexe == 1:
                self.ui.radioButton_sexeF.setChecked(True)
            else:
                self.ui.radioButton_sexeH.setChecked(True)
            # Nationalite
            self.ui.comboBox_nationalite.setCurrentIndex(random.randint(1,  self.ui.comboBox_nationalite.count() - 1))
            #etudiant
            self.ui.radioButton_etudiant_oui.setChecked(True)
            if random.randint(0,  1): self.ui.radioButton_etudiant_non.setChecked(True)
            if self.ui.radioButton_etudiant_oui.isChecked():
                self.ui.comboBox_discipline.setCurrentIndex(random.randint(1,  self.ui.comboBox_discipline.count() - 1))
                self.ui.comboBox_niveau.setCurrentIndex(random.randint(1,  self.ui.comboBox_niveau.count() - 1))            
            #expériences antérieures
            self.ui.radioButton_expe_oui.setChecked(True)
            if random.randint(0,  1): self.ui.radioButton_expe_non.setChecked(True)
            # Prise de risques
            tirage_risque = random.randint(0, 10)
            self.ui.horizontalSlider_risques.setValue(tirage_risque)
            
 
            self._timer_automatique = QtCore.QTimer()
            self._timer_automatique.timeout.connect(self._accept)
            self._timer_automatique.start(7000)

        # Bouton de validation
        self.ui.pushButton_valider.clicked.connect(self._accept)

    def reject(self):
        pass
    
    def _accept(self):
        try:
            self._timer_automatique.stop()
        except AttributeError:
            pass
        # Test des saisir du questionnaire
        # Age
        try:
            test_age = int(self.ui.lineEdit_age.text())
        except ValueError:
            QtGui.QMessageBox.warning(self, "ATTENTION" , u"Votre saisie age n'est pas correcte",  QtGui.QMessageBox.Ok)
            return
        if test_age <= 6 or test_age >= 78:
            QtGui.QMessageBox.warning(self, "ATTENTION" , u"Votre saisie age n'est pas correcte",  QtGui.QMessageBox.Ok)
            return
        # Sexe
        test_sexe = 0
        if self.ui.radioButton_sexeF.isChecked() == 1 or self.ui.radioButton_sexeH.isChecked() == 1:
            test_sexe = 1
        if test_sexe == 0:
            QtGui.QMessageBox.warning(self, "ATTENTION" , u"Vous n'avez pas indiqué votre sexe",  QtGui.QMessageBox.Ok)
            return
        # nationalite
        if self.ui.comboBox_nationalite.currentIndex() == 0:
            QtGui.QMessageBox.warning(self, "ATTENTION" , u"Vous devez préciser votre nationalité.",  QtGui.QMessageBox.Ok)
            return
        # étudiant
        if not self.ui.radioButton_etudiant_oui.isChecked() and not self.ui.radioButton_etudiant_non.isChecked():
            QtGui.QMessageBox.warning(self, "ATTENTION" , u"Vous devez préciser si vous êtes ou non étudiant(e).",  QtGui.QMessageBox.Ok)
            return 
        else: 
            etudiant = self.ui.radioButton_etudiant_oui.isChecked()
        if etudiant is True:
            if self.ui.comboBox_discipline.currentIndex()  == 0:
                QtGui.QMessageBox.warning(self, "ATTENTION" , u"Vous devez préciser la discipline que vous étudiez.",  QtGui.QMessageBox.Ok)
                return  
            else: 
                etudiant_discipline = self.ui.comboBox_discipline.currentIndex()
            if self.ui.comboBox_niveau.currentIndex() == 0: 
                QtGui.QMessageBox.warning(self, "ATTENTION" , u"Vous devez préciser votre niveau d'études.",  QtGui.QMessageBox.Ok)
                return  
            else: 
                etudiant_niveau = self.ui.comboBox_niveau.currentIndex()
        else:
            etudiant_discipline = ""
            etudiant_niveau = ""
        # participation expériences
        if not self.ui.radioButton_expe_oui.isChecked() and not self.ui.radioButton_expe_non.isChecked(): 
            QtGui.QMessageBox.warning(self, "ATTENTION" , u"Vous devez préciser si vous avez déjà ou non participé à une expérience d'économie.",  QtGui.QMessageBox.Ok)
            return 
        else: 
            experiences = self.ui.radioButton_expe_oui.isChecked()
        # Prise de risques
        

        # On recupere les valeurs a passer produit Y
        # Choix coche question 1 maximum courbe bleue profit produit Y
        rep_cbleuy = 0
        preciscbleuy = ''
        if self.ui.radioButton_cbleuY_oui.isChecked() == 1:
            rep_cbleuy = 1
        elif self.ui.radioButton_cbleuY_non.isChecked() == 1:
            rep_cbleuy = 2
        elif self.ui.radioButton_cbleuYaut.isChecked() == 1:
            rep_cbleuy = 3
            # ICI RECUPERE LA VALEUR DE self.ui.lineEdit_cbleuY_precis LA PRECISION DE AUTRE
            preciscbleuy = unicode(self.ui.lineEdit_cbleuY_precis.text().toUtf8(), "utf-8")
        #  Choix coche question 2 choisir nombre ateliers produit Y
        rep_nbately = 0
        preciscnbately = ''
        if self.ui.radioButton_nbatelY1.isChecked() == 1:
            rep_nbately = 1
        elif self.ui.radioButton_nbatelY2.isChecked() == 1:
            rep_nbately = 2
        elif self.ui.radioButton_nbatelYaut.isChecked() == 1:
            rep_nbately = 3
            # ET ON RECUPERE LA VALEUR DE self.ui.lineEdit_nbatelYprecis
            preciscnbately = unicode(self.ui.lineEdit_nbatelYprecis.text().toUtf8(), "utf-8")
        # Autre strategie produit Y
        autstrategiey = ''
        autstrategiey = unicode(self.ui.lineEdit_autstrategieY.text().toUtf8(), "utf-8")
        
        # On recupere les valeurs a passer produit Z
        # Choix courbe rouge
        rep_crougez = 0
        if self.ui.radioButton_crougeZ_oui.isChecked() == 1:
            rep_crougez = 1
        elif self.ui.radioButton_crougeZ_non.isChecked() == 1:
            rep_crougez = 2
        rep_cbleuz = 0
        if self.ui.radioButton_cbleuZ_oui.isChecked() == 1:
            rep_cbleuz = 1
        elif self.ui.radioButton_cbleuZ_non.isChecked() == 1:
            rep_cbleuz = 2
        rep_cvertz = 0
        if self.ui.radioButton_cvertZ_oui.isChecked() == 1:
            rep_cvertz = 1
        elif self.ui.radioButton_cvertZ_non.isChecked() == 1:
            rep_cvertz = 2
        rep_c3courbesz = 0
        if self.ui.radioButton_c3courbesZ_oui.isChecked() == 1:
            rep_c3courbesz = 1
        elif self.ui.radioButton_c3courbesZ_non.isChecked() == 1:
            rep_c3courbesz = 2
        #  Choix coche question 2 choisir nombre ateliers produit Z
        rep_nbatelz = 0
        preciscnbatelz = ''
        if self.ui.radioButton_cnbatelZ1.isChecked() == 1:
            rep_nbatelz = 1
        elif self.ui.radioButton_cnbatelZ2.isChecked() == 1:
            rep_nbatelz = 2
        elif self.ui.radioButton_cnbatelZaut.isChecked() == 1:
            rep_nbatelz = 3
            # ET ON RECUPERE LA VALEUR DE self.ui.lineEdit_nbatelYprecis
            preciscnbatelz = unicode(self.ui.lineEdit_nbatelZprecis.text().toUtf8(), "utf-8")
        #  Choix coche question 3 choisir nombre ateliers produit Z
        rep_cpqz = 0
        preciscpqz = ''
        if self.ui.radioButton_cpqZ1.isChecked() == 1:
            rep_cpqz = 1
        elif self.ui.radioButton_cpqZ2.isChecked() == 1:
            rep_cpqz = 2
        elif self.ui.radioButton_cpqZaut.isChecked() == 1:
            rep_cpqz = 3
            # ET ON RECUPERE LA VALEUR DE self.ui.lineEdit_nbatelYprecis
            preciscpqz = unicode(self.ui.lineEdit_pqZprecis.text().toUtf8(), "utf-8")  
        # Autre strategie produit Z
        autstrategiez = ''
        autstrategiez = unicode(self.ui.lineEdit_autstrategieZ.text().toUtf8(), "utf-8")        
        # Recuperation des données obligatoires
        # age
        age = int(self.ui.lineEdit_age.text())
        # Sexe
        if self.ui.radioButton_sexeF.isChecked() == 1:
            sexe = 0
        else:
            sexe = 1
        # Nationalite
        nationalite = self.ui.comboBox_nationalite.currentIndex()
        # Etudiant Recupere plus haut
        # Participation experiences voir plus haut
        # prise de risques
        rep_risque = self.ui.horizontalSlider_risques.value()
        
        
        decision = [] # METREE LES VALEURS DE CHOIX
        decision.append(rep_cbleuy)
        decision.append(preciscbleuy)
        decision.append(rep_nbately)
        decision.append(preciscnbately)
        decision.append(autstrategiey)
        decision.append(rep_crougez)
        decision.append(rep_cbleuz)
        decision.append(rep_cvertz)
        decision.append(rep_c3courbesz)
        decision.append(rep_nbatelz)
        decision.append(preciscnbatelz)
        decision.append(rep_cpqz)
        decision.append(preciscpqz)
        decision.append(autstrategiez)
        decision.append(age)
        decision.append(sexe)
        decision.append(nationalite)
        decision.append(etudiant)
        decision.append(etudiant_discipline)
        decision.append(etudiant_niveau)
        decision.append(experiences)
        decision.append(rep_risque)
        if not self._automatique:
            confirmation = QtGui.QMessageBox.question(
                self, le2mtrans(u"Confirmation"),
                le2mtrans(u"Do you confirm your choice?"),
                QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)
            if confirmation != QtGui.QMessageBox.Yes: 
                return
        logger.info(u"Send back {}".format(decision))
        self.accept()
        self._defered.callback(decision)


class DConfigure(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)

        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)

        form = QtGui.QFormLayout()
        layout.addLayout(form)

        # treatment
        self._combo_treatment = QtGui.QComboBox()
        self._combo_treatment.addItems(
            list(sorted(pms.TREATMENTS_NAMES.viewvalues())))
        self._combo_treatment.setCurrentIndex(pms.TREATMENT)
        form.addRow(QtGui.QLabel(u"Traitement"), self._combo_treatment)

        # nombre de périodes
        self._spin_periods = QtGui.QSpinBox()
        self._spin_periods.setMinimum(0)
        self._spin_periods.setMaximum(100)
        self._spin_periods.setSingleStep(1)
        self._spin_periods.setValue(pms.NOMBRE_PERIODES)
        self._spin_periods.setButtonSymbols(QtGui.QSpinBox.NoButtons)
        self._spin_periods.setMaximumWidth(50)
        form.addRow(QtGui.QLabel(u"Nombre de périodes"), self._spin_periods)

        # periode essai
        self._checkbox_essai = QtGui.QCheckBox()
        self._checkbox_essai.setChecked(pms.PERIODE_ESSAI)
        form.addRow(QtGui.QLabel(u"Période d'essai"), self._checkbox_essai)

        # taille groupes
        self._spin_groups = QtGui.QSpinBox()
        self._spin_groups.setMinimum(0)
        self._spin_groups.setMaximum(100)
        self._spin_groups.setSingleStep(1)
        self._spin_groups.setValue(pms.TAILLE_GROUPES)
        self._spin_groups.setButtonSymbols(QtGui.QSpinBox.NoButtons)
        self._spin_groups.setMaximumWidth(50)
        form.addRow(QtGui.QLabel(u"Taille des groupes"), self._spin_groups)

        button = QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
        button.accepted.connect(self._accept)
        button.rejected.connect(self.reject)
        layout.addWidget(button)

        self.setWindowTitle(u"Configurer")
        self.adjustSize()
        self.setFixedSize(self.size())

    def _accept(self):
        pms.TREATMENT = self._combo_treatment.currentIndex()
        pms.PERIODE_ESSAI = self._checkbox_essai.isChecked()
        pms.NOMBRE_PERIODES = self._spin_periods.value()
        pms.TAILLE_GROUPES = self._spin_groups.value()
        self.accept()
