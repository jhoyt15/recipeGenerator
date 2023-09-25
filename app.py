import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.0.0')

class RecipeGenerator(App):

    def build(self):
        return BoxLayout()
    

RecipeGeneratorApp = RecipeGenerator()
RecipeGeneratorApp.run()