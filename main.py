

dnainp = input("Please enter your DNA sequence")
dna = dnainp.upper()
#print(dna[0:3]) #print first part of the dna string
#dna1 = (str(dna[0:3])) #create string for first part of the dna string
#print(dna[4:7]) #part 2
#dna2 = (dna[4:7]) #create string for second part of the dna string
#print(dna[8:11])
#dna3 = (dna[8:11]) #create string for third part of the dna string
#print(dna[12:15])
#dna4 = (dna[12:15]) #create string for fourth part of the dna string


##mRNA Transcription
#mrnadict = {"A": "U", "T": "A", "C": "G", "G": "C"}
mrnadict = {65: 85, 84: 65, 67: 71, 71: 67}
mrna = dna.translate(mrnadict)
#print('mRNA:', dna.translate(mrnadict))
mn = 3
mrnaall = [mrna[i:i+mn] for i in range(0, len(mrna), mn)]
#print(mrnaall)

##change list to string
mrnaallstr = ' '.join(mrnaall)
print('mRNA:', mrnaallstr)
##mrna Translation to amino acids

#trnadict = {"UAG": "STOP", "AUG": "Start", "UAA": "Stop", "UGA": "Stop", "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu", "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser", "UAU": "Tyr", "UAC": "Tyr", "UGU": "Cys", "UGC": "Cys", "UGG": "Trp", "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu", "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro", "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln", "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg", "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr", "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys", "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg", "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val", "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala", "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu", "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"}

trnadict = {"UAG": "STOP",
 "AUG": "START", 
 "UAA": "STOP", 
 "UGA": "STOP", 
 "UUU": "Phe", 
 "UUC": "Phe", 
 "UUA": "Leu", 
 "UUG": "Leu", 
 "UCU": "Ser", 
 "UCC": "Ser", 
 "UCA": "Ser", 
 "UCG": "Ser", 
 "UAU": "Tyr", 
 "UAC": "Tyr", 
 "UGU": "Cys", 
 "UGC": "Cys", 
 "UGG": "Trp", 
 "CUU": "Leu", 
 "CUC": "Leu", 
 "CUA": "Leu", 
 "CUG": "Leu", 
 "CCU": "Pro", 
 "CCC": "Pro", 
 "CCA": "Pro", 
 "CCG": "Pro", 
 "CAU": "His", 
 "CAC": "His", 
 "CAA": "Gln", 
 "CAG": "Gln", 
 "CGU": "Arg", 
 "CGC": "Arg", 
 "CGA": "Arg", 
 "CGG": "Arg", 
 "AUU": "Ile", 
 "AUC": "Ile", 
 "AUA": "Ile", 
 "ACU": "Thr", 
 "ACC": "Thr", 
 "ACA": "Thr", 
 "ACG": "Thr", 
 "AAU": "Asn", 
 "AAC": "Asn", 
 "AAA": "Lys", 
 "AAG": "Lys", 
 "AGU": "Ser", 
 "AGC": "Ser", 
 "AGA": "Arg", 
 "AGG": "Arg", 
 "GUU": "Val", 
 "GUC": "Val", 
 "GUA": "Val", 
 "GUG": "Val", 
 "GCU": "Ala", 
 "GCC": "Ala", 
 "GCA": "Ala", 
 "GCG": "Ala", 
 "GAU": "Asp", 
 "GAC": "Asp",
 "GAA": "Glu", 
 "GAG": "Glu", 
 "GGU": "Gly", 
 "GGC": "Gly", 
 "GGA": "Gly", 
 "GGG": "Gly"}


#trna = mrnaallstr.translate(trnadict)
trna = (" ".join([trnadict[w] for w in mrnaallstr.split()]))
print('Amino Acids:', trna)