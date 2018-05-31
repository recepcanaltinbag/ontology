from ontotrial import *

#Some Useful Functions
#All of them returns Lists

WishedPollutants = GetMyWantedPollutantOnly('Pesticides','Agricultural','Toxic')  # Send(Types,Domains,Effects) returns
print(WishedPollutants)                                                     #Pollutants (Micro+Metal)

Types = GetPollutantTypes(LoadOntologyForMe())                              # To see Types
print(PrintingNicely(Types))

Domains = GetPollutantDomains(LoadOntologyForMe())                           #To see Domains
print(PrintingNicely(Domains))

Effects = GetPollutantEffects(LoadOntologyForMe())                           #To see Effects
print(PrintingNicely(Effects))

MicroPollutants = GetMicroPollutants(LoadOntologyForMe())                    #To see MicroPollutants
print(PrintingNicely(MicroPollutants))

MetalPollutants = GetMetalPollutants(LoadOntologyForMe())                    #To see MicroPollutants
print(PrintingNicely(MetalPollutants))

ConvPollutants = GetConventionalPollutants(LoadOntologyForMe())               #To see ConvetionalPollutants
print(PrintingNicely(ConvPollutants))