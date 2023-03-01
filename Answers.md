
#### Question 1:
	LongPower(int n, int x) {
	      long ans;
	      if(n==0) return  1;
	      else{
	            ans = Power (n/2, x) * Power (n/2, x);
	            if (n % 2 == 1) ans *= x;
	           return ans;
	
		}    
	}
#### Answer:  C)  T(n) = 2T(n/2) + O(1)

#### Question 2:  T(n) = 1 if  n = 1 , n * T(n-1) if n>1 

https://www.youtube.com/watch?v=icS-e8RaCyo

#### Answer: O(n^n)

#### Question 3:

T(n) is O(f(n))" basically means that f(n) describes the upper bound for T(n)
T(n) is Ω(f(n))" basically means that f(n) describes the lower bound for T(n)
T(n) is Θ(f(n))" basically means that f(n) describes the exact bound for T(n)
T(n) is o(f(n))" basically means that f(n) is the upper bound for T(n) but that T(n) can never be equal to f(n)
Lowercase Omega and Theta are non-inclusive of the function they bound so Uppercase Omega(g(n) union lowercase o(g(n)) is empty

#### Answer:  A

#### Question 4:

post-order: left->right->root

#### Answer:  A ADBKHF

#### Question 5:

From wiki:
> Quicksort is an efficient, general-purpose sorting algorithm. Quicksort was developed by British computer scientist Tony Hoare in 1959[1] and published in 1961.[2] It is still a commonly used algorithm for sorting. Overall, it is slightly faster than merge sort and heapsort for randomized data, particularly on larger distributions.[3]
> 
> Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. For this reason, it is sometimes called partition-exchange sort.[4] The sub-arrays are then sorted recursively. This can be done in-place, requiring small additional amounts of memory to perform the sorting.
> 
> Quicksort is a comparison sort, meaning that it can sort items of any type for which a "less-than" relation (formally, a total order) is defined. Most implementations of quicksort are not stable, meaning that the relative order of equal sort items is not preserved.
> 
> Mathematical analysis of quicksort shows that, on average, the algorithm takes O ( n log ⁡ n ) O(n\log {n}) comparisons to sort n items. In the worst case, it makes O ( n 2 ) O(n^{2}) comparisons. 
> 
For Quick sort, which of the following is accurate?

False	A. The worst case and best case have the same order running time

False	B. It always needs another same-sized array (extra space) to finish the sorting

False	C. Two elements with the same value will always change their order after sorting

True	D. The best case and average case have the same order running time

#### Answer: D. The best case and average case have the same order running time



#### Question 6 1 pts

	for (i=n/2; i <= n; i++)
	     for (j = 1; j <= n; j = j*2)
	               count++;

The complexity of the above computation is:

I.  O(n)<br>
II. O(log n )<br>
III. O(log n)^2 <br>
IV. O(n^2 log n)<br>
V. O(n log n)<br>

#### Answer: II. O(log n )<br>

#### Question 7 1 pts
A) for(i = 0; i < n; i++) <br>
B) for(i = 0; i < n; i += 2) <br>
C) for(i = 1; i < n; i *= 2) <br>
D) for(i = n; i > -1; i /= 2)<br>

Consider the above "for" loops. If n is the size of input (positive), which function is most efficient(if the task to be performed is not an issue)?


#### Answer: C) for(i = 1; i < n; i *= 2) <br>


#### Question 8 

What is the asymptotic running time complexity of the algorithm as a function of n.

	i=1 
	while (i<= n) {
                j=n;    
        	while (j>=1) {
                                       // Something
                	j=j/2
                }
                i=i+1;
         }
A: Ɵ (n)<br>
B:  Ɵ (logn)<br>
C: Ɵ (n logn)<br>
D: Ɵ (n2)<br>
E: Ɵ (log n2)<br>


#### Answer: C: Ɵ (n logn)<br>

#### Question 9 

Which of the following have the same order of growth? Choose ALL that apply:

<img src="./images/Question\ 9.png">



#### Question 10 

<img src="./images/Question10.png">


#### Answer: IV <br>

