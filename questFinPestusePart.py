# -*- coding: utf-8 -*-

import logging
from datetime import datetime
from twisted.internet import defer
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Float, ForeignKey,  String
from server.servbase import Base
from server.servparties import Partie
from util.utiltools import get_module_attributes
import questFinPestuseParams as pms


logger = logging.getLogger("le2m")


class PartieQFP(Partie):
    __tablename__ = "partie_questFinPestuse"
    __mapper_args__ = {'polymorphic_identity': 'questFinPestuse'}
    partie_id = Column(Integer, ForeignKey('parties.id'), primary_key=True)
    repetitions = relationship('RepetitionsQFP')

    def __init__(self, le2mserv, joueur):
        super(PartieQFP, self).__init__(
            nom="questFinPestuse", nom_court="QFP",
            joueur=joueur, le2mserv=le2mserv)
        self.QFP_gain_ecus = 0
        self.QFP_gain_euros = 0

    @defer.inlineCallbacks
    def configure(self):
        logger.debug(u"{} Configure".format(self.joueur))
        yield (self.remote.callRemote("configure", get_module_attributes(pms)))
        self.joueur.info(u"Ok")

    @defer.inlineCallbacks
    def newperiod(self, period):
        """
        Create a new period and inform the remote
        If this is the first period then empty the historic
        :param periode:
        :return:
        """
        logger.debug(u"{} New Period".format(self.joueur))
        self.currentperiod = RepetitionsQFP(period)
        self.le2mserv.gestionnaire_base.ajouter(self.currentperiod)
        self.repetitions.append(self.currentperiod)
        yield (self.remote.callRemote("newperiod", period))
        logger.info(u"{} Ready for period {}".format(self.joueur, period))

    @defer.inlineCallbacks
    def display_decision(self):
        """
        Display the decision screen on the remote
        Get back the decision
        :return:
        """
        logger.debug(u"{} Decision".format(self.joueur))
        debut = datetime.now()
        les_decisions = yield(self.remote.callRemote(
            "display_decision"))
        self.currentperiod.QFP_decisiontime = (datetime.now() - debut).seconds
        # Extraction des decisions
        self.currentperiod.QFP_rep_cbleuY = les_decisions[0]
        self.currentperiod.QFP_precis_cbleuY = les_decisions[1]
        self.currentperiod.QFP_rep_cnbatelY = les_decisions[2]
        self.currentperiod.QFP_precis_cnbatelY = les_decisions[3]
        self.currentperiod.QFP_aut_strategieY = les_decisions[4]
        self.currentperiod.QFP_rep_crougeZ = les_decisions[5]
        self.currentperiod.QFP_rep_cbleuZ = les_decisions[6]
        self.currentperiod.QFP_rep_cvertZ = les_decisions[7]
        self.currentperiod.QFP_rep_c3courbes = les_decisions[8]
        self.currentperiod.QFP_rep_cnbatelZ = les_decisions[9]
        self.currentperiod.QFP_precis_cnbatelZ = les_decisions[10]
        self.currentperiod.QFP_rep_cpqz = les_decisions[11]
        self.currentperiod.QFP_precis_cpqz = les_decisions[12]
        self.currentperiod.QFP_aut_strategieZ = les_decisions[13]
        self.currentperiod.QFP_age = les_decisions[14]
        self.currentperiod.QFP_sexe = les_decisions[15]
        self.currentperiod.QFP_nationalite = les_decisions[16]
        self.currentperiod.QFP_etudiant = les_decisions[17]
        self.currentperiod.QFP_discipline = les_decisions[18]
        self.currentperiod.QFP_niveau = les_decisions[19]
        self.currentperiod.QFP_expe = les_decisions[20]
        self.currentperiod.QFP_risque = les_decisions[21]
#        self.currentperiod.QFP_risque = Column(Integer)
        
        self.joueur.info(u"{}".format(self.currentperiod.QFP_decision))
        self.joueur.remove_waitmode()

    def compute_periodpayoff(self):
        """
        Compute the payoff for the period
        :return:
        """
        logger.debug(u"{} Period Payoff".format(self.joueur))
        self.currentperiod.QFP_periodpayoff = 0

        # cumulative payoff since the first period
        if self.currentperiod.QFP_period < 2:
            self.currentperiod.QFP_cumulativepayoff = \
                self.currentperiod.QFP_periodpayoff
        else: 
            previousperiod = self.periods[self.currentperiod.QFP_period - 1]
            self.currentperiod.QFP_cumulativepayoff = \
                previousperiod.QFP_cumulativepayoff + \
                self.currentperiod.QFP_periodpayoff

        # we store the period in the self.periodes dictionnary
        self.periods[self.currentperiod.QFP_period] = self.currentperiod

        logger.debug(u"{} Period Payoff {}".format(
            self.joueur,
            self.currentperiod.QFP_periodpayoff))

    @defer.inlineCallbacks
    def display_summary(self, *args):
        """
        Send a dictionary with the period content values to the remote.
        The remote creates the text and the history
        :param args:
        :return:
        """
        logger.debug(u"{} Summary".format(self.joueur))
        yield(self.remote.callRemote(
            "display_summary", self.currentperiod.todict()))
        self.joueur.info("Ok")
        self.joueur.remove_waitmode()

    @defer.inlineCallbacks
    def compute_partpayoff(self):
        """
        Compute the payoff for the part and set it on the remote.
        The remote stores it and creates the corresponding text for display
        (if asked)
        :return:
        """
        logger.debug(u"{} Part Payoff".format(self.joueur))

        self.QFP_gain_ecus = self.currentperiod.QFP_cumulativepayoff
        self.QFP_gain_euros = float(self.QFP_gain_ecus) * float(pms.TAUX_CONVERSION)
        yield (self.remote.callRemote(
            "set_payoffs", self.QFP_gain_euros, self.QFP_gain_ecus))

        logger.info(u'{} Payoff ecus {} Payoff euros {:.2f}'.format(
            self.joueur, self.QFP_gain_ecus, self.QFP_gain_euros))


class RepetitionsQFP(Base):
    __tablename__ = 'partie_questFinPestuse_repetitions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    partie_partie_id = Column(
        Integer,
        ForeignKey("partie_questFinPestuse.partie_id"))

    QFP_period = Column(Integer)
    QFP_treatment = Column(Integer)
    QFP_group = Column(Integer)
    QFP_decision = Column(Integer)
    QFP_decisiontime = Column(Integer)
    QFP_periodpayoff = Column(Float)
    QFP_cumulativepayoff = Column(Float)
    
    QFP_rep_cbleuY = Column(Integer)
    QFP_precis_cbleuY = Column(String)
    QFP_rep_cnbatelY = Column(Integer)
    QFP_precis_cnbatelY = Column(String)
    QFP_aut_strategieY = Column(String)
    QFP_rep_crougeZ = Column(Integer)
    QFP_rep_cbleuZ = Column(Integer)
    QFP_rep_cvertZ = Column(Integer)
    QFP_rep_c3courbes = Column(Integer)
    QFP_rep_cnbatelZ = Column(Integer)
    QFP_precis_cnbatelZ = Column(String)
    QFP_rep_cpqz = Column(Integer)
    QFP_precis_cpqz = Column(String)
    QFP_aut_strategieZ = Column(String)
    QFP_age = Column(Integer)
    QFP_sexe = Column(Integer)
    QFP_nationalite = Column(Integer)
    QFP_etudiant = Column(Integer)
    QFP_discipline = Column(Integer)
    QFP_niveau = Column(Integer)
    QFP_expe = Column(Integer)
    QFP_risque = Column(Integer)

    def __init__(self, period):
        self.QFP_treatment = pms.TREATMENT
        self.QFP_period = period
        self.QFP_decisiontime = 0
        self.QFP_periodpayoff = 0
        self.QFP_cumulativepayoff = 0

    def todict(self, joueur=None):
        temp = {c.name: getattr(self, c.name) for c in self.__table__.columns
                if "QFP" in c.name}
        if joueur:
            temp["joueur"] = joueur
        return temp

