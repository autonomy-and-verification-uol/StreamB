grammar Stream;

propertyExpr : ty=tyExpr child=namedExpr;

tyExpr : (tname=IDENTIFIER (':') t=types ';')*;

namedExpr : (name=IDENTIFIER ('=') child=expr ';')+;

expr : child=mtlExpr                                                   # AtomicExpression
     | left=expr ('and') right=expr                              	     # And
     | left=expr ('or') right=expr                                     # Or
     ;

mtlExpr : child=evalExpr                                               # Evaluation
     | ('!' | 'not') child=mtlExpr                                     # Negation
     | left=mtlExpr ('&&') right=mtlExpr                               # Conjunction
     | left=mtlExpr ('||') right=mtlExpr                               # Disjunction
     | left=mtlExpr ('->' | 'implies') right=mtlExpr                      # Implies

     | 'pre' child=mtlExpr                                             # Previously

     | 'once' child=mtlExpr                                            # Once
     | 'once' '[' l=NUMBER ',' u=NUMBER ']' child=mtlExpr              # TimedOnce
     | 'once' '[' l=NUMBER ',' 'inf' ']' child=mtlExpr                 # TimedOnceInf

     | 'always' child=mtlExpr                                          # Always
     | 'always' '[' l=NUMBER ',' u=NUMBER ']' child=mtlExpr            # TimedAlways
     | 'always' '[' l=NUMBER ',' 'inf' ']' child=mtlExpr               # TimedAlwaysInf

     | left=mtlExpr 'since' right=mtlExpr                                 # Since
     | left=mtlExpr 'since' '[' l=NUMBER ',' u=NUMBER ']' right=mtlExpr   # TimedSince
     | left=mtlExpr 'since' '[' l=NUMBER ',' 'inf' ']' right=mtlExpr      # TimedSinceInf
     ;

evalExpr : child=aggregationExpr                                       # Aggregation
     | left=aggregationExpr ('<') right=aggregationExpr                # Less
     | left=aggregationExpr ('<=') right=aggregationExpr               # LessEq
     | left=aggregationExpr ('>') right=aggregationExpr                # Greater
     | left=aggregationExpr ('>=') right=aggregationExpr               # GreaterEq
     | left=aggregationExpr ('==') right=aggregationExpr               # Eq
     | left=aggregationExpr ('!=') right=aggregationExpr               # Neq
     ;
aggregationExpr : child=atom                                           # Atomic
     | child=NUMBER                                                    # Int
     | child=REAL                                                      # Real
     | ('min') child=aggregationExpr                                   # Min
     | ('min') '[' l=NUMBER ']' child=aggregationExpr                  # TimedMin
     | ('max') child=aggregationExpr                                   # Max
     | ('max') '[' l=NUMBER ']' child=aggregationExpr                  # TimedMax
     | ('avg') child=aggregationExpr                                   # Avg
     | ('avg') '[' l=NUMBER ']' child=aggregationExpr                  # TimedAvg
     | '(' child=expr ')'                                              # Grouping
    ;

atom : name=IDENTIFIER                         # Prop
	| name=IDENTIFIER '(' args=idlist ')'     # Pred
	;

idlist : param=IDENTIFIER (',' param=IDENTIFIER)*;

IDENTIFIER : [_a-zA-Z][_a-zA-Z0-9]*;

types : v='int' | v='real' | v='bool';

NUMBER: DIGIT | (DIGIT_NOT_ZERO DIGIT+);

REAL: NUMBER '.' (DIGIT+);

WS         : [ \r\n\t]+ -> channel (HIDDEN);

fragment DIGIT: ('0'..'9');
fragment DIGIT_NOT_ZERO: ('1'..'9');
