from owlready2 import *

def LoadOntologyForMe ():
    #onto_path.append("C:/Users/Recep/Desktop")   /for local copy
    onto = get_ontology("http://web.itu.edu.tr/altinbagr/ontology/ProjectOwl_v4.owl")   #online updated version
    onto.load()
    return onto

def GetPollutantTypes(onto):
    PollutantTypeFinder = list(onto.search(type=onto.PollutantType))
    return PollutantTypeFinder

def GetPollutantDomains(onto):
    PollutantDomainFinder = list(onto.search(type = onto.PollutantDomain))
    return PollutantDomainFinder

def GetPollutantEffects(onto):
    PollutantEffectFinder = list(onto.search(type = onto.PollutantEffect))
    return PollutantEffectFinder

def GetConventionalPollutants(onto):
    PollutantConventionalFinder = list(onto.search(type = onto.Conventional))
    return PollutantConventionalFinder

def GetMicroPollutants(onto):
    PollutantMicroFinder = list(onto.search(type = onto.Micro))
    return PollutantMicroFinder

def GetMetalPollutants(onto):
    PollutantMetalFinder = list(onto.search(type = onto.Metal))
    return PollutantMetalFinder

def GetPollutantEffect(onto,PickedPollutant):
    EffectsOfPickedPollutant = list(PickedPollutant.hasEffect)
    return EffectsOfPickedPollutant

def GetPollutantDomain(onto,PickedPollutant):
    DomainsOfPickedPollutant = list(PickedPollutant.hasDomain)
    return DomainsOfPickedPollutant

def GetPollutantType(onto,PickedPollutant):
    TypesOfPollutant = list(PickedPollutant.hasType)
    return TypesOfPollutant

def SearchingPollutants(onto,PickedType,PickedDomain,PickedEffect):
    Result  = []
    Pollutants = GetMicroPollutants(onto) + GetMetalPollutants(onto)
    for item in Pollutants:
        TypesOfPollutants = GetPollutantType(onto,item)
        DomainsOfPollutants = GetPollutantDomain(onto,item)
        EffectsOfPollutants = GetPollutantEffect(onto,item)
        ControlValueForComparison=0
        if PickedType != None:
            for existence in TypesOfPollutants:
                if existence == PickedType:
                    ControlValueForComparison = ControlValueForComparison + 1
        if PickedDomain != None:
            for existence in DomainsOfPollutants:
                if existence == PickedDomain:
                    ControlValueForComparison = ControlValueForComparison + 1
        if PickedEffect != None:
            for existence in EffectsOfPollutants:
                if existence == PickedEffect:
                    ControlValueForComparison = ControlValueForComparison + 1
        if PickedType == None: ControlValueForComparison = ControlValueForComparison + 1
        if PickedDomain == None: ControlValueForComparison = ControlValueForComparison + 1
        if PickedEffect == None: ControlValueForComparison = ControlValueForComparison + 1

        if ControlValueForComparison==3:
            TemporaryItem=str(item).split(".")
            Result.append(TemporaryItem[1])

    return Result

def PrintingNicely(Item):
    Result=[]
    for item in Item:
        TemporaryItem=item.label
        Result.append(TemporaryItem)
    return Result

def GetMyWantedPollutantOnly(PickedType=None,PickedDomain=None,PickedEffect=None):
    onto = LoadOntologyForMe()

    PickedOntologyType = onto.Acaricide
    PickedOntologyEffect = onto.Toxic
    PickedOntologyDomain = onto.Agricultural

    PollutantTypeFinder = GetPollutantTypes(onto)
    PollutantDomainFinder = GetPollutantDomains(onto)
    PollutantEffectFinder = GetPollutantEffects(onto)
    if PickedType != None:
        for item in PollutantTypeFinder:
            if str(label[item]) == "['" + PickedType + "']":
                PickedOntologyType = item
    else:
        PickedOntologyType = None
    if PickedEffect != None:
        for item in PollutantEffectFinder:
            if str(label[item]) == "['" + PickedEffect + "']":
                PickedOntologyEffect = item
    else:
        PickedOntologyEffect = None
    if PickedDomain!=None:
        for item in PollutantDomainFinder:
            if str(label[item]) == "['" + PickedDomain + "']":
                PickedOntologyDomain = item
    else:
        PickedOntologyDomain = None
    FinalPollutants = SearchingPollutants(onto, PickedOntologyType, PickedOntologyDomain,PickedOntologyEffect)
    return FinalPollutants



#Main Function
                            #To see Types,Domains,Effects   Use GetPollutantTypes,GetPollutantDomains,
                            # GetPollutantEffects Functions
#PickedType='Metal Products'     #One of or two of them can be None, If everyone is none, returns all Pollutans
#PickedDomain=None
#PickedEffect='Toxic'

#FinalPollutants = GetMyWantedPollutantOnly(PickedType,PickedDomain,PickedEffect)


