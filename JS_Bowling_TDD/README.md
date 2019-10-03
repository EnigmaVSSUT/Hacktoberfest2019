# js-bowling-TDD-demo
A demo to showcase how to do TDD in a javascript project
## Installation
1. `Yarn install`
2. `Yarn Test` to run tests
## Lifecycle of this project


### Start
1. Start: Testing suite test
### First Test
1. Red 1 - Minimum Failing Test: File does not exist
2. Green 1 - Test fail? Game still undefined? 
   - Open up new file in IDE
   - \f -> s on file -> CTRL + W + (SHIFT L)
3. Green 2 -  Tests pass! We required the file. But hey... It does not do much.
4. Red 2 - Error - Not a function: roll
5. Green 2 - Test passes! roll exists but has no implementation, but does not produce an error
6. Red 3 - Score should be 0 - Undefined not 0... Perhaps not implemented
7. Green 3 - Test Fail? Expected function:score to be 0.. Ohh I must have forgot to put ()
8. Green 4 - Test Fail? Expected 1 to be 0. Changed test to call score()
9. Green 5 - Tests pass! Gutter game returns 0
### Second Test
1. Red 1 - An all ones game should have a score of 20.  Current implementation does not give anything other than 0
2. Green 1 - Tests Pass! Bad variable naming, but tests pass
3. Refactor 1 - First Refactor! Remove Duplication of new game
4. Refactor 2 - Remove magic numbers
5. Refactor 3 - Arrow Functions + rollMany function to remove duplication
6. Refactor 4 - Magic numbers again, but it simplifies code
7. Refactor 5 - Remove duplication of loop. All functions now use rollMany TODO
### Third Test
1. Red 1 - New behaviour! An game with a spare should have an increased multiplier
2. TODO Green 1 - Tests Pass! Only passing because I have commented. Not ready for this new feature.
3. Refactor 1 - Function with better names that do when they say they do + flexibility 
4. Refactor 2 - Use frames rather than 20 rolls. Closer to context, allows for different size frame
5. TODO Red 2 - Removal of comments. Now ready to test 
6. Green 2 - Tests Pass! Calculates a spare in a frame. Spares are calculated correctly.
7. Refactor 3 - Frame index is a better name than i.
8. Refactor 4 - Use of boolean isSpare() rather than in conditional
9. Refactor 5 - rollSpare() in Test so that rolling a spare is better understood.
### Fourth Test
1. Red 1 - New behaviour! Strikes should have an increased multiplier
2. Green 1 - Tests pass! Strikes are calculated correctly
3. TODO Refactor 1 - strikeBonus() function. Better readability.
4. Refactor 2 - spareBonus(). Better readability.
5. Refactor 3 - standard calculation for a frame in a sumInFrame(). Score is getting much better
6. Refactor 4 - isStrike() to used rather than in-conditional logic.
7. Refactor 5 - rollStrike() in Test so that rolling a strike is better understood.
### Fifth Test
1. Red & Green - New behaviour! A perfect game with all strikes has a score of 300.
* Behaviour works already because of how we tackled the other problems intelligently
