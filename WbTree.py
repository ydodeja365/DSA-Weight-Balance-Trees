def checkRotation(t):
	wbal=weight(t.left)/t.weight
	if wbal>0.707011:
		if (weight(t.left.left)/weight(t.left))>0.414213:
			t=rightRotate(t)
		else:
			t.left=leftRotate(t.left)
			t=rightRotate(t)
	elif wbal<0.292893:
		if(weight(t.right.left)/weight(t.right))<0.585786:
			t=leftRotate(t)
		else:
			t.right=rightRotate(t.right)
			t=leftRotate(t)
	return t

def rightRotate(t):
	temp=t
	t=t.left
	temp.left=t.right
	t.right=temp
	t.weight=temp.weight
	temp.weight=weight(temp.left)+weight(temp.right)
	return t

def leftRotate(t):
	temp=t
	t=t.right
	temp.right=t.left
	t.left=temp
	t.weight=temp.weight
	temp.weight=weight(temp.left)+weight(temp.right)
	return t

def weight(t):
	if t is None:
		return 0
	return weight(t.left)+weight(t.right)

class TreeNode:
	def __init__(self,k,l=None,r=None):
		self.weight=None
		self.left=l
		self.right=r
		self.key=k

class WBTree:
	def __init__(self):
		self.root=None

	def insert(self,x,r="Default"):
		if r=="Default":
			r=self.root
		if r is None:
			self.root=TreeNode(x)
			self.root.weight=2
		elif r.key==x:
			print("Already exists!")
		else:
			if r.key<x:
				r.right=self.insert(x,r.right)
			else:
				r.left=self.insert(x,r.left)
				t.weight=weight(t.left)+weight(t.right)
				r=checkRotation(r)
		return r

	def delete(self,x,t="Default"):
		if t=="Default":
			t=self.root
		if t is None:
			print("Key not found!")
		else:
			if t.key<x:
				t.right=self.delete(x,t.right)
			elif t.key>x:
				t.left=self.delete(x,t.left)
			elif t.left is None:
				t=t.right
			elif t.right is None:
				t=t.left
			elif(weight(t.left)>weight(t.right)):
				t=rightRotate(t)
				t.right=self.delete(x,t.right)
			else:
				t=leftRotate(t)
				t.left=self.delete(x,t.left)
			if t is not None:
				t.weight=weight(t.left)+weight(t.right)
				t=checkRotation(t)
			return t