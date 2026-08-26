amount = eval(input("Enter an integer amount of money in Thai Baht: "))


remaining = amount
count1000 = 0
count500 = 0
count100 = 0
count50 = 0
count20 = 0
count10 = 0
count5 = 0
count2 = 0
count1 = 0

while remaining > 0:
    if remaining >=1:
        
        if remaining >= 2:
            
            if remaining >= 5:
                
                if remaining >= 10:
                    
                    if remaining >= 20:
                        
                        if remaining >= 50:
                            
                            if remaining >= 100:
                                
                                if remaining >= 500:
                                    
                                    if remaining >= 1000:
                                        remaining -= 1000
                                        count1000 += 1
                                        continue
                                
                                    remaining -= 500
                                    count500 += 1
                                    continue
                            
                                remaining -= 100
                                count100 += 1
                                continue
                            
                            remaining -= 50
                            count50 += 1
                            continue
                        
                        remaining -= 20
                        count20 += 1
                        continue
                    
                    remaining -= 10
                    count10 += 1
                    continue
                
                remaining -= 5
                count5 += 1
                continue
            
            remaining -= 2
            count2 += 1
            continue
        
        remaining -= 1
        count1 += 1
        continue
    
    

if count1 >= 1 or count2 >= 1 or count5 >= 1 or count10 >= 1 or count20 >= 1 or count50 >= 1 or count100 >= 1 or count500 >= 1 or count1000 >= 1:
        
    print("\nYou get:")    
    
    if count2 >= 1 or count5 >= 1 or count10 >= 1 or count20 >= 1 or count50 >= 1 or count100 >= 1 or count500 >= 1 or count1000 >= 1:
            
        if count5 >= 1 or count10 >= 1 or count20 >= 1 or count50 >= 1 or count100 >= 1 or count500 >= 1 or count1000 >= 1:
                
            if count10 >= 1 or count20 >= 1 or count50 >= 1 or count100 >= 1 or count500 >= 1 or count1000 >= 1:
                    
                if count20 >= 1 or count50 >= 1 or count100 >= 1 or count500 >= 1 or count1000 >= 1:
                        
                    if count50 >= 1 or count100 >= 1 or count500 >= 1 or count1000 >= 1:
                            
                        if count100 >= 1 or count500 >= 1 or count1000 >= 1:
                                
                            if count500 >= 1 or count1000 >= 1:
                                    
                                if count1000 >= 1:
                                    if count1000 == 1:
                                        print(f"    {count1000} 1000-Baht note")
                                    elif count1000 > 1:
                                        print(f"    {count1000} 1000-Baht notes")
                                            
                                if count500 == 1:
                                    print(f"    {count500} 500-Baht note")
                                elif count500 > 1:
                                    print(f"    {count500} 500-Baht notes")
                                        
                            if count100 == 1:
                                print(f"    {count100} 100-Baht note")
                            elif count100 > 1:
                                print(f"    {count100} 100-Baht notes")
                                    
                        if count50 == 1:
                            print(f"    {count50} 50-Baht note")
                        elif count50 > 1:
                            print(f"    {count50} 50-Baht notes")
                        
                    if count20 == 1:
                        print(f"    {count20} 20-Baht note")
                    elif count20 > 1:
                        print(f"    {count20} 20-Baht notes")
                            
                if count10 == 1:
                    print(f"    {count10} 10-Baht coins")
                elif count10 > 1:
                    print(f"    {count10} 10-Baht coints")
                        
            if count5 == 1:
                print(f"    {count5} 5-Baht coin")
            elif count5 > 1:
                print(f"    {count5} 5-Baht coins")
                    
        if count2 == 1:
            print(f"    {count2} 2-Baht coin")
        elif count2 > 1:
            print(f"    {count2} 2-Baht coins")
                
    if count1 == 1:
        print(f"    {count1} 1-Baht coin")
    elif count1 > 1:
        print(f"    {count1} 1-Baht coins")
                                
                                    
                    

        