__author__ = "June Jin"
__version__ = "9.8.1"

import heapq

def restaurantFinder(d, site_list):
    '''
    Function description: 

    This function returns a tuple containing (the total maximum revenue and selected sites) where selected sites is a list.
    containing the site numbers where the restaurant should be opened.
    For the sum of maximum revenue, it uses Bottom-Up approach of Dynamic Programming and backtracking.
    
    The restaurant can open within the distance. 
    For example, if the distance is 1, 
    if restaurant 3 need to be selected, then restaurant 2 and 4 cannot be chosen.

    Approach description:
    
    We start from the maximum revenue is 0 because there are no restaurant we chose yet. (base case)
    if based on the distance, we can choose the restaurant and add the revenue to the maximum revenue.
    if the current selected restaurant - 1 revenue is bigger than 
    the last calculated minimum revenue (based on the distance) + current restaurant revenue,
    then we update the maximum revenue.

    For this comparison, we will use the list to store the maximum revenue for each restaurant.
    Memo will be the list of the maximum revenue for each restaurant with beginning 0 which is base case.

    memo[i] - subproblems:
        memo[i] = { the maximum revenue when we have i restaurants to choose from, with the distance d apart.}

    Recurrence memo[i] =
        1. 0;                                                       if i = 0   or distance is out of range (bigger than length of memo)
        2. max(memo[i-(d+1)] + site_list[i-1], memo[i-1]);          else 

    The first loop through the range(1,length of site_list + 1) is for the memo table costs O(n) time, for maximum revenue the number of i restaurant.
    The second loop through the memo table to backtrack and find the maximum restaurant revenue costs O(n) time.
    Making reverse of the first chosen_sites costs O(N) time.

    The memo list takes O(N) space. (N is the length of site_list)
    The temp_maximum takes O(1) space.
    The length_site_list takes O(1) space.
    The first chosen_sites takes O(N) space. (N is the length of site_list)

    :Input:
        argv1: d(distance): integers, which represents the distance between restaurants.
        argv2: site_list: list of integers, which represents the location of each restaurant that we choose for maximum revenue.

    :Output, return: tuple containing (the total maximum revenue and selected sites)
    :Time complexity: O(N) where N is the length of site_list (number of restaurants)
    :Aux space complexity: O(N) where N is the length of site_list (number of restaurants)
    '''
    # Initialize memo and temp_maximum
    memo = [0 for _ in range(len(site_list) + 1)]
    temp_maximum = 0

    # Record temp_maximum in a memo based on the optimal and maximum income for each restaurant.
    for i in range(1, len(site_list) + 1):

        # If the restaurant location is still out of range distance, we need to choose the one restaurant based on their each revenue.
        if i < d+1:

            # Compare one by one each restaurant revenue, and choose the greater one.
            if site_list[i-1] > temp_maximum:
                temp_maximum = site_list[i-1]
                memo[i] = temp_maximum
            else:
                memo[i] = temp_maximum

        # If the restaurant location is in range distance, we need to choose the greater value between the temp_maximum revenue and lastest revenue + current i restaurant revenue.
        else: 
            if temp_maximum < site_list[i-1] + memo[i-(d+1)]:
                temp_maximum = site_list[i-1] + memo[i-(d+1)]
                memo[i] = temp_maximum
            else:
                memo[i] = temp_maximum

    # Backtrack and find the restaurant location that makes maximum revenue.
    chosen_sites = []
    length_site_list = len(site_list)

    # We will start from the last restaurant location, and backtrack to the first restaurant location.
    # If we detect the revenue is different from the previous revenue, it means we choose the restaurant.
    # And, we will subtract the distance from the current index+1 location.
    while length_site_list > 0:
        if memo[length_site_list] == memo[length_site_list-1]:
            length_site_list -= 1
        else:
            chosen_sites.append(length_site_list)
            length_site_list -= (d+1)
        
    chosen_sites.reverse()
    
    return (temp_maximum, chosen_sites)
