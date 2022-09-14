or a more uniform representation, facts can be represented as rules with condition true. Also, to distinguish different knowledge bases, rules can be labeled with a knowledge base identifier.

:- op(1100, xfx, if).
:- op(1000, xfy, and). % <== EDITED

forward(KB, Fact) :-
    fixpoint(KB, nil, [true], Facts),
    member(Fact, Facts).

fixpoint(_, Base, Base, Base) :- !.
fixpoint(KB, _, Base, Facts) :-
    setof(Fact, derived(Fact, KB, Base), NewFacts),
    ord_union(NewFacts, Base, NewBase),
    fixpoint(KB, Base, NewBase, Facts).

derived(Fact, KB, Base) :-
    rule(KB : Fact if Condition),
    satisfy(Base, Condition).

satisfy(Base, Condition) :-
    (   Condition = (A and B)
    ->  member(A, Base),
        satisfy(Base, B)
    ;   member(Condition, Base) ).


% first knowledge base

rule(1 : eats_flies(fritz) if true).
rule(1 : croaks(fritz)     if true).
rule(1 : sings(tweety)     if true).
rule(1 : chips(tweety)     if true).
rule(1 : has_wings(tweety) if true). % <== EDITED
rule(1 : croaks(kroger)    if true).
rule(1 : chips(kroger)     if true).
rule(1 : frog(X)           if croaks(X) and eats_flies(X)).
rule(1 : green(X)          if frog(X)).
rule(1 : yellow(X)         if canary(X)).
rule(1 : canary(X)         if sings(X) and chips(X) and has_wings(X)). % <== EDITED

% second knowledge base (recursive example)

rule(2 : connected(a,b) if true).
rule(2 : connected(b,c) if true).
rule(2 : connected(c,d) if true).
rule(2 : connected(X,Z) if connected(X,Y) and connected(Y,Z)).
