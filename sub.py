import re

class scene:
  def __init__(self,lines:str,Tlist=[],Flist=[],Ts=0,Fs=0,Os=0) -> None:
    self.lines = lines
    self.T_reaction = Tlist
    self.F_reaction = Flist
    self.Ts = Ts
    self.Fs = Fs
    self.Myindex = None
    self.Os = Os


class gamesystem:
  def __init__(self) -> None:
    self.scene = []

    self.scene.append(scene('夢ノ中へようこそ\nボクは「ユメ」だよ',Os=1))
    self.scene.append(scene('ここはボクの世界．ボクがここのアルジだ．ボクがゼッタイのばしょだ',Os=2))
    self.scene.append(scene('あそぶトモダチがいないんだ．いっしょにあそぼうよ．',Tlist=[r'いいよ',r'^うん',r'良いよ',r'おっけー',r'オッケー',r'おｋ',r'^$'],Flist=[r'いや[だ]?',r'嫌[だ]?',r'遊びたくない'],Ts=3,Fs=8,Os=-1))
    self.scene.append(scene('それじゃあ......\n「カクレンボ」をしよう',Flist=[r'いや[だ]?',r'嫌[だ]?',r'おにぎり'],Os=4,Fs=-1))
    self.scene.append(scene('じゃあ，キミがかくれて',Flist=[r'いや[だ]?',r'嫌[だ]?',r'おにがいい',r'鬼がいい'],Os=5,Fs=-1))
    self.scene.append(scene('1,2,3,...,10 もういいかーい！',Tlist=[r''],Os=6,Ts=-1))
    self.scene.append(scene('みっけー！声出したらだめだよ',Os=7))
    self.scene.append(scene('いっかいきゅうけいにしよう．',Os=8))
    self.scene.append(scene('じゃあ...\nなにかたべたいんだけど，きみごはんつくれる？',Tlist=[r'つくれる',r'できる',r'うん'],Ts=9))
    self.scene.append(scene('つくれるの！じゃあ作ってよ．\nたのしみだなぁ．',Os=-1))
    
    self.scene.append(scene('--製作途中につきここで終了--'))
    
    for i,s in enumerate(self.scene):
      s.Myindex = i
      if s.Ts == 0:
        s.Ts = i
      elif s.Os == 0:
        s.Os = i
      elif s.Fs == 0:
        s.Fs = i

    self.sceneNow = self.scene[0]
  
  
  def text_checker(self,text:str,scene:scene):
    if self.searchTalk(text,scene.T_reaction):
      return 1
    elif self.searchTalk(text,scene.F_reaction):
      return 2
    else:
      return 0
    
  
  def searchTalk(self,talk,text):
    for t in text:
      if re.search(t,talk):
        return True
    else:
      return False
