
# Author : Neo Ramotlou
# Date : 22 April 2023


import random
import sys

def main():

    
    No_of_pages = int(input("Enter the number of pages :\n")) 
    pages = []

    for i in range(No_of_pages):
         pages.append(random.randrange(9))

    print(pages)
    size = int(sys.argv[1])
    print("FIFO",FIFO(size,pages),'page faults')
    print('LRU',LRU(size,pages),'page faults')
    print('OPT',OPT(size,pages),'page faults')
    
    
def FIFO(size,pages):
    page_faults = 0
    frames = []
    
    for page in pages:

        if (len(frames)<size) and (page not in frames): # Adding pages and frame not full
            frames.append(page)
            page_faults += 1 

        else: 
            if page not in frames: # Remove page and add page to a full frame
                    frames.pop(0) 
                    frames.append(page) 
                    page_faults += 1     

    return page_faults

def LRU(size,pages):
    page_faults = 0
    frames = [] 

    for page in pages:
        if (len(frames)<size) and (page not in frames): # Adding pages and frame not full
            frames.append(page)
            
            page_faults += 1 

        elif page in frames:
                frames.sort(key=page.__eq__) # shift the page to the end of frame
                

        elif page not in frames:
             frames.pop(0)
             frames.append(page)
             
             page_faults += 1 

            
    return page_faults

             
             

def OPT(size,pages):
    page_faults = 0
    frames = [] 
    

    for page in pages:
      
        if (len(frames)<size) and (page not in frames): # Adding pages and frame not full
            frames.append(page)
        
            page_faults += 1 
     

        elif page not in frames:
                frame_index = farthestPage(pages,frames,pages.index(page))        
                frames.pop(frame_index)
                frames.append(page)
                
                page_faults += 1 

    return page_faults


def farthestPage(pages,frames,start):

    farthest_page = 0
    frame_page = 0
    for i in frames:
        page_not_used = 0

        for j in range(start+1,len(pages)):      
            if  (i==pages[j]) : # Page used in future
                page_not_used+=1
                if(j>farthest_page): # farthest page
                    farthest_page = j
                    frame_page = frames.index(i) 
                break

        if (page_not_used==0): # Page not used in the future
             return frames.index(i)
        
           
    return  frame_page
         
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage : python3.py [number of pages] ')
    else:
        main()
