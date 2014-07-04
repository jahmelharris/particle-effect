#!/usr/bin/python
import pygame, sys, random, array
from pygame.locals import *

class particle:
	xstart = 0 
	ystart = 0
	def __init__(self, x, y):
		random.seed()
		self.xstart = x
		self.ystart = y
		self.xoffset = random.randint(-40,40)
		self.yoffset = random.randint(-40,40)
	def getXoffset(self):
		self.xstart += self.xoffset
		return self.xstart
	def getYoffset(self):
		self.ystart += self.yoffset
		return self.ystart
windowSurfaceObj = pygame.display.set_mode((1024,768))
#particles = [particle(200,300) for count in xrange(300)]
def draw():
	windowSurfaceObj.fill(pygame.Color(0,0,0))
	for x in particles:
		pygame.draw.rect(windowSurfaceObj,redColor,(x.getXoffset(),x.getYoffset(),2,2))


def init():
	pygame.display.set_caption('Particle Test')
	pygame.init()

init()
particles = []
fpsClock = pygame.time.Clock()
redColor = pygame.Color(255,255,255)
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_q:
				pygame.quit()
				sys.exit()
		elif event.type == MOUSEBUTTONUP:
			mousex, mousey = event.pos
			particles = [particle(mousex,mousey) for count in xrange(300)]

	pygame.display.update();
	fpsClock.tick(30)
	draw()

