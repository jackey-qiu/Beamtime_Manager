# -*- coding: utf-8 -*-
from pyqtgraph.parametertree import Parameter, ParameterTree
import configparser
from pathlib import Path
from os import listdir
root = Path(__file__).parent.parent/ "resources" / "templates"

class SolverParameters(ParameterTree):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.data_type = None
        self.config_file = None

    def _build_pars(self):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        pars = []
        for section in config.sections():
            par = {'name': section, 'type': 'group', 'children': []}
            for key, item in config.items(section):
                par['children'].append( {"name":key,"type":["str","text"][int(len(item)>20)],"value":str(item)})
            pars.append(par)
        return Parameter.create(name='params', type='group', children=pars)

    def init_pars(self,config_file):
        self.config_file = str(root/config_file)
        pars = self._build_pars()
        self.setParameters(pars, showTop=False)
        self.par = pars

    def save_parameter(self):
        config = configparser.ConfigParser()
        sections = self.par.names.keys()
        for section in sections:
            sub_sections = self.par.names[section].names.keys()
            items = {}
            for each in sub_sections:
                items[each] = str(self.par[(section,each)])
            config[section] = items
        with open(self.config_file,'w') as config_file:
            config.write(config_file)

    def update_parameter_in_solver(self,parent):
        pass

