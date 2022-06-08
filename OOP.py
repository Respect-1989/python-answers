# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 14:25:31 2022

@author: Proger
"""

class Talaba:
    def __init__(self,ism,familya,tyil):
        self.name=ism
        self.s_name=familya
        self.year=tyil
    
    def tanishuv(self):
        print(f"Ismim: {self.name} {self.s_name} Tug'ilgan yilim: {self.year}")
    
        
talaba1=Talaba("Dilshod", "Atadjanov", 1989)
talaba2=Talaba("Anvar", "Atadjanov", 1980)
talaba3=Talaba("Alisher", "Atadjanov", 1983)


 