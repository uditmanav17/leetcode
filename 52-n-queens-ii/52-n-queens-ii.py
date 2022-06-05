class Solution:
    def totalNQueens(self, n: int) -> int:
        blockedCols = set()
        blockedUpDiagonals = set()
        blockedDownDiagonals = set()
        return self.getNumberOfNonAttackingPositions(0, blockedCols, blockedUpDiagonals, 
                                                     blockedDownDiagonals, n)


    def isNonAttackingPosition(self, row, col, blockedCols, 
                               blockedUpDiagonals, blockedDownDiagonals):
        if (
            col in blockedCols
            or row + col in blockedUpDiagonals
            or row - col in blockedDownDiagonals
        ):
            return False
        return True


    def placeQueen(self, row, col, blockedCols, blockedUpDiagonals, blockedDownDiagonals):
        blockedCols.add(col)
        blockedUpDiagonals.add(row + col)
        blockedDownDiagonals.add(row - col)


    def removeQueen(self, row, col, blockedCols, blockedUpDiagonals, blockedDownDiagonals):
        blockedCols.remove(col)
        blockedUpDiagonals.remove(row + col)
        blockedDownDiagonals.remove(row - col)


    def getNumberOfNonAttackingPositions(self, row, blockedCols, blockedUpDiagonals, 
                                         blockedDownDiagonals, boardSize):
        if row == boardSize:
            return 1

        validPlacements = 0
        for col in range(boardSize):
            if self.isNonAttackingPosition(row, col, blockedCols, 
                                           blockedUpDiagonals, blockedDownDiagonals):
                self.placeQueen(row, col, blockedCols, 
                                blockedUpDiagonals, blockedDownDiagonals)
                validPlacements += self.getNumberOfNonAttackingPositions(
                    row + 1,
                    blockedCols,
                    blockedUpDiagonals,
                    blockedDownDiagonals,
                    boardSize,
                )
                self.removeQueen(row, col, blockedCols, 
                                 blockedUpDiagonals, blockedDownDiagonals)
        return validPlacements


