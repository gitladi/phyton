# Tip Calculator

## კითხვები
1. ჩეკის ოდენობა / bill amount
2. თიფის % / tip rate
3. სრული ოდენობა / total
4. რა უნდა ვკითხოთ იუზერს / Prompt
5. რა უნდა გამოჩნდეს პროგრამის ჩართვისას? / Display
6. რა უნდა გამოიტანოს პროგრამამ პასუხად / Output / Displa

## ტექნიკური დავალება
შექმენი მარტივი თიფ კალკულატორი, პროგრამამ უნდა კითხოს ჩეკის რაოდენობისა და პროცენტის შესახებ, პროგრამამ უნდა დათვალოს თიფი და უნდა გამოაჩინოს მისი სრული ოდენობა


### TDD - Tests Driven Development - Tests
ტესტის გეგმა #1
inputs :
- bill amount: 10
- tip rate: 15
Expected result:
- Tip: 1.50
- Total: 11.50


## ფსევდოკოდი - Pseudocode
TipCalculator
    Inicialize Billamoult 0 
    Inicialize tip to 0
    Inicialize tipRate to 0
    Inicialize total to 0

    Prompt for billamount eitg " what is rge bull amount
    Prompt dor tipRate with :what is the tip rate?"
    convert bill
