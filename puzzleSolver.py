import Queue
import copy

class PuzzleNode(object):
	
	def __init__(self, a_state, a_parent, a_action, a_columns, a_rows):
		self.state = copy.deepcopy(a_state)
		self.parent = a_parent
		self.action = copy.copy(a_action)
		self.columns = a_columns
		self.rows = a_rows

	def getAllMoves(self): #return a list of states? or PuzzleNodes?
		moves = [] #gonna need to compute the zero's coordinates, as a list (x,y)
			   #gonna need zeroIsOnLeft,Right,Top,Bottom methods
	# UP - if (!zeroOnTop()) return TRUE
	# DOWN - if (!zeroOnBottom()) return TRUE 
	# RIGHT - if (!zeroOnRight()) return TRUE
	# LEFT - if (!zeroOnLeft()) return TRUE
		if not self.zeroIsOnLeft():
			moves.append('L')
		if not self.zeroIsOnRight():
			moves.append('R')
		if not self.zeroIsOnTop():
			moves.append('U')
		if not self.zeroIsOnBottom():
			moves.append('D')

		return moves

	def zeroPos(self):
		#return position (x,y) of zero
		#need to search 2D array

		for i in range(len(self.state)):
			for j in range(len(self.state[i])):
				if self.state[i][j] == int(0):
					#print 'zero is:' + [i,j]
					return [i,j]
		print 'zero not found'

	def zeroIsOnLeft(self):   
		#return true if zeroPos is (0,*)
		zeroPosition = self.zeroPos()
		if zeroPosition[1]==0:
			return True
		else:
			return False
	
	def zeroIsOnRight(self):
		#return TRUE if zeroPos is (*, columns-1)
		zeroPosition = self.zeroPos()
		if zeroPosition[1]==self.columns-1:
			return True
		else:
			return False

	def zeroIsOnTop(self):
		#return TRUE if zeroPos is (*,0)
		zeroPosition = self.zeroPos()
		if zeroPosition[0]==0:
			return True
		else:
			return False

	def zeroIsOnBottom(self):
		#return TRUE if zeroPos is(*,rows-1)
		zeroPosition = self.zeroPos()
		if zeroPosition[0]==self.rows-1:
			return True
		else:
			return False
	def printState(self):
		print self.state
	
class Problem(object):
	def __init__(self, a_rows, a_columns, a_state):
		self.rows = a_rows
		self.columns = a_columns
		self.state = copy.deepcopy(a_state)
		#self.goalState=[]
		#self.goalState.append([])
		#self.goalState=self.state
		self.goalState = []

		for i in range(0, self.rows*self.columns, columns):
			inner_list = []
			for x in range(i,i+columns):
				inner_list.append(int(0))
			self.goalState.append(inner_list)	
		self.count=int(1)
		for i in range(len(a_state)):
			for j in range(len(a_state[i])):
				self.goalState[i][j] = self.count
				self.count = self.count+1
		self.goalState[self.rows-1][self.columns-1]=0
		print 'GoalState:'
		print self.goalState	
	def goalTest(self, a_state):
		#if a_state is at goal, return TRUE - else FALSE
		# build goalState in Problem init
		print 'GoalTest:'
		print 'a_state:'
		print a_state
		print 'goal state'
		print self.goalState
		for i in range(len(a_state)):
			for j in range(len(a_state[i])):
				if not self.goalState[i][j]==a_state[i][j]:
					return False
		return True
	#def printState(a_state):
		#print a state in the correct format

	def getResult(self, a_node, a_action):
		#return a new state given a_state and a_action
		newState=copy.deepcopy(a_node.state)
		zeroCoord = a_node.zeroPos()
		zeroI = copy.copy(zeroCoord[0])
		zeroJ = copy.copy(zeroCoord[1])

		if a_action == 'U':
			newI = zeroI-1
			newJ = zeroJ

		if a_action == 'D':
			newI = zeroI+1
			newJ = zeroJ

		if a_action == 'L':
			newI = zeroI
			newJ = zeroJ-1

		if a_action == 'R':
			newI = zeroI
			newJ = zeroJ+1
		tmp = newState[newI][newJ]
		newState[zeroI][zeroJ]=	tmp
		newState[newI][newJ]=int(0)
		return newState
	def getNewNodes(self, a_node):
		newNodes = []
		legalMoves = a_node.getAllMoves()
		
		for move in legalMoves:
			print 'new move:' + move
			newNodes.append(PuzzleNode(self.getResult(a_node, move), copy.deepcopy(a_node), copy.copy(move), self.columns, self.rows))
		print 'newNodes from allLegalMoves:'
		for node in newNodes:
			print node.state
		return newNodes

	def printPathToNode(self, a_node):
		tmpNode = a_node
		while not tmpNode == None:
			print tmpNode.action
			tmpNode=tmpNode.parent
	def haveVisited(self, a_visited, a_state):
		for visit in a_visited:
			for i in range(len(a_state)):
				for j in range (len(a_state[i])):
					if not visit.state[i][j]==a_state[i][j]:
						return False
		return True		
	def BFS(self, a_node):
		queue = Queue.Queue()
		queue.put(copy.deepcopy(a_node))

		visited = []
		visited.append(a_node)
		print 'starting the while loop'
		while not queue.empty():
			print 'in the while loop'
			tmpNode = queue.get()
			if (self.goalTest(tmpNode.state)):
				print 'PATH FOUND'
				self.printPathToNode(tmpNode)	
				return True
			for newNode in self.getNewNodes(tmpNode):
				#need to write method in Problem that will create instances
				# of PuzzleNode for all legal moves given tmpNode
				print 'in the for get new nodes loop'
				if not self.haveVisited(visited, newNode.state):
					print 'adding a node to the queue'
					visited.append(newNode)
					queue.put(copy.deepcopy(newNode))			 					

columns = 3
rows = 3
file = open('testData.dat')
i=0
word_list=[]
puzzle = []
for line in open('testData.dat'):
	for word in line.split():
		word_list.insert(i, word)
		i=i+1

algo_code = word_list[0]
heuristic_code = word_list[1]
output_code = word_list[2]

for i in xrange (3, rows*columns+3, columns):
	inner_list = []
	for x  in xrange(i,i+columns):
		inner_list.append(int(word_list[x]))

	puzzle.append(inner_list)
print word_list
print 'algo_code:' + algo_code
print 'heuristic_code:' + heuristic_code
print 'output_code' + output_code
print puzzle

myPuzzle = Problem(rows, columns, puzzle)
newNode = PuzzleNode(puzzle, None, None, columns, rows)
print 'puzzleNode state:'
print newNode.state
#myNewMoves=[]
#myNewMoves = newNode.getAllMoves()
#print myNewMoves
#print newNode.zeroPos()
#newNode.printState()

#secondNode = PuzzleNode(myPuzzle.getResult(newNode, 'R'), newNode, 'R', columns, rows)
#secondNode.printState()
#print secondNode.getAllMoves()
myPuzzle.BFS(newNode)
