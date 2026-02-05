class UndoRedo:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def do(self, action):
        self.undo_stack.append(action)

    def undo(self):
        if self.undo_stack:
            action = self.undo_stack.pop()
            self.redo_stack.append(action)
            return f"Undo: {action}"
        else:
            return "Nothing to undo"

    def redo(self):
        if self.redo_stack:
            action = self.redo_stack.pop()
            self.undo_stack.append(action)
            return f"Redo: {action}"
        else:
            return "Nothing to redo"


undoredo = UndoRedo()
undoredo.do("Apple")
undoredo.do("Mango")

print(undoredo.undo())
print("Undo stack contents=", undoredo.undo_stack)
print("Redo stack contents=", undoredo.redo_stack)

print(undoredo.undo())
print("Undo stack contents=", undoredo.undo_stack)
print("Redo stack contents=", undoredo.redo_stack)

print(undoredo.undo())
print("Undo stack contents=", undoredo.undo_stack)
print("Redo stack contents=", undoredo.redo_stack)

print(undoredo.redo())
print("Undo stack contents=", undoredo.undo_stack)
print("Redo stack contents=", undoredo.redo_stack)

print(undoredo.redo())
print("Undo stack contents=", undoredo.undo_stack)
print("Redo stack contents=", undoredo.redo_stack)

print(undoredo.redo())
print("Undo stack contents=", undoredo.undo_stack)
print("Redo stack contents=", undoredo.redo_stack)
