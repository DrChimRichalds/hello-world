# Python code​​​​​‌​​​​​​​‌‌​‌‌​‌​‌​​‌​‌​​‌​ below

def encodeString(myword):
    #new_list = [(char, myword.count(char)) for char in set(myword)]
    #don't want .count because that doesn't retain the order 
    #new_list.sort(key=lambda x: myword.index(x[0]))
    PrevChar = myword[0]
    count = 0
    new_list = []
    for char in myword: 
        if char != PrevChar:
            new_list.append((PrevChar, count))
            count = 0
        PrevChar = char
        count = count + 1
    new_list.append((PrevChar, count))
    return print(new_list)


input_test = 'Bookkeeper'

#decodeString([('\n', 37), (' ', 2211), ('%', 510)])

#it'd be easy to iterate through and craete
#  a new list that represents the string as a list, 
# then i wonder if I can iterate through a list and 
# create a count in a dictionary where the value + 

art = '''

                                                                                
                                                                                
                               %%%%%%%%%%%%%%%%%%%                              
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                    %%%%%%%%                         %%%%%%%%                   
                %%%%%%%                                   %%%%%%                
              %%%%%%                                         %%%%%%             
           %%%%%%                                               %%%%%           
          %%%%%                                                   %%%%%         
        %%%%%                                                       %%%%%       
       %%%%                 %%%%%              %%%%%                  %%%%      
      %%%%                 %%%%%%%            %%%%%%%                  %%%%     
     %%%%                  %%%%%%%            %%%%%%%                   %%%%    
    %%%%                   %%%%%%%            %%%%%%%                    %%%%   
    %%%%                    %%%%%              %%%%%                     %%%%   
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                      %%%%        %%%%   
    %%%%       %%%%%%                                        %%%%%       %%%%   
    %%%%         %%%%                                       %%%%        %%%%    
     %%%%         %%%%                                     %%%%         %%%%    
      %%%%         %%%%%                                  %%%%         %%%%     
       %%%%%         %%%%%                             %%%%%         %%%%%      
        %%%%%          %%%%%%                        %%%%%          %%%%        
          %%%%%           %%%%%%%               %%%%%%%           %%%%%         
            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           
              %%%%%%%                                        %%%%%              
                 %%%%%%%                                 %%%%%%%                
                     %%%%%%%%%                     %%%%%%%%%                    
                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         
                                   %%%%%%%%%%%%                                 
                                                                                
                                                                                 

'''
encoded = encodeString(art)
#decoded = decodeString(encoded)