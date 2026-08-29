genome = str(input("Enter a genome: "))

index = 0
active = False

while index < len(genome) - 2:
    codon = genome[index: index + 3]
    gene = ""
    
    if codon == "ATG" and index < len(genome) - 6:
        active = True
        index += 3
        codon = genome[index: index + 3]
        print(codon)
        if index < len(genome) - 3:
            index += 3
            while active:
                codon = genome[index: index + 3]
                if codon != "ATG" and codon != "TAG" and codon != "TAA" and codon != "TGA":
                    print(codon)
                active = False
            

        
    index += 1
    