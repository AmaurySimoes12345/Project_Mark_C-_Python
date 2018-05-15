#Criar um arquivo XML com os dados abaixo:
import xml.etree.cElementTree as ET

class XML(object):
    def __init__(self, usuario, senha, nome):
        self.usuario = usuario
        self.senha = senha
        self.nome = nome

    def gerar_xml(self):    
        lista = ET.Element("lista")
        no_usuario = ET.SubElement(lista, "usuario")
        ET.SubElement(no_usuario, "user", name="user").text = self.usuario
        ET.SubElement(no_usuario, "senha", name="senha").text = self.senha
        ET.SubElement(no_usuario, "nome", name="nome").text = self.nome                
        arquivo = ET.ElementTree(lista)
        arquivo.write("Arquivo_xml.xml")

def main():
    xml = XML("admin", "123456", "teste")
    xml.gerar_xml()    

main()
