import View as v
import GeneticImages
import FitnessFunctions as ff
import PIL

f = ff.CircleFitnessFunction()
g = GeneticImages.GeneticImages(f, 8)

v.initGUI(g)
#p = g.get_population()
#g.step(500)
#p = g.get_population()
#p[0].show()