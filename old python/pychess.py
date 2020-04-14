import chess
import chess.uci
import winspeech
import time
board = chess.Board()
def make_move():
 y = input("please input your move: ")
 u = chess.Move.from_uci(y)
 board.push(u)
 print (board)

def moves():
 f = board.legal_moves()
def check():
 c = board.is_check()
 print (c)
def unmake():
 board.pop()
def game_over():
 a = board.is_game_over()
 print (a)
def ai_move():
 engine = chess.uci.popen_engine("C:\\Users\\arunm\\Downloads\\stockfish-10-win\\stockfish-10-win\\Windows\\stockfish_10_x64.exe")
 info_handlers = chess.uci.InfoHandler()
 engine.info_handlers.append(info_handlers)
 engine.position(board)
 com = engine.go(searchmoves = board.legal_moves,movetime = 3000)
 print (com)
 x = input ("please play the move displayed: ")
 d = chess.Move.from_uci(x)
 board.push(d)
 print (board)

def congrats():
 for i in range(1):
  winspeech.say("you played very well and its okay if you lost cause theres always time to improve. Take this as rather a lesson to learn from I felt very honoured to play with you and wish you better luck next time")