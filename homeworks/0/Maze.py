# -*- coding: utf-8 -*-
import numpy as np
import tkinter as tk

class TkDrawer:
    def __init__(self,maze):
        self.maze=maze
        self.gifImages={ 0: 'R0lGODlhIAAgAPAAAP///wAAACH5BAAAAAAALAAAAAAgACAAAAIehI+py+0Po5y02ouz3rz7D4bi\nSJbmiabqyrbuC5sFADs=\n', 5: 'R0lGODlhIAAgAPYAAAAAAIlTAgKJPkGcBUKcB0KcCEKdCEOdCkOdC0OeC0OeDESeDESeDUSeDkSf\nDkWfEEafEUagEkagE0egFEehFUehFkihF0miGUmiGkqjG0qjHEujHkukH0ukIEykIk2lJE2lJU6m\nJU6mJk6mJ0+nKlCoLFCoLVGoLlGoL1KpMFKpMVOqM1OqNFSqNVSqNlSrNlSrN1WrOFWsOVatPFet\nPliuQFmuQlqvRFqwRluwR1uwSF2yTV6yTl6yT16zUF+zUmC0VWK1WWK2WmW4YWi6aGm7amm7bGu9\ncWy9cm2+dG/Ae//wBnLCg3TDhnTEiHfGj3jHknzKm4LOqojTuY3XxpTc15vi6gAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5\nBAAAAAAAIf8LTkVUU0NBUEUyLjADAQAAACwAAAAAIAAgAAAH/oAAgoOEhYaHiImKi1aNjo+QkUuT\nlEuEkZiZlZSXmZ6Om5OdkVONVVWaoaOPTUlDR0o6nqqDj1NSKjMqHCgoPj1TpZC0go5NGw8kLRQZ\nDTEkPVFTTpiVl1M9IhIoLy0GBCobHhlGTlGonpdOQh4UHCINBgYvGQY2PjZP6JmXPkckJlDMMNCg\noIEMP2LoILIPE6EqQ26IsCGCQoAGAwwU+CHCggofn6w8VEJERAwiAeY9aIBCRYYNL6CEHDlFiJAW\nAShQWDnOgo0mwtLVitJEhAoRAV6i8HAxQxKZM2tZmYIjwAyUM5g2eJBESpSQIqU2ohKgB4cAAW7c\nMPcV7KqpTmjjogXr6G2juHQh2bWCN29dsY/6+g1bLJJgv3blBhhMGICAxwLiRo4cALLly5YJQa6M\neXLnzpo/ix4derTpy6VPq06t2vSi17BjywYQCAAh+QQBAAABACwKAAUAEQAjAID/AAYAAAACKoyP\nqcvtj4CcslFqATx1h75dUyZm3qd5ILQ+Yhu950zX9o3n+s73/g8pAAA7\n', 3: 'R0lGODlhIAAgAPABAAAAAP///yH5BAAAAAAALAAAAAAgACAAAAJajI+py+0Po5y02gByvmsbz31A\nAnKjcoZjuoZf52Kwu2otPeNIGtt8jCnRfJohsXg5Ei3FY/D3QDqfEdth+oSiWMqrlsRThr8Nce8n\nZKLJEmG64mZX10buO1EAADs=\n',1:'R0lGODlhIAAgAPEAAAAAANIjI9DIyAAAACH5BAAAAAAALAAAAAAgACAAAAKAlI+pi+EBxJsu0mkv\nlHp3r2UhN3bidVLps7Ik+gLyTNf2TTP6ngCd4PsAf8HLUFikHI1JJvGJhDqjGiDuis3xtgzMS/X1\nmsKuTwtUGqvX6Ur2jePKe9Jq87FU3id5/j7Qp1fn9wH4ZwWXODPHGENW8YgGZhZ5diY52QZDiaHo\nWQAAOw==\n',4:'R0lGODdhIAAgAJEAAAAAAMzotf///wAAACH5BAkKAAMALAAAAAAgACAAAAIejI+py+0Po5y02ouz3rz7D4biSJbmiabqyrbuC5sFADs='}
        self.generateGuiObjects(maze)
        self.render(maze)
        self.root.mainloop()

    def render(self,maze):
        maze_width, maze_height = maze.shape
        for x in reversed(range(maze_width)):
            for y in reversed(range(maze_height)):
                self.tiles[(x,y)].configure(image = self.images[maze[x,y]])
                self.tiles[(x,y)].image=self.images[maze[x,y]]

    def generateGuiObjects(self,maze):
        self.root=tk.Tk()
        self.tiles={}
        self.images={k:tk.PhotoImage(data=self.gifImages[k]) for k in self.gifImages.keys()}
        maze_width, maze_height = maze.shape
        for x in reversed(range(maze_width)):
            for y in reversed(range(maze_height)):
                self.tiles[(x,y)]=tk.Label(self.root, image=self.images[maze[x,y]], borderwidth=1 )
                self.tiles[(x,y)].grid(row=y,column=x)


maze=np.array([[1,1,1,1,1],[1,0,0,0,1],[1,3,0,0,1],[1,1,1,0,1], [1,1,5,0,1], [1,1,1,1,1]])

if __name__ == '__main__':
    tk=TkDrawer(maze.transpose())
    tk.root.mainloop()
