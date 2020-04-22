class heap:
    pass 


def siftdown(H, i):
    siftkey = H.s[i]

    parent = i 
    largerchild = 0
    spotfound = False 
    while (2*parent+1  < H.heapsize and spotfound == False):
        if (2 * parent < H.heapsize and H.s[2*parent] < H.s[2*parent +1 ] ):
            largerchild = 2*parent + 1 
        else:
            largerchild = 2*parent
        if (siftkey < H.s[largerchild]):
            H.s[parent] = H.s[largerchild]
            parent = largerchild
        else:
            spotfound = True 
    H.s[parent] = siftkey

def root (H):
    keyout = 0 
    keyout = H.s[0]
    H.s[0] = H.s[H.heapsize-1]
    H.heapsize = H.heapsize -1
    siftdown(H,0)
    return keyout


def removekeys(n, H, S):
    i = 0 
    for i in range(n-1, -1, -1):
        S[i] = root(H)
def makeheap(n, H):
    i = 0

    H.heapsize = n 
    for i in range(n//2, -1, -1 ):
        siftdown(H, i)
def heapsort(n, H):
    makeheap(n,H)
    removekeys(n, H, H.s)
    
lstheap = heap()
lstheap.s = [12, 11, 13, 5, 6, 7]  
lstheap.heapsize= len(lstheap.s)


heapsort(lstheap.heapsize, lstheap)
print(lstheap.s)