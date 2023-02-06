
from typing import Any
import json


class DummyArgs:
    """ Essa classe eh so para exemplo e nao devera existir
    na versao final do codigo. Ela foi criada porque a forma
    de usar os argumentos de linha de comando depois sera
    similar.
    """

    def __init__(self):
        self.config_path = ""
        self.report_path = ""


def parse_args() -> Any:
    """ le os argumentos de linha de comando usando a biblioteca argparse """
    import argparse 
  
  
    parser = argparse.ArgumentParser(description ='nome e endereço json, nome arq final') 
    parser.add_argument('config', metavar ='N',  
                        type = str, nargs ='+', 
                        help ='arquivo json') 
    
    
    
    args = parser.parse_args()

    
    
    with open('data/configs/' + str(args.config[0])) as file:
        data = json.load(file)
    
    
    return data
        # Exemplo. Utilizar o argparse na versao final
    
