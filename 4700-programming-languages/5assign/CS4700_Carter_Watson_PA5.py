# -*- coding: utf-8 -*-
"""Delta User Functions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15L0oeLNu2vJbXoAPc5ZG3aWJfZyEjz_X

Delta Language Inperpreter
"""

def run(program, debug = True):
  # input string, multiple expressions.
  # tokenize and parse all, then evaluate each Delta program 
  global UserFunctions, Debug
  Debug = debug
  UserFunctions = {}
  tokens = tokenize(program)
  codeList = []
  while tokens != []:
    codeList.append(parse(tokens))
  #print(codeList)
  for code in codeList:
    evalDeltaShow(code)

def tokenize(string):
  #inputs a string containing a Delta expression
  #returns a list of atoms of the language
  tokenList = string.replace('(', ' ( ').replace(')', ' )').replace('::=', ' ').replace('[', ' ( ').replace(']', ' ) ').split()
  return tokenList
  
def parse(tokenList):
  #inputs a list of tokens
  #returns a parse tree, represented as a nested list structure
  token = tokenList.pop(0)
  if token[0].isdigit(): #terminal
    return int(token)
  if token[0] != '(': #terminal
    return token
  #  <exp> can be (<operator> <exp>) or (<operator> <exp> <exp>) or (<operator> followed by any number of expressions
  ans = [tokenList.pop(0)]
  while tokenList[0] != ')':
    ans.append(parse(tokenList)) 
  tokenList.pop(0) # to get rid of the ')'
  return ans

def evalDeltaShow(exp, stackFrames = [], depth = 0):
  if Debug:
    print("   |"*depth + "-> " + str(exp))
  result = evalDelta(exp, stackFrames, depth + 1)
  if Debug:
    print("   |"*depth + "-< " + str(result))
  return result

def evalDelta(exp, stackFrames = [], depth = 0):
  # input a parsed expression, list of stack frames
  if not isinstance(exp, list) or exp == "nil":
    return evalDeltaAtom(exp, stackFrames, depth)
  if exp[0] == 'fun': # user defined function, remember (formal parameters, body)
     UserFunctions[exp[1]] = exp[2:]
     return None
  if exp[0] == '❗':
    return not evalDeltaShow(exp[1], stackFrames, depth)
  if exp[0] == '|':
    return evalDeltaShow(exp[1], stackFrames, depth) or evalDeltaShow(exp[2], stackFrames, depth)
  if exp[0] == '&':
    return evalDeltaShow(exp[1], stackFrames, depth) and evalDeltaShow(exp[2], stackFrames, depth)
  if exp[0] == '+':
    return evalDeltaShow(exp[1], stackFrames, depth) + evalDeltaShow(exp[2], stackFrames, depth)
  if exp[0] == '-':
    return evalDeltaShow(exp[1], stackFrames, depth) - evalDeltaShow(exp[2], stackFrames, depth)
  if exp[0] == '/':
    return evalDeltaShow(exp[1], stackFrames, depth) // evalDeltaShow(exp[2], stackFrames, depth)
  if exp[0] == '*':
    return evalDeltaShow(exp[1], stackFrames, depth) * evalDeltaShow(exp[2], stackFrames, depth)
  if exp[0] == '==':
    return evalDeltaShow(exp[1], stackFrames, depth) == evalDeltaShow(exp[2], stackFrames, depth)
  if exp[0] == '<':
    return evalDeltaShow(exp[1], stackFrames, depth) < evalDeltaShow(exp[2], stackFrames, depth)
  # builtins
  if exp[0] == "quote":
    return exp[1]
  if exp[0] == "eval":
    return evalDeltaShow(exp[1], stackFrames, depth)
  if exp[0] == "atom":
    return evalDeltaAtom(exp[1], stackFrames, depth) != None
  if exp[0] == "first":
    return evalDeltaShow(exp[1], stackFrames, depth)[0]
  if exp[0] == "rest":
    return evalDeltaShow(exp[1], stackFrames, depth)[1:]
  if exp[0] == "comp":
    return [evalDeltaShow(exp[1], stackFrames, depth)] + evalDeltaShow(exp[2], stackFrames, depth)
  if exp[0] == 'if':
    if evalDeltaShow(exp[1], stackFrames, depth): 
       return evalDeltaShow(exp[2], stackFrames, depth)
    return evalDeltaShow(exp[3], stackFrames, depth) 
  #must be a user defined function
  return evalDeltaUserCall(exp, stackFrames, depth)

def evalDeltaAtom(exp, stackFrames, depth):
  # exp is an atom in Delta
  if isinstance(exp, int):
    return exp
  if exp == '👍':
    return True
  if exp == '👎':
    return False
  if exp == "nil":
    return []
  #user defined variable, look up its value 
  for frame in stackFrames:
    if exp in frame:
      return frame[exp]
  if exp in ['+', '-', '/', '*', '|', '&', '==', '<', '❗']:
    return exp
  return None

def evalDeltaUserCall(exp, stackFrames, depth):
  #must be a user defined function
  (formalParameters, functionBody) = UserFunctions[exp[0]]
  variableValues = {} # use a dictionary to map formal parameters to actual parameters (values)
  for (parameter, actual) in zip(formalParameters, exp[1:]):
    variableValues[parameter] = evalDeltaShow(actual, stackFrames, depth)
  return evalDeltaShow(functionBody, [variableValues] + stackFrames, depth)

# ----- builtin functions -----
code = ""
# # --- provided functions
# code += "(fun fact (x) (if (== x 0) 1 (* x (fact (- x 1)))))"
# code += "(fun fib (x) (if (| (== x 0) (== x 1)) 1 (+ (fib (- x 1)) (fib (- x 2)))))"
# # --- assigned functions - assign4
# code += '''(fun createList (start increment howMany)
#               (if (❗(== howMany 1))
#                 (comp start (createList (+ start increment) increment (- howMany 1)))
#                 (comp start nil)
#               )
#             )'''
# code += '''(fun nth (index list)
#               (if (❗(== index 0))
#                 (nth (- index 1) (rest list))
#                 (first list)
#               )
#             )'''
code += '''(fun append (list0 list1)
              (if (❗(== list0 nil))
                (if (❗(== list1 nil))
                  (comp (first list0) (append (rest list0) list1))
                  list0 
                )
                list1 
              )
            )'''
# --- assigned functions - assign5
code +=  '''(fun front (int, list)
              if (❗(== list nil))
                (if (❗(== int 0))
                  (append (first list) (front (- int 1) (rest list)))
                ) 
                (quote list)
              )
              (quote list)
            )'''

# ----- test cases -----
# --- provided test code for comp, rest, first, and nil
# code = "(comp 1 nil) (first (comp (+ 3 4) nil)) (rest (comp 1 (comp 2 nil)))"
# --- test cases for builtin functions
# # createList
# code += "(createList 20 10 4)"
# code += "(createList 100 5 10)"
# # nth index 
# code += "(nth 0 (comp 100 nil))"
# code += "(nth 7 (createList 100 100 10))"
# # append
# code += "(append nil nil)"
# code += "(append (comp 6 nil) nil)"
# code += "(append nil (comp 7 nil))"
# code += "(append (comp 1 nil) (createList 100 200 3))"
# code += "(append (createList 1 2 3) (createList 20 30 3))"
# code += "(nth 4 (append (createList 1 2 3) (createList 20 30 3)))"
# atom
code += "(atom 5) (atom nil) (atom (+ 5 6)) (atom +)"
# quote
code += "(quote 5) (quote nil) (quote (+ 5 6)) (quote (0 1 2 3))"
# eval
code += "(eval 5) (eval (quote (comp 5 nil)))"
# front
code += "(front 0 (nil)) (front 0 (quote (0 1 2 3 4))) (front 2 (quote (0 1 2 3 4)))"


run(code)
