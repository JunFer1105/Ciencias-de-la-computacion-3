# Ejemplos de lexer y parser usando ply

G =< {E,T, F}, {+, ∗, num,(,)}, P, E >
E → E + T
E → T
T → T ∗ F
T → F
F → num
F → (E)
#Integrantes Juan Fernando Arango 20141020068
             Joan Sebastian Diaz  20141020103
