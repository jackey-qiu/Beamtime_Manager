from pathlib import Path
from os import listdir
from .db_operations import logical_query, init_pandas_model_from_db
from ..config import config

def populate_config_template_files(self):
    root = Path(__file__).parent.parent/ "resources" / "templates"
    init_files = [each[0:-4] for each in listdir(str(root)) if each.endswith('ini')]
    self.comboBox_templates.clear()
    self.comboBox_templates.addItems(init_files)

def extract_config_template(self):
    self.widget_analysis_config.init_pars(self.comboBox_templates.currentText()+'.ini')

def parse_query_conditions(self):
    logic = self.comboBox_logic.currentText()
    left_field = {self.comboBox_search_field.currentText():self.lineEdit_search_item1.text()}
    right_field = {self.comboBox_search_field2.currentText():self.lineEdit_search_item2.text()}
    fields = [each for each in config.display_fields if each!='select']
    targets = logical_query(self,'scan_info',logic,left_field,right_field,fields)
    init_pandas_model_from_db(self,targets)


