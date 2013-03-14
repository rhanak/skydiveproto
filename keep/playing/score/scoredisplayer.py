from pygame import *
font.init()

class ScoreDisplayer(Rect):

    def __init__(self,scoreformat,font,color):
        self.font           = font
        self.color      = Color(color)
        entier,_,decimal    = scoreformat.partition('.')
        self.entier         = len(entier)
        self.decimal        = len(decimal)
        self.intermed       = float(scoreformat)+1
        self.w_char,h_char  = font.size('X')
        self.char_pos       = [(x*self.w_char,0) for x in range(len(scoreformat))]
        self._image         = Surface((self.w_char*len(scoreformat),h_char),SRCALPHA)
        Rect.__init__(self,self._image.get_rect())

        self.clock          = time.Clock()
        self.set(float(scoreformat),0)

    def set(self,new,laps=0):
        self.new    = float(new)
        self.old    = self.intermed
        self.run    = 1
        self.laps   = laps
        self.time   = 0
        self.clock.tick()

    def __str__(self):
        entier,point,decimal  = str(self.intermed).partition('.')
        return entier.zfill(self.entier)+point+decimal.ljust(self.decimal,'0')

    @property
    def image(self):
        if self.run:
            self.time += self.clock.tick()
            if self.time >= self.laps:
                intermed = self.new
                self.run = 0
            else:
                intermed = round(self.old+(self.new-self.old)/self.laps*self.time,self.decimal)
            if intermed != self.intermed:
                self.intermed = intermed
                self._image.fill((0,0,0,0))
                [self._image.blit(self.font.render(c,1,self.color),pos)for pos,c in zip(self.char_pos,self.__str__())]
        return self._image
