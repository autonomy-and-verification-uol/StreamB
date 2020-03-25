# Generated from Stream.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .StreamParser import StreamParser
else:
    from StreamParser import StreamParser

# This class defines a complete generic visitor for a parse tree produced by StreamParser.

class StreamVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by StreamParser#propertyExpr.
    def visitPropertyExpr(self, ctx:StreamParser.PropertyExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#tyExpr.
    def visitTyExpr(self, ctx:StreamParser.TyExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#namedExpr.
    def visitNamedExpr(self, ctx:StreamParser.NamedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#AtomicExpression.
    def visitAtomicExpression(self, ctx:StreamParser.AtomicExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#And.
    def visitAnd(self, ctx:StreamParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Or.
    def visitOr(self, ctx:StreamParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#TimedAlwaysInf.
    def visitTimedAlwaysInf(self, ctx:StreamParser.TimedAlwaysInfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Evaluation.
    def visitEvaluation(self, ctx:StreamParser.EvaluationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#TimedAlways.
    def visitTimedAlways(self, ctx:StreamParser.TimedAlwaysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Negation.
    def visitNegation(self, ctx:StreamParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Once.
    def visitOnce(self, ctx:StreamParser.OnceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#TimedSince.
    def visitTimedSince(self, ctx:StreamParser.TimedSinceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Previously.
    def visitPreviously(self, ctx:StreamParser.PreviouslyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#TimedSinceInf.
    def visitTimedSinceInf(self, ctx:StreamParser.TimedSinceInfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#TimedOnce.
    def visitTimedOnce(self, ctx:StreamParser.TimedOnceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Disjunction.
    def visitDisjunction(self, ctx:StreamParser.DisjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Implies.
    def visitImplies(self, ctx:StreamParser.ImpliesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Conjunction.
    def visitConjunction(self, ctx:StreamParser.ConjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Grouping1.
    def visitGrouping1(self, ctx:StreamParser.Grouping1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Since.
    def visitSince(self, ctx:StreamParser.SinceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Always.
    def visitAlways(self, ctx:StreamParser.AlwaysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#TimedOnceInf.
    def visitTimedOnceInf(self, ctx:StreamParser.TimedOnceInfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Atomic1.
    def visitAtomic1(self, ctx:StreamParser.Atomic1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Less.
    def visitLess(self, ctx:StreamParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#LessEq.
    def visitLessEq(self, ctx:StreamParser.LessEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Greater.
    def visitGreater(self, ctx:StreamParser.GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#GreaterEq.
    def visitGreaterEq(self, ctx:StreamParser.GreaterEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Eq.
    def visitEq(self, ctx:StreamParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Neq.
    def visitNeq(self, ctx:StreamParser.NeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Grouping2.
    def visitGrouping2(self, ctx:StreamParser.Grouping2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Atomic2.
    def visitAtomic2(self, ctx:StreamParser.Atomic2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Int.
    def visitInt(self, ctx:StreamParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Real.
    def visitReal(self, ctx:StreamParser.RealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Min.
    def visitMin(self, ctx:StreamParser.MinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#TimedMin.
    def visitTimedMin(self, ctx:StreamParser.TimedMinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Max.
    def visitMax(self, ctx:StreamParser.MaxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#TimedMax.
    def visitTimedMax(self, ctx:StreamParser.TimedMaxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Avg.
    def visitAvg(self, ctx:StreamParser.AvgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#TimedAvg.
    def visitTimedAvg(self, ctx:StreamParser.TimedAvgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Grouping3.
    def visitGrouping3(self, ctx:StreamParser.Grouping3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Prop.
    def visitProp(self, ctx:StreamParser.PropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#Pred.
    def visitPred(self, ctx:StreamParser.PredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#idlist.
    def visitIdlist(self, ctx:StreamParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StreamParser#types.
    def visitTypes(self, ctx:StreamParser.TypesContext):
        return self.visitChildren(ctx)



del StreamParser